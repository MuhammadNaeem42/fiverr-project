from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import model

# Import the Prediction class from models
from models import Prediction

# Initialize Flask app
app = Flask(__name__, template_folder='Template')
Bootstrap(app)

# Initialize SQLAlchemy
Base = declarative_base()
engine = create_engine('postgresql://project:project@localhost:5432/project')  # Replace with your actual credentials
Session = sessionmaker(bind=engine)
session = Session()

# Connect to the PostgreSQL database
Base.metadata.create_all(engine)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
            class_name = model.get_prediction(image_path)

            # Store data in PostgreSQL database using SQLAlchemy
            query_time = datetime.now()
            new_prediction = Prediction(
                query=image_path,
                response=class_name,
                query_time=query_time,
                response_time=datetime.now()  # Update this with an appropriate value
            )
            try:
                session.add(new_prediction)
                session.commit()
                print("Data successfully stored in the database!")
            except Exception as e:
                session.rollback()
                print(f"Error: {e}")

            result = {
                'class_name': class_name,
                'image_path': image_path,
                'query': image_path,
                'response' : class_name,
                "query_time" : query_time,
                "response_time" : new_prediction.response_time,
            }
            return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

