import requests
ACCESS_TOKEN = ""
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

# search for events with "library" in title/description, in Texas cities
url = "https://www.eventbriteapi.com/v3/events/search"
cities = ["Dallas, TX", "Houston, TX", "Austin, TX", "San Antonio, TX"]

for city in cities:
    params = {
        "q": "library",
        "location.address": city,
        "expand": "venue,category"
    }

    response = requests.get(url, headers=headers, params=params)

    print(f"\n===== Results for {city} =====")
    if response.status_code == 200:
        data = response.json()
        events = data.get("events", [])
        if not events:
            print("No events found.")
        for e in events:
            print("Title:", e["name"]["text"])
            print("Category:", e.get("category", {}).get("name"))
            venue = e.get("venue")
            if venue:
                print("Location:", venue["address"]["localized_address_display"])
            print("Start:", e["start"]["local"])
            print("------")
    else:
        print("Error:", response.status_code, response.text[:500])