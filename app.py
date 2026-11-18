from flask import Flask, render_template, jsonify
from datetime import datetime, timezone
import random
import os

app = Flask(__name__)

# Software simulation: replace this function with real sensor readings when hardware is added.
def generate_readings():
    return {
        "soil_moisture": round(random.uniform(25, 85), 1),
        "temperature": round(random.uniform(20, 38), 1),
        "humidity": round(random.uniform(35, 90), 1),
        "rainfall": round(random.uniform(0, 12), 1),
        "updated_at": datetime.now(timezone.utc).astimezone().strftime("%d %b %Y, %I:%M:%S %p")
    }

def get_status(data):
    moisture = data["soil_moisture"]
    if moisture < 35:
        return {"label": "Needs watering", "class": "warning",
                "advice": "Soil moisture is low. Consider starting irrigation."}
    if moisture > 75:
        return {"label": "Soil is very wet", "class": "info",
                "advice": "Soil moisture is high. Avoid additional watering for now."}
    return {"label": "Healthy conditions", "class": "good",
            "advice": "Soil moisture is within the target range."}

@app.route("/")
def home():
    readings = generate_readings()
    return render_template("index.html", readings=readings, status=get_status(readings))

@app.route("/api/readings")
def api_readings():
    readings = generate_readings()
    readings["status"] = get_status(readings)
    return jsonify(readings)

@app.route("/health")
def health():
    return jsonify({"status": "ok", "application": "Smart Agriculture Monitoring System"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
