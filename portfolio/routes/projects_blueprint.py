from flask import Blueprint, render_template, abort

projects = Blueprint("projects", __name__)

projects_list = [
    {
        "technologies": "Python | Flask",
        "description": "My first ever portfolio project. Created it under the guidance of Jose Salvatierra during 'Web Developer Bootcamp with Flask and Python in 2024' Udemy course.",
        "image": "noteup.png",
        "slug": "noteup"
    }
]

slugs = [project["slug"] for project in projects_list]

@projects.route("/")
def Projects():
    return render_template("projects.html", title="My projects", projects=projects_list)

@projects.route("/<string:slug>")
def Projects_noteup(slug):
    if slug in slugs:
        return render_template(slug + ".html", title="My projects - NoteUP", page="")
    else:
        abort(404)