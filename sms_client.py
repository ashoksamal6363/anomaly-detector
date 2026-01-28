
import requests
import variables as v

def send_sms(numbers, text):
    url = f"https://api.twilio.com/2010-04-01/Accounts/{v.TWILIO_ACCOUNT_SID}/Messages.json"
    for n in numbers:
        requests.post(url, data={"To":n,"From":v.TWILIO_FROM_NUMBER,"Body":text},
                      auth=(v.TWILIO_ACCOUNT_SID, v.TWILIO_AUTH_TOKEN))
