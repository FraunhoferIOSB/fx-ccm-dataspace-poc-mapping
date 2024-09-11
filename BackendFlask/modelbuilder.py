# Here, models like the submodel, and descriptors will be build according to
# information InterfaceSetup module. 

import string
import random
'''
### Submodel object (json) modelling workflow. 

1.  In each of the datapoints in InterfaceSetup module, there is a 
    mapping enpoint object. if the submodelId endpoint is empty, 
    then a random one will be generated and assigned to the submodel object 
    being developed and the submodelId endpoint for future requests. 

2.  If the submodel element path is empty, a submodel element  is build with IdShort 
    similar to the datapoint "name" 
    
3.  The submodel Type helps know what type of submodel element to attach to
    the submodel payload. This field here is adviced not tobe left empty
'''


Submodel =  {
      "idShort": "SourceDataSink",
      "id": "https://example.com/ids/sm/5552_0182_8042_8250",
      "semanticId": {
        "type": "ModelReference",
        "keys": [
          {
            "type": "Submodel",
            "value": "https://admin-shell.io/sinksubmodel"
          }
        ]
      },
      "submodelElements": [],
      "modelType": "Submodel"
}

BlobSubmodelElement = {
          "idShort": "",
          "value": "",
          "semanticId": {
            "type": "ModelReference",
            "keys": [
              {
                "type": "GlobalReference",
                "value": "0173-1#02-AAM556#002"
              }
            ]
          },
          "contentType": "application/csv",
          "modelType": "Blob"
        }

PropertySubmodelElement =  {
          "category": "PARAMETER",
          "idShort": "",
          "description": [],
          "semanticId": {
            "type": "ModelReference",
            "keys": [
              {
                "type": "GlobalReference",
                "value": "0173-1#02-AAM556#002"
              }
            ]
          },
          "valueType": "xs:string",
          "value": "",
          "modelType": "Property"
        }

aasDescriptor = {
    "kind" : "instance",
    "idshort" : "Component-" + ' '.join(random.choices(string.ascii_uppercase, k=1)),
    "id" : "https://example.com/ids/sm/" + random.randint(0, 100000),
    "globalAssetId" : "",
    "submodelDescriptors": [
        
    ]

}

submodelDescriptor = {
        "endpoints" : [
            {
          "protocolInformation": {
            "href": "https://localhost:1234/api/v3.0/submodels",
            "endpointProtocol": "HTTP",
            "endpointProtocolVersion": [
              "1.1"
            ]
          },
          "interface": "AAS-3.0"
        }
        ],
         "idShort" : "data_sink",
         "id" : "https://factoryxTP204.com/submodel-for-data-sink"
}
