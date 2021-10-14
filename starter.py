import requests
from flask import Blueprint, render_template
from algorithm.images import image_data


app_starter = Blueprint('starter', __name__,
                       template_folder='templates')

@app_starter.route('/joke', methods=['GET', 'POST'])
def joke():
    url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    response = requests.request("GET", url)
    return render_template("/joke.html", joke=response.json())






