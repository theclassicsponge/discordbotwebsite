from flask import Flask, render_template, request, session, redirect, url_for, g

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    """Home Page"""
    return(render_template("site/home.html"))

@app.route("/commands")
def comamnds():
    """Commands Page"""
    return(render_template("site/commands.html"))

@app.route("/contact")
def contact():
    """Contact Page"""
    return(render_template("site/contact.html"))

@app.route("/support")
def support():
    """Support Page"""
    return(render_template("site/support.html"))

@app.route("/addbot")
def addbot():
    """Support Page"""
    return(redirect("https://discord.com/api/oauth2/authorize?client_id=850477894044221512&permissions=8&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Flogin&scope=bot"))



def main():
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)
    main()
