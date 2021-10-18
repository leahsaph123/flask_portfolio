# import "packages" from flask
import requests
from flask import Flask, render_template, request
from algorithm.images import image_data
from pathlib import Path


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


@app.route('/Articles/')
def Articles():
    return render_template("Articles.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/meditation/')
def meditation():
    return render_template("meditation.html")

@app.route('/logicgates/')
def logicgates():
    return render_template("logicgates.html")

@app.route('/hexcodes/')
def hexcodes():
    return render_template("hexcodes.html")

@app.route('/Experiment/')
def Experiemnt():
    return render_template("Experiment.html")

@app.route('/pomodoro/')
def pomodoro():
    return render_template("pomodoro.html")

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


@app.route('/binary', methods=['GET', 'POST'])
def binary():
    if request.form:
        num = int(request.form.get("number"))
        if  num >= 0 and num <= 255:  # input field has content
            return render_template("binary.html", number1=num)
    return render_template("binary.html")

@app.route('/rgb', methods=["GET", "POST"])
def rgb():
    path = Path(app.root_path) / "static" / "img"
    return render_template('rgb.html', images=image_data(path))

@app.route('/signedaddition/')
def signed():
    return render_template("signedaddition.html")

@app.route('/unsignedaddition/')
def unsigned():
    return render_template("unsignedaddition.html")


@app.route('/calmingSounds', methods=['GET', 'POST'])
def calmingSounds():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("calmingSounds.html", name1=name)
    # starting and empty input default
    return render_template("calmingSounds.html", name1="World")



student_list = [
    'pam', 'rob', 'joe', 'greg', 'bob', 'amy', 'matt'
]
print(student_list[2:5])
print(student_list[:-5])
print(student_list[6])
print(student_list)




# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)




