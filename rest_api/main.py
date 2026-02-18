"""
Flask Travel Destinations API

A simple REST API for managing travel destinations.
Supports CRUD operations with SQLite database.

Run with: python main.py
Test with: curl http://127.0.0.1:5000/destinations
"""

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"
db = SQLAlchemy(app)


class Destination(db.Model):
    """Database model for travel destinations."""
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert destination to dictionary for JSON response."""
        return {
            "id": self.id,
            "destination": self.destination,
            "country": self.country,
            "rating": self.rating
        }


# Create database tables
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    """Root endpoint - API welcome message."""
    return jsonify({"message": "Welcome to Travel Destinations API"})


@app.route("/destinations", methods=["GET"])
def get_destinations():
    """Get all travel destinations."""
    destinations = Destination.query.all()
    return jsonify([destination.to_dict() for destination in destinations])


@app.route("/destinations/<int:destination_id>", methods=["GET"])
def get_destination(destination_id):
    """Get a specific destination by ID."""
    destination = Destination.query.get(destination_id)
    if destination:
        return jsonify(destination.to_dict())
    return jsonify({"error": "Destination not found"}), 404


@app.route("/destinations", methods=["POST"])
def add_destination():
    """Add a new destination.
    
    Expected JSON:
    {
        "destination": "Paris",
        "country": "France", 
        "rating": 4.8
    }
    """
    data = request.get_json()
    new_destination = Destination(
        destination=data["destination"],
        country=data["country"],
        rating=data["rating"]
    )
    db.session.add(new_destination)
    db.session.commit()
    return jsonify(new_destination.to_dict()), 201


@app.route("/destinations/<int:destination_id>", methods=["PUT"])
def update_destination(destination_id):
    """Update an existing destination."""
    data = request.get_json()
    destination = Destination.query.get(destination_id)
    
    if destination:
        destination.destination = data.get("destination", destination.destination)
        destination.country = data.get("country", destination.country)
        destination.rating = data.get("rating", destination.rating)
        db.session.commit()
        return jsonify(destination.to_dict())
    
    return jsonify({"error": "Destination not found"}), 404


@app.route("/destinations/<int:destination_id>", methods=["DELETE"])
def delete_destination(destination_id):
    """Delete a destination."""
    destination = Destination.query.get(destination_id)
    
    if destination:
        db.session.delete(destination)
        db.session.commit()
        return jsonify({"message": "Destination deleted successfully"})
    
    return jsonify({"error": "Destination not found"}), 404


if __name__ == "__main__":
    # Run the Flask development server
    app.run(debug=True)
