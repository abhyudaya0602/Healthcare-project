from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests

app = Flask(__name__)
app.secret_key = "your_secret_key"

BACKEND_URL = "http://backend:5001"

@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = {
            "username": request.form["username"],
            "password": request.form["password"]
        }
        headers = {"Content-Type": "application/json"}  # 🔥 Fix: Ensure JSON format
        response = requests.post(f"{BACKEND_URL}/register", json=data, headers=headers)

        if response.status_code == 201:
            return redirect(url_for("login"))
        return "Registration failed", 400
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = {
            "username": request.form["username"],
            "password": request.form["password"]
        }
        headers = {"Content-Type": "application/json"}  # 🔥 Fix: Ensure JSON format
        response = requests.post(f"{BACKEND_URL}/login", json=data, headers=headers)

        if response.status_code == 200:
            session["username"] = request.form["username"]
            return redirect(url_for("dashboard"))
        return "Invalid credentials", 401
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", username=session["username"])

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")