from flask import Flask, request, jsonify

app = Flask("__name__")

@app.route("/", methods = ["GET"])
def home():
    return "Hey there theres some code missing!"


# Created an API but did not save it :')

if __name__ == '__main__':
    app.run(debug=True)