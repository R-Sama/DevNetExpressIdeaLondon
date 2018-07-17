import json
import requests

accessToken = "ODI2MjBhMzUtZjJiMC00MWE4LTg0MzktYzczOTJlM2Y5MmEyNWVkZmFjYTktYzZl" #put your access token between the quotes.


accessToken_hdr = 'Bearer ' + accessToken
spark_header = {'Authorization': accessToken_hdr}
uri = 'https://api.ciscospark.com/v1/rooms'
resp = requests.get(uri, headers=spark_header)
print (json.dumps(resp.json(), indent=4, separators=(',', ': ')))
