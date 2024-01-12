import requests
import re

def find_sensitive_info(target_url):
    try:
        response = requests.get(target_url)
        credit_card_numbers = re.findall(r'\b\d{4} ?\d{4} ?\d{4} ?\d{4}\b', response.text)
        email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', response.text)
        print("Credit Card Numbers:", credit_card_numbers)
        print("Email Addresses:", email_addresses)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

target_url = "http://example.com"
find_sensitive_info(target_url)
