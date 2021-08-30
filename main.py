# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    print("hello")
    for i in range(0,70):
        print("hi :3 {}".format(i))
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/simon/')
def simon():
    return render_template("simon.html")


@app.route('/leah/')
def leah():
    return render_template("leah.html")


@app.route('/isabella/')
def isabella():
    return render_template("isabella.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
print("hello")

@app.route('/greet', method=['GET,POST'])
def greet():

    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("simon.html", name=name)

    return render_template("simon.html, name=World")

