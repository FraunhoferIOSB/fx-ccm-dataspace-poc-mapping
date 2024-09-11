# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
import random


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)




@app.route("/counter/properties/count1", methods=["GET"])
# ‘/’ URL is bound with countState() function.
def countState1():
    payload = str(round((random.random() * 100), 2))
    return payload

@app.route("/counter/properties/count2", methods=["GET"])
# ‘/’ URL is bound with countState2() function.
def countState2():
    payload = str(round((random.random() * 100), 2))
    return payload


@app.route("/counter/properties/objectPayload", methods=["GET"])
# ‘/’ URL is bound with hello_world() function.
def objectPayload():
    payload = {
        "foo": round((random.random() * 100), 2),
        "bar": round((random.random() * 100), 2),
    }
    return payload


# main driver function
if __name__ == "__main__":

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(port=8500, debug=True, host='0.0.0.0')
