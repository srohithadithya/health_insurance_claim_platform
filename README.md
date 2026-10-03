# Health & Insurance Routing Platform

A modern, highly efficient FastAPI-based platform that validates insurance details and provides a safe handoff to trusted eligibility and provider registries. It includes location-based routing to nearby network hospitals and specialists with a clean, minimal user interface.

## 🚀 Features

- **Insurance Validation:** Real-time insurance ID verification (supports Regex fallbacks).
- **Location-based Hospital Search:** Integrates with OpenStreetMap Overpass API for discovering nearby facilities.
- **Smart Routing & ETA:** Calculates travel time and distance utilizing the Open Source Routing Machine (OSRM).
- **Specialist Matching:** Automatically suggests relevant medical specialists based on health conditions.
- **Alternative Options:** Recommends alternative care options (e.g., telemedicine, urgent care, cash-pay) when necessary.
- **Interactive UI:** A highly intuitive, minimal, and mobile-responsive UI with a live Leaflet map.
- **High Efficiency Caching:** Built-in SQLite caching reduces redundant external API calls and ensures low latency.

## 📁 Project Structure

```
.
├── app/
│   ├── main.py          # Core FastAPI application with logic and routing
├── static/
│   ├── index.html       # Minimal and understandable UI with Leaflet integration
├── tests/
│   ├── test_main.py     # Pytest suite for endpoint and logic validation
├── cache.db             # Local SQLite database for caching
├── requirements.txt     # Python dependencies
└── README.md            # Technical documentation
```

## 🛠️ Setup & Installation

### Prerequisites

- Python 3.11 or higher
- Git

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set up a Virtual Environment:**
   ```bash
   python -m venv .venv
   
   # Windows
   .\.venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory:
   ```dotenv
   SQLITE_DB=cache.db
   NVIDIA_API_KEY=your_nvidia_api_key_here # Optional, for LLM-based verification
   ```

5. **Run the Application:**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the Platform:**
   Open your browser and navigate to `http://localhost:8000` to interact with the UI.

## 🧪 Testing

The project includes a suite of tests to ensure stability and proper functionality.

Run the tests using Pytest:
```bash
python -m pytest tests/
```

## ⚙️ Architecture & Technical Details

- **Backend:** FastAPI for high-performance async API handling. Pydantic is used for strict data validation.
- **Frontend:** Vanilla HTML/CSS/JS ensuring minimal overhead, rapid load times, and a highly understandable user experience. Leaflet.js handles the interactive map.
- **Caching:** SQLite is utilized to cache OSM and OSRM results, preventing unnecessary external requests for identical queries and improving efficiency.
- **Routing API:** OpenStreetMap (OSM) via Overpass API for mapping facilities, and OSRM for dynamic route generation.

## 🔒 Production Hardening (Next Steps)

If you plan to deploy this into a production environment, consider the following enhancements:

- **Trusted Registries:** Integrate real health facility and doctor registries (e.g., ABHA in India or NPPES in the US) to replace mock/fallback validation.
- **Security:** Add rate-limiting (e.g., via `slowapi`), enforce CORS policies, and deploy behind a reverse proxy (like NGINX or Caddy) with TLS/HTTPS.
- **Scale Cache:** Migrate from SQLite caching to Redis if scaling horizontally across multiple worker nodes.

## 📜 License
This project is open-source and available under the MIT License.
