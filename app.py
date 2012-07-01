__author__ = 'robyoung'

import flask as fl
import os

def get_urls():
    return [s.strip() for s in open(os.path.join(os.path.dirname(__file__), "urls.txt")).readlines()]

app = fl.Flask(__name__)

@app.route("/")
def index():
    return fl.redirect(fl.url_for("week_notes", date="2012-07-01"))


@app.route("/notes/<date>")
def week_notes(date):
    return fl.render_template("%s.html" % date, urls=get_urls())

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)