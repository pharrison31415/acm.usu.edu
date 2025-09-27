from flask import Flask, render_template, abort, send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/activities")
def activities():
    return render_template('activities.html')


@app.route("/activities/<path:filename>")
def activity_page(filename):
    try:
        return send_from_directory("templates/activities", filename)
    except Exception:
        abort(404)
