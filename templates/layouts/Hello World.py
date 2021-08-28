@app.route('/greet', method=['GET, 'POST'])
def greet():

    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("simon.html", name=name)

    return render_template("simon.html, name=World")

