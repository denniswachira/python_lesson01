Rooms Flask App

This is a simple Flask web application that displays a list of rooms stored in a PostgreSQL database. The project separates the Flask app, database connection, and configuration into different files for easier management.

How to Run

Install the required packages:
pip install flask psycopg2-binary

Update your database settings in:
config/db_config.py

Create the rooms table in your PostgreSQL database:
db.sql

Run the application:
python app.py

Open your browser and go to:
http://127.0.0.1:5000/
