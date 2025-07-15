from flask import Flask

# Create flask app instance
app = Flask(__name__)


# Pre set up
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# Root route that returns a welcome message


@app.route('/')
def index():
    return "Welcome to Flatiron Cars"

# Dynamic route returns info based on the specific model in the URL


@app.route('/<model>')
def get_model(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'
