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
        
        self.TimeSeries_Submodel = {
                                    "idShort": "TimeSeries",
                                    "description": [
                                        {
                                        "language": "de",
                                        "text": "Enth\u00E4lt Zeitreihendaten und Referenzen auf Zeitreihendaten, um diese entlang des Asset Lebenszyklus aufzufinden und semantisch zu beschreiben."
                                        },
                                        {
                                        "language": "en",
                                        "text": "Contains time series data and references to time series data to discover and semantically describe them along the asset lifecycle."
                                        }
                                    ],
                                    "administration": {
                                        "version": "1",
                                        "revision": "1"
                                    },
                                    "id": "https://admin-shell.io/idta/SubmodelTemplate/TimeSeries/1/1_",
                                    "kind": "Instance",
                                    "semanticId": {
                                        "type": "ModelReference",
                                        "keys": [
                                        {
                                            "type": "Submodel",
                                            "value": "https://admin-shell.io/idta/TimeSeries/1/1"
                                        }
                                        ]
                                    },
                                    "submodelElements": [
                                        {
                                        "idShort": "Metadata",
                                        "semanticId": {
                                            "type": "ExternalReference",
                                            "keys": [
                                            {
                                                "type": "GlobalReference",
                                                "value": "https://admin-shell.io/idta/TimeSeries/Metadata/1/1"
                                            }
                                            ]
                                        },
                                        "value": [
                                            {
                                            "category": "PARAMETER",
                                            "idShort": "Name",
                                            "semanticId": {
                                                "type": "ExternalReference",
                                                "keys": [
                                                {
                                                    "type": "GlobalReference",
                                                    "value": "https://admin-shell.io/idta/TimeSeries/Metadata/Name/1/1"
                                                }
                                                ]
                                            },
                                            "value": [
                                                {
                                                "language": "en",
                                                "text": "Meaningful name for labeling"
                                                }
                                            ],
                                            "modelType": "MultiLanguageProperty"
                                            },
                                            {
                                            "category": "PARAMETER",
                                            "idShort": "Description",
                                            "semanticId": {
                                                "type": "ExternalReference",
                                                "keys": [
                                                {
                                                    "type": "GlobalReference",
                                                    "value": "https://admin-shell.io/idta/TimeSeries/Metadata/Description/1/1"
                                                }
                                                ]
                                            },
                                            "qualifiers": [
                                                {
                                                "type": "Cardinality",
                                                "valueType": "xs:string",
                                                "value": "ZeroToOne"
                                                }
                                            ],
                                            "value": [
                                                {
                                                "language": "en",
                                                "text": "Short description of the time series segment."
                                                }
                                            ],
                                            "modelType": "MultiLanguageProperty"
                                            },
                                            {
                                            "idShort": "Record",
                                            "semanticId": {
                                                "type": "ExternalReference",
                                                "keys": [
                                                {
                                                    "type": "GlobalReference",
                                                    "value": "https://admin-shell.io/idta/TimeSeries/Record/1/1"
                                                }
                                                ]
                                            },
                                            "qualifiers": [
                                                {
                                                "type": "Cardinality",
                                                "valueType": "xs:string",
                                                "value": "One"
                                                }
                                            ],
                                            "value": [
                                                {
                                                "category": "VARIABLE",
                                                "idShort": "Time",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://admin-shell.io/idta/TimeSeries/RelativePointInTime/1/1"
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "semanticId": {
                                                        "type": "ExternalReference",
                                                        "keys": [
                                                        {
                                                            "type": "GlobalReference",
                                                            "value": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"
                                                        }
                                                        ]
                                                    },
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "OneToMany"
                                                    },
                                                    {
                                                    "semanticId": {
                                                        "type": "ExternalReference",
                                                        "keys": [
                                                        {
                                                            "type": "GlobalReference",
                                                            "value": "https://admin-shell.io/SubmodelTemplates/AllowedIdShort/1/0"
                                                        }
                                                        ]
                                                    },
                                                    "type": "AllowedIdShort",
                                                    "valueType": "xs:string",
                                                    "value": "Time[\\d{2,3}]"
                                                    }
                                                ],
                                                "valueType": "xs:long",
                                                "modelType": "Property"
                                                },
                                                {
                                                "category": "VARIABLE",
                                                "idShort": "sampleAccelerationX",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://sample.com/AccelerationX/1/1"
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "ZeroToOne"
                                                    }
                                                ],
                                                "valueType": "xs:long",
                                                "modelType": "Property"
                                                },
                                                {
                                                "category": "VARIABLE",
                                                "idShort": "sampleAccelerationY",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://sample.com/AccelerationY/1/1"
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "ZeroToOne"
                                                    }
                                                ],
                                                "valueType": "xs:long",
                                                "modelType": "Property"
                                                },
                                                {
                                                "category": "VARIABLE",
                                                "idShort": "sampleAccelerationZ",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://sample.com/AccelerationZ/1/1"
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "ZeroToOne"
                                                    }
                                                ],
                                                "valueType": "xs:long",
                                                "modelType": "Property"
                                                }
                                            ],
                                            "modelType": "SubmodelElementCollection"
                                            }
                                        ],
                                        "modelType": "SubmodelElementCollection"
                                        },
                                        {
                                        "idShort": "Segments",
                                        "semanticId": {
                                            "type": "ExternalReference",
                                            "keys": [
                                            {
                                                "type": "GlobalReference",
                                                "value": "https://admin-shell.io/idta/TimeSeries/Segments/1/1"
                                            }
                                            ]
                                        },
                                        "qualifiers": [
                                            {
                                            "type": "Cardinality",
                                            "valueType": "xs:string",
                                            "value": "One"
                                            }
                                        ],
                                        "value": [
                                            {
                                            "idShort": "ExternalSegment",
                                            "semanticId": {
                                                "type": "ExternalReference",
                                                "keys": [
                                                {
                                                    "type": "GlobalReference",
                                                    "value": "https://admin-shell.io/idta/TimeSeries/Segments/ExternalSegment/1/1"
                                                }
                                                ]
                                            },
                                            "qualifiers": [
                                                {
                                                "type": "Cardinality",
                                                "valueType": "xs:string",
                                                "value": "ZeroToMany"
                                                }
                                            ],
                                            "value": [
                                                {
                                                "category": "PARAMETER",
                                                "idShort": "Name",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1"
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "ZeroToOne"
                                                    }
                                                ],
                                                "value": [
                                                    {
                                                    "language": "en",
                                                    "text": "Meaningful name for labeling."
                                                    }
                                                ],
                                                "modelType": "MultiLanguageProperty"
                                                },
                                                {
                                                "category": "PARAMETER",
                                                "idShort": "Description",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://admin-shell.io/idta/TimeSeries/Segment/Description/1/1"
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "ZeroToOne"
                                                    }
                                                ],
                                                "value": [
                                                    {
                                                    "language": "en",
                                                    "text": "Short description of the time series segment."
                                                    }
                                                ],
                                                "modelType": "MultiLanguageProperty"
                                                },
                                                {
                                                "category": "VARIABLE",
                                                "idShort": "RecordCount",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1"
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "ZeroToOne"
                                                    }
                                                ],
                                                "valueType": "xs:long",
                                                "modelType": "Property"
                                                },
                                                {
                                                "category": "VARIABLE",
                                                "idShort": "StartTime",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1"
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "ZeroToOne"
                                                    }
                                                ],
                                                "valueType": "xs:string",
                                                "modelType": "Property"
                                                },
                                                {
                                                "category": "VARIABLE",
                                                "idShort": "EndTime",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1 "
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "ZeroToOne"
                                                    }
                                                ],
                                                "valueType": "xs:string",
                                                "modelType": "Property"
                                                },
                                                {
                                                "category": "VARIABLE",
                                                "idShort": "Duration",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1"
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "ZeroToOne"
                                                    }
                                                ],
                                                "valueType": "xs:string",
                                                "modelType": "Property"
                                                },
                                                {
                                                "category": "PARAMETER",
                                                "idShort": "SamplingInterval",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1"
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "ZeroToOne"
                                                    }
                                                ],
                                                "valueType": "xs:long",
                                                "modelType": "Property"
                                                },
                                                {
                                                "category": "PARAMETER",
                                                "idShort": "SamplingRate",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1"
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "ZeroToOne"
                                                    }
                                                ],
                                                "valueType": "xs:long",
                                                "modelType": "Property"
                                                },
                                                {
                                                "category": "PARAMETER",
                                                "idShort": "State",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://admin-shell.io/idta/TimeSeries/Segment/State/1/1"
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "ZeroToOne"
                                                    }
                                                ],
                                                "valueType": "xs:string",
                                                "modelType": "Property"
                                                },
                                                {
                                                "category": "VARIABLE",
                                                "idShort": "LastUpdate",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1"
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "ZeroToOne"
                                                    }
                                                ],
                                                "valueType": "xs:string",
                                                "modelType": "Property"
                                                },
                                                {
                                                "category": "PARAMETER",
                                                "idShort": "File",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://admin-shell.io/idta/TimeSeries/File/1/1"
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "ZeroToOne"
                                                    }
                                                ],
                                                "contentType": "application/json",
                                                "modelType": "File"
                                                },
                                                {
                                                "category": "VARIABLE",
                                                "idShort": "Blob",
                                                "semanticId": {
                                                    "type": "ExternalReference",
                                                    "keys": [
                                                    {
                                                        "type": "GlobalReference",
                                                        "value": "https://admin-shell.io/idta/TimeSeries/Blob/1/1"
                                                    }
                                                    ]
                                                },
                                                "qualifiers": [
                                                    {
                                                    "type": "Cardinality",
                                                    "valueType": "xs:string",
                                                    "value": "ZeroToOne"
                                                    }
                                                ],
                                                "contentType": "application/json",
                                                "modelType": "Blob"
                                                }
                                            ],
                                            "modelType": "SubmodelElementCollection"
                                            }
                                        ],
                                        "modelType": "SubmodelElementCollection"
                                        }
                                    ],
                                    "modelType": "Submodel"
                                    }

        self.Submodel =  {
                            "idShort": "",
                            "id": "",
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
                                "submodelDescriptor": [
                                    
                                ]
                            }

        self.submodelDescriptor = {
                                    "endpoints" : [
                                        {
                                    "protocolInformation": {
                                        "href": "",
                                        "endpointProtocol": "HTTP",
                                        "endpointProtocolVersion": [
                                        "1.1"
                                        ]
                                    },
                                    "interface": "AAS-3.0"
                                    }
                                    ],
                                    "idShort" : "data_sink",
                                    "id" : "https://factoryxTP204.com/submodel-for-data-sink",
                                    "semanticId" : [

                                    ]
                                }

        self.registryHeader = {
            'Content-Type': 'application/json',
            'edc-bpn':'default-tenant'
        }

        self.submodelBasicAuth = ("fx","fx-ccm-poc")

        self.assetId = ""
        self.id = 0
        self.counter = 0
        self.indexes = {
            "assetIndex" : 0,       
            "datapointIndex" : 0,
            "aasId" : ""
        }
