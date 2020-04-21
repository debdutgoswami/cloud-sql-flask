from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
app.config:
    For local development:
    SQLALCHEMY_DATABASE_URI = mysql+mysqldb://root:<password>@/<dbname>?unix_socket=/cloudsql/<projectid>:<instancename>

    For production:
    SQLALCHEMY_DATABASE_URI = mysql+mysqldb://root:<password>@<public_ip_address>/<dbname>?unix_socket=/cloudsql/<projectid>:<instancename>

Cloud SQL configuration:
    For local development:
    We don't mention the <public_ip_address> then the default is localhost.
    The database gets hosted in the local machine.

    For production:
    We need to add the public ip of the local machine (machine we are deploying the server to)
    to the 'Authorised networks' under 'Public IP' of the SQL configuration
"""

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)

from flask_app import routes