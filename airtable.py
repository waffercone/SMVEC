import requests
AIRTABLE_BASE_ID = "appjrOltyQk231hcd"
AIRTABLE_API_KEY = "patMrEIyQnnfwMI1I.18eef26ab44daafc0538c0c0e4f107ee7295be52699eb666d2b61db0cb210c04"
AIRTABLE_TABLE_NAME = "chatbot"
endpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"

headers = {
"Authorization": f"Bearer {AIRTABLE_API_KEY}",
"Content-Type": "application/json"
}
def save_rec(user_query,response):
    data = {
  "records": [
          {
        "fields": {
            "Query": f"{user_query}",
            "Response": f"{response}"
        }
        },
    ]
    }

    r = requests.post(endpoint, json=data , headers=headers)
    r.json()


if __name__ == '__main__':
    save_rec("hello","hi there")