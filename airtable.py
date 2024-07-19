import requests
AIRTABLE_BASE_ID = "appB6LFUMhkx681r3"
AIRTABLE_API_KEY = "patvOdvupRPT8kBRg.9caf5e416b2f998138cc403bbd375b52f8df131c2027e622da894813d5622403"
AIRTABLE_TABLE_NAME = "chatbot"
endpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"

headers = {
"Authorization": f"Bearer {AIRTABLE_API_KEY}",
"Content-Type": "application/json"
}
def save_rec(user_query,response,ip_address):
    data = {
  "records": [
          {
        "fields": {
            "IP_address": f"{ip_address}",
            "Query": f"{user_query}",
            "Response": f"{response}"
        }
        },
    ]
    }

    r = requests.post(endpoint, json=data , headers=headers)
    r.json()


if __name__ == '__main__':
    save_rec("hello","hi there","ip")
