import json

import requests
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth


def getAccessToken(request):
    consumer_key = 'AUfqJWrHpavFgKPBd15Zbd0DPt0ANUF6'
    consumer_secret = '5pqIjQKDEG6X5jYD'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)