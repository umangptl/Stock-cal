import yfinance as yf
from requests.exceptions import HTTPError
from datetime import datetime
import pytz

def get_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        company = stock.info['longName']
        price = stock.info['currentPrice']
        closedprice = stock.info['previousClose']
        change = price - closedprice
        percentage = (change / closedprice) * 100
        return change, percentage, company, price
    except HTTPError as e:
        if e.response.status_code == 404:
            return f"Error: {symbol} is not a recognized stock symbol."
        else:
            return f"Error fetching data for {symbol}: {e}"
    except KeyError:
        return f"Error: {symbol} is not a recognized stock symbol."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def main():
    while True:
        symbol = input("Enter the stock symbol (type 'exit' to quit): ").upper()
        if symbol == 'EXIT':
            print("Exiting program...")
            break

        pt_timezone = pytz.timezone('America/Los_Angeles')
        current_time = datetime.now(pt_timezone)
        formatted_time = current_time.strftime("%a %b %d %H:%M:%S %Z %Y")

        result = get_stock_price(symbol)
        if isinstance(result, tuple):
            change, percentage, company, price = result
            change_sign = '+' if change > 0 else ''
            print("output:")
            print(formatted_time)
            print(f"{company} ({symbol})")
            print(f"{price} {change_sign}{change:.2f} ({change_sign}{percentage:.2f}%)")
        else:
            print(result)

if __name__ == "__main__":
    main()
