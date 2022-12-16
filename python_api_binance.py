
# Binance API setup
api_key = ''
api_secret = ''
client = Client(api_key, api_secret)

# Flask API setup
app = Flask(__name__)

@app.route('/market', methods=['POST'])
def market():
    data = request.get_json()
    quantity = data['quantity']
    side = data["side"]
    if side=="SIDE_BUY":
        side2 = SIDE_BUY
    elif side=="SIDE_SELL":
        side2= SIDE_SELL
    # buy margin loan
    client.create_margin_order(symbol="BTCBUSD", side=side2, type="MARKET",quantity=quantity, sideEffectType="MARGIN_BUY",isIsolated=True)
    return 'OK'

@app.route('/trade_btc_busd_margin_long', methods=['POST'])
def trade_btc_busd_margin_long():
    data = request.get_json()
    quantity = data['quantity']
    price_a = data['price_a']
    price_b = data['price_b']
    # buy margin loan
    client.create_margin_order(symbol="BTCBUSD", side=SIDE_BUY, type="MARKET",quantity=quantity, sideEffectType="MARGIN_BUY",isIsolated=True)
    # loop until price reaches either price_a or price_b
    while True:
        ticker = client.get_ticker(symbol='BTCBUSD')
        current_price = float(ticker['lastPrice'])
        if current_price >= price_a or current_price <= price_b:
            side = SIDE_SELL if current_price >= price_a else SIDE_BUY
            client.create_margin_order(symbol="BTCBUSD", side=side, type="MARKET",quantity=quantity , sideEffectType="AUTO_REPAY",isIsolated=True)
            break
    return 'OK'


@app.route('/trade_btc_busd_margin_short', methods=['POST'])
@app.route('/trade_btc_busd_margin_long_oco', methods=['POST'])
@app.route('/trade_btc_busd_margin_short_oco', methods=['POST'])
def trade_btc_busd_margin_short_or_long_oco():
    data = request.get_json()
    quantity = data['quantity']
    price_a = data['price_a']
    price_b = data['price_b']
    # buy/sell margin loan
    side = SIDE_SELL if request.path == '/trade_btc_busd_margin_short' else SIDE_BUY
    client.create_margin_order(symbol="BTCBUSD", side=side, type="MARKET",quantity=quantity, sideEffectType="MARGIN_BUY",isIsolated=True)
    # loop until price reaches either price_a or price_b
    while True:
        ticker = client.get_ticker(symbol='BTCBUSD')
        current_price = float(ticker['lastPrice'])
        if current_price >= price_a or current_price <= price_b:
            side = SIDE_SELL if current_price >= price_a else SIDE_BUY
            client.create_margin_order(symbol="BTCBUSD", side=side, type="MARKET",quantity=quantity , sideEffectType="AUTO_REPAY",isIsolated=True)
            break
    return 'OK'

# JSON body example for ocos: 
# {
#     "quantity": "1",
#     "price_a": "10.00",
#     "price_b": "5.00"
# }
# JSON body example for market: 
#{
 #   "quantity": "1",
  #  "side": "SIDE_BUY"
#}

if __name__ == '__main__':
    app.run()
