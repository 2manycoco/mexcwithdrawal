import time
import hmac
import hashlib
import requests

apiKey = 'MEXC_API_KEY'
secret = 'MEXC_SECRET'

coin = "USDT"
network = "TRC20"
amount = "10"
address = "YOUR_WHITELISTED_ADDRESS"
timestamp = str(int(time.time() * 1000))

query_string = f"coin={coin}&network={network}&address={address}&amount={amount}&timestamp={timestamp}"
signature = hmac.new(secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

headers = {
    "X-MEXC-APIKEY": apiKey
}

url = f"https://api.mexc.com/api/v3/capital/withdraw/apply?{query_string}&signature={signature}"
response = requests.post(url, headers=headers)
print("MEXC withdrawal:", response.json())
