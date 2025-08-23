# import requests

# ACCESS_TOKEN = "OAUTH-"
# headers = {
#     "Authorization": f"Bearer {ACCESS_TOKEN}"
# }

# # search for events with "library" in title/description, in Texas cities
# url = "https://www.eventbriteapi.com/v3/events/search/"
# params = {
#     "q": "library",
#     "location.address": "Dallas, TX",
#     "expand": "venue,category"
# }

# response = requests.get(url, headers=headers, params=params)
# if response.status_code == 200:
#     data = response.json()
#     events = data.get("events", [])
#     for e in events:
#         print("Title:", e["name"]["text"])
#         print("Category:", e.get("category", {}).get("name"))
#         venue = e.get("venue")
#         if venue:
#             print("Location:", venue["address"]["localized_address_display"])
#         print("Start:", e["start"]["local"])
#         print("------")
# else:
#     print("Error:", response.status_code, response.text[:500])

import requests
ACCESS_TOKEN = ""
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

url = "https://www.eventbriteapi.com/v3/users/me/?token=2IKDGJHGIK7D2ACOC7DJ"
response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print(response.text)