from flask import render_template, request, redirect, url_for, flash, jsonify, session
from flask_login import login_required, logout_user, login_user, current_user
from app.models import Report, Info, Users
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.extensions import LoginForm
from itsdangerous import URLSafeTimedSerializer
from itsdangerous.exc import SignatureExpired, BadSignature 
from flask_mail import Mail, Message
from datetime import timedelta
import json
import re
from app.assistant import LegalChatbot

def routesManager(app, db, encrypt):
    mail = Mail(app)
    limiter = Limiter(app=app, key_func=get_remote_address)
    chatbot=LegalChatbot()

    def secure_hash(password):
        try:
            if not password.startswith("pbkdf2:sha256:"):
                return encrypt.generate_password_hash(password).decode('utf-8')
            return password
        except Exception as e:
            app.logger.error(f"Password hashing error: {str(e)}")
            raise

    @app.route('/', methods=['GET'])
    def home():
        return render_template('home.html')

    @app.route('/rights')
    def rights():
        return render_template('rights.html')

    @app.route('/report', methods=['GET', 'POST'])
    def report():
        # Store the intended destination before login
        if request.method == 'GET' and not current_user.is_authenticated:
            session['next_url'] = url_for('report')
            
        if request.method == 'GET':
            return render_template('report.html')
        elif request.method == 'POST' and request.form:
            form_type = request.form.get('form_type')

            if form_type == 'incident_report':
                # Only allow reporting if user is logged in
                if not current_user.is_authenticated:
                    session['next_url'] = url_for('report')
                    flash('Please login to report an incident', 'error')
                    return redirect(url_for('login'))
                
                firstName = request.form.get('firstName')
                lastName = request.form.get('lastName')
                phone = request.form.get('phone')
                email = request.form.get('email')
                location = request.form.get('location')
                incidentType = request.form.get('incidentType')

                try:
                    phone = int(phone)
                except (TypeError, ValueError):
                    flash("Invalid phone number.", "error")
                    return redirect(url_for('report'))

                report_msg = Report(firstName=firstName, lastName=lastName,
                                    phone=phone, email=email, location=location,
                                    incidentType=incidentType)
                db.session.add(report_msg)
                db.session.commit()
                flash('Report Successful', 'info')
                return redirect(url_for('home'))

            elif form_type == 'signup':
                username = request.form.get('username', '').strip()
                email = request.form.get('email', '').strip().lower()
                password = request.form.get('password', '')
                confirm_password = request.form.get('confirm_password', '')

                # Input validation
                if not all([username, email, password, confirm_password]):
                    flash('All fields are required', 'error')
                    return redirect(url_for('report'))

                if len(password) < 6:
                    flash('Password must be at least 6 characters', 'error')
                    return redirect(url_for('report'))

                if password != confirm_password:
                    flash('Passwords do not match', 'error')
                    return redirect(url_for('report'))

                # Check if user already exists
                existing_user = Users.query.filter(
                    (Users.username == username) | (Users.email == email)
                ).first()
                
                if existing_user:
                    if existing_user.username == username:
                        flash('Username already exists', 'error')
                    else:
                        flash('Email already registered', 'error')
                    return redirect(url_for('report'))

                try:
                    hashed_password = secure_hash(password)
                    user = Users(username=username, email=email, password=hashed_password)
                    db.session.add(user)
                    db.session.commit()
                    
                    # Auto-login after signup and redirect to intended destination
                    login_user(user)
                    next_url = session.pop('next_url', None) or url_for('report')
                    flash('Signup successful! You can now report your incident.', 'success')
                    return redirect(next_url)
                    
                except Exception as e:
                    db.session.rollback()
                    app.logger.error(f"Signup error: {str(e)}")
                    flash('Error creating account. Please try again.', 'error')
                    return redirect(url_for('report'))

    @app.route('/privacy')
    def privacy():
        return render_template('privacy.html')

    @app.route('/lawyers')
    def lawyers():
        return render_template('lawyers.html')

    @app.route('/info', methods=['GET', 'POST'])
    def info():
        if request.method == 'GET':
            return render_template('info.html')
        elif request.method == 'POST' and request.form:
            form_type=request.form.get('form_type')

            if form_type=='info_query':
                name = request.form.get('name')
                email = request.form.get('email')
                subject = request.form.get('subject')
                message = request.form.get('message')
                user_msg = Info(name=name, email=email, subject=subject, message=message)
                db.session.add(user_msg)
                db.session.commit()
                flash('Message sent', 'info')
                return redirect(url_for('home'))
            elif form_type=='signup':
                username = request.form.get('username')
                email = request.form.get('email')
                password = request.form.get('password')
                confirm_password = request.form.get('confirm_password')

                if password != confirm_password:
                    flash('Passwords do not match', 'error')
                    return redirect(url_for('info'))

                try:
                    hashed_password = secure_hash(password)
                    user = Users(username=username, email=email, password=hashed_password)
                    db.session.add(user)
                    db.session.commit()
                    flash('Signup successful', 'info')
                    return redirect(url_for('login'))
                except Exception as e:
                    db.session.rollback()
                    app.logger.error(f"Signup error: {str(e)}")
                    flash('Error creating account. Please try again.', 'error')
                    return redirect(url_for('info'))

            else:
                flash('Invalid form submission.', 'error')
                return redirect(url_for('info'))

    @app.route('/gbvResources')
    def gbvResources():
        return render_template('gbv-resources.html')

    @app.route('/emergency')
    def emergency():
        return render_template('emergency.html')

    @app.route('/courts')
    def courts():
        return render_template('courts.html')

    @app.route('/terms')
    def terms():
        return render_template('terms.html')

    @app.route('/board')
    def bod():
        return render_template('bod.html')

    @app.route('/faq')
    def faq():
        return render_template('faq.html')

    @app.route('/security')
    def security():
        return render_template('security.html')

    @app.route('/settings')
    def settings():
        return render_template('settings.html')

    @app.route('/profile')
    @login_required
    def profile():
        return render_template('profile.html')
    
    @app.route('/chatbot')
    def chatbot_page():
        return render_template('chatbot.html')

    @app.route('/api/chat', methods=['POST'])
    def chat():
        try:
            data = request.get_json()
            
            if not data or 'message' not in data:
                return jsonify({
                    'status': 'error',
                    'response': 'No message provided'
                }), 400
            
            user_message = data['message']
            
            if not user_message.strip():
                return jsonify({
                    'status': 'error', 
                    'response': 'Message cannot be empty'
                }), 400
            
            response = chatbot.find_answer(user_message)
            
            return jsonify({
                'status': 'success',
                'response': response
            })
            
        except Exception as e:
            print(f"Error in chat endpoint: {e}") 
            return jsonify({
                'status': 'error',
                'response': 'Sorry, I encountered an error. Please try again.'
            }), 500

    @app.route('/login', methods=['GET', 'POST'])
    @limiter.limit('5 per minute', error_message='Too many attempts - please wait')
    def login():
        form = LoginForm()
        
        # Store the intended destination before showing login form
        if request.method == 'GET':
            # If user came from another page, store it for redirect after login
            if request.referrer and url_for('login') not in request.referrer:
                session['next_url'] = request.referrer
            return render_template('login.html', form=form)
            
        elif request.method == 'POST' and request.form:
            email = request.form.get('email')
            password = request.form.get('password')
            user = Users.query.filter_by(email=email).first()
            try:
                if user and encrypt.check_password_hash(user.password, password):
                    login_user(user)
                    flash('Login Successful', 'success')
                    
                    # Redirect to intended destination or report page
                    next_url = session.pop('next_url', None)
                    if next_url and next_url != url_for('login'):
                        return redirect(next_url)
                    else:
                        return redirect(url_for('report'))  
                else:
                    flash('Invalid email or password', 'error')
            except ValueError as e:
                app.logger.error(f"Password hash error for user {email}: {str(e)}")
                flash('Authentication system error. Please use password reset if needed.', 'error')
            return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Logged out', 'info')
        return redirect(url_for('home')) 

    @app.route('/dashboard')
    @login_required
    def dashboard():
        reports = Report.query.order_by(Report.firstName).all()
        info = Info.query.order_by(Info.name).all()
        return render_template('dashboard.html', report=reports, questions=info)

    @app.route('/request-password-reset', methods=['GET', 'POST'])
    def request_password_reset():
        if request.method == 'GET':
            return render_template('request_password_reset.html')

        email = request.form.get('email')
        user = Users.query.filter_by(email=email).first()

        if user:
            try:
                serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
                token = serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])
                reset_url = url_for('reset_password', token=token, _external=True)

                msg = Message('Password Reset Request',
                              sender=app.config['MAIL_DEFAULT_SENDER'],
                              recipients=[user.email])
                msg.body = f'''You requested a password reset for ConnectAid.

                Click this link to reset your password:
                {reset_url}

                This link will expire in 1 hour.

                If you didn't request this, please ignore this email.'''

                mail.send(msg)
                app.logger.info(f"Password reset email sent to {email}")

            except Exception as e:
                app.logger.error(f"Failed to send password reset email: {str(e)}")
                flash('Error sending reset email. Please try again.', 'error')
                return redirect(url_for('request_password_reset'))

        flash('If an account exists with this email, a reset link has been sent.', 'info')
        return redirect(url_for('login'))

    @app.route('/reset-password/<token>', methods=['GET', 'POST'])
    def reset_password(token):
        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        try:
            email = serializer.loads(
                token,
                salt=app.config['SECURITY_PASSWORD_SALT'],
                max_age=3600  # 1 hour expiration
            )
        except (SignatureExpired, BadSignature): 
            flash('The reset link is invalid or has expired.', 'error')
            return redirect(url_for('request_password_reset'))

        user = Users.query.filter_by(email=email).first()
        if not user:
            flash('Invalid user.', 'error')
            return redirect(url_for('login'))

        if request.method == 'POST':
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')

            if password != confirm_password:
                flash('Passwords do not match.', 'error')
                return render_template('reset_password.html', token=token)

            if len(password) < 8:
                flash('Password must be at least 8 characters.', 'error')
                return render_template('reset_password.html', token=token)

            try:
                user.password = secure_hash(password)
                db.session.commit()
                flash('Your password has been updated.', 'success')
                return redirect(url_for('login'))
            except Exception as e:
                db.session.rollback()
                app.logger.error(f"Password reset failed: {str(e)}")
                flash('Error updating password. Please try again.', 'error')

        return render_template('reset_password.html', token=token)
    