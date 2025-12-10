import psycopg2
import json
from muzeum import json_str
from main import json_str_events

json_data = json.loads(json_str)
json_data_events = json.loads(json_str_events)


conn = psycopg2.connect(
    dbname="postgres",
    user="admin",
    password="admin",
    host="172.16.177.20",
    port=5432
)

cur = conn.cursor()

query = """
        INSERT INTO "Point" (name, latitude, longitude, category)
        VALUES (%s, %s, %s, %s)
        """

for item in json_data:
    if not item["name"]:
        continue

    values = (
        item["name"],
        item["lat"],
        item["lon"],
        item["categories"]
    )
    cur.execute(query, values)


query_events = """
               INSERT INTO "Event" (name, latitude, longitude, place, time)
               VALUES (%s, %s, %s, %s, %s) \
               """

for item in json_data_events:
    if not item["lat"] or not item["lon"]:
        continue

    values = (
        item["name"],
        item["lat"],
        item["lon"],
        item["place"],
        item["date"]
    )
    cur.execute(query_events, values)

conn.commit()
cur.close()
conn.close()