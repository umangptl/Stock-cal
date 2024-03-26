import os

from flask import Flask, render_template, request
import yfinance as yf
from requests.exceptions import HTTPError

app = Flask(__name__)

def get_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        company = stock.info['longName']
        price = stock.info['currentPrice']
        closedprice = stock.info['previousClose']
        change = round(price - closedprice, 2)
        percentage = round((change / closedprice) * 100, 2)
        return change, percentage, company, round(price, 2)
    except HTTPError as e:
        if e.response.status_code == 404:
            return f"Error: {symbol} is not a recognized stock symbol."
        else:
            return f"Error fetching data for {symbol}: {e}"
    except KeyError:
        return f"Error: {symbol} is not a recognized stock symbol."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symbol = request.form['symbol'].upper()
        result = get_stock_price(symbol)
        if isinstance(result, tuple):
            change, percentage, company, price = result
            change_sign = '+' if change > 0 else ''
            return render_template('result.html', company=company, symbol=symbol, price=price, change_sign=change_sign, change=change, percentage=percentage)
        else:
            return render_template('error.html', error=result)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(
        host=os.getenv('URL'),
        port=os.getenv('PORT'),
        debug=True
    )
