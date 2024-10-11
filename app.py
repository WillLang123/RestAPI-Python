from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (in-memory storage)
data = []

# Route for getting all items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(data), 200

# Route for adding a new item
@app.route('/api/items', methods=['POST'])
def add_item():
    new_item = request.json  # Get the JSON data from the request
    if not new_item or 'name' not in new_item:
        return jsonify({'error': 'Bad Request: Missing name'}), 400
    
    data.append(new_item)  # Add the new item to the list
    return jsonify(new_item), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
