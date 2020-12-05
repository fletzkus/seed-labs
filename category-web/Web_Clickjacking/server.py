from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route("/not_malicious")
def not_malicious():
    resp = Response()
    resp.data = render_template('not_malicious.html')

    # Add in for safety
    # resp.headers['X-Frame-Options'] = 'DENY'
    # resp.headers['Content-Security-Policy'] = "frame-ancestors 'none'"

    return resp
