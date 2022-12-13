# Binance API setup
api_key = ''
api_secret = ''
client = Client(api_key, api_secret)

# Flask API setup
app = Flask(__name__)


@app.route('/market', methods=['POST'])
def market():
    """This route makes a market order in the Binance exchange
    
    Sample JSON:
    {
        "quantity": 10,
        "side": "SIDE_BUY"
    }
    """
    data = request.get_json()
    quantity = data['quantity']
    side = data["side"]
    if side=="SIDE_BUY":
        side2 = SIDE_BUY
    elif side=="SIDE_SELL":
        side2= SIDE_SELL
    
    # buy margin loan

    buy_loan = client.create_margin_order(
        symbol="BTCBUSD", 
        side=side2, 
        type="MARKET",
        quantity=quantity, 
        sideEffectType="MARGIN_BUY",
        isIsolated=True
    )
    return 'OK'


@app.route('/trade_btc_busd_margin_long', methods=['POST'])
def trade_btc_busd_margin_long():
    """This route makes a long margin order in the Binance exchange
    
    Sample JSON:
    {
        "quantity": 10,
        "price_a": 15000,
        "price_b": 12000
    }
    """
    data = request.get_json()
    quantity = data['quantity']
    price_a = data['price_a']
    price_b = data['price_b']
    
    # buy margin loan

    buy_loan = client.create_margin_order(
        symbol="BTCBUSD", 
        side=SIDE_BUY, 
        type="MARKET",
        quantity=quantity, 
        sideEffectType="MARGIN_BUY",
        isIsolated=True
    )
  
    # loop until price reaches either price_a or price_b
    while True:
        ticker = client.get_ticker(symbol='BTCBUSD')
        current_price = float(ticker['lastPrice'])
        if current_price >= price_a:
            sell_loan = client.create_margin_order(
                symbol="BTCBUSD", 
                side=SIDE_SELL, 
                type="MARKET",
                quantity=quantity , 
                sideEffectType="AUTO_REPAY",
                isIsolated=True
            )
            break
        elif current_price <= price_b:
            sell_loan = client.create_margin_order(
                symbol="BTCBUSD", 
                side=SIDE_SELL, 
                type="MARKET",
                quantity=quantity , 
                sideEffectType="AUTO_REPAY",
                isIsolated=True
            )
            break

    return 'OK'

@app.route('/trade_btc_busd_margin_short', methods=['POST'])
def trade_btc_busd_margin_short():
    """This route makes a short margin order in the Binance exchange
    
    Sample JSON:
    {
        "quantity": 10,
        "price_a": 15000,
        "price_b": 12000
    }
    """
    data = request.get_json()
    quantity = data['quantity']
    price_a = data['price_a']
    price_b = data['price_b']
    
    # sell margin loan

    buy_loan = client.create_margin_order(
        symbol="BTCBUSD", 
        side=SIDE_SELL, 
        type="MARKET",
        quantity=quantity, 
        sideEffectType="MARGIN_BUY",
        isIsolated=True
    )
  
    # loop until price reaches either price_a or price_b
    while True:
        ticker = client.get_ticker(symbol='BTCBUSD')
        current_price = float(ticker['lastPrice'])
        if current_price >= price_a:
            sell_loan = client.create_margin_order(
                symbol="BTCBUSD", 
                side=SIDE_BUY, 
                type="MARKET",
                quantity=quantity , 
                sideEffectType="AUTO_REPAY",
                isIsolated=True
            )
            break
        elif current_price <= price_b:
            sell_loan = client.create_margin_order(
                symbol="BTCBUSD", 
                side=SIDE_BUY, 
                type="MARKET",
                quantity=quantity , 
                sideEffectType="AUTO_REPAY",
                isIsolated=True
            )
            break
    return 'OK'



@app.route('/trade_btc_busd_margin_short_oco', methods=['POST'])
def trade_btc_busd_margin_short_oco():
    """This route makes a short margin order with an One-Cancels-Other (OCO) order in the Binance exchange
    
    Sample JSON:
    {
        "quantity": 10,
        "price_a": 15000,
        "price_b": 12000
    }
    """
    data = request.get_json()
    quantity = data['quantity']
    price_a = data['price_a']
    price_b = data['price_b']
    
    # sell margin loan

  
    # loop until price reaches either price_a or price_b
    while True:
        ticker = client.get_ticker(symbol='BTCBUSD')
        current_price = float(ticker['lastPrice'])
        if current_price >= price_a:
            sell_loan = client.create_margin_order(
                symbol="BTCBUSD", 
                side=SIDE_BUY, 
                type="MARKET",
                quantity=quantity , 
                sideEffectType="AUTO_REPAY",
                isIsolated=True
            )
            break
        elif current_price <= price_b:
            sell_loan = client.create_margin_order(
                symbol="BTCBUSD", 
                side=SIDE_BUY, 
                type="MARKET",
                quantity=quantity , 
                sideEffectType="AUTO_REPAY",
                isIsolated=True
            )
            break
    return 'OK'


@app.route('/trade_btc_busd_margin_long_oco', methods=['POST'])
def trade_btc_busd_margin_long_oco():
    """This route makes a long margin order with an One-Cancels-Other (OCO) order in the Binance exchange
    
    Sample JSON:
    {
        "quantity": 10,
        "price_a": 15000,
        "price_b": 12000
    }
    """
    data = request.get_json()
    quantity = data['quantity']
    price_a = data['price_a']
    price_b = data['price_b']
    
    # buy margin loan

    while True:
        ticker = client.get_ticker(symbol='BTCBUSD')
        current_price = float(ticker['lastPrice'])
        if current_price >= price_a:
            sell_loan = client.create_margin_order(
                symbol="BTCBUSD", 
                side=SIDE_SELL, 
                type="MARKET",
                quantity=quantity , 
                sideEffectType="AUTO_REPAY",
                isIsolated=True
            )
            break
        elif current_price <= price_b:
            sell_loan = client.create_margin_order(
                symbol="BTCBUSD", 
                side=SIDE_SELL, 
                type="MARKET",
                quantity=quantity , 
                sideEffectType="AUTO_REPAY",
                isIsolated=True
            )
            break

    return 'OK'

if __name__ == '__main__':
    app.run()
