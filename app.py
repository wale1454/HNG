from flask import Flask
from flask import request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask !'

@app.route("/api", methods=("GET", "POST"))
def Task_1_API():

    # Get slack_name and track from URL
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Time and Date
    day_of_week = datetime.today().strftime('%A')
    current_utc_time = datetime.utcnow()

    # Format the current time in the desired format
    formatted_time = current_utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    response = { "slack_name": slack_name,
                "current_day": day_of_week,
                "utc_time": formatted_time,
                "track": track,
                "github_file_url": "https://github.com/wale1454/HNG/blob/main/app.py",
                "github_repo_url": "https://github.com/wale1454/HNG",
                "status_code": 200            
    }

    return jsonify(response)

