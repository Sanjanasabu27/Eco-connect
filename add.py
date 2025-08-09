from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(_name_)

# Database setup
def init_db():
    conn = sqlite3.connect("authors.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            institution TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get("name")
    institution = data.get("institution")

    conn = sqlite3.connect("authors.db")
    c = conn.cursor()
    c.execute("INSERT INTO authors (name, institution) VALUES (?, ?)", (name, institution))
    conn.commit()
    conn.close()

    return jsonify({"message": "Institution registered successfully"})

@app.route("/institutions", methods=["GET"])
def get_institutions():
    conn = sqlite3.connect("authors.db")
    c = conn.cursor()
    c.execute("SELECT name, institution FROM authors")
    rows = c.fetchall()
    conn.close()

    return jsonify(rows)

if _name_ == "_main_":
    init_db()
    app.run(debug=True)