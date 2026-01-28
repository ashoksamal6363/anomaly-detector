
import requests
import variables as v

def send_whatsapp_message(numbers, text):
    for n in numbers:
        payload = {"messaging_product":"whatsapp","to":n,"type":"text","text":{"body":text}}
        headers = {"Authorization": f"Bearer {v.WHATSAPP_ACCESS_TOKEN}"}
        requests.post(v.WHATSAPP_API_BASE_URL, headers=headers, json=payload)
