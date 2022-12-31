from binance import Client
from flask import Flask, render_template, request, redirect, url_for
from binance.enums import *
from flask_bootstrap import Bootstrap
import logging

api_key = ''
api_secret = ''
client = Client(api_key, api_secret)

app = Flask(__name__)
Bootstrap(app)

# Set up log
logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def index():
    return redirect(url_for('market'))

@app.route('/market', methods=['GET', 'POST'])
def market():
    if request.method == 'POST':
        try:
            quantity = request.form['quantity']
            side = request.form['side']
            if side == 'SIDE_BUY':
                side2 = SIDE_BUY
            elif side == 'SIDE_SELL':
                side2 = SIDE_SELL
            buy_loan = client.create_margin_order(symbol="BTCBUSD", side=side2, type="MARKET", quantity=quantity, sideEffectType="MARGIN_BUY", isIsolated=True)
            return render_template('market.html', result=buy_loan)
        except Exception as e:
            logging.error(e, exc_info=True)
    return render_template('market.html')

@app.route('/oco', methods=['GET', 'POST'])
def oco():
    if request.method == 'POST':
        try:
            quantity = request.form['quantity']
            price_a = float(request.form['price_a'])
            price_b = float(request.form['price_b'])
            side = request.form['side']
            while True:
                ticker = client.get_ticker(symbol='BTCBUSD')
                current_price = float(ticker['lastPrice'])
                if side == 'FROM_SHORT':
                    if current_price >= price_a:
                        sell_loan = client.create_margin_order(symbol="BTCBUSD", side=SIDE_BUY, type="MARKET", quantity=quantity, sideEffectType="AUTO_REPAY", isIsolated=True)
                        break
                    elif current_price <= price_b:
                        sell_loan = client.create_margin_order(symbol="BTCBUSD", side=SIDE_BUY, type="MARKET", quantity=quantity, sideEffectType="AUTO_REPAY", isIsolated=True)
                        break
                elif side == 'FROM_LONG':
                    if current_price >= price_a:
                        sell_loan = client.create_margin_order(symbol="BTCBUSD", side=SIDE_SELL, type="MARKET", quantity=quantity, sideEffectType="AUTO_REPAY", isIsolated=True)
                        break
                    elif current_price <= price_b:
                        sell_loan = client.create_margin_order(symbol="BTCBUSD", side=SIDE_SELL, type="MARKET", quantity=quantity, sideEffectType="AUTO_REPAY", isIsolated=True)
                        break
            return render_template('oco.html', result=sell_loan)
        except Exception as e:
            logging.error(e, exc_info=True)
    return render_template('oco.html')

if __name__ == '__main__':
    app.run()
