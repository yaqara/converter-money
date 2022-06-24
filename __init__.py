from locale import currency
from django.shortcuts import render
from flask import Flask, render_template, request
import json

from currencies_course import currencies_course

app = Flask(__name__)

class Checker:
    def __init__(self, currency_names, raw_value):
        self.currency_names = currency_names
        self.raw_value = raw_value
        self.values = []
        self.rate = currencies_course() 
    def result_gen(self):
        for name in self.currency_names:
            self.values.append(self.rate["data"][name]["value"])
        self.result_value = round(float(self.raw_value) / self.values[0] * self.values[1])
        return self.result_value

with open("converter-money/menu.json") as f:
    options = json.loads(f.read())

@app.route("/", methods = ["POST", "GET"])
def index_page():
    if request.method == "POST":
        currency_names = []
        raw_value = request.form.get("currency_number") 
        currency_names.append(request.form.get("from-currency-menu"))
        currency_names.append(request.form.get("to-currency-menu"))
        if raw_value:
            checker = Checker(currency_names, raw_value)
            currency = [raw_value, checker.result_gen()]
            return render_template("index.html", options = options, currency = currency, selected_currencies = currency_names)   
    return render_template("index.html", options = options, currency = [0, 0], selected_currencies = ['AED', 'AED'])

if __name__ == "__main__":
    app.run(debug=True)