import React, {useState, useEffect} from 'react';
import './home.css';
import {AiFillRightCircle} from 'react-icons/ai';

const Home = () => {
    // generate AAS treeview if any is already existing in AAS directory.
    const[open, setOpen]=useState(true);
    const[showDiv, setShowDiv]=useState('configure');
    const[assetDatapoints, setAssetDatapoints] = useState([]);
    const[endpoints, setEndpoints] = useState({});
    const[datapointId, setdatapointId] = useState(-1);
    const[assetId, setAssetId] = useState("");
    const[value, setValue] = useState("");
    


    useEffect(()=>{
        fetchItems();
    
      }, []);

      async function fetchItems(){
        const response = await fetch('http://server:5000/getdatapoints');
        const data = await response.json();
        setAssetDatapoints(data['assets']);
        setEndpoints(data['endpoints']);
        console.log(data['assets']);
        console.log(data['endpoints']);
      };
    function openclose(){
        setOpen(!open)
        console.log("The state of the arrow " +open);
        //props.open(open)
      }

      function handleClick(windowType){
        setShowDiv(windowType);
      }

      async function configForm(e) {
        e.preventDefault();
        const formData = new FormData(e.target);
        const configObject = Object.fromEntries(formData);
        console.log(configObject);
        //post request from asset. 
        const configData = {
            method : 'POST',
            headers : {'Content-Type' : 'application/json'},
            body : JSON.stringify(configObject)
        };
        const response = await fetch('http://server:5000/configinfo', configData);
        if(response.ok){
            const data = await response.json();
            setAssetDatapoints(data['assets']);
            setEndpoints(data['endpoints']);
            console.log(data['assets']);

        }
        
      }

    async function datapointForm(e) {
        e.preventDefault();
        const formData = new FormData(e.target);
        const datapointObject = Object.fromEntries(formData);
        console.log(datapointObject)
        const datapointData = {
            method : 'POST',
            headers : {'Content-Type' : 'application/json'},
            body : JSON.stringify(datapointObject)
        };
        const response = await fetch('http://server:5000/adddatapoint', datapointData);
        if(response.ok){
            const data = await response.json();
            setAssetDatapoints(data['assets']);
            console.log(data["assets"])
        }

    }

    async function readDatapoint(id, assetId) {
        setdatapointId(id)
        setAssetId(assetId)
        const responseData =  await fetch('http://server:5000/readdatapoint?id='+id+'&assetId='+assetId);
        for(let i = 0;  i < assetDatapoints.length; i++){
            if(assetDatapoints[i]['assetId'] === assetId){
                let datapoints = assetDatapoints[i]['datapoints']
                for(let j=0; j < datapoints.length; j++){
                    
                    if(datapoints[j]['source-endpoint']['id'] === id){
                        const data =  await responseData.text();
        
                        setValue(data);
                        console.log(data);
                        assetDatapoints[i]['datapoints'][j]['source-endpoint']['value'] = data;
                    }

                }


            }
           
        }
        // eslint-disable-next-line no-restricted-globals
        //location.reload();
        

    }
    if(showDiv === 'configure')
      {
        return(
            <div className='main'>

                {/* div for texts */}
                <div className= 'intro-text'>
                    <h1 >AAS Mapper UI</h1>
                    <p>This User interface in built to facilitate the integration of shofloor data from TP 2.4 PoC. This integration is aimed to be flexible enough to integrate data from different sources (protocols and technologies) and formats into AAS.
                    for fast integration, submodel Asset interfaces description and Asset Interfaces Mapping configuration will be used to configure the AAS Mapper accordingly. In absense of these submodels, a form will be filled to facility the onboarding process.</p>
                </div>

                <div className='work-window'>
                    {/* right hand side for datapoints view */}
                    <div className='dir' style={{width: open ? "50%" : "0%" }}>
                        <h3 className='datapoint-header'>Datapoints</h3>
                        {
                        assetDatapoints.map((asset, index) => (
                            asset.length?
                            <div></div>
                            :
                            <div>
                                <h4 style={{marginLeft : "15px"}}>Asset : {asset["assetId"]}</h4>
                                <table className='datapoint-table'>
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>ContentType</th>
                                    <th>MappingCount</th>
                                    <th>Value</th>
                                    <th>Action</th>
                                </tr>  
                            </thead>
                            <tbody>
                                {
                                  
                                    asset["datapoints"].map((datapoint, index) => (
                                        datapoint['source-endpoint']['id'] === datapointId && asset["assetId"] === assetId ? 
                                        <tr>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{datapoint['sink-endpoint'].length}</td>
                                            <td>{value}</td>
                                            <td>
                                                <button onClick = {() => readDatapoint(datapoint['source-endpoint']['id'], asset["assetId"])} type="button">Read</button>
                                            </td>
                                        </tr>
                                        :
                                        <tr key = {index}>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{datapoint['sink-endpoint'].length}</td>
                                            <td>{datapoint['source-endpoint']['value']}</td>
                                            <td>
                                                <button  onClick ={() => readDatapoint(datapoint['source-endpoint']['id'], asset["assetId"])} type="button">Read</button>
                                            </td>

                                        </tr>

                                    ))
                                }
                            </tbody>
                        </table>
                            </div>
                        ))
                      }
                        {/* <table className='datapoint-table'>
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>contentType</th>
                                    <th>Value</th>
                                    <th>Action</th>
                                </tr>  
                            </thead>
                            <tbody>
                                {
                                    datapoints.map((datapoint, index) => (
                                        datapoint['source-endpoint']['id'] === datapointId ? 
                                        <tr>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{value}</td>
                                            <td>
                                                <button onClick = {() => readDatapoint(datapoint['source-endpoint']['id'])} type="button">Read</button>
                                            </td>
                                        </tr>
                                        :
                                        <tr key = {index}>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{datapoint['source-endpoint']['value']}</td>
                                            <td>
                                                <button  onClick ={() => readDatapoint(datapoint['source-endpoint']['id'])} type="button">Read</button>
                                            </td>

                                        </tr>

                                    ))
                                }
                            </tbody>
                        </table> */}
                    </div>

                    {/* button that opens or collapses the paage */}

                    <div className='openclose'>
                        <i onClick={openclose}><AiFillRightCircle className='icon' size={25} style={{transform : open ? 'rotate(180deg)' : 'rotate(0deg)'}} /></i>
                    </div>

                    {/* left hand side for filling some informations */}
                    <div className='aas-def' style={{float: open ? "left" : "none", width: open ? "49%" : "99%"}}>
                        <div className='buttons-div'>
                            <button className = 'active-window' type="button" onClick={()=>handleClick('configure')}>Configure</button>
                            <button className = 'non-active-window' type="button" onClick={()=>handleClick('create datapoint')}>Create datapoint</button>
                            <button className = 'non-active-window' type="button" onClick={()=>handleClick('dump submodels')}>Dump AID & AIMC submodel</button>
                            <button className = 'non-active-window' type="button" onClick={()=>handleClick('import submodels')}>import AID & AIMC(json) submodel</button>
                        </div>

                        <div className='configure-div'>
                            <form onSubmit={configForm}>
                                <div>
                                    <label htmlFor="registry">Registry URL: </label>
                                    <br />
                                    <input className= 'text-input-box' style={{minWidth: open ? "50%" : "25%"}} type="text" id='registry' name='registry' placeholder='Please enter valid registry base URL'/>
                                </div>
                                <br />

                                <div>
                                    <label htmlFor="submodel">Submodel URL: </label>
                                    <br />
                                    <input className= 'text-input-box' style={{minWidth: open ? "50%" : "25%"}} type="text" id='submodel' name='submodel' placeholder='Please enter valid submodel base URL'/>
                                </div>

                                <br />

                                <div>
                                    <label htmlFor="assetId">Asset ID: </label>
                                    <br />
                                    <input className= 'text-input-box' style={{minWidth: open ? "50%" : "25%"}} type="text" id='assetId' name='assetId' placeholder='Please enter a valid assetId'/>
                                </div>

                                <br />

                                <div>
                                    <button className='submit-info' type="submit">Submit</button>   
                                </div>     
                            </form>
                        </div>

                        <div className='configure-div'>
                            <label>Registry Endpoint: </label>
                            <label>{endpoints['registry-endpoint']}</label>

                            <br />
                            <br />

                            <label>Submodel Endpoint: </label>
                            <label>{endpoints['submodel-endpoint']}</label>

                            <br />

                        </div>
        
                    </div>
                </div>
            </div>
        )
      }
    else if(showDiv === 'create datapoint')
        {
          return(
              <div className='main'>
                    {/* div for texts */}
                    <div className= 'intro-text'>
                        <h1 >AAS Mapper UI</h1>
                        <p>This User interface in built to facilitate the integration of shofloor data from TP 2.4 PoC. This integration is aimed to be flexible enough to integrate data from different sources (protocols and technologies) and formats into AAS.
                        for fast integration, submodel Asset interfaces description and Asset Interfaces Mapping configuration will be used to configure the AAS Mapper accordingly. In absense of these submodels, a form will be filled to facility the onboarding process.</p>
                    </div>

                    <div className='work-window'>
                      {/* right hand side for datapoints view */}
                      <div className='dir' style={{width: open ? "50%" : "0px" }}>
                      <h3 className='datapoint-header'>Datapoints</h3>
                      
                      {
                        assetDatapoints.map((asset, index) => (
                            asset.length?
                            <div></div>
                            :
                            <div>
                                <h4 style={{marginLeft : "15px"}}>Asset : {asset["assetId"]}</h4>
                                <table className='datapoint-table'>
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>ContentType</th>
                                    <th>MappingCount</th>
                                    <th>Value</th>
                                    <th>Action</th>
                                </tr>  
                            </thead>
                            <tbody>
                                {
                                  
                                    asset["datapoints"].map((datapoint, index) => (
                                        datapoint['source-endpoint']['id'] === datapointId && asset["assetId"] === assetId ? 
                                        <tr>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{datapoint['sink-endpoint'].length}</td>
                                            <td>{value}</td>
                                            <td>
                                                <button onClick = {() => readDatapoint(datapoint['source-endpoint']['id'],asset["assetId"])} type="button">Read</button>
                                            </td>
                                        </tr>
                                        :
                                        <tr key = {index}>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{datapoint['sink-endpoint'].length}</td>
                                            <td>{datapoint['source-endpoint']['value']}</td>
                                            <td>
                                                <button  onClick ={() => readDatapoint(datapoint['source-endpoint']['id'], asset["assetId"])} type="button">Read</button>
                                            </td>

                                        </tr>

                                    ))
                                }
                            </tbody>
                        </table>
                            </div>
                        ))
                      }
                      
                      {/* <table className='datapoint-table'>
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>contentType</th>
                                    <th>Value</th>
                                    <th>Action</th>
                                </tr>  
                            </thead>
                            <tbody>
                                {
                                    assetDatapoints.map((datapoint, index) => (
                                        datapoint['source-endpoint']['id'] === datapointId ? 
                                        <tr>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{value}</td>
                                            <td>
                                                <button onClick = {() => readDatapoint(datapoint['source-endpoint']['id'])} type="button">Read</button>
                                            </td>
                                        </tr>
                                        :
                                        <tr key = {index}>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{datapoint['source-endpoint']['value']}</td>
                                            <td>
                                                <button  onClick ={() => readDatapoint(datapoint['source-endpoint']['id'])} type="button">Read</button>
                                            </td>

                                        </tr>

                                    ))
                                }
                            </tbody>
                        </table> */}
                      </div>
  
                      {/* button that opens or collapses the paage */}
  
                      <div className='openclose'>
                          <i onClick={openclose}><AiFillRightCircle className='icon' size={25} style={{transform : open ? 'rotate(180deg)' : 'rotate(0deg)'}} /></i>
                      </div>
  
                      {/* left hand side for filling some informations */}
                      <div className='aas-def' style={{float: open ? "left" : "none", width: open ? "49%" : "99%"}}>
                          <div className='buttons-div'>
                              <button className = 'non-active-window' type="button" onClick={()=>handleClick('configure')}>Configure</button>
                              <button className = 'active-window' type="button" onClick={()=>handleClick('create datapoint')}>Create datapoint</button>
                              <button className = 'non-active-window' type="button" onClick={()=>handleClick('dump submodels')}>Dump AID & AIMC submodel</button>
                              <button className = 'non-active-window' type="button" onClick={()=>handleClick('import submodels')}>import AID & AIMC(json) submodel</button>
                          </div>

                          <div className='configure-div'>
                            <form onSubmit={datapointForm}>
                                    <div>
                                    <label style = {{margin: "10px 0 20px 0px", fontWeight: "bold"}} htmlFor="">assetId</label>
                                        <br />
                                        
                                        <label htmlFor="registry">assetId: </label>
                                        <select style = {{height : "25px"}} defaultValue = "HTTP" name="assetId" id="assetId">
                                            {
                                                assetDatapoints.map((asset, index) => (
                                                    <option value={asset["assetId"]}>{asset["assetId"]}</option>
                                                ))     
                                            }
                                        </select>

                                        <br />
                                        <label style = {{margin: "10px 0 20px 0px", fontWeight: "bold"}} htmlFor="">Endpoints</label>
                                    

                                        <br />
                                        <label htmlFor="registry">Protocol: </label>
                                        <select style = {{height : "25px"}} defaultValue = "HTTP" name="protocol" id="protocol">
                                            <option value="HTTP">HTTP</option>
                                            <option value="MODBUS">MODBUS</option>
                                            <option value="OPCUA">OPCUA</option>
                                            <option value="MQTT">MQTT</option>
                                        </select>

                                        <br />
                                        <label htmlFor="base">Base Enpoint: </label>
                                        <input className= 'text-input-box-create-datapoint' style={{minWidth: open ? "50%" : "25%" }} type="text" id='base' name='base' placeholder='Please enter base URL of your datapoint' required/>
                                    </div>

                                    <div>
                                        <label style = {{margin: "30px 0 20px 0px", fontWeight: "bold"}} htmlFor="">Payload Information</label>
                                        
                                        <br />

                                        <label htmlFor="datapointName">Datapoint Name: </label>
                                        
                                        <input className= 'text-input-box' style={{minWidth: open ? "50%" : "25%"}} type="text" id='datapointName' name='datapointName' placeholder='Please enter a datapoint name'/>

                                        <br />


                                        <label htmlFor="contentType">ContentType: </label>
                                        <select style = {{height : "25px"}} defaultValue = "application/json" name="contentType" id="contentType">
                                            <option value="application/json">application/json</option>
                                            <option value="text/csv">text/csv</option>
                                            <option value="application/octet-stream">application/octet-stream</option>
                                            <option value="text/plain">text/plain</option>
                                        </select>

                                        <br />

                                        <label htmlFor="dataType">DataType: </label>
                                        <select style = {{height : "25px"}} defaultValue = "Number" name="dataType" id="dataType">
                                            <option value="number">Number</option>
                                            <option value="boolean">Boolean</option>
                                            <option value="string">String</option>
                                            <option value="object">Object</option>
                                            <option value="array">Array</option>
                                        </select>
                                    </div>

                                    <br />

                                    <div>
                                        <label style = {{margin: "30px 0 20px 0px", fontWeight: "bold"}} htmlFor="">Sink Information</label>
                                        
                                        <br />

                                        <label htmlFor="submodelId">Submodel ID: </label>
                                        
                                        <input className= 'text-input-box' style={{minWidth: open ? "50%" : "25%"}} type="text" id='submodelId' name='submodelId' placeholder='A random Id will be generated if empty'/>

                                        <br />

                                        
                                        <label htmlFor="submodelElementPath">Submodel Element Path: </label>
                                        
                                        <input className= 'text-input-box' style={{minWidth: open ? "50%" : "25%"}} type="text" id='submodelElementPath' name='submodelElementPath' placeholder='A random path will be generated if empty'/>

                                        <br />

                                        <label htmlFor="submodelElementType">Submodel Element Type: </label>
                                        
                                        <input className= 'text-input-box' style={{minWidth: open ? "50%" : "25%"}} type="text" id='submodelElementType' name='submodelElementType' placeholder='A random path will be generated if empty'/>

                                        <br />

                                        <label htmlFor="payloadMapping">Payload Mapping </label>
                                        
                                        <input className= 'text-input-box' style={{minWidth: open ? "50%" : "25%"}} type="text" id='payloadMapping' name='payloadMapping' placeholder='enter key(s) to map for json or csv payload'/>

                                        <br />

                                    </div>

                                    <br />

                                    <div>
                                        <input className='submit-info' type="submit" value="Submit" />    
                                    </div>     
                                </form>
                          </div>
                      </div>
                  </div>
              </div>
          )
        }
    else if(showDiv === 'dump submodels')
            {
                return(
                    <div className='main'>
                                {/* div for texts */}
                        <div className= 'intro-text'>
                            <h1 >AAS Mapper UI</h1>
                            <p>This User interface in built to facilitate the integration of shofloor data from TP 2.4 PoC. This integration is aimed to be flexible enough to integrate data from different sources (protocols and technologies) and formats into AAS.
                            for fast integration, submodel Asset interfaces description and Asset Interfaces Mapping configuration will be used to configure the AAS Mapper accordingly. In absense of these submodels, a form will be filled to facility the onboarding process.</p>
                        </div>
                        <div className='work-window'>
                            {/* right hand side for datapoints view */}
                            <div className='dir' style={{width: open ? "50%" : "0px" }}>
                            <h3 className='datapoint-header'>Datapoints</h3>
                            {
                            assetDatapoints.map((asset, index) => (
                            asset.length?
                            <div></div>
                            :
                            <div>
                                <h4 style={{marginLeft : "15px"}}>Asset : {asset["assetId"]}</h4>
                                <table className='datapoint-table'>
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>ContentType</th>
                                    <th>MappingCount</th>
                                    <th>Value</th>
                                    <th>Action</th>
                                </tr>  
                            </thead>
                            <tbody>
                                {
                                    asset["datapoints"].map((datapoint, index) => (
                                        datapoint['source-endpoint']['id'] === datapointId && asset["assetId"] === assetId ? 
                                        <tr>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{datapoint['sink-endpoint'].length}</td>
                                            <td>{value}</td>
                                            <td>
                                                <button onClick = {() => readDatapoint(datapoint['source-endpoint']['id'])} type="button">Read</button>
                                            </td>
                                        </tr>
                                        :
                                        <tr key = {index}>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{datapoint['sink-endpoint'].length}</td>
                                            <td>{datapoint['source-endpoint']['value']}</td>
                                            <td>
                                                <button  onClick ={() => readDatapoint(datapoint['source-endpoint']['id'])} type="button">Read</button>
                                            </td>

                                        </tr>

                                    ))
                                }
                            </tbody>
                        </table>
                            </div>
                                ))
                            }
                            {/* <table className='datapoint-table'>
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>contentType</th>
                                    <th>Value</th>
                                    <th>Action</th>
                                </tr>  
                            </thead>
                            <tbody>
                                {
                                    datapoints.map((datapoint, index) => (
                                        datapoint['source-endpoint']['id'] === datapointId ? 
                                        <tr>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{value}</td>
                                            <td>
                                                <button onClick = {() => readDatapoint(datapoint['source-endpoint']['id'])} type="button">Read</button>
                                            </td>
                                        </tr>
                                        :
                                        <tr key = {index}>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{datapoint['source-endpoint']['value']}</td>
                                            <td>
                                                <button  onClick ={() => readDatapoint(datapoint['source-endpoint']['id'])} type="button">Read</button>
                                            </td>

                                        </tr>

                                    ))
                                }
                            </tbody>
                        </table> */}
                            </div>
        
                            {/* button that opens or collapses the paage */}
        
                            <div className='openclose'>
                                <i onClick={openclose}><AiFillRightCircle className='icon' size={25} style={{transform : open ? 'rotate(180deg)' : 'rotate(0deg)'}} /></i>
                            </div>
        
                            {/* left hand side for filling some informations */}
                            <div className='aas-def' style={{float: open ? "left" : "none", width: open ? "49%" : "99%"}}>
                                <div className='buttons-div'>
                                    <button className = 'non-active-window' type="button" onClick={()=>handleClick('configure')}>Configure</button>
                                    <button className = 'non-active-window' type="button" onClick={()=>handleClick('create datapoint')}>Create datapoint</button>
                                    <button className = 'active-window' type="button" onClick={()=>handleClick('dump submodels')}>Dump AID & AIMC submodel</button>
                                    <button className = 'non-active-window' type="button" onClick={()=>handleClick('import submodels')}>import AID & AIMC(json) submodel</button>
                                </div>
                                <div className='configure-div'>
                                    <form action="">
                                        <div >
                                            <p>Please dump AID(JSON) submodel here:</p>
                                            <textarea className = 'json-dump-data' name="aid" id="aid"></textarea>
                                        </div>
                                        <br />
                                        <div>
                                            <p>Please dump AIMC(JSON) submodel here:</p>
                                            <textarea className = 'json-dump-data' name="aimc" id="aimc"></textarea>
                                        </div>

                                        <br />

                                        <div>
                                            <input className='submit-info' type="submit" value="Submit" />    
                                        </div>     

                                    </form>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                )
            }
    else if(showDiv === 'import submodels')
        {
            return(
                <div className='main'>
                      {/* div for texts */}
                    <div className= 'intro-text'>
                        <h1 >AAS Mapper UI</h1>
                        <p>This User interface in built to facilitate the integration of shofloor data from TP 2.4 PoC. This integration is aimed to be flexible enough to integrate data from different sources (protocols and technologies) and formats into AAS.
                        for fast integration, submodel Asset interfaces description and Asset Interfaces Mapping configuration will be used to configure the AAS Mapper accordingly. In absense of these submodels, a form will be filled to facility the onboarding process.</p>
                    </div>
                    <div className='work-window'>
                        {/* right hand side for datapoints view */}
                        <div className='dir' style={{width: open ? "50%" : "0px" }}>
                        <h3 className='datapoint-header'>Datapoints</h3>
                        {
                        assetDatapoints.map((asset, index) => (
                            asset.length?
                            <div></div>
                            :
                            <div>
                                <h4 style={{marginLeft : "15px"}}>Asset : {asset["assetId"]}</h4>
                                <table className='datapoint-table'>
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>contentType</th>
                                    <th>MappingCount</th>
                                    <th>Value</th>
                                    <th>Action</th>
                                </tr>  
                            </thead>
                            <tbody>
                                {
                                  
                                    asset["datapoints"].map((datapoint, index) => (
                                        datapoint['source-endpoint']['id'] === datapointId && asset["assetId"] === assetId ? 
                                        <tr>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{datapoint['sink-endpoint'].length}</td>
                                            <td>{value}</td>
                                            <td>
                                                <button onClick = {() => readDatapoint(datapoint['source-endpoint']['id'])} type="button">Read</button>
                                            </td>
                                        </tr>
                                        :
                                        <tr key = {index}>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{datapoint['sink-endpoint'].length}</td>
                                            <td>{datapoint['source-endpoint']['value']}</td>
                                            <td>
                                                <button  onClick ={() => readDatapoint(datapoint['source-endpoint']['id'])} type="button">Read</button>
                                            </td>

                                        </tr>

                                    ))
                                }
                            </tbody>
                        </table>
                            </div>
                            ))
                        }
                        {/* <table className='datapoint-table'>
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>contentType</th>
                                    <th>Value</th>
                                    <th>Action</th>
                                </tr>  
                            </thead>
                            <tbody>
                                {
                                    datapoints.map((datapoint, index) => (
                                        datapoint['source-endpoint']['id'] === datapointId ? 
                                        <tr>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{value}</td>
                                            <td>
                                                <button onClick = {() => readDatapoint(datapoint['source-endpoint']['id'])} type="button">Read</button>
                                            </td>
                                        </tr>
                                        :
                                        <tr key = {index}>
                                            <td>{datapoint['source-endpoint']['id']}</td>
                                            <td>{datapoint['source-endpoint']['name']}</td>
                                            <td>{datapoint['source-endpoint']['content-type']}</td>
                                            <td>{datapoint['source-endpoint']['value']}</td>
                                            <td>
                                                <button  onClick ={() => readDatapoint(datapoint['source-endpoint']['id'])} type="button">Read</button>
                                            </td>

                                        </tr>

                                    ))
                                }
                            </tbody>
                        </table> */}
                        </div>
    
                        {/* button that opens or collapses the paage */}
    
                        <div className='openclose'>
                            <i onClick={openclose}><AiFillRightCircle className='icon' size={25} style={{transform : open ? 'rotate(180deg)' : 'rotate(0deg)'}} /></i>
                        </div>
    
                        {/* left hand side for filling some informations */}
                        <div className='aas-def' style={{float: open ? "left" : "none", width: open ? "49%" : "99%"}}>
                            <div className='buttons-div'>
                                <button className = 'non-active-window' type="button" onClick={()=>handleClick('configure')}>Configure</button>
                                <button className = 'non-active-window' type="button" onClick={()=>handleClick('create datapoint')}>Create datapoint</button>
                                <button className = 'non-active-window' type="button" onClick={()=>handleClick('dump submodels')}>Dump AID & AIMC submodel</button>
                                <button className = 'active-window' type="button" onClick={()=>handleClick('import submodels')}>import AID & AIMC(json) submodel</button>
                            </div>
                            <div>
                                <h3>work area</h3>
                            </div>
                            <div>
                                <h3>save and upload</h3>
                            </div>
                        </div>
                    </div>
                </div>
            )
        }
}

export default Home