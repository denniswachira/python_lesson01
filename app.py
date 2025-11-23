from flask import Flask, render_template
from conn.db import RoomRepository
from config.db_config import DB_CONFIG

app = Flask(__name__)

# Read db configuration from external file
repo = RoomRepository(DB_CONFIG)

@app.route("/")
def show_rooms():
    rooms = repo.get_rooms()
    return render_template("rooms.html", rooms=rooms)

if __name__ == "__main__":
    app.run(debug=True)
