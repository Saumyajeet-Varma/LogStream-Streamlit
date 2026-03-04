# LogStream

**LogStream** is a proffessional, Dockerized web dashboard built in Python and Streamlit. It allows you to fetch logs from public URL, parse them using fuzzy date logic, filter by specific keywords, and export the results in multiple format.

---

## Key Features

- **Smart Fetching:** Automatically extracts timestamps from raw text lines using fuzzy logic.
- **Live Keyword Filtering:** Instantly isolate errors, specific User IDs, or IP addresses.
- **Dynamic Export:** Download your filtered results as **CSV**, **JSON**, or **TXT**.
- **Standardized Naming:** Downloads are automatically named using the format:  
    `URL-FromDate-ToTime.ext` (e.g., `api_site_com-20260301-1542.csv`).
- **Production Ready:** Fully containerized with Docker and optimized for small image size.

---

## Project Structure

```md
logstream-streamlit/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
└── README.md
```

---

## Quick Start

### 1. Using Docker (Recommended)
The easiest way to run the app is Docker Compose. This handles all dependencies for you.

```bash
# Clone the repository
git clone [https://github.com/Saumyajeet-Varma/logstream-streamlit.git](https://github.com/Saumyajeet-Varma/logstream-streamlit.git)
cd logstream-streamlit

# Build and start the container
docker-compose up --build
```

> Navigate to `http://localhost:8501` in your browser.

### 2. Manual Installation
If you preferto run it locally without Docker.

```bash
```bash
# Clone the repository
git clone [https://github.com/Saumyajeet-Varma/logstream-streamlit.git](https://github.com/Saumyajeet-Varma/logstream-streamlit.git)
cd logstream-streamlit

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app/main.py
```

