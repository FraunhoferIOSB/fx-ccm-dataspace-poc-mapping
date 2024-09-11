
function getAASElement(aasData, nodeid){
    if(nodeid.includes("#")){
        let nodes = nodeid.split('#');
        if(nodes.length === 2){
           let submodel =  getSubmodel(aasData.submodels, nodes[1]);
           return submodel;   
        }
        else if(nodes.length > 2){
            //get the submodel object first
            let submodel = getSubmodel(aasData.submodels, nodes[1])
            let number = 2;
            for(const sme of submodel.submodelElements){
                if(sme.idShort === nodes[number] && sme.modelType.name === "SubmodelElementCollection"){
                    if(number === nodes.length -1){
                        //it is a collection, return collection
                        return sme;
                    }
                    else{
                        let submdelelement = getSubmodelElement(sme, number, nodes)
                        return submdelelement;
                    }
                }
                else if(sme.idShort === nodes[number] && number === nodes.length -1){
                    //it is submodel elememt, return data element.
                    return sme;
                }
            }

        }
    }
}

function getSubmodel(submodels, submodelId){
    for(const submodel of submodels){
        if(submodel.identification.id === submodelId){
            return submodel 
        }
    }
}

function getSubmodelElement(submodelCollection, number, nodes){
    number = number + 1;
    for(const sme of submodelCollection.value){
        if(sme.idShort === nodes[number] && sme.modelType.name === "SubmodelElementCollection"){
            if(number === nodes.length -1){
                //it is a collection, return collection
                return sme;
            }
            else{
                let submodelElement = getSubmodelElement(sme, number, nodes)
                return submodelElement
            }
        }
        else if(sme.idShort === nodes[number] && number === nodes.length -1){
            //it is submodel elememt, return data element.
            return sme;
        }
    }
}

exports.getAASElement = getAASElement;