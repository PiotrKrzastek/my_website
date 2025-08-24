from flask import Blueprint, render_template


contact = Blueprint("contact", __name__)

@contact.route("/")
def Contact():
    return render_template("contact.html", title="My contact", page="contact")