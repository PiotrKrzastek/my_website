from flask import Blueprint, render_template

about = Blueprint("about", __name__)

@about.route("/")
def About():
    return render_template("about.html", title="About me", page="about")