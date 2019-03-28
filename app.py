from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from stocktext.credentials import obtain_credentials
from stocktext.stocks import get_last_interval

CREDENTIALS_FILE = "auth/credentials.json"
ALPHA_API_KEY = obtain_credentials(CREDENTIALS_FILE, "ALPHA_API")
TWILIO_ACCOUNT_SID = obtain_credentials(CREDENTIALS_FILE, "ACCOUNT_SID")
TWILIO_AUTH_TOKEN = obtain_credentials(CREDENTIALS_FILE, "AUTH_TOKEN")

app = Flask(__name__)

@app.route("/")
def home():
    return 'StockText'

@app.route("/sms", methods=['GET', 'POST'])
def sms_response():
    incoming = str(request.values.get('Body', None))

    # Get last interval info
    try:
        st = get_last_interval(ALPHA_API_KEY, incoming)

        info_message = "StockText (By Fernando)\n\n{0} last interval:".format(incoming)
        for key, val in st.items():
            info_message += "\n{0}: {1}".format(key, float(val))
    
    except:
        info_message = "Error: Stock not founded."

    resp = MessagingResponse()
    resp.message(info_message)

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)