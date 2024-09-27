import base64
import copy
import  httpx 
import random
import string
import pandas
from io import StringIO
from Models import Models
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

class AasMapper(Models):
    
    def add_datapoint(self, datapoint:dict):
        
        for asset in self.interfaces["assets"]:
            if datapoint["assetId"] == asset["assetId"]:
                datapoint_exist, _datapoint = self.datapoint_already_exist(asset, datapoint)
                if datapoint_exist:
                    _sinkEndpoint = copy.deepcopy(self.sinkEndpoint)
                    _sinkEndpoint["submodelElementType"] = datapoint["submodelElementType"]
                    _sinkEndpoint["payloadMappingKeys"] = datapoint["payloadMapping"]
                    _sinkEndpoint["submodelId"] = datapoint["submodelId"]
                    _sinkEndpoint["submodelElementPath"] = datapoint["submodelElementPath"]
                    _datapoint["sink-endpoint"].append(_sinkEndpoint)
                    
                    break
                
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
                    _sinkEndpoint["submodelId"] = datapoint["submodelId"]
                    _sinkEndpoint["submodelElementPath"] = datapoint["submodelElementPath"]
                    
                    _datapoint["sink-endpoint"].append(_sinkEndpoint)
                
                    asset["datapoints"].append(_datapoint)
                    break
          
                
        
        return self.interfaces["assets"]

    def datapoint_already_exist(self, asset, datapoint):
        
        for _datapoint in asset["datapoints"]:
            if datapoint["base"] == _datapoint["source-endpoint"]["url"]:
                return True, _datapoint
        return False, None
    
    def asset_already_existing(self, assetId):
        for asset in self.interfaces["assets"]:
            if asset["assetId"] == assetId:
                return True
              
        return False
           
    def descriptor_already_exist(self, descriptors, assetId):
        descriptor = {}
        for _descriptor in descriptors:
            if assetId == _descriptor.get("globalAssetId", ""):
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
                response = httpx.post(registryEndpoint, headers=self.registryHeader, json=aasDescriptor, timeout=15)
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
        #method at the moment is automatically 'GET'
        response = httpx.get(url, timeout=15)
        
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
        
        elif ((source["content-type"] == "text/csv" or source["content-type"] == "application/csv") and \
              source["data-type"].lower() == "object"):
            csv_payload = response.text 
            

            updatedMappings= self.write_datapoint_to_sink(source["name"], mappings, csv_payload)
            
            datapoint["source-endpoint"]["value"] = f"NaN{self.counter}"
            datapoint["sink-endpoint"] = updatedMappings
            asset["datapoints"][self.indexes["datapointIndex"]] = datapoint
            self.interfaces["assets"][self.indexes["assetIndex"]] = asset
            self.counter += self.counter
            return f"NaN{self.counter}"
            
    def write_datapoint_to_sink(self, name, mappings, payload):
        submodel_url = self.interfaces["endpoints"]["submodel-endpoint"]
        for mappingIndex in range(len(mappings)): #using indexing here to be able to update the mapping array on the fly
            if mappings[mappingIndex]["sink-created"]:
                submodel = mappings[mappingIndex]["submodel"]
                submodel = self.push_payload_to_submodelElement(submodel, name, payload)

                submodelId_base64 = mappings[mappingIndex]["submodelIdBase64"]
                
                url = f'{submodel_url}/{submodelId_base64}'
                
                response = httpx.put(url, auth=self.submodelBasicAuth, json=submodel, timeout=15)

                if response.is_success:
                    pass
                #just post to the submodelId and submodel element in mapping
                
            elif mappings[mappingIndex]["submodelElementType"].lower() == "property":
                submodel = self.set_up_submodel_property(payload, name)

                if httpx.post(submodel_url, auth=self.submodelBasicAuth, json=submodel, timeout=15).is_success:
                    #load mappings and register submodel descriptor.
                    mappings = self.load_mappings(mappings, mappingIndex, submodel, name)
                    
                      
            elif mappings[mappingIndex]["submodelElementType"].lower() == "blob":
                
                submodel = self.set_up_submodel_blob(payload, name, mappings[mappingIndex]["payloadMappingKeys"])

                if httpx.post(submodel_url, auth=self.submodelBasicAuth, json=submodel, timeout=15).is_success:
                    #load mappings and register submodel descriptor.
                    mappings = self.load_mappings(mappings, mappingIndex, submodel, name)
                    
                
                    
        return mappings  


    def set_up_submodel_property(self,value, idShort):
        submodel = copy.deepcopy(self.Submodel)
        submodel["idShort"] = "SourceDataSink_"+' '.join(random.choices(string.ascii_uppercase, k=1))
        submodel["id"] = "https://example.com/ids/sm/5552_0182_8042_"+str(random.randint(1000, 9999))
        propertySME = copy.deepcopy(self.PropertySubmodelElement)
        propertySME["value"] = value
        propertySME["idShort"] = idShort
        submodel["submodelElements"].append(propertySME)
        return submodel

    def set_up_submodel_blob(self, value, idShort, mappingKeys):
        submodel = copy.deepcopy(self.Submodel)
        submodel["idShort"] = "SourceDataSink_"+' '.join(random.choices(string.ascii_uppercase, k=1))
        submodel["id"] = "https://example.com/ids/sm/5552_0182_8042_"+str(random.randint(1000, 9999))
        blobSME = copy.deepcopy(self.BlobSubmodelElement)
        blobSME["idShort"] = idShort
        if mappingKeys == "":
            #convert payload to base64 string. 
            payload_byte = value.encode('utf-8')
        else:
            mappingKeys = mappingKeys.replace(' ', '')
            keys = mappingKeys.split(',')
            csv_payload = StringIO(value) 
            csv_dataFrame = pandas.read_csv(csv_payload, usecols=keys)
            #convert csv to string
            csv_string = csv_dataFrame.to_csv(index=False)
            payload_byte = csv_string.encode('utf-8')

        blobSME["value"] = base64.b64encode(payload_byte).decode('utf-8')
        submodel["submodelElements"].append(blobSME)

        return submodel


    def load_mappings(self, mappings, mappingIndex, submodel, idShortPath):
        #submodel created, turn on the flag, assign the Ids to sink-created and register the submodel in registry
        mappings[mappingIndex]["submodel"] = submodel
        mappings[mappingIndex]["sink-created"] = True
        mappings[mappingIndex]["submodelId"] = submodel["id"]
        submodelId_byte = submodel["id"].encode('utf-8')
        mappings[mappingIndex]["submodelIdBase64"] = base64.b64encode(submodelId_byte).decode('utf-8')
        mappings[mappingIndex]["submodelElementPath"] = idShortPath
        
        return mappings
        #create submodel descriptor and post it

    def extract_asset(self,assetId):
        for assetIndex in range(len(self.interfaces["assets"])): #using indexing here to be able to update the asset array and datapoint array
            asset = self.interfaces["assets"][assetIndex]
            if asset['assetId'] == assetId:
                self.indexes["assetIndex"] = assetIndex
                self.indexes["aasId"] = asset["aasId"]
                
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
    
