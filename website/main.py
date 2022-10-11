# Nathan Everette - Oct 10, 2022

from flask import Flask, render_template, redirect, url_for

# Create instance of Flask webapp
app = Flask(__name__)

# pages
@app.route("/")
def homePage():
    return render_template("index.html")

@app.route("/projects/")
def projectsPage():
    return render_template("projects.html")

@app.route("/resume/")
def resumePage():
    return render_template("resume.html")







#@app.route("/<name>")
#def user(name):
#    return f"Hello {name}!"
#
#
#@app.route("/admin")
#def admin():
#    return redirect(url_for("user", name = "Admin!"))




if __name__ == "__main__":
    app.run()