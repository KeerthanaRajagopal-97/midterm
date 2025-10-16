from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🦄 Wild Rydes</h1><p>Keerthana Rajagopal - Student ID: 1234567</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
