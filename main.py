import requests
import dotenv
import bs4
import os
import smtplib

# Load environment variables from .env file
dotenv.load_dotenv()

# Email credentials
TO_EMAIL = "your_email@example.com"  # Replace with your email or use a placeholder
MY_EMAIL = os.environ["EMAIL"]
MY_PASSWORD = os.environ["PASSWORD"]

# HTTP headers for the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# Cookies to send with the request
cookies = {
    "lc-main": "en_US"
}

# Prompt the user to input the URL of the product
product_url = input("Enter the product URL: ")

# Send an HTTP request to fetch the page content
response = requests.get(product_url, headers=headers, cookies=cookies)

# Parse the page content using BeautifulSoup
soup = bs4.BeautifulSoup(markup=response.text, features="lxml")

# Extract the product price from the page
price_section = soup.find(class_="a-section a-spacing-none aok-align-center aok-relative")
price_text = price_section.getText().split("$")[1]
current_price = float(price_text.split(" ")[0])

# Ask the user for the price they want to pay
desired_price = float(input("Enter the price you are willing to pay: "))

# Check if the desired price is lower than the current price
if desired_price > current_price:

    # Send an email if the desired price is lower than the current price
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=f"Subject: Price Alert\n\nProduct URL: {product_url}\n"
                                f"Current price: {price_section.getText().strip()}\n"
                                f"Your desired price: ${desired_price}")
        print("Email sent successfully!")

