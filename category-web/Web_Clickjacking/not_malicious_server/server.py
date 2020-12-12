from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route("/not_malicious")
def not_malicious():
    resp = Response()
    resp.data = render_template('not_malicious.html')

    # TODO: Task 5

    return resp
