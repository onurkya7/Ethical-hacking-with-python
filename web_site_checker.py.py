import requests

# Specify the URL of the website you want to access
url = "https://www.example.com"

# Send a request to the website and get the response status code
response = requests.get(url)
status_code = response.status_code

print(f"Response Status Code: {status_code}")

# Evaluate the response status code to determine if it's successful or an error
if status_code == 200:
    print("The website is accessible.")
elif status_code == 404:
    print("The website could not be found.")
else:
    print("An error occurred while trying to access the website.")
