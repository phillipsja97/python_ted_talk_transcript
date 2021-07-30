import requests

req = requests.get("https://www.ted.com/talks/{mariana_atencio_what_makes_you_special}/transcript")
print(req.text)