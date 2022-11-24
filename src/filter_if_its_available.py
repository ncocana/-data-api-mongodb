import requests
import json
url = "https://data.mongodb-api.com/app/data-ivdit/endpoint/data/v1/action/find"

payload = json.dumps({
    "collection": "bikes",
    "database": "rental_bikes",
    "dataSource": "Sandbox",
    "filter": {"avalaibility":True},
    "projection": {"_id":0, "type":1, "avalaibility":1, "price_of_rent_per_hour":1}
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': '6NFpzs43ERy96QMn8io03GXFuUPteyDRDb0cMzBLIe2ya0TOLsu9CzhtMx24hhAZ', 
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)