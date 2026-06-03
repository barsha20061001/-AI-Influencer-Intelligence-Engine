# AI Influencer Intelligence Engine

An AI-powered influencer analysis platform that evaluates influencer profiles, calculates performance scores, and recommends suitable brand collaborations. The system analyzes engagement, audience demographics, authenticity, growth trends, and niche relevance to generate actionable insights for brands and marketers.

## Live Demo

**Frontend:**  
https://ai-influencer-intelligence-engine.vercel.app/

**Backend API:**  
https://ai-influencer-intelligence-engine.onrender.com/

**API Endpoint:**  
https://ai-influencer-intelligence-engine.onrender.com/influencers

---

## Presentation Deck

https://drive.google.com/file/d/1U1mQJw6OC_UZlEHpexaIpaj6rYKNB7pv/view?usp=drivesdk

---

## Demo Video

https://drive.google.com/file/d/1Sm4PIzmMrtPZagIFCfeUpIVRkrcvtygj/view?usp=drivesdk

---


## Features

- AI-based influencer scoring system
- Audience analysis and demographic insights
- Authenticity score calculation
- Growth score evaluation
- Brand recommendation engine
- Influencer ranking and comparison
- REST API powered backend
- Responsive React frontend
- Cross-origin API integration

---

## Tech Stack

### Frontend
- React.js
- Vite
- JavaScript
- CSS

### Backend
- Python
- FastAPI
- Uvicorn

### Data & AI
- Pandas
- NumPy
- Scikit-Learn

### Deployment
- Vercel
- Render
- GitHub

---

## Project Structure

```text
AI-Influencer-Intelligence-Engine/
│
├── backend/
│   ├── services/
│   │   ├── authenticity_service.py
│   │   ├── brand_service.py
│   │   ├── data_service.py
│   │   ├── growth_service.py
│   │   ├── ml_service.py
│   │   └── score_service.py
│   │
│   ├── data/
│   │   └── influencers.csv
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   └── package.json
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/barsha20061001/-AI-Influencer-Intelligence-Engine.git
cd -AI-Influencer-Intelligence-Engine
```

### Backend Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at:

```text
http://localhost:8000
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

## API Endpoints

### Home

```http
GET /
```

Response:

```json
{
  "message": "Ratefluencer AI Backend is running"
}
```

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

### Influencers

```http
GET /influencers
```

Returns analyzed influencer data including:

- Ratefluencer Score
- Authenticity Score
- Growth Score
- Brand Match Score
- Recommended Brand
- Audience Details
- Engagement Metrics

---

## Scoring Logic

### Authenticity Score
- Engagement consistency
- Audience quality
- Activity metrics

### Growth Score
- Audience expansion
- Growth trends
- Content performance

### Brand Match Score
- Niche alignment
- Audience demographics
- Category relevance

### Final Ratefluencer Score
Combines:
- Authenticity
- Growth
- Brand relevance
- Engagement metrics

to generate the final influencer rating.

---

## Sample Output

```json
{
  "username": "techguru",
  "followers": 120000,
  "best_brand": "Apple",
  "brand_match_score": 70,
  "ratefluencer_score": 74
}
```

---

## Future Improvements

- Real social media API integration
- Advanced machine learning models
- Influencer comparison dashboard
- Campaign performance prediction
- Real-time analytics
- Export reports as PDF/CSV

---

## Author

**Barsha Mondal**

GitHub: https://github.com/barsha20061001

**Harsh Sahu**

GitHub: https://github.com/hsahu1726

---

## License

This project was developed as part of the RateInfluencer Hackathon submission. It is intended solely for hackathon evaluation, learning, research, and demonstration purposes. The project is not an official product of RateInfluencer and is not intended for commercial deployment without appropriate review, testing, and authorization.
