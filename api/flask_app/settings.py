from os import environ

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

SECRET_KEY = environ.get('SECRET_KEY')
API_KEY = environ.get('API_KEY')

#Google Cloud SQL
PASSWORD=environ.get('PASSWORD')
PUBLIC_IP_ADDRESS=environ.get('PUBLIC_IP_ADDRESS')
DBNAME=environ.get('DBNAME')
PROJECT_ID=environ.get('PROJECT_ID')
INSTANCE_NAME=environ.get('INSTANCE_NAME')

SQLALCHEMY_DATABASE_URI=f"mysql+mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')