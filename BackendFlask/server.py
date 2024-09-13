from flask import Flask, request
from flask_cors import cross_origin
import json
import InterfaceSetup


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

#Interface object

aasmapper = InterfaceSetup.AasMapper()
ui_origin_localhost = "http://localhost:3000"
ui_origin_docker = "http://client:3000"

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route("/")
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return "Hello World"


@app.route("/adddatapoint/", methods=["POST"])
@cross_origin(origins=[ui_origin_localhost])
#/add-datapoint is bound with addDatapoint() function to add new datapoint
def addDatapoint():
    data = json.loads(request.data)
    assets = aasmapper.add_datapoint(data)
    return {"assets":assets}

@app.route("/getdatapoints", methods=["GET"])
@cross_origin(origins=[ui_origin_localhost])
# ‘/’ URL is bound with getDatapoint() function.
def getDatapoints():

    datapoints = aasmapper.interfaces["assets"]
    endpoints = aasmapper.interfaces["endpoints"]
    return {"assets": datapoints, "endpoints": endpoints}


@app.route("/readdatapoint/", methods=["GET"])
@cross_origin(origins=[ui_origin_localhost])
# ‘/’ URL is bound with readDatapoint() function.
def readDatapoint():
    id = request.args.get("id")
    assetId = request.args.get("assetId")
    
    payload = aasmapper.read_datapoint_from_source(assetId=assetId, id=id)
    

    return payload


@app.route("/configinfo", methods=["POST"])
@cross_origin(origins=[ui_origin_localhost])
# ‘/’ URL is bound with submitConfigInfo() function.
def submitConfigInfo():
    data = json.loads(request.data)
    print(data)
    configData = aasmapper.add_configdata(data)
    endpoints = configData["endpoints"]
    assets = configData["assets"]

    return {
        "assets": assets,
        "endpoints": endpoints,
    }


# main driver function
if __name__ == "__main__":

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True, host="0.0.0.0")
