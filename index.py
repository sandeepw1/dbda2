from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "This app build is automatic...working.finally???"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)
