from binance.exceptions import BinanceAPIException
from bot.client import client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):

    try:
        logger.info(f"MARKET ORDER => {symbol} {side} {quantity}")

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"Response => {response}")

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error => {e}")
        raise

    except Exception as e:
        logger.error(f"General Error => {e}")
        raise


def place_limit_order(symbol, side, quantity, price):

    try:
        logger.info(f"LIMIT ORDER => {symbol} {side} {quantity} {price}")

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"Response => {response}")

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error => {e}")
        raise

    except Exception as e:
        logger.error(f"General Error => {e}")
        raise