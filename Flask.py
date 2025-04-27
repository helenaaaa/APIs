from flask import Flask, jsonify, request

app = Flask(__name__)

# Root endpoint
@app.route("/", methods=["GET"])
def read_root():
    return jsonify({"Hello": "World"})

# Endpoint with a path parameter
@app.route("/items/<int:item_id>", methods=["GET"])
def read_item(item_id):
    return jsonify({"item_id": item_id})

# Endpoint with a query parameter
@app.route("/search/", methods=["GET"])
def search_items():
    query = request.args.get('query')  # get query parameter
    return jsonify({"query": query})

# Endpoint that accepts JSON body via POST
@app.route("/items/", methods=["POST"])
def create_item():
    item = request.get_json()  # get JSON payload
    return jsonify(item)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
