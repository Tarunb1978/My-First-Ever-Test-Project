import requests
import time

API_KEY = '05XV1KB84W22CHHI'  # Always use your own, not demo
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={API_KEY}'

# Wait 12 seconds (Alpha Vantage allows 5 requests/minute for free accounts)
time.sleep(30)

response = requests.get(url)
print("HTTP status code:", response.status_code)
print("Raw response:", response.text)
try:
    data = response.json()
except Exception as e:
    print("Error parsing JSON:", e)
    data = None

# Check for invalid or error messages
if data is not None and "Note" in data:
    print("Hit the API rate limit. The message from Alpha Vantage is:", data["Note"])
elif data is not None and "Error Message" in data:
    print("There was an error in your API call:", data["Error Message"])
else:
    print(data)