#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Set the Flask app environment variable
export FLASK_APP=main.py

# Set the Flask app to run in production mode
export FLASK_ENV=production

# Run the Flask app with gunicorn
gunicorn --bind 0.0.0.0:$PORT main:app