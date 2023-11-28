'''Import pandas to read the data'''
import pandas as pd
# import random
from flask_ngrok import run_with_ngrok
from flask import *


app = Flask(__name__)
run_with_ngrok(app)  # Makes Flask run with ngrok


# Define data to be consumed
data = [
    {"Number": 1, "Name": "Mahesh", "Age": 25, "City": "Bangalore", "Country": "India"},
    {"Number": 2, "Name": "Alex", "Age": 26, "City": "London", "Country": "UK"},
    {"Number": 3, "Name": "David", "Age": 27, "City": "San Francisco", "Country": "USA"},
    {"Number": 4, "Name": "John", "Age": 28, "City": "Toronto", "Country": "Canada"},
    {"Number": 5, "Name": "Chris", "Age": 29, "City": "Paris", "Country": "France"},
]


# Routing
@app.route("/index")

def index():
    x = pd.DataFrame(data)
    return x.to_html()

app.run()

