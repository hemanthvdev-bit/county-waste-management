
# County Waste Management System

A full-stack web application designed to help county administrations manage waste collection operations efficiently.

This system allows county administrators to manage residents, schedule waste pickups, assign routes to collection trucks, monitor complaints, and analyze waste collection data.

This project demonstrates backend API design, database modeling, authentication, and frontend integration using modern technologies.

---

# Features

## User Management
- Admin authentication using JWT
- Secure password hashing
- Role-based access control

## Resident Management
- Register residents
- Update resident information
- Assign zones and bin sizes
- Track resident pickup schedules

## Waste Pickup Scheduling
- Create waste pickup schedules
- Assign trucks to pickup routes
- Track pickup completion status

## Route Management
- Create and manage waste collection routes
- Assign trucks and drivers to routes
- Zone-based collection planning

## Truck Management
- Register trucks
- Assign drivers
- Track truck availability

## Complaint Management
- Residents can report waste issues
- Admin can resolve complaints
- Track complaint status

## Analytics Dashboard
- Total waste collected
- Daily pickup statistics
- Zone-based collection metrics
- Complaint analytics

---

# Tech Stack

## Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication
- Pydantic

## Frontend
- React
- Axios
- Tailwind CSS

## DevOps
- Docker
- Docker Compose

---

# System Architecture

Client (React)

↓

FastAPI REST API

↓

PostgreSQL Database

---

# Project Structure

county-waste-management
│
├── backend
│   ├── app
│   │   ├── api
│   │   │   └── routes
│   │   ├── models
│   │   ├── schemas
│   │   ├── services
│   │   ├── core
│   │   └── main.py
│
├── frontend
│   ├── src
│   │   ├── pages
│   │   ├── components
│   │   └── services
│
├── docker-compose.yml
├── README.md
└── .gitignore

---

# Setup Instructions

## Clone Repository

git clone https://github.com/YOUR_USERNAME/county-waste-management.git
cd county-waste-management

---

## Backend Setup

cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

Backend will run at:

http://localhost:8000

API docs:

http://localhost:8000/docs

---

## Frontend Setup

cd frontend
npm install
npm run dev

Frontend will run at:

http://localhost:5173

---

# API Endpoints

## Authentication

POST /auth/login  
POST /auth/register  

---

## Residents

GET /residents  
POST /residents  
PUT /residents/{id}  
DELETE /residents/{id}

---

## Waste Pickups

GET /pickups  
POST /pickups  
PUT /pickups/{id}

---

## Complaints

GET /complaints  
POST /complaints  
PUT /complaints/{id}

---

# Example Dashboard Metrics

- Total Residents
- Active Trucks
- Daily Pickups
- Pending Complaints
- Recycling Percentage

---

# Future Improvements

- Smart bin IoT integration
- Route optimization using AI
- GPS tracking for collection trucks
- Mobile app for drivers
- Predictive waste analytics


