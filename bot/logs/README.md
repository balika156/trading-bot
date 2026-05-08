# Binance Futures Trading Bot

A simplified trading bot using Binance Futures Testnet.

## Features

- MARKET Orders
- LIMIT Orders
- BUY / SELL
- CLI Support
- Logging
- Error Handling

## Install

pip install -r requirements.txt

## Run MARKET Order

python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

## Run LIMIT Order

python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000