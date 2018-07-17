#! /usr/bin/env python3
__author__ = 'sihart'

import requests

url = "https://api.ciscospark.com/v1/rooms"

headers = {
    'authorization': "Bearer ODI2MjBhMzUtZjJiMC00MWE4LTg0MzktYzczOTJlM2Y5MmEyNWVkZmFjYTktYzZl",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "19f4dc40-49c1-6a05-ceba-f77098eb9738"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)