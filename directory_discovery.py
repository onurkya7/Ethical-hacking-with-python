import requests
from concurrent.futures import ThreadPoolExecutor

def make_request(url):
    try:
        with requests.Session() as session:
            return session.get(url, timeout=1)
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        pass

target_url = input("[*] Enter Target URL: ")

with open("data/common.txt", "r") as file:
    with ThreadPoolExecutor(max_workers=50) as executor:
        urls = [f"{target_url}/{word.strip()}" for word in file]
        results = executor.map(make_request, urls)
        
        for url, response in zip(urls, results):
            if response and response.status_code == 200:
                print(f"[+] Discovered Directory At This Link: {url}")
