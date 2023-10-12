"use strict";(self.webpackChunkamun_sdk=self.webpackChunkamun_sdk||[]).push([[372],{3905:(e,t,a)=>{a.d(t,{Zo:()=>p,kt:()=>k});var n=a(7294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function l(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?l(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):l(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function o(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},l=Object.keys(e);for(n=0;n<l.length;n++)a=l[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(n=0;n<l.length;n++)a=l[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var s=n.createContext({}),u=function(e){var t=n.useContext(s),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},p=function(e){var t=u(e.components);return n.createElement(s.Provider,{value:t},e.children)},m="mdxType",c={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},d=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,l=e.originalType,s=e.parentName,p=o(e,["components","mdxType","originalType","parentName"]),m=u(a),d=r,k=m["".concat(s,".").concat(d)]||m[d]||c[d]||l;return a?n.createElement(k,i(i({ref:t},p),{},{components:a})):n.createElement(k,i({ref:t},p))}));function k(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var l=a.length,i=new Array(l);i[0]=d;var o={};for(var s in t)hasOwnProperty.call(t,s)&&(o[s]=t[s]);o.originalType=e,o[m]="string"==typeof e?e:r,i[1]=o;for(var u=2;u<l;u++)i[u]=a[u];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}d.displayName="MDXCreateElement"},9373:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>s,contentTitle:()=>i,default:()=>c,frontMatter:()=>l,metadata:()=>o,toc:()=>u});var n=a(7462),r=(a(7294),a(3905));const l={sidebar_label:"session",title:"session"},i=void 0,o={unversionedId:"Reference/session",id:"Reference/session",title:"session",description:"APISession Objects",source:"@site/docs/Reference/session.md",sourceDirName:"Reference",slug:"/Reference/session",permalink:"/aurora-amun-python-sdk/docs/Reference/session",draft:!1,tags:[],version:"current",frontMatter:{sidebar_label:"session",title:"session"},sidebar:"docSidebar",previous:{title:"responses",permalink:"/aurora-amun-python-sdk/docs/Reference/responses"}},s={},u=[{value:"APISession Objects",id:"apisession-objects",level:2},{value:"AmunSession Objects",id:"amunsession-objects",level:2},{value:"get_turbines",id:"get_turbines",level:4},{value:"get_turbine_by_name",id:"get_turbine_by_name",level:4},{value:"get_power_curve",id:"get_power_curve",level:4},{value:"get_region_details",id:"get_region_details",level:4},{value:"get_scenarios",id:"get_scenarios",level:4},{value:"get_scenario_by_name",id:"get_scenario_by_name",level:4},{value:"create_valuation",id:"create_valuation",level:4},{value:"submit_load_factor_calculations",id:"submit_load_factor_calculations",level:4},{value:"get_load_factor_calculation",id:"get_load_factor_calculation",level:4},{value:"track_load_factor_calculation",id:"track_load_factor_calculation",level:4},{value:"run_load_factors_in_batch",id:"run_load_factors_in_batch",level:4},{value:"run_load_factor_calculation",id:"run_load_factor_calculation",level:4},{value:"run_load_factors_for_parameters_batch",id:"run_load_factors_for_parameters_batch",level:4},{value:"run_load_factor_for_parameters",id:"run_load_factor_for_parameters",level:4},{value:"get_valuation_results",id:"get_valuation_results",level:4},{value:"delete_valuation",id:"delete_valuation",level:4},{value:"get_wind",id:"get_wind",level:4},{value:"get_wind_atlas",id:"get_wind_atlas",level:4},{value:"get_windfarms",id:"get_windfarms",level:4},{value:"get_windfarm",id:"get_windfarm",level:4}],p={toc:u},m="wrapper";function c(e){let{components:t,...a}=e;return(0,r.kt)(m,(0,n.Z)({},p,a,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h2",{id:"apisession-objects"},"APISession Objects"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"class APISession()\n")),(0,r.kt)("p",null,"Internal class to hold base methods for interacting with the Aurora HTTP API"),(0,r.kt)("h2",{id:"amunsession-objects"},"AmunSession Objects"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"class AmunSession(APISession)\n")),(0,r.kt)("p",null,"Manage access to the Amun API."),(0,r.kt)("p",null,"By default the session will connect to the production Amun API endpoint. This can be overridden by passing the base_url into the constructor\nor by setting the environment variable ",(0,r.kt)("em",{parentName:"p"},"AURORA_API_BASE_URL"),". This is for internal use only."),(0,r.kt)("p",null,"The authentication token is read from the users home directory ",(0,r.kt)("em",{parentName:"p"},"$home/.aurora-api-key")," e.g. ",(0,r.kt)("em",{parentName:"p"},"C:/Users/Joe Bloggs/.aurora-api-key"),".\nThis can be overridden by passing the token into the constructor or by setting the environment variable ",(0,r.kt)("em",{parentName:"p"},"AURORA_API_KEY"),"."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"base_url")," ",(0,r.kt)("em",{parentName:"li"},"string, optional")," - Override the base url used to contact the Amun API. Defaults to None."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"token")," ",(0,r.kt)("em",{parentName:"li"},"string, optional")," - Overide the api authentication token used for API access. Defaults to None.")),(0,r.kt)("h4",{id:"get_turbines"},"get","_","turbines"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def get_turbines()\n")),(0,r.kt)("p",null,"Get the turbines available to the user."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Response example"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-json"},"    [{\n        'id': 29,\n        'manufacturer': 'EWT Directwind',\n        'name': 'EWT Directwind 2000/96',\n        'ratedCapacity': 2,\n        'rotorDiameter': 96,\n        'minHubHeight': None,\n        'maxHubHeight': None,\n        'cutInSpeed': 3.5,\n        'cutOutSpeed': 25,\n        'specSource': 'https://www.thewindpower.net/turbine_en_879_ewt_directwind-2000-96.php',\n        'type': 'public',\n        },\n            ...\n")),(0,r.kt)("h4",{id:"get_turbine_by_name"},"get","_","turbine","_","by","_","name"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def get_turbine_by_name(turbine_name)\n")),(0,r.kt)("p",null,"Get turbine information by name."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Returns"),":"),(0,r.kt)("p",null,"  A dictionary with the turbine information. If not found, raises an error."),(0,r.kt)("p",null,"  ",(0,r.kt)("strong",{parentName:"p"},"Response example"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-json"},"    {\n        'id': 29,\n        'manufacturer': 'EWT Directwind',\n        'name': 'EWT Directwind 2000/96',\n        'ratedCapacity': 2,\n        'rotorDiameter': 96,\n        'minHubHeight': None,\n        'maxHubHeight': None,\n        'cutInSpeed': 3.5,\n        'cutOutSpeed': 25,\n        'specSource': 'https://www.thewindpower.net/turbine_en_879_ewt_directwind-2000-96.php',\n        'type': 'public',\n    }\n")),(0,r.kt)("h4",{id:"get_power_curve"},"get","_","power","_","curve"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def get_power_curve(turbine_id)\n")),(0,r.kt)("p",null,"Get the power curve for a turbine."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"turbine_id")," ",(0,r.kt)("em",{parentName:"li"},"int")," - The id of the turbine. To get ID (with additional info), refer to ",(0,r.kt)("inlineCode",{parentName:"li"},"AmunSession.get_turbines"),"\nor ",(0,r.kt)("inlineCode",{parentName:"li"},"AmunSession.get_turbine_by_name"))),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Returns"),":"),(0,r.kt)("p",null,"  List of dictionaries with these fields:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"speed")," - wind speed in m/s"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"power")," - generated power in kW")),(0,r.kt)("h4",{id:"get_region_details"},"get","_","region","_","details"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def get_region_details(latitude: float,\n                       longitude: float) -> List[RegionDetail]\n")),(0,r.kt)("p",null,"Get a list of supported regions for a given point."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"latitude")," ",(0,r.kt)("em",{parentName:"li"},"float")," - latitude of the point to lookup."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"longitude")," ",(0,r.kt)("em",{parentName:"li"},"float")," - longitude")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Returns"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"List[RegionDetail]")," - A list of all the supported regions for the point.")),(0,r.kt)("h4",{id:"get_scenarios"},"get","_","scenarios"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def get_scenarios(region)\n")),(0,r.kt)("p",null,"Get the scenarios that are available for the specified region. The regions for a given location\nto use can be found be using ",(0,r.kt)("inlineCode",{parentName:"p"},".AmunSession.get_region_details")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"region")," ",(0,r.kt)("em",{parentName:"li"},"str")," - The code for the region to lookup scenarios for.")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Returns"),":"),(0,r.kt)("p",null,"  List of Scenario details."),(0,r.kt)("p",null,"  ",(0,r.kt)("strong",{parentName:"p"},"Response example"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-json"},"        [{\n            'id': 3,\n            'name': '2019 Smart Power Scenario',\n            'description': 'To examine the impact of a smarter power system with more flexible capacity and demand',\n            'region': 'gbr',\n            'S3uri': None,\n            'currency': 'GBP',\n            'currencyYear': 2018,\n            'hasFile': False\n        },\n        ...\n")),(0,r.kt)("h4",{id:"get_scenario_by_name"},"get","_","scenario","_","by","_","name"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def get_scenario_by_name(region, scenario_name)\n")),(0,r.kt)("p",null,"Get a scenario by name"),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"region")," ",(0,r.kt)("em",{parentName:"li"},"str")," - The code for the region to lookup scenarios for. Use ",(0,r.kt)("inlineCode",{parentName:"li"},"AmunSession.get_region_details")," to get the region code for a point."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"scenario_name")," ",(0,r.kt)("em",{parentName:"li"},"str")," - The name of the scenario to get. Please ensure the name is spelled correctly.")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Returns"),":"),(0,r.kt)("p",null,"  An object with infomation about the scenario. If not found, raises an error."),(0,r.kt)("p",null,"  ",(0,r.kt)("strong",{parentName:"p"},"Response example"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-json"},"        [{\n            'id': 3,\n            'name': '2019 Smart Power Scenario',\n            'description': 'To examine the impact of a smarter power system with more flexible capacity and demand',\n            'region': 'gbr',\n            'S3uri': None,\n            'currency': 'GBP',\n            'currencyYear': 2018,\n            'hasFile': False\n        },\n        ...\n")),(0,r.kt)("h4",{id:"create_valuation"},"create","_","valuation"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def create_valuation(valuation)\n")),(0,r.kt)("p",null,"Creates a valuation in Amun."),(0,r.kt)("p",null,"Expects a dictionary of with these fields:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"name")," (str)"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"description")," (str)"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"longitude")," (str)"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"latitude")," (str)"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"windType")," (str) - One of ",'"',"era5",'"',", ",'"',"merra2",'"',", ",'"',"weibull",'"',", ",'"',"newa",'"',", ",'"',"p50scaling",'"',", ",'"',"powerdensity",'"',", ",'"',"averagewindspeed",'"',", ",'"',"aurorawindatlas",'"',", ",'"',"p50yieldscaling",'"',". Not applicable for uploaded data."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"scenarioId")," (string) to get the id of the scenario you want to use, check ",(0,r.kt)("inlineCode",{parentName:"li"},"AmunSession.get_scenario_by_name")," or ",(0,r.kt)("inlineCode",{parentName:"li"},"AmunSession.get_scenarios")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"useReanalysisCorrection")," - if True, will use regional reanalysis correction if it is available for the location"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"usePowerCurveSmoothing")," - if True, will use regional reanalysis correction if it is available for the location"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"lossesWake")," (float, optional): The percentage to apply for wake loss. (0 ","<","= lossesWake ","<"," 1)"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"lossesAvailability")," (float, optional): Percentage for external losses. (0 ","<","= lossesAvailability ","<"," 1)"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"lossesElectrical")," (float, optional): Percentage for external losses. (0 ","<","= lossesElectrical ","<"," 1)"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"lossesTurbinePerformance")," (float, optional): Percentage for external losses. (0 ","<","= lossesTurbinePerformance ","<"," 1)"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"lossesEnvironmental")," (float, optional): Percentage for external losses. (0 ","<","= lossesEnvironmental ","<"," 1)"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"lossesOtherCurtailment")," (float, optional): Percentage for external losses. (0 ","<","= lossesOtherCurtailment ","<"," 1)"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"curtailmentThreshold")," (float, optional): Defaults to 0"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"roughnessLength")," (float, optional): Static roughness. If not given, will be derived from reanalysis data")),(0,r.kt)("p",null,"Additional parameters that are specific to a wind type will be required. Please look at the parameters section of SDK Reference documentation and\nsee Amun SDK Examples to see how to create a valuation for your use case."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Returns"),":"),(0,r.kt)("p",null,"  A dictionary with the valuation information. Additionally provides a unique valuation id that should be used to run it and get results. Please see ",(0,r.kt)("inlineCode",{parentName:"p"},"AmunSession.get_valuation_results")," for more details."),(0,r.kt)("h4",{id:"submit_load_factor_calculations"},"submit","_","load","_","factor","_","calculations"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def submit_load_factor_calculations(\n        load_factor_configurations: List[Dict]) -> List[str]\n")),(0,r.kt)("p",null,"Submits a request to calculate the load factor and wind speeds for a year given\na start time and a location.\nYou can submit a lot of calculations at once and then use the tokens in response\nto check on the status of each calculation."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"See Also"),":"),(0,r.kt)("p",null,"  ",(0,r.kt)("inlineCode",{parentName:"p"},"AmunSession.get_region_details")," to get region codes and available datasets for a point"),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("p",null,"  list of load_factor_configurations where each load_factor_configuration is a dictionary of load factor parameters."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Returns"),":"),(0,r.kt)("p",null,"  List of tokens where each token is a unique identifier for the calculation. The order of the tokens matches the order of the input parameters."),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"token: unique identifier for the calculation")),(0,r.kt)("h4",{id:"get_load_factor_calculation"},"get","_","load","_","factor","_","calculation"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def get_load_factor_calculation(token: str)\n")),(0,r.kt)("p",null,"V2 feature.\nGets the status of a load factor calculation given its token."),(0,r.kt)("p",null,"For calculation that is still running:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"status")," - ",'"',"Running",'"')),(0,r.kt)("p",null,"For a finished calculation:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"status")," - ",'"',"Complete",'"'),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"exiryTime")," - Date and time of when the results will be deleted,"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"results")," - load factors")),(0,r.kt)("p",null,"For errored calculation:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"status")," - ",'"',"Errored",'"'),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"error")," - a string explaining the error")),(0,r.kt)("h4",{id:"track_load_factor_calculation"},"track","_","load","_","factor","_","calculation"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def track_load_factor_calculation(tokens: List[str]) -> List[Dict]\n")),(0,r.kt)("p",null,"V2 feature\nTracks the status of a load factor calculation/simulation given their token and\nreturns the results of the simulations as soon as they finish running."),(0,r.kt)("p",null,"Accepts a list of tokens of calculations and returns a list of results.\nThe order of the results matches the order of the input parameters.\nDepending on the status of the calculation the result will have different keys:"),(0,r.kt)("p",null,"For finished calculations:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"parameters")," - the parameters used for the calculation"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"appliedParams")," - smoothing coefficients and other parameters applied to the calculation"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"typicalHourly")," - typical hourly load factors"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"weatherYearHourly")," - hourly load factors for the weather year  ")),(0,r.kt)("p",null,"For errored calculations:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"error")," - a string explaining the error  ")),(0,r.kt)("p",null,"For calcualtions that failed to be submitted:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"None"))),(0,r.kt)("h4",{id:"run_load_factors_in_batch"},"run","_","load","_","factors","_","in","_","batch"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def run_load_factors_in_batch(\n        load_factor_configurations: List[Dict]) -> List[Dict]\n")),(0,r.kt)("p",null,"Perform multiple load factor calculations in parallel."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"See Also"),":"),(0,r.kt)("p",null,"  ",(0,r.kt)("inlineCode",{parentName:"p"},".AmunSession.get_region_details")," to get region codes and available datasets for a point"),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("p",null,"  list of load_factor_configurations where each load_factor_configuration is a dictionary of load factor parameters."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Returns"),":"),(0,r.kt)("p",null,"  List of dictionaries of this type. Order of the results matches the order of the input parameters:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"parameters")," - the parameters used for the calculation"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"appliedParams")," - smoothing coefficients and other parameters applied to the calculation"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"typicalHourly")," - typical hourly load factors"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"weatherYearHourly")," - hourly load factors for the weather year")),(0,r.kt)("h4",{id:"run_load_factor_calculation"},"run","_","load","_","factor","_","calculation"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def run_load_factor_calculation(load_factor_configuration: Dict)\n")),(0,r.kt)("p",null,"Calculate the load factor and wind speeds for a year given a start time and a location."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"See Also"),":"),(0,r.kt)("p",null,"  ",(0,r.kt)("inlineCode",{parentName:"p"},".AmunSession.get_region_details")," to get region codes and available datasets for a point"),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"load_factor_configuration")," - A dictionary of load factor parameters.")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Returns"),":"),(0,r.kt)("p",null,"  A Dictionary with the keys"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"parameters")," - the parameters used for the calculation"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"appliedParams")," - smoothing coefficients and other parameters applied to the calculation"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"typicalHourly")," - typical hourly load factors"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"weatherYearHourly")," - hourly load factors for the weather year")),(0,r.kt)("h4",{id:"run_load_factors_for_parameters_batch"},"run","_","load","_","factors","_","for","_","parameters","_","batch"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def run_load_factors_for_parameters_batch(\n        flow_parameters: List[FlowParameters],\n        base_parameters: List[LoadFactorBaseParameters]) -> List[Dict]\n")),(0,r.kt)("p",null,"Perform multiple load factor calculations in parallel by providing flow parameters and base parameters\nfor each calculation."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"See Also"),":"),(0,r.kt)("p",null,"  ",(0,r.kt)("inlineCode",{parentName:"p"},".AmunSession.get_region_details")," to get region codes and available datasets for a point"),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"flow_parameters")," - The list of parameters specific to the calculation type",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"aurora.amun.client.parameters.AverageWindSpeedParameters")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"aurora.amun.client.parameters.BuiltInWindParameters")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"aurora.amun.client.parameters.PowerDensityParameters")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"aurora.amun.client.parameters.WeibullParameters")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"aurora.amun.client.parameters.UploadedWindParameters")))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"base_parameters")," - List of parameters required for all flows to the calculation type. These are applied to all the flow parameters")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Returns"),":"),(0,r.kt)("p",null,"  List of dictionaries of this type. Order of the results matches the order of the input parameters:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"parameters")," - the parameters used for the calculation"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"appliedParams")," - smoothing coefficients and other parameters applied to the calculation"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"flow_parameters"),"0 - typical hourly load factors"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"flow_parameters"),"1 - hourly load factors for the weather year")),(0,r.kt)("h4",{id:"run_load_factor_for_parameters"},"run","_","load","_","factor","_","for","_","parameters"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def run_load_factor_for_parameters(flow_parameters: FlowParameters,\n                                   base_parameters: LoadFactorBaseParameters)\n")),(0,r.kt)("p",null,"Calculate the load factor and wind speeds for a year given a start time and a location."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"See Also"),":"),(0,r.kt)("p",null,"  ",(0,r.kt)("inlineCode",{parentName:"p"},"AmunSession.get_region_details")," to get region codes and available datasets for a point"),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"flow_parameters")," - The parameters specific to the calculation type",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"aurora.amun.client.parameters.AverageWindSpeedParameters")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"aurora.amun.client.parameters.BuiltInWindParameters")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"aurora.amun.client.parameters.PowerDensityParameters")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"aurora.amun.client.parameters.WeibullParameters")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"aurora.amun.client.parameters.UploadedWindParameters")))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"base_parameters")," ",(0,r.kt)("em",{parentName:"li"},"LoadFactorBaseParameters")," - The parameters required for all flows to the calculation type.")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Returns"),":"),(0,r.kt)("p",null,"  A Dictionary with the keys"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"parameters")," - the parameters used for the calculation"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"appliedParams")," - smoothing coefficients and other parameters applied to the calculation"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"typicalHourly")," - typical hourly load factors"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"weatherYearHourly")," - hourly load factors for the weather year")),(0,r.kt)("h4",{id:"get_valuation_results"},"get","_","valuation","_","results"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def get_valuation_results(valuation_id, format, should_return_hourly_data)\n")),(0,r.kt)("p",null,"Gets the results of a valuation"),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"valuation_id")," ",(0,r.kt)("em",{parentName:"li"},"number")," - The id of the valuation to get the results for."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"format")," ",(0,r.kt)("em",{parentName:"li"},"string")," - The format of the results. One of (",'"',"json",'"',",",'"',"xlsx",'"',")"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"should_return_hourly_data")," ",(0,r.kt)("em",{parentName:"li"},"bool")," - Set to true to return the hourly data for the valuation.")),(0,r.kt)("h4",{id:"delete_valuation"},"delete","_","valuation"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def delete_valuation(valuation_id)\n")),(0,r.kt)("p",null,"Deletes a valuation from Amun."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"valuation_id")," ",(0,r.kt)("em",{parentName:"li"},"string")," - The id of the valuation to delete.")),(0,r.kt)("h4",{id:"get_wind"},"get","_","wind"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def get_wind(lat, lon, year, dataset)\n")),(0,r.kt)("p",null,"The parameters used for built in wind calculations (",(0,r.kt)("em",{parentName:"p"},"era5"),",",(0,r.kt)("em",{parentName:"p"},"merra2"),",",(0,r.kt)("em",{parentName:"p"},"newa"),")."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Notes"),":"),(0,r.kt)("p",null,"  Not all locations support all wind types and not all locations support Regional Reanalysis Correction."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"latitude")," ",(0,r.kt)("em",{parentName:"li"},"float")," - The latitude of the point (-90 to 90)."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"longitude")," ",(0,r.kt)("em",{parentName:"li"},"float")," - The latitude of the point (-180 to 180).\nyear (number):The year to fetch wind data for."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"dataset")," ",(0,r.kt)("em",{parentName:"li"},"str")," - one of (",'"',"Era5",'"',",",'"',"Merra2",'"',",",'"',"NEWA",'"',").")),(0,r.kt)("h4",{id:"get_wind_atlas"},"get","_","wind","_","atlas"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def get_wind_atlas(lat, lon, radius, numberOfTurbines, rotorDiameterInMeters,\n                   regionCode)\n")),(0,r.kt)("p",null,"The parameters used for built in wind calculations (",(0,r.kt)("em",{parentName:"p"},"era5"),",",(0,r.kt)("em",{parentName:"p"},"merra2"),",",(0,r.kt)("em",{parentName:"p"},"newa"),")."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Notes"),":"),(0,r.kt)("p",null,"  Not all locations are supported."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"latitude")," ",(0,r.kt)("em",{parentName:"li"},"float")," - The latitude of the point (-90 to 90)."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"longitude")," ",(0,r.kt)("em",{parentName:"li"},"float")," - The latitude of the point (-180 to 180).\nradius (int):The radius of the area to average wind speed over 0 to 1000."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"numberOfTurbines")," ",(0,r.kt)("em",{parentName:"li"},"int")," - If no radius specified this is required to allow the size of the windfarm to be estimated.\nrotorDiameterInMeters (int):The rotor diameter of the turbines used to calculate size of the windfarm from the number of turbines if None a default value is used.")),(0,r.kt)("h4",{id:"get_windfarms"},"get","_","windfarms"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def get_windfarms(search)\n")),(0,r.kt)("p",null,"Search for windfarms"),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"search")," ",(0,r.kt)("em",{parentName:"li"},"string")," - Search term to filter by.")),(0,r.kt)("h4",{id:"get_windfarm"},"get","_","windfarm"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def get_windfarm(uuid)\n")),(0,r.kt)("p",null,"Get windfarm by uuid"),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"search")," ",(0,r.kt)("em",{parentName:"li"},"uuid")," - uuid of windfarm to get.")))}c.isMDXComponent=!0}}]);