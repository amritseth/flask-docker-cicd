from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! My Dockerized Flask App is running with CI/CD!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)