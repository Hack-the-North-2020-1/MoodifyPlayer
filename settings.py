import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv('FLASK_ENV', default='production')
DEBUG = ENV == 'development'
SECRET_KEY = os.getenv('SECRET_KEY', default='octocat')
GENIUS_ACCESS_TOKEN = os.getenv('GENIUS_ACCESS_TOKEN')
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
GENIUS_CLIENT_ID = os.getenv('GENIUS_CLIENT_ID')
GENIUS_CLIENT_SECRET = os.getenv('GENIUS_CLIENT_SECRET')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
AZURE_IMAGE_API_KEY = os.getenv('AZURE_IMAGE_API_KEY')
IBM_NLU_API_KEY = os.getenv('IBM_NLU_API_KEY')
