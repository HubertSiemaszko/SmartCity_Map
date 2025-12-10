import requests
import json

url = [
    "https://api.geoapify.com/v2/places?categories=entertainment&filter=place:5173199c4fec9c3240593de474c0752f4b40f00101f9016da2270000000000c00206920307476461c584736b&lang=en&limit=50&apiKey=41329cb7076540aba52794f7226b2e21",
    "https://api.geoapify.com/v2/places?categories=parking&filter=place:5173199c4fec9c3240593de474c0752f4b40f00101f9016da2270000000000c00206920307476461c584736b&lang=en&limit=50&apiKey=41329cb7076540aba52794f7226b2e21",
    "https://api.geoapify.com/v2/places?categories=activity&filter=place:5173199c4fec9c3240593de474c0752f4b40f00101f9016da2270000000000c00206920307476461c584736b&lang=en&limit=50&apiKey=41329cb7076540aba52794f7226b2e21",
    "https://api.geoapify.com/v2/places?categories=education&filter=place:5173199c4fec9c3240593de474c0752f4b40f00101f9016da2270000000000c00206920307476461c584736b&lang=en&limit=50&apiKey=41329cb7076540aba52794f7226b2e21"
]

results = []
categoryArray = ["entertainment", "parking", "activity", "education"]

for link in url:
    response = requests.get(link).json()

    for f in response.get("features", []):
        p = f.get("properties", {})

        feature_categories = p.get("categories", [])

        matched_categories = [
            c for c in feature_categories if c in categoryArray
        ]

        if matched_categories:
            results.append({
                "name": p.get("name"),
                "lat": p.get("lat"),
                "lon": p.get("lon"),
                "categories": matched_categories
            })

print(results)
json_str = json.dumps(results, ensure_ascii=False, indent=2)
