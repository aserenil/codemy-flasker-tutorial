from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     # put application's code here
#     # return '<h1>Hello World!</h1>'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    stuff = "This is <strong>BOLD</strong> Text"
    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template(
        "user.html",
        user_name=name,
        stuff=stuff,
        favorite_pizza=favorite_pizza
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run()
