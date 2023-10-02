import os
import geocoder
from email.message import EmailMessage
import smtplib
import json
import requests
import geocoder

# get request to get ip address
url = requests.get("https://api.ipify.org/?format=json")
url = url.json()
location = geocoder.ip(url["ip"])

# Body of email
body = f"Hello my friend my location informations now are : \nLatitude: {location.latlng[0]}\nLongitude: {location.latlng[1]}\nCity: {location.city}\nCountry: {location.country}"

# sender and reciever info
sender = "Sender's Email"
email_password = "Sender's Email password if use gmail must Enable sign-in with 2-Step Verification "
reciever = "reciever's Email"

# subjet of email
subject = "To sending my device location"

# To initiate email parameters
email = EmailMessage()

email['From'] = sender
email['To'] = reciever
email['Subject'] = subject
email.set_content(body)


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender, email_password)
    smtp.sendmail(from_addr= sender, to_addrs= reciever, msg= email.as_string())
    smtp.close()
