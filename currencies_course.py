import requests
import json
from datetime import datetime, timedelta

def currencies_course():
    with open("converter-money/file.json", "r") as f:
        data = json.loads(f.read())
    time = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")    
    if data["meta"]["last_updated_at"].split("T")[0] == time:
        data = parse()
        with open("converter-money/file.json", "w") as f:
            json.dump(data, f)
    return data

def parse():
    url = "https://api.currencyapi.com/v3/latest?apikey=BTfXB0MKEoYvjUkN7S7D2HEgDlF4h3miRc3v0Efl"
    req = requests.get(url).text
    data = json.loads(req)
    return data    