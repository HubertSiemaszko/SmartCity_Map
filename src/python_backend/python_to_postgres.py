import psycopg2
import json
from muzeum import json_str
from main import json_str_events
from dotenv import load_dotenv
json_data = json.loads(json_str)
json_data_events = json.loads(json_str_events)


load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
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