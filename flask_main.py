from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Default: Hello"

@app.route('/test_helloWorld')
@app.route('/helloWorld')
def test_helloWorld():
    return "Hello, World!"

# Runs if you call the script directly:
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 9000)



