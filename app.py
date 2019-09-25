from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    r = requests.get("http://169.254.169.254/latest/meta-data/public-ipv4")
    return r.content
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')


