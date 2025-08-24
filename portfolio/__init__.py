from flask import Flask, url_for, redirect, render_template
from portfolio.routes.projects_blueprint import projects
from portfolio.routes.contact_blueprint import contact
from portfolio.routes.about_blueprint import about

app = Flask(__name__)

app.register_blueprint(projects, url_prefix="/projects")
app.register_blueprint(contact, url_prefix="/contact")
app.register_blueprint(about, url_prefix="/about")

@app.route("/")
def Home_redrect():
    return redirect(url_for("projects.Projects"))

@app.errorhandler(404)
def Not_found(error):
    return render_template("error/404.html"), 404