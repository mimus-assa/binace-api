# binace-api

This is a Flask API that allows users to trade Bitcoin/USDT on the Binance exchange. It provides a set of routes for making different types of market orders, margin orders, and One-Cancels-Other (OCO) orders in the Binance exchange.

The API uses the Python Binance library to make requests to the Binance API. Before using the API, users must provide their API key and API secret to authenticate their requests. 

The API provides three routes for making market orders: /market, /trade_btc_busd_margin_long, and /trade_btc_busd_margin_short. 

The /market route allows users to make a market order in the Binance exchange. It requires a JSON object containing the “quantity” and “side” parameters. The “quantity” parameter specifies the number of coins to be bought or sold, while the “side” parameter specifies whether to buy or sell.

The /trade_btc_busd_margin_long route allows users to make a long margin order on the Binance exchange. It requires a JSON object containing the “quantity”, “price_a”, and “price_b” parameters. The “quantity” parameter specifies the number of coins to be bought, while the “price_a” and “price_b” parameters specify the two price points at which the order should be placed.

The /trade_btc_busd_margin_short route allows users to make a short margin order on the Binance exchange. It requires a JSON object containing the “quantity”, “price_a”, and “price_b” parameters. The “quantity” parameter specifies the number of coins to be sold, while the “price_a” and “price_b” parameters specify the two price points at which the order should be placed.

The /trade_btc_busd_margin_long_oco and /trade_btc_busd_margin_short_oco routes allow users to make an One-Cancels-Other (OCO) order on the Binance exchange. It requires a JSON object containing the “quantity”, “price_a”, and “price_b” parameters. The “quantity” parameter specifies the number of coins to be bought or sold, while the “price_a” and “price_b” parameters specify the two price points at which the order should be placed.

Overall, this API provides an easy way to make different types of orders on the Binance exchange. It is important to note that users must provide their API key and API secret before using the API.
