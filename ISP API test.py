import requests
import json
def trigger_api(ip):
  querystring = {"ip": ip}
  headers = {
          'x-rapidapi-host': "geoplugin.p.rapidapi.com",
          'x-rapidapi-key': RAPIDAPI_KEY
        }
  url = "https://geoplugin.p.rapidapi.com/ip/json.gp"
  response = requests.request("GET", url, headers=headers, params=querystring)
  if(200 == response.status_code):
    return json.loads(response.text)
  else:
    return None