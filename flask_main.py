
# Python Libraries
from flask import Flask

# My Files
from dash_main import incorporate_into_server_Dash

# app = Flask(__name__)

# @app.route('/')
# @app.route('/index')
# def index():
#     return "Default: Hello"

# @app.route('/test_helloWorld')
# @app.route('/helloWorld')
# def test_helloWorld():
#     return "Hello, World!"



def setup_FlaskApp():
    app = Flask(__name__)
    incorporate_into_server_Dash(app)
    return app



# Runs if you call the script directly:
if __name__ == '__main__':
    app = setup_FlaskApp()
    app.run(host = '0.0.0.0', port = 9000)



