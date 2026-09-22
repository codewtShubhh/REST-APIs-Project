from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Shubham", "email": "shubham@example.com"},
    {"id": 2, "name": "Rahul", "email": "rahul@example.com"},
]


@app.route("/")
def home():
    return {"success": True, "message": "REST API Server is Running!"}


@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify({"success": True, "users": users})


@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify({"success": True, "user": user})

    return jsonify({"success": False, "message": "User not found"}), 404


@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"success": False, "message": "Request Body is Required"}), 400

    if "name" not in data or "email" not in data:
        return (
            jsonify({"success": False, "message": "Name and email are required"}),
            400,
        )

    new_user = {"id": len(users) + 1, "name": data["name"], "email": data["email"]}

    users.append(new_user)

    return (
        jsonify(
            {"success": True, "message": "User created successfully", "user": new_user}
        ),
        201,
    )


jobs = [
    {"id": 1, "title": "Python Developer", "company": "ABC Technologies"},
    {"id": 2, "title": "Frontend Developer", "company": "XYZ Solutions"},
]


@app.route("/api/jobs", methods=["GET"])
def get_jobs():
    return jsonify({"success": True, "jobs": jobs})


@app.route("/api/jobs/<int:job_id>", methods=["GET"])
def get_job(job_id):
    for job in jobs:
        if job["id"] == job_id:
            return jsonify({"success": True, "jobs": job})

    return jsonify({"succes": False, "message": "Job not found"}), 404


@app.errorhandler(404)
def not_fount(error):
    return (
        jsonify(
            {"success": False, "message": "The requested API endpoint was not found"}
        ),
        404,
    )


@app.errorhandler(405)
def method_not_allowed(error):
    return (
        jsonify(
            {"success": False, "message": "HTTP method not allowed for this endpoint"}
        ),
        405,
    )


if __name__ == "__main__":
    app.run(debug=True)
