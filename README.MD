markdown
Copy code
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

2. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
Run Docker Services

Navigate to the directory containing docker-compose.yml and run the following command:

bash
Copy code
docker-compose up -d
This will create and start the Docker containers for TensorFlow serving and PostgreSQL.

Setting Up the Database

Access the PostgreSQL container:

bash
Copy code
docker exec -it postgres_db bash
Connect to the database:

bash
Copy code
psql -U project project
Create the project database:

sql
Copy code
CREATE DATABASE project;
Create the predictions table:

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

sql
Copy code
SELECT * FROM predictions;
Running the Flask App

Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Run the Flask application:

bash
Copy code
python app.py
Project Structure
Flask App (app.py)

The Flask application for image classification and database interaction.

TensorFlow Serving (docker-compose.yml)

Docker Compose file for setting up TensorFlow serving and PostgreSQL.

Model Files

The TensorFlow model files are expected to be present in the ./pets/1 directory.

Database (postgres_db)

The PostgreSQL database container.

Custom Network (my_network)

A custom Docker network to connect the services.

Static Files

Uploaded images and other static assets are stored in the static directory.

Using the App
Access the application at http://localhost:5000 in your web browser.
Upload an image for classification.
The app will classify the image and store the prediction and relevant data in the database.
