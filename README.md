# Gdańsk Smart City Map

> **Project created during the "Best Coding Marathon" Hackathon.**

## About The Project
This application is a Smart City prototype designed for the city of Gdańsk. It integrates statistical data, cultural events, and city infrastructure into a single interactive map. The goal was not only to visualize data but also to engage citizens by allowing them to propose changes to the urban space.

The system combines a modern frontend with a robust data pipeline powered by Python and Dockerized PostgreSQL.

---

## Key Features

### Interactive Dashboard
* **Dynamic Map:** Built with **Leaflet**, featuring custom layers for city districts.
* **District Analytics:** Clickable zones displaying key statistics (population density, service availability).

### Real-Time Data & Infrastructure
* **Cultural Events:** Latest events in Gdańsk, automatically scraped from external websites using **Python**.
* **City Infrastructure:** Visualization of public spaces, parking lots, and cultural venues fetched via external APIs.

### Citizen Engagement (Crowdsourcing)
* **Interactive Suggestions:** Users can drop pins on the map to suggest new facilities (e.g., "We need a bench here").
* **Community Driven:** Visualizes the needs of local residents in real-time.

---

## Tech Stack

We used a microservices-oriented approach to separate data collection from the presentation layer.

### Frontend
* **Framework:** [Next.js](https://nextjs.org/), React
* **Language:** TypeScript
* **Maps:** Leaflet / React-Leaflet
* **Styling:** CSS Modules

### Backend & Data Pipeline
* **Data Scraper:** Python (BeautifulSoup) - scrapes event data.
* **Data Aggregation:** Python scripts fetching POI data (parking, culture) from external APIs.
* **Database:** PostgreSQL
* **DevOps:** Docker (containerized database instance).

---

## Architecture & Data Flow

1.  **Data Ingestion:** Python scripts scrape event websites and query public APIs for infrastructure data.
2.  **Storage:** Cleaned data is pushed to a **PostgreSQL** database running in a **Docker** container.
3.  **Presentation:** The **Next.js** application fetches data from the database and renders it on the **Leaflet** map.

---

## Getting Started

To run this project locally, you need Node.js, Python, and Docker installed.

### 1. Database Setup
Start the PostgreSQL container:
```bash
# Inside the root directory
docker-compose up -d
```

### 2. Data Population (Python)
```bash
cd python_backend
python main.py
python muzeum.py
cd ..
```

### 3. Frontend Setup
```bash
npm install
npm run dev
```