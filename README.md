# PriceDropNotifier

## Description
PriceDropNotifier is a simple web scraping tool built with BeautifulSoup that tracks product prices. When the price drops below a target set by the user, an email notification is sent.

## How it works:
1. Enter the product URL.
2. Set your desired price.
3. The script scrapes the current price of the product.
4. If the price is below your target, an email notification is sent with the product details.

## Requirements:
- requests
- beautifulsoup4
- lxml
- python-dotenv
- smtplib
