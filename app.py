from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/dashboard-data')
def dashboard_data():
    data = {
        "user": {
            "name": "Alex Johnson",
            "status": "Premium Member",
            "avatar_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuDncb98cFnjTUG0_qZX9xj9aF7aaU2Kx4LnvpsHmCPt6nmhlTBNgkRstaP139-LTgs91QHlv4k6RJ6VO99FS4-hP1h5vPaxWIxEHL9l6zH6npd484TbP7ntUBQdpztKzZysRogUbaxCyGWEUlaEJpVuFNcF0BehGAq0HtN_T6tJqeXjDx9nbI8Kp0CqQ9ZVfFLtoGX2mAMLIb5Oqpa4vZSjt3yqQLaoxLVcGKbIkjmR4uIFWfFq-28xFW-Q5Yh_r-5mvz4V2DbQBXZe"
        },
        "metrics": {
            "readiness": {
                "score": 82,
                "trend": 5,
                "trend_label": "+5%"
            },
            "daily_goal": {
                "current": 2,
                "target": 3,
                "label": "2/3"
            },
            "performance": {
                "score": 78.5,
                "trend": 12,
                "trend_label": "12%"
            }
        },
        "skills": [
            {"name": "Aptitude", "score": 90, "color": "blue"},
            {"name": "Speaking", "score": 75, "color": "indigo"},
            {"name": "Listening", "score": 88, "color": "cyan"},
            {"name": "Reading", "score": 82, "color": "sky"}
        ],
        "reminders": {
            "next_session": "Tomorrow, 10:00 AM"
        },
        "recent_activity": [
            {
                "type": "Mock Interview: Tech Lead",
                "status": "Completed • Score: 88%",
                "icon": "check",
                "icon_bg": "primary"
            },
            {
                "type": "New Skill: Active Listening",
                "status": "Lesson finished • 20 mins ago",
                "icon": "history_edu",
                "icon_bg": "slate"
            }
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
