from flask import Flask, jsonify

# Create the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/api/greet/<name>')
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)