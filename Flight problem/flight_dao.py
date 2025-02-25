import pymysql

class Flight:
    def __init__(self, airline="", source="", destination="", duration="", id=None):
        self.id = id
        self.airline = airline
        self.source = source
        self.destination = destination
        self.duration = duration

    def to_dict(self):
        print(type(self.duration))
        return {
            'id': self.id,
            'airline': self.airline,
            'source': self.source,
            'destination': self.destination,
            'duration': str(self.duration)
        }

class Db_operations:
    def __init__(self):
        pass

    def connect_db(self):
        return pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            password='D@tteb@yo#106',
            database='jaishnav_db',
            charset='utf8',
            autocommit=True
        )

    def create_table(self):
        with self.connect_db() as connection:
            with connection.cursor() as cursor:
                cursor.execute('''CREATE TABLE IF NOT EXISTS Flights (
                                    id INT PRIMARY KEY AUTO_INCREMENT,
                                    airline VARCHAR(50) NOT NULL,
                                    source VARCHAR(50) NOT NULL,
                                    destination VARCHAR(50) NOT NULL,
                                    duration TIME NOT NULL
                                );''')
                cursor.execute("ALTER TABLE flights AUTO_INCREMENT = 1;")
                
        print('+----------------------------+') 
        print('| Table created successfully |')
        print('+----------------------------+') 

    def insert_row(self, flight):
        with self.connect_db() as connection:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO flights (airline, source, destination, duration) VALUES (%s, %s, %s, %s)',
                            (flight.airline, flight.source, flight.destination, flight.duration))
                print('+---------------------------+') 
                print('| Row inserted successfully |')
                print('+---------------------------+') 
                return cursor.lastrowid

    def search_row(self, id):
        with self.connect_db() as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT id, airline, source, destination, duration FROM flights WHERE id = %s', (id,))
                row = cursor.fetchone()
                return Flight(*row) if row else None

    def list_all_rows(self):
        with self.connect_db() as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT id, airline, source, destination, duration FROM flights')
                return cursor.fetchall()

    def update_row(self, flight):
        with self.connect_db() as connection:
            with connection.cursor() as cursor:
                cursor.execute('UPDATE flights SET airline = %s, source = %s, destination = %s, duration = %s WHERE id = %s',
                            (flight.airline, flight.source, flight.destination, flight.duration, flight.id))

    def delete_row(self, id):
        with self.connect_db() as connection:
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM flights WHERE id = %s', (id,))