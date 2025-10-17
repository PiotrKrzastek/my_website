from flask import Flask, url_for, redirect, render_template, session, request
from portfolio.routes.projects_blueprint import projects
from portfolio.routes.contact_blueprint import contact
from portfolio.routes.about_blueprint import about


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'temporary_secret_key_for_session_themes'

    @app.route("/")
    def home_redirect():
        return redirect(url_for("projects.Projects"))

    @app.errorhandler(404)
    def not_found(error):
        return render_template("error/404.html"), 404
    
    @app.route("/theme")
    def swap_theme():
        if "theme" not in session or session["theme"] == "dark":
            session["theme"] = "light"
        else:
            session["theme"] = "dark"
        return redirect(request.referrer)

    app.register_blueprint(projects, url_prefix="/projects")
    app.register_blueprint(contact, url_prefix="/contact")
    app.register_blueprint(about, url_prefix="/about")

    return app