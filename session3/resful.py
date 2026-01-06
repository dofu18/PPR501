from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello, World!"

#run main program
if __name__ == "__main__":
    app.run()
