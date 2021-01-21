import threading
import time
import requests

start = False
url = 'https://webhook.site/16a868b7-15b5-4a4d-9aa9-9c5b0e16b188'
myobj = {
    "localization": 0,
    "cvv2": "837",
    "terminalNumber": "12345",
    "amount": 1000,
    "approvalCode": "77777777",
    "sourceAddress": "127.0.0.1",
    "destinationPAN": "6280231400741541",
    "sourcePAN": "6280231400751300",
    "terminalType": 1,
    "expiryDate": "9909",
    "pin": "123456",
    "referenceNumber": "7",
    "acceptorCode": "000000009999432",
    "securityControl": 0,
    "trackingNumber": "13e447f23ea6450bb843cbfcc2d62b2c"
}


def send_request():
    while not start:continue
    x = requests.post(url, json=myobj, headers={"Authorization": "Basic dXNlcjp1c2Vy"})
    print(x.text)


for i in range(30):
    threading.Thread(target=send_request,args=[t]).start()

start = True
