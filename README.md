# Dockerized Expense Tracker API 🐳

A simple Expense Tracker REST API built with **Python and FastAPI**, and containerized using **Docker**.

This project was developed as a hands-on learning exercise to understand REST APIs, Docker images, containers, and application deployment fundamentals.

## Technologies Used

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn
- Docker
- Git and GitHub

## Features

- Welcome endpoint to verify that the API is running.
- Expense calculation endpoint that accepts multiple expenses.
- Automatic request validation using Pydantic.
- Interactive API documentation using Swagger UI.
- Containerized application that can run using Docker.

## Project Structure

```text
docker-expense-tracker/
├── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## API Endpoints

### GET /

Returns a welcome message.

```json
{
  "message": "Welcome to the Expense Tracker API"
}
```

### POST /calculate

Accepts a list of expenses and calculates their total.

Example request:

```json
[
  {"category": "Food", "amount": 80},
  {"category": "Transport", "amount": 50},
  {"category": "Internet", "amount": 30}
]
```

Example response:

```json
{
  "total_expenses": 3,
  "total_amount": 160.0,
  "currency": "GHS"
}
```

## Running the Application with Docker

### 1. Clone the repository

```bash
git clone https://github.com/adobea-dev/docker-expense-tracker.git
cd docker-expense-tracker
```

### 2. Build the Docker image

```bash
docker build -t expense-tracker:v1 .
```

### 3. Run the Docker container

```bash
docker run -d --name expense-container -p 8000:8000 expense-tracker:v1
```

### 4. Access the API

Open:

- API: http://localhost:8000
- Interactive documentation: http://localhost:8000/docs

### 5. Stop and remove the container

```bash
docker stop expense-container
docker rm expense-container
```

## Key Learning Outcomes

Through this project, I explored:

- The difference between Dockerfiles, Docker images, and containers.
- Writing Dockerfiles and building images.
- Container networking and port mapping.
- Running and inspecting containers.
- Using Git for version control and GitHub for code hosting.

## Future Improvements

- Store expense records in a database.
- Add endpoints to create, retrieve, update, and delete expenses.
- Introduce automated testing.
- Add Docker Compose for multi-service development.

## Acknowledgements

Built as part of my hands-on learning journey during the **Ishango Data & AI Industry Readiness Programme**.