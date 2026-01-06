from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bhanu Backend Server - Secured via NGINX Reverse Proxy"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
