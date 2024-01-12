import requests

def detect_honeypot(target_url):
    try:
        response = requests.get(target_url)
        if "honeypot" in response.text.lower():
            print("Honeypot Detected!")
        else:
            print("No Honeypot Detected.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

target_url = "https://example.com"
detect_honeypot(target_url)
