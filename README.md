# RestAPI-Python
# Ensure you have flask installed
pip3 install Flask
# Run the program
python app.py
# Test the server
curl -X GET http://127.0.0.1:5000/api/items
curl -X POST http://127.0.0.1:5000/api/items -H "Content-Type: application/json" -d '{"name": "Item 1"}'
