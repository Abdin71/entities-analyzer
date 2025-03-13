from flask import request, jsonify, render_template
from . import app
from flask_swagger_ui import get_swaggerui_blueprint
from .entities_analyzer import entities_analyzer

# Swagger UI setup
SWAGGER_URL = '/api/docs'  
API_URL = '/swagger' 

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Entity Analysis API"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the submitted text from the form
    text = request.form['text']

    if not text:
        return {"error": "No text provided"}, 400
    
    entities = entities_analyzer(text)

    return render_template('results.html', entities=entities)