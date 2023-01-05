from flask import Flask, flash, render_template, request
from forex_python.converter import CurrencyCodes, CurrencyRates

c = CurrencyRates()
s = CurrencyCodes()

app = Flask(__name__)
app.config["SECRET_KEY"] = 'Beginner.py'

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/forex', methods=['POST'])
def forex():
    
    convert_from = request.form['convert-from']
    cf_symbol =  s.get_symbol(convert_from)
    convert_to = request.form['convert-to']
    ct_symbol =  s.get_symbol(convert_to)
    amount = request.form['amount']
    try:
        conversion = c.convert(convert_from, convert_to, float(amount))
        conversion = round(conversion, 2)
    except:
        flash('Invalid Input')
        return render_template('msg.html')

    return render_template('conversion.html', convert_from=convert_from,cf_symbol=cf_symbol, convert_to=convert_to, ct_symbol=ct_symbol, amount=amount, conversion=conversion)

