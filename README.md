# HTML to PDF Service (FastAPI + WeasyPrint)

A lightweight Dockerized FastAPI microservice that converts HTML strings into PDF files using WeasyPrint. Designed for use in automation pipelines (e.g., n8n), backend services, or programmatic PDF generation.

---

## Features

- Convert raw HTML → PDF via REST API  
- FastAPI backend with a single `/html-to-pdf` POST endpoint  
- WeasyPrint for clean, consistent typographic rendering  
- Dockerized for easy deployment on any Linux server  
- Ideal for services like Megyk Books summary PDFs or similar content

---

## Requirements

- Docker
- Docker Compose

---

## Quick Start

Build and run the service:

docker compose up --build -d

arduino
Copy code

Service will be available at:

http://localhost:8000/html-to-pdf

yaml
Copy code

---

## API Usage

**POST /html-to-pdf**

Send an HTML string and receive a PDF file.

**Request (JSON):**
{
"html": "<h1>Hello World</h1><p>Generated PDF</p>"
}

markdown
Copy code

**Example cURL:**
curl -X POST http://localhost:8000/html-to-pdf
-H "Content-Type: application/json"
-d '{ "html": "<h1>Test</h1>" }'
--output test.pdf

yaml
Copy code

---

## Project Structure

.
├── app.py # FastAPI app
├── Dockerfile # WeasyPrint + FastAPI image
├── docker-compose.yml # Container orchestration
└── README.md

yaml
Copy code

---

## Environment Variables (optional)

Not required, but you may define:

- `API_KEY` — Require a header for requests
- `PORT` — Change FastAPI port (default 8000)

---

## Deployment

Deploy on any Linux server (DigitalOcean, Lightsail, VPS):

docker compose up --build -d

css
Copy code

To view logs:

docker compose logs -f

css
Copy code

To restart:

docker compose restart

yaml
Copy code

---

## License

MIT License
