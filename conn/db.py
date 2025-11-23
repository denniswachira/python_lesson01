import psycopg2

class RoomRepository:
    def __init__(self, config):
        self.conn = psycopg2.connect(
            host=config["host"],
            database=config["dbname"],
            user=config["user"],
            password=config["password"]
        )

    def get_rooms(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, capacity, available FROM rooms ORDER BY id")
        rows = cursor.fetchall()
        cursor.close()

        rooms = []
        for r in rows:
            rooms.append({
                "id": r[0],
                "name": r[1],
                "capacity": r[2],
                "available": r[3]
            })
        return rooms

