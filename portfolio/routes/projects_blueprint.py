from flask import Blueprint, render_template, abort, session

projects = Blueprint("projects", __name__)

projects_list = [
    {
        "technologies": "Python | Flask | HTML | CSS | MongoDB",
        "description": "Simple note taking app. Created it under the guidance of Jose Salvatierra during 'Web Developer Bootcamp with Flask and Python in 2024' Udemy course.",
        "image": "noteup.png",
        "slug": "noteup"
    },
    {
        "technologies": "Python | Flask | HTML | CSS | MongoDB",
        "description": "App for rating and tracking your watched movies. Created it under the guidance of Jose Salvatierra during 'Web Developer Bootcamp with Flask and Python in 2024' Udemy course.",
        "image": "movies.png",
        "slug": "movies"
    },
    {
        "technologies": "HTML | CSS | Python | Flask",
        "description": "My very own portfolio website. This is the website you are currently looking at with all the information about me and my projects",
        "image": "portfolio.png",
        "slug": "portfolio"
    }
]

slugs = [project["slug"] for project in projects_list]

@projects.route("/")
def Projects():
    if "theme" in session:
        print(session["theme"])
    return render_template("projects.html", title="My projects", projects=projects_list)

@projects.route("/<string:slug>")
def Projects_noteup(slug):
    if slug in slugs:
        return render_template(slug + ".html", title=f"My projects - {slug}", page="")
    else:
        abort(404)