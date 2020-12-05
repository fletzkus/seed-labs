from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, yeet!"

@app.route("/home")
def home():
    resp = Response()
    resp.data = render_template('index.html')
    # resp = Flask.make_response(render_template('index.html', title="Welcome", username="Stanley"))
    resp.headers['X-Frame-Options'] = 'DENY'
    resp.headers['Content-Security-Policy'] = "frame-ancestors 'none'"
    return resp

@app.route("/clicked_button")
def clicked_button():
    resp = Response()
    resp.headers['X-Frame-Options'] = 'DENY'
    resp.headers['Content-Security-Policy'] = "frame-ancestors 'none'"
    return resp

@app.route("/test")
def test():
    return "Hello, test!"