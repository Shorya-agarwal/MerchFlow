# MerchFlow: Product Lifecycle Dashboard

![Status](https://img.shields.io/badge/Status-Active-success)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![Tests](https://img.shields.io/badge/Coverage-90%25-green)
![Tech Stack](https://img.shields.io/badge/Stack-React%20|%20FastAPI%20|%20AI-blue)

## 🚀 Executive Summary
**MerchFlow** is an internal merchandising tool designed to streamline product inventory management. By leveraging **Generative AI (Google Gemini)**, the system automatically classifies product materials based on SKU descriptions, reducing manual data entry errors. The project demonstrates a modern full-stack architecture with a strong emphasis on **Test-Driven Development (TDD)** and **End-to-End (E2E) automation**.

---

## 🏗 System Architecture

The application follows a decoupled client-server architecture. The frontend communicates with a RESTful API, which orchestrates logic between the database and the external AI service.

```mermaid
graph TD
    %% Nodes
    User((User))
    FE[Frontend SPA<br/>(React + Vite)]
    BE[Backend API<br/>(FastAPI)]
    DB[(Database<br/>SQLite)]
    AI[AI Service<br/>(Google Gemini)]

    %% Edges
    User -->|Interacts| FE
    FE -->|HTTP JSON| BE
    BE -->|Classify SKU| AI
    AI -->|Material Tags| BE
    BE -->|Read/Write| DB
    DB -->|Data| BE
    BE -->|Response| FE
```

## ✨ Key Features

### 1. Smart Inventory Management: 
Real-time tracking of Product SKUs and Stock Counts.

### 2. AI-Driven Auto-Tagging:
Automatically detects material types (e.g., "Leather", "Mesh", "Knit") from product names using LLMs.

### 3. Dashboard Analytics: 
Visual indicators for stock levels (In Stock / Out of Stock).

### 4. Robust Testing Suite:

* #### Unit Testing: Jest for frontend logic.

* #### Integration Testing: Pytest for backend API endpoints.

* #### E2E Testing: Cypress for full user journey simulation.


## 🛠️ Installation & Setup

### Prerequisites
* Node.js & npm
* Python 3.10+
* Docker Desktop

### 1. Database Setup
```bash
docker-compose up -d
# Starts PostgreSQL on port 5432
```
### 2. Backend Setup
``` bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure Environment Variables
# Create a .env file in /backend and add:
# GEMINI_API_KEY=your_api_key_here

# Start the Server
uvicorn main:app --reload
```
Server runs on: http://127.0.0.1:8000


### 3.Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Client runs on: http://localhost:5173

## 🧪 Testing Strategy
This project adheres to rigorous testing standards to ensure reliability in a production-like environment.

## 🟢 Unit Tests (Jest)
Verifies individual component logic and utility functions
```bash
cd frontend
npm run test:unit
```
## 🔵 Integration Tests (Pytest)
Ensures API endpoints correctly process data and interact with the database.
```bash
cd backend
pytest
```
## 🟠 End-to-End Tests (Cypress)
Simulates a real user flow: opening the app, typing a product name, and verifying the dashboard updates.
```bash

cd frontend
npx cypress open
# Select E2E Testing -> Start E2E in Chrome
```
## 📂 Project Structure
```PlainText
merchflow/
├── backend/
│   ├── main.py              # API Entry point
│   ├── models.py            # SQLAlchemy Database Models
│   ├── ai_service.py        # Gemini AI Integration Logic
│   ├── test_main.py         # API Integration Tests
│   └── requirements.txt     # Python Dependencies
├── frontend/
│   ├── src/
│   │   ├── components/      # Reusable React Components
│   │   ├── App.jsx          # Main Dashboard Layout
│   │   └── product.test.js  # Jest Unit Tests
│   ├── cypress/             # E2E Test Specifications
│   └── package.json         # Node Dependencies
└── README.md                # Project Documentation
```


## 🔮 Future Roadmap
* **Authentication:** Implement JWT-based login for secure access.
* **Anomaly Detection:** Using Isolation Forests (Scikit-Learn) to flag fraudulent transactions.
* **CI/CD:** GitHub Actions pipeline for automated testing.

