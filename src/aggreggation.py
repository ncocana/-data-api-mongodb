import requests
import json
url = "https://data.mongodb-api.com/app/data-ivdit/endpoint/data/v1/action/aggregate"

payload = json.dumps({
    "collection": "bikes",
    "database": "rental_bikes",
    "dataSource": "Sandbox",
    "pipeline": [{"$group": {"_id": "$type", "count": {"$sum":1}}},
                { "$sort": { "count": 1 } }]
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': '6NFpzs43ERy96QMn8io03GXFuUPteyDRDb0cMzBLIe2ya0TOLsu9CzhtMx24hhAZ', 
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)