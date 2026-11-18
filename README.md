# Smart Agriculture Monitoring System (AgriSense)

A beginner-friendly, software-only IoT mini-project demonstration built with Python Flask.

## Features
- Dashboard for soil moisture, temperature, humidity and rainfall.
- Simulated sensor readings that refresh every 15 seconds.
- Soil-condition status and basic irrigation advice.
- JSON API at `/api/readings`.
- Health-check endpoint at `/health`.
- Responsive dashboard for mobile and desktop.

## Important project note
This version uses **simulated sensor data**. It does not connect to a physical ESP32 or sensors. It is suitable for demonstrating the dashboard and application workflow online. To make it a real hardware IoT project later, connect an ESP32 and replace `generate_readings()` in `app.py` with authenticated sensor data.

## Deploy on Render using the website (no VS Code or terminal)
1. Download and extract this ZIP on your device.
2. Create a new public or private GitHub repository.
3. In the repository, choose **Add file → Upload files**.
4. Upload the extracted project files and folders (not just this ZIP archive). Make sure `app.py`, `requirements.txt`, `render.yaml`, `templates/` and `static/` are at the repository root.
5. Commit the uploaded files.
6. Sign in to Render and choose **New → Web Service**.
7. Connect GitHub and select this repository.
8. Render should detect `render.yaml`. If it asks for settings, use:
   - Runtime: Python
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
9. Click **Deploy Web Service** and wait for the build to finish.
10. Open the `onrender.com` URL shown by Render.

## Run locally (optional)
Install dependencies with `pip install -r requirements.txt`, then run `python app.py`.

## API
- `GET /` — dashboard
- `GET /api/readings` — latest simulated sensor readings as JSON
- `GET /health` — service health status

## Suggested mini-project explanation
The system simulates IoT sensor readings from a farm and displays them on a web dashboard. The application evaluates soil moisture and gives an irrigation suggestion. A future hardware version can send real sensor readings from an ESP32 to the Flask API.
