import pymysql

def connect_db():
    try:
        connection = pymysql.Connect(host='localhost', port=3306, user='root', password='Root123', database='nithin_db', charset='utf8')
        print('DB connected')
        return connection
    except:
        print('DB connection failed')

def disconnect_db(connection):
    try:
        connection.close()
        print('DB dis-connected')
    except:
        print('Error while disconnecting DB')

def create_db():
    connection = connect_db()
    query = 'create database IF NOT EXISTS nithin_db;'
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    print('DB created')
    disconnect_db(connection)

def create_table():
    connection = connect_db()
    query = "create table IF NOT EXISTS persons(id int primary key auto_increment, name varchar(32) not null, gender char check(gender in('m','M', 'f','F')), location varchar(32), dob date);"
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    print('Table created')
    disconnect_db(connection)

def read_person_details():
    name = input('Enter person name: ')
    gender = input('Enter person gender: ')[0]
    location = input('Enter person location: ')
    dob = input('Enter person date of borth(yyyy-mm-dd): ')
    return (name, gender, location, dob)

def insert_row():
    person = read_person_details()
    print(person)
    query = 'insert into persons(name, gender, location, dob) values(%s, %s, %s, %s);'
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(query, person)
    connection.commit()
    cursor.close()
    disconnect_db(connection)

def update_row():
    new_location = input('Enter new location of the person: ')
    id = int(input('Enter Id of the person to update the location: '))
    query = f'update persons set location = {new_location} where id = {id}'
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    disconnect_db(connection)

def update_row():
    id = int(input('Enter Id of the person to delete: '))
    query = f'delete from persons where id = {id}'
    connection = connect_db()
    cursor = connection.cursor()
    count = cursor.execute(query)
    if count == 0:
        print(f'Person with id = {id} not found')
    else:
        print(f'Person with id = {id} deleted')
    connection.commit()
    cursor.close()
    disconnect_db(connection)