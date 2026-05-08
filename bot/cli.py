import argparse
from colorama import Fore, init

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.orders import (
    place_market_order,
    place_limit_order
)

init(autoreset=True)


def print_success(message):
    print(Fore.GREEN + message)


def print_error(message):
    print(Fore.RED + message)


def print_info(message):
    print(Fore.CYAN + message)


def run_cli():

    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()

        side = validate_side(args.side)

        order_type = validate_order_type(args.type)

        quantity = validate_quantity(args.quantity)

        price = None

        if order_type == "LIMIT":

            if not args.price:
                raise ValueError(
                    "Price is required for LIMIT orders"
                )

            price = validate_price(args.price)

        print_info("\n========= ORDER SUMMARY =========")

        print_info(f"Symbol      : {symbol}")
        print_info(f"Side        : {side}")
        print_info(f"Order Type  : {order_type}")
        print_info(f"Quantity    : {quantity}")

        if price:
            print_info(f"Price       : {price}")

        print_info("=================================\n")

        if order_type == "MARKET":

            response = place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            response = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print_success("ORDER PLACED SUCCESSFULLY\n")

        print_info("========= ORDER RESPONSE =========")

        print_info(f"Order ID       : {response.get('orderId')}")
        print_info(f"Status         : {response.get('status')}")
        print_info(f"Executed Qty   : {response.get('executedQty')}")
        print_info(f"Average Price  : {response.get('avgPrice')}")

        print_info("==================================")

    except Exception as e:

        print_error(f"\nERROR : {e}\n")