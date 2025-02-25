from flask import Flask, jsonify, request
from flight_dao import Flight, Db_operations

flights = Db_operations()
flights.create_table()

app = Flask(__name__)

@app.route('/flights', methods=['POST'])
def create_person():
    body = request.get_json()
    flight = Flight(body['airline'], body['source'], body['destination'], body['duration'])
    flight.id = flights.insert_row(flight)
    return jsonify(flight.to_dict())

@app.route('/flights/<int:id>', methods=['GET'])
def get_person(id):
    flight = flights.search_row(id)
    return jsonify(flight.to_dict() if flight else {'message': 'Flight not found'})

@app.route('/flights', methods=['GET'])
def get_all_flights():
    all_rows = flights.list_all_rows()
    flights_list = []
    for row in all_rows:
        flight_obj = Flight(*row)
        flight_dict = flight_obj.to_dict()
        flights_list.append(flight_dict)
    return jsonify(flights_list)


@app.route('/flights/<int:id>', methods=['PUT'])
def update_person(id):
    body = request.get_json()
    flight = flights.search_row(id)
    if flight is None:
        return jsonify({'message': 'Flight not found'})
    flight.airline = body['airline']
    flight.source = body['source']
    flight.destination = body['destination']
    flight.duration = body['duration']
    flights.update_row(flight)
    return jsonify(flight.to_dict())

@app.route('/flights/<int:id>', methods=['DELETE'])
def delete_person(id):
    flight = flights.search_row(id)
    if flight is None:
        return jsonify({'message': 'Flight not found'})
    flights.delete_row(id)
    return jsonify({'message': 'Flight deleted'})

if __name__ == '__main__':
    app.run(debug=True)