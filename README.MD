# TME Flask Postgres Docker Setup Project

## Project Overview
This project utilizes Flask, TensorFlow, and Postgres to create a web application that performs image classification using a TensorFlow model served via Docker. The predictions and relevant data are stored in a Postgres database.

### Prerequisites
- Docker Desktop (for Windows users)
- Docker Compose

## Setup Instructions

1. **Install Docker**

   - For Windows users, install Docker Desktop.
   - For other platforms, ensure Docker is installed.

2. **unzip the project**

3. **Run Docker Services**

Navigate to the directory containing docker-compose.yml and run the following command:

```bash
docker-compose up -d
 this will create and start the Docker containers for TensorFlow serving and PostgreSQL.

4. **Setting Up the Database**

Access the PostgreSQL container:

```bash
docker exec -it postgres_db bash
 Connect to the database:

```bash
psql -U project project
 Create the project database:

```bash
CREATE DATABASE project;
 Create the predictions table:

```bash
sql
Copy code
CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    query VARCHAR(255),
    response VARCHAR(255),
    query_time TIMESTAMP,
    response_time TIMESTAMP
);
 To check the tables:

```sql
SELECT * FROM predictions;
 Running the Flask App

Install the required Python packages:

```bash
pip install -r requirements.txt
 Run the Flask application:

```bash
python app.py
