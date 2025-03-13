from flask import Flask
from dotenv import load_dotenv
import os
from .utils.logger import setup_logger

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['API_URL'] = os.getenv('API_URL')
    app.config['API_KEY'] = os.getenv('API_KEY')

    # Set up logger
    logger = setup_logger(__name__)
    app.logger = logger

    return app

# Create the Flask app
app = create_app()

# Import routes
from .routes import *