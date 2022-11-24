import requests
import json
url = "https://data.mongodb-api.com/app/data-nxnpm/endpoint/data/v1/action/aggregate"
payload = json.dumps({
    "collection": "bikes",
    "database": "rental_bikes",
    "dataSource": "SANDBOXX",
    "pipeline": [{"$group": {"_id": "$characteristics.min_age"}}]})
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': "taIj5LjbfEgsNcnWAtCfctE9wGgPZzub4XCT9bex1nbLA9VHMhKhrsRGvbd7iE51",
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)