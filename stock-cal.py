
def calculate_stock_profit():
    # User inputs
    print("Please provide the following to compute your profit: ")
    stock_symbol = input("Ticker Symbol: ")
    allotment = int(input("Allotment: "))
    final_share_price = float(input("Final Share Price: "))
    sell_commission = float(input("Sell Commission: "))
    initial_share_price = float(input("Initial Share Price: "))
    buy_commission = float(input("Buy Commission: "))
    capital_gain_tax_rate = float(input("Capital Gain Tax Rate(%): "))

    # Calculations
    proceeds = allotment * final_share_price
    total_purchase_price = allotment * initial_share_price
    capital_gain = proceeds - total_purchase_price - sell_commission - buy_commission
    tax_on_capital_gain = capital_gain * (capital_gain_tax_rate / 100) if capital_gain > 0 else 0
    cost = total_purchase_price + buy_commission + sell_commission + tax_on_capital_gain
    net_profit = proceeds - cost
    return_on_investment = (net_profit / cost) * 100
    break_even_price = (total_purchase_price + buy_commission + sell_commission) / allotment

    # Output
    print("\nPROFIT REPORT for {}:".format(stock_symbol))
    print(f"Proceeds\n${proceeds:,.2f}")
    print(f"Cost\n${cost:,.2f}")
    print("\nCost details:")
    print(f"Total Purchase Price\n{allotment} × ${initial_share_price} = ${total_purchase_price:,.2f}")
    print(f"Buy Commission = ${buy_commission:,.2f}")
    print(f"Sell Commission = ${sell_commission:,.2f}")
    print(f"Tax on Capital Gain = {capital_gain_tax_rate}% of ${capital_gain:,.2f} = ${tax_on_capital_gain:,.2f}")
    print(f"Net Profit\n${net_profit:,.2f}")
    print(f"Return on Investment\n{return_on_investment:.2f}%")
    print(f"To break even, you should have a final share price of\n${break_even_price:.2f}")

# Run the function to calculate stock profit
calculate_stock_profit()