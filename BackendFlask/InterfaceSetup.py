import base64
import copy
import  httpx 
import random
import string
'''
TODOs
-- Creat a method that extract asset, work on it and return it back. 
examples. 
def Extract assetInfo(assetId) #? during a add datapoint operation?
def Extract datapoint(assetId, datapointId) #during a read datapoint operation
def update datapoint(assetId, datapointId) 
#if anything changes from the datapoint (e.g, value, new sink registration e.t.c), 
# it should be updated. 
'''
class Models():
    def __init__(self):
        self.interfaces = {
            "endpoints" : {}, 

            "assets" : []
        }

        self.endpoint = {
                "submodel-endpoint" : "none",
                "registry-endpoint" : "none",
            }
        
        self.asset = {

            "assetId" : "",
            "aasId":"",
            "aasDescriptor" : {},
            "datapoints" : []

        }

        self.datapoint = {
                
                "source-endpoint": {
                "id" : 0,
                "name" : "",
                "url" : "",
                "method" : "",
                "content-type" : "",
                "data-type" : "number",
                "value" : "NaN"

                },

                "sink-endpoint" : []
            
            }
        self.sinkEndpoint =  {
                                "sink-created": False,
                                "submodel" : {},
                                "submodelId" : "",
                                "submodelIdBase64" : "",
                                "submodelElementPath" : "",
                                "submodelElementType" : "",
                                "payloadMappingKeys" : ""
                            }

        self.Submodel =  {
                            "idShort": "SourceDataSink_"+' '.join(random.choices(string.ascii_uppercase, k=1)),
                            "id": "https://example.com/ids/sm/5552_0182_8042_"+str(random.randint(1000, 9999)),
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

        self.BlobSubmodelElement = {
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

        self.PropertySubmodelElement =  {
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

        self.aasDescriptor = {
                                "assetKind" : "Instance",
                                "idShort" : "",
                                "id" : "",
                                "globalAssetId" : " ",
                                "submodelDescriptors": [
                                    
                                ]
                            }

        self.submodelDescriptor = {
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

        self.registryHeader = {
            'Content-Type': 'application/json',
            'edc-bpn':'default-tenant'
        }

        self.submodelBasicAuth = ("fx","fx-ccm-poc")

        self.assetId = ""
        self.id = 0
        self.indexes = {
            "assetIndex" : 0,       
            "datapointIndex" : 0,
        }

class AasMapper(Models):
    
    def add_datapoint(self, datapoint:dict):
        
        for asset in self.interfaces["assets"]:
            if datapoint["assetId"] == asset["assetId"]:

                if self.datapoint_already_existing(asset, datapoint):
                    return self.interfaces["assets"] #add nothing
                else:  #add new datapoint
                    _datapoint = copy.deepcopy(self.datapoint)
                    _sinkEndpoint = copy.deepcopy(self.sinkEndpoint)
                    _datapoint["source-endpoint"]["id"] = len(asset["datapoints"]) + 1
                    _datapoint["source-endpoint"]["url"] = datapoint["base"]
                    _datapoint["source-endpoint"]["name"] = datapoint["datapointName"]
                    _datapoint["source-endpoint"]["content-type"] = datapoint["contentType"]
                    _datapoint["source-endpoint"]["data-type"] = datapoint["dataType"]

                    _sinkEndpoint["submodelElementType"] = datapoint["submodelElementType"]

                    _sinkEndpoint["payloadMappingKeys"] = datapoint["payloadMapping"]

                    if datapoint["submodelId"] == "":
                        #genetate a new submodelId
                        pass
                    else:
                        _sinkEndpoint["submodelId"] = datapoint["submodelId"]
                    
                    if datapoint["submodelElementPath"] == "":
                        #genetate a new submodel Element Path
                        pass
                    else:
                        _sinkEndpoint["submodelElementPath"] = datapoint["submodelElementPath"]
                    
                    _datapoint["sink-endpoint"].append(_sinkEndpoint)
                
                    asset["datapoints"].append(_datapoint)
                    break
          
                
        
        return self.interfaces["assets"]

    def datapoint_already_existing(self, asset, datapoint):
        
        for _datapoint in asset["datapoints"]:
            if datapoint["base"] == _datapoint["source-endpoint"]["url"]:
                return True
        return False
    
    def asset_already_existing(self, assetId):
        for asset in self.interfaces["assets"]:
            if asset["assetId"] == assetId:
                return True
              
        return False
           
    def descriptor_already_exist(self, descriptors, assetId):
        descriptor = {}
        for _descriptor in descriptors:
            if assetId == _descriptor["globalAssetId"]:
                return _descriptor
        return descriptor
            
    
    def add_configdata(self, configInfo:dict):
        registryEndpoint = configInfo["registry"]
        submodelEndpoint = configInfo["submodel"]
        # is registry endpoint the same as the one in configInfo or none?
        if registryEndpoint == self.endpoint["registry-endpoint"] or registryEndpoint == "none":
            pass
        else:
            self.endpoint["registry-endpoint"] = registryEndpoint

        # is submodel endpoint the same as the one in configInfo or none?
        if submodelEndpoint == self.endpoint["submodel-endpoint"] or submodelEndpoint == "none":
            pass
        else:
            self.endpoint["submodel-endpoint"] = submodelEndpoint

        #add endpoint to interfaces object
        self.interfaces["endpoints"] = self.endpoint

        if self.asset_already_existing(configInfo["assetId"]):
            pass
        else:
            asset = copy.deepcopy(self.asset)
            asset["assetId"] = configInfo["assetId"]
            

            #check if this descriptor with globalAssetId is existing in registry. 
            response = httpx.get(registryEndpoint, headers=self.registryHeader)
            descriptors = response.json()
            #return empty dictionary or not empty dictionary
            descriptor = self.descriptor_already_exist(descriptors["result"], configInfo["assetId"]) 

            if descriptor:
                #A descriptor with such assetId is existing and should be logged.
                print("Descriptor already registered in the registry")
                asset["aasId"] = descriptor["id"]
                asset["aasDescriptor"] = descriptor
                

            else:
                #create an AAS descriptor and registrer it.
                aasDescriptor = copy.deepcopy(self.aasDescriptor)
                aasDescriptor["globalAssetId"] = configInfo["assetId"]
                aasDescriptor["idShort"] = "Component-" + ' '.join(random.choices(string.ascii_uppercase, k=1))
                aasDescriptor["id"] = "https://example.com/ids/sm/" + str(random.randint(0, 100000))
                response = httpx.post(registryEndpoint, headers=self.registryHeader, json=aasDescriptor)
                if response.status_code == httpx.codes.CREATED: #change to response.is_success
                    print("aas is successfully registered")
                    asset["aasId"] = aasDescriptor["id"]
                    asset["aasDescriptor"] = aasDescriptor
            
            self.interfaces["assets"].append(asset)

        return self.interfaces

    def read_datapoint_from_source(self, assetId, id):
        self.assetId = assetId
        self.id = int(id)
        asset = self.extract_asset(assetId)
        datapoint = self.extract_datapoint(asset, id)
        source = datapoint["source-endpoint"]
        mappings = datapoint["sink-endpoint"]
        url = source["url"]
        response = httpx.get(url)
        
        #find the type of payload
        if (source["content-type"] == "text/plain") and \
            ((source["data-type"].lower() == "number") or \
                (source["data-type"].lower() == "string")):
            textPayload = response.text
            print(textPayload)
            updatedMappings= self.write_datapoint_to_sink(source["name"], mappings, textPayload)
            
            datapoint["source-endpoint"]["value"] = textPayload
            datapoint["sink-endpoint"] = updatedMappings
            asset["datapoints"][self.indexes["datapointIndex"]] = datapoint
            self.interfaces["assets"][self.indexes["assetIndex"]] = asset
            return textPayload
        
    
    def write_datapoint_to_sink(self, name, mappings, payload):
        submodel_url = self.interfaces["endpoints"]["submodel-endpoint"]
        for mappingIndex in range(len(mappings)): #using indexing here to be able to update the mapping array on the fly
            if mappings[mappingIndex]["sink-created"]:
                submodel = mappings[mappingIndex]["submodel"]
                submodel = self.push_payload_to_submodelElement(submodel, name, payload)

                submodelId_base64 = mappings[mappingIndex]["submodelIdBase64"]
                
                url = f'{submodel_url}/{submodelId_base64}'
                
                response = httpx.put(url, auth=self.submodelBasicAuth, json=submodel)

                if response.is_success:
                    return mappings
                #just post to the submodelId and submodel element in mapping
                
            elif mappings[mappingIndex]["submodelElementType"].lower() == "property":
                submodel = self.Submodel
                propertySME = self.PropertySubmodelElement
                propertySME["value"] = payload
                propertySME["idShort"] = name
                submodel["submodelElements"].append(propertySME)

                response = httpx.post(submodel_url, auth=self.submodelBasicAuth, json=submodel)
                if response.is_success:
                    #submodel created, turn on the flag, assign the Ids to sink-created and register the submodel in registry
                    mappings[mappingIndex]["submodel"] = submodel
                    mappings[mappingIndex]["sink-created"] = True
                    mappings[mappingIndex]["submodelId"] = submodel["id"]
                    submodelId_byte = submodel["id"].encode('utf-8')
                    mappings[mappingIndex]["submodelIdBase64"] = base64.b64encode(submodelId_byte).decode('utf-8')
                    mappings[mappingIndex]["submodelElementPath"] = name
        
                    return mappings
                    
        return mappings  


                        #method at the moment is automatically 'GET'


    def extract_asset(self,assetId):
        for assetIndex in range(len(self.interfaces["assets"])): #using indexing here to be able to update the asset array and datapoint array
            asset = self.interfaces["assets"][assetIndex]
            if asset['assetId'] == assetId:
                self.indexes["assetIndex"] = assetIndex
                
                return asset
        

    def extract_datapoint(self, asset, id):
        for datapointindex in range(len(asset["datapoints"])): #using indexing here to be able to update the datapoint array and datapoint array
            datapoint = asset["datapoints"][datapointindex]
            if str(datapoint["source-endpoint"]["id"]) == id:
                self.indexes["datapointIndex"] = datapointindex
            
                return datapoint

    def push_payload_to_submodelElement(self, submodel, name, payload):
        for submodelElementIndex in range(len(submodel["submodelElements"])):
            if submodel["submodelElements"][submodelElementIndex]["idShort"] == name:
                submodel["submodelElements"][submodelElementIndex]["value"] = payload
                return submodel
        
        return submodel
    

'''
 {
                            "source-endpoint": 
                            {
                            "submodelCreated" : False,
                            "id" : 1,
                            "name" : "count",
                            "url" : "http://asset:8500/counter/properties/count",
                            "method" : "get",
                            "content-type" : "text/plain",
                            "data-type" : "number",
                            "value" : "Factory X"

                            },

                            "sink-endpoint" : 
                            [
                                {
                                "submodelId" : "",
                                "submodelElementPath" : "",
                                "submodelElementType" : "",
                                "payloadMappingKeys" : "Time,Sensor1,Sensor2"
                                }
                            ]
                        
                        }




descritor = {
    "kind" : "instance",
    "idshort" : "ComponentA",
    "id" : "https://example.com/ids/sm/5552_0182_8042_7251",
    "submodelDescriptors": [
        {
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
         "idShort" : "Nameplate",
         "id" : "https://admin-shell.io/zvei/nameplate/1/0/Nameplate"
        }
    ]

}

'''     
        
        


        