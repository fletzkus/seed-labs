from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, yeet!"

# @app.route("/malicious")
# def malicious():
#     resp = Response()
#     resp.data = render_template('malicious.html')
#     # resp = Flask.make_response(render_template('index.html', title="Welcome", username="Stanley"))
#     return resp

# @app.route("/safe_malicious")
# def safe_malicious():
#     resp = Response()
#     resp.data = render_template('malicious.html')
#     # resp = Flask.make_response(render_template('index.html', title="Welcome", username="Stanley"))
#     resp.headers['X-Frame-Options'] = 'DENY'
#     resp.headers['Content-Security-Policy'] = "frame-ancestors 'none'"
#     return resp

@app.route("/not_malicious")
def not_malicious():
    resp = Response()
    resp.data = render_template('not_malicious.html')

    # Add in for safety
    # resp.headers['X-Frame-Options'] = 'DENY'
    # resp.headers['Content-Security-Policy'] = "frame-ancestors 'none'"

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