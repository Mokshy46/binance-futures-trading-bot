# Binance Futures Trading Bot (CLI)

A CLI-based Python trading bot built for Binance Futures Testnet (USDT-M). The application supports placing MARKET and LIMIT orders with input validation, structured logging, and exception handling.

## Features

* Place **MARKET** orders on Binance Futures Testnet
* Place **LIMIT** orders on Binance Futures Testnet
* Supports both **BUY** and **SELL** sides
* Command-line interface using `argparse`
* Input validation for:

  * Side (`BUY` / `SELL`)
  * Order type (`MARKET` / `LIMIT`)
  * Quantity
  * Price requirements for LIMIT orders
* Structured project architecture
* Logging of requests, responses, and errors
* Exception handling for invalid input and API failures

## Project Structure

```
binance-futures-trading-bot/
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── logs/
│   └── app.log
├── cli.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Mokshy46/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

### 2. Create and activate a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

You can obtain Testnet API credentials from Binance Futures Testnet.

## Usage

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

## Example Output

```
===== ORDER REQUEST =====
Symbol       : BTCUSDT
Side         : BUY
Type         : MARKET
Quantity     : 0.001
Price        : N/A

===== ORDER RESPONSE =====
Order ID     : 15010971338
Status       : NEW
Executed Qty : 0.0000
Avg Price    : N/A

Order processed successfully.
```

## Logging

The application logs order requests, responses, and errors to a log file.

Example:

```
2026-06-12 14:54:46,504 - INFO - Order Request: symbol=BTCUSDT, side=BUY, type=MARKET, quantity=0.001, price=None
2026-06-12 14:54:47,198 - INFO - Order Response: orderId=15010710525, status=NEW, executedQty=0.0000, avgPrice=N/A
```

## Assumptions

* Binance Futures Testnet credentials are valid and active.
* MARKET orders do not require a price.
* LIMIT orders require a positive price.
* The application reports the immediate response returned by Binance Testnet.

## Technologies Used

* Python 3
* python-binance
* python-dotenv
* argparse
* logging

## Notes

This project was developed as part of a Python developer assessment to demonstrate:

* API integration
* CLI application development
* Validation and error handling
* Logging practices
* Clean code organization
