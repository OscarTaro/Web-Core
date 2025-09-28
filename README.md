# ConnectAid - Legal Support Platform

A full-stack web application providing legal support and resources for Zimbabwean citizens.  
ConnectAid bridges justice gaps by offering free legal information, organization referrals, and educational resources with the mission of "Justice Through Community Support."

## Live Demo
[ConnectAid.org](https://connectaid.org)  
*Note: Update with your actual deployment URL*

## Features
- Multi-language Support: English, Shona, Ndebele, and Shivenda
- Legal Information Assistant: AI-powered chatbot for legal guidance
- Secure Incident Reporting: Protected reporting system for legal violations
- Emergency Contacts: Direct access to legal aid organizations
- Educational Resources: Downloadable legal documents and guides
- User Authentication: Secure login and profile management

## Tech Stack
**Backend:** Python, Flask, SQLAlchemy  
**Frontend:** HTML, CSS, JavaScript, Jinja2 Templates  
**Database:** SQLite  
**Authentication:** Flask-Login, Bcrypt  
**Security:** Flask-Limiter, CSRF protection  
**Email:** Flask-Mail for password resets  
**Additional:** Alembic for database migrations  

## Project Structure
```
connectaid/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── routes.py            # All application routes
│   ├── models.py            # Database models (Users, Report, Info)
│   ├── extensions.py        # Flask extensions initialization
│   ├── assistant.py         # Legal chatbot AI logic
│   └── templates/           # HTML templates
│       ├── base.html        # Base template
│       ├── home.html        # Landing page
│       ├── login.html       # User authentication
│       ├── report.html      # Incident reporting
│       └── ...              # Other templates
├── static/
│   ├── css/                 # Stylesheets
│   ├── js/                  # JavaScript files
│   │   └── languages.js     # Multi-language support
│   └── images/              # Logos and graphics
├── requirements.txt         # Python dependencies
└── connectaid_db.db        # SQLite database (generated)
```

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/web-core.git
cd web-core/connectaid
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables by creating a `.env` file in the project root:
```
SECRET_KEY=your-secret-key-here
SECURITY_PASSWORD_SALT=your-password-salt-here
GMAIL_APP_PASSWORD=your-gmail-app-password
```

5. Initialize the database:
```bash
flask db upgrade
```

6. Run the application:
```bash
flask run
```

7. Access the application at:  
[http://localhost:5000](http://localhost:5000)

## Configuration

### Environment Variables
- `SECRET_KEY`: Flask secret key for session security
- `SECURITY_PASSWORD_SALT`: Password reset token generation
- `GMAIL_APP_PASSWORD`: Gmail credentials for email functionality

### Database Models
- **Users**: User authentication and profiles
- **Report**: Incident reports from users
- **Info**: Contact form submissions

## Legal Chatbot
The integrated AI assistant provides information on:
- Zimbabwean legal rights and procedures
- Court processes and filing requirements
- Partner organizations (Angel of Hope, LRF, Childline, etc.)
- Emergency contacts and legal aid resources
- Family law, property rights, and employment disputes

## Multi-language Support
ConnectAid supports four languages:
- English (default)
- Shona
- Ndebele
- Shivenda

Language switching is implemented with JavaScript and translation dictionaries.

## Security Features
- Password hashing with bcrypt
- Rate limiting on authentication endpoints
- CSRF protection
- Secure session management
- SQL injection prevention with SQLAlchemy
- Input validation and sanitization

## Email Functionality
- Password reset system with timed tokens
- Secure token generation with itsdangerous
- Gmail SMTP integration

## Database Management
```bash
# Create new migration
flask db migrate -m "description"

# Apply migrations
flask db upgrade
```

## Emergency Resources
The platform provides immediate access to:
- Zimbabwe Republic Police Victim Friendly Unit
- Angel of Hope Foundation
- Legal Resources Foundation
- Childline Zimbabwe
- Human Rights NGO Forum
- Adult Rape Clinic
- GBV support resources

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
All rights reserved. This project is proprietary software - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Zimbabwean legal professionals for guidance
- Partner organizations for resource sharing
- Flask community for excellent documentation
- Contributors and testers
