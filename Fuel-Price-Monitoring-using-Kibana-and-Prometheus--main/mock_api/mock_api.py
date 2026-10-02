from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/v1/prices")
def prices():
    return jsonify({
        "prices": [
            {
                "city": "Mumbai",
                "fuel_type": "Petrol",
                "price": round(random.uniform(104, 110), 2)
            },
            {
                "city": "Mumbai",
                "fuel_type": "Diesel",
                "price": round(random.uniform(92, 98), 2)
            },
            {
                "city": "Bengaluru",
                "fuel_type": "Petrol",
                "price": round(random.uniform(100, 108), 2)
            },
            {
                "city": "Bengaluru",
                "fuel_type": "Diesel",
                "price": round(random.uniform(88, 96), 2)
            },
            {
                "city": "Mysuru",
                "fuel_type": "Petrol",
                "price": round(random.uniform(100, 108), 2)
            },
            {
                "city": "Mysuru",
                "fuel_type": "Diesel",
                "price": round(random.uniform(88, 96), 2)
            }
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)