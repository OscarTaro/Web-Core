from app.extensions import db
from flask_login import UserMixin

class Report(db.Model):
    __tablename__='Incident Details'
    id=db.Column(db.Integer, primary_key=True)
    firstName=db.Column(db.String, nullable=False)
    lastName=db.Column(db.String, nullable=False)
    phone=db.Column(db.Integer, nullable=False)
    email=db.Column(db.String)
    location=db.Column(db.String)
    incidentType=db.Column(db.String)
    message=db.Column(db.String)
    consent=db.Column(db.Integer)

    def get_id(self):
        return str(self.id)
    
    def __repr__(self):
        return f'Report from user {self.firstName}, with lastName {self.lastName}, phone number: {self.phone}, email adress:{self.email} and location: {self.location}, on the incident {self.incidentType}.\n Message Submitted:\n{self.message}.'

class Info(db.Model):
    __tablename__='Contact Us Directly'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False)
    subject=db.Column(db.String, nullable=False)
    message=db.Column(db.String, nullable=False)

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f'Information request by {self.name}, on the email: {self.email}, regarding the subject: {self.subject}.\n Message: {self.message}.'
    


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)  
    email = db.Column(db.String(120), unique=True, nullable=False)    
    password = db.Column(db.String(255), nullable=False)              

    def get_id(self):
        return str(self.id)
    
    def __repr__(self):
        return f'User: {self.username} ({self.email})'