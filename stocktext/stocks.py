import requests
import json

def get_last_interval(api_key, symbol):
    FUNCTION_NAME = "TIME_SERIES_INTRADAY"

    url = "https://www.alphavantage.co/query?function={0}&symbol={1}&interval=5min&apikey={2}".format(
        FUNCTION_NAME, 
        symbol, 
        api_key
    )

    # Request and decode response
    req = requests.get(url)
    res = json.loads(req.content.decode('utf-8').replace("'", '"'))

    # Info and Intervals
    metadata = res['Meta Data']
    intervals = res['Time Series (5min)']

    last_interval = list(intervals.values())[0]

    return last_interval
