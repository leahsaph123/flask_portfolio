# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    #print("hello")
    #for i in range(0,70):
        #print("hi :3 {}".format(i))
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


@app.route('/simon', methods=['GET', 'POST'])
def simon():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("simon.html", name1=name)
    # starting and empty input default
    return render_template("simon.html", name1="World")

@app.route('/minilab', methods=['GET', 'POST'])
def minilab():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("minilab.html", name1=name)
    # starting and empty input default
    return render_template("minilab.html", name1="World")


@app.route('/leah', methods=['GET', 'POST'])
def leah():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("leah.html", name1=name)
    # starting and empty input default
    return render_template("leah.html", name1="World")

@app.route('/Tigran', methods=['GET', 'POST'])
def Tigran():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Tigran.html", name=name)
    # starting and empty input default
    return render_template("Tigran.html", name="World")

@app.route('/isabella', methods=['GET', 'POST'])
def isabella():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("isabella.html", name=name)
    # starting and empty input default
    return render_template("isabella.html", name="world")

@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    if request.form:
        num = int(request.form.get("number"))
        if  num >= 0 and num <= 255:  # input field has content
            return render_template("binary.html", number1=num)
    return render_template("binary.html")

@app.route('/rgb/')
def rgb():
    return render_template("rgb.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)


