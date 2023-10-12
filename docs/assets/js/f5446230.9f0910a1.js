"use strict";(self.webpackChunkamun_sdk=self.webpackChunkamun_sdk||[]).push([[579],{3905:(e,t,a)=>{a.d(t,{Zo:()=>u,kt:()=>h});var r=a(7294);function n(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function l(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,r)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?l(Object(a),!0).forEach((function(t){n(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):l(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function s(e,t){if(null==e)return{};var a,r,n=function(e,t){if(null==e)return{};var a,r,n={},l=Object.keys(e);for(r=0;r<l.length;r++)a=l[r],t.indexOf(a)>=0||(n[a]=e[a]);return n}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(r=0;r<l.length;r++)a=l[r],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(n[a]=e[a])}return n}var o=r.createContext({}),p=function(e){var t=r.useContext(o),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},u=function(e){var t=p(e.components);return r.createElement(o.Provider,{value:t},e.children)},m="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},c=r.forwardRef((function(e,t){var a=e.components,n=e.mdxType,l=e.originalType,o=e.parentName,u=s(e,["components","mdxType","originalType","parentName"]),m=p(a),c=n,h=m["".concat(o,".").concat(c)]||m[c]||d[c]||l;return a?r.createElement(h,i(i({ref:t},u),{},{components:a})):r.createElement(h,i({ref:t},u))}));function h(e,t){var a=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var l=a.length,i=new Array(l);i[0]=c;var s={};for(var o in t)hasOwnProperty.call(t,o)&&(s[o]=t[o]);s.originalType=e,s[m]="string"==typeof e?e:n,i[1]=s;for(var p=2;p<l;p++)i[p]=a[p];return r.createElement.apply(null,i)}return r.createElement.apply(null,a)}c.displayName="MDXCreateElement"},209:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>o,contentTitle:()=>i,default:()=>d,frontMatter:()=>l,metadata:()=>s,toc:()=>p});var r=a(7462),n=(a(7294),a(3905));const l={sidebar_label:"parameters",title:"parameters"},i=void 0,s={unversionedId:"Reference/parameters",id:"Reference/parameters",title:"parameters",description:"WindType Objects",source:"@site/docs/Reference/parameters.md",sourceDirName:"Reference",slug:"/Reference/parameters",permalink:"/aurora-amun-python-sdk/docs/Reference/parameters",draft:!1,tags:[],version:"current",frontMatter:{sidebar_label:"parameters",title:"parameters"},sidebar:"docSidebar",previous:{title:"Get a Power Curve for a Turbine",permalink:"/aurora-amun-python-sdk/docs/Examples/Turbines/get-power-curve"},next:{title:"responses",permalink:"/aurora-amun-python-sdk/docs/Reference/responses"}},o={},p=[{value:"WindType Objects",id:"windtype-objects",level:2},{value:"AverageWindSpeed",id:"averagewindspeed",level:4},{value:"AuroraWindAtlas",id:"aurorawindatlas",level:4},{value:"CalibratedGeneration",id:"calibratedgeneration",level:4},{value:"Era5",id:"era5",level:4},{value:"Generation",id:"generation",level:4},{value:"Merra2",id:"merra2",level:4},{value:"NEWA",id:"newa",level:4},{value:"P50Scaling",id:"p50scaling",level:4},{value:"P50YieldScaling",id:"p50yieldscaling",level:4},{value:"PowerDensity",id:"powerdensity",level:4},{value:"UploadedWind",id:"uploadedwind",level:4},{value:"Weibull",id:"weibull",level:4},{value:"SpeedAtHeight Objects",id:"speedatheight-objects",level:2},{value:"LoadFactorBaseParameters Objects",id:"loadfactorbaseparameters-objects",level:2},{value:"FlowParameters Objects",id:"flowparameters-objects",level:2},{value:"AverageWindSpeedParameters Objects",id:"averagewindspeedparameters-objects",level:2},{value:"BuiltInWindParameters Objects",id:"builtinwindparameters-objects",level:2},{value:"P50ScalingParameters Objects",id:"p50scalingparameters-objects",level:2},{value:"P50YieldScalingParameters Objects",id:"p50yieldscalingparameters-objects",level:2},{value:"PowerDensityParameters Objects",id:"powerdensityparameters-objects",level:2},{value:"UploadedWindParameters Objects",id:"uploadedwindparameters-objects",level:2},{value:"WeibullParameters Objects",id:"weibullparameters-objects",level:2}],u={toc:p},m="wrapper";function d(e){let{components:t,...a}=e;return(0,n.kt)(m,(0,r.Z)({},u,a,{components:t,mdxType:"MDXLayout"}),(0,n.kt)("h2",{id:"windtype-objects"},"WindType Objects"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},"class WindType(Enum)\n")),(0,n.kt)("p",null,"The types of wind to use in calculations"),(0,n.kt)("h4",{id:"averagewindspeed"},"AverageWindSpeed"),(0,n.kt)("p",null,"Amun will use wind speed reanalysis data in the location and calibrate it so that the long-term average wind speed matched the user","'","s projection."),(0,n.kt)("h4",{id:"aurorawindatlas"},"AuroraWindAtlas"),(0,n.kt)("p",null,"Aurora","'","s high-resolution wind speed atlas based on Aurora","'","s data from existing wind farms. Check the region details for availability."),(0,n.kt)("h4",{id:"calibratedgeneration"},"CalibratedGeneration"),(0,n.kt)("p",null,"Hourly simulated production series in the same reference year as Aurora","'","s power market model uploaded by the user. The only adjustment made by Amun to this data will come from price-based economic curtailment."),(0,n.kt)("h4",{id:"era5"},"Era5"),(0,n.kt)("p",null,"ERA5 reanalysis dataset. Check the region details for availability."),(0,n.kt)("h4",{id:"generation"},"Generation"),(0,n.kt)("p",null,"At least one year of hourly metered or modelled production uploaded by the user. Amun will use this data create bespoke power curve that captures the relationship between reanalysis wind speed and observed generation."),(0,n.kt)("h4",{id:"merra2"},"Merra2"),(0,n.kt)("p",null,"MERRA-2 reanalysis dataset. Check the region details for availability."),(0,n.kt)("h4",{id:"newa"},"NEWA"),(0,n.kt)("p",null,"NEWA reanalysis dataset. Check the region details for availability."),(0,n.kt)("h4",{id:"p50scaling"},"P50Scaling"),(0,n.kt)("p",null,"Represents the site","'","s long-term P50 production potential as a load factor. Amun will calibrate underlying reanalysis wind speeds to match the long-term P50 load factor."),(0,n.kt)("h4",{id:"p50yieldscaling"},"P50YieldScaling"),(0,n.kt)("p",null,"Represents the site","'","s long-term production P50 potential as generation (GWh/year). Amun will calibrate underlying reanalysis wind speeds to match the long-term P50 production."),(0,n.kt)("h4",{id:"powerdensity"},"PowerDensity"),(0,n.kt)("p",null,"Power Density is a quantitative measure of wind energy available at a location. Amun will calibrate underlying reanalysis wind speeds to match the average power density."),(0,n.kt)("h4",{id:"uploadedwind"},"UploadedWind"),(0,n.kt)("p",null,"Upload at least one year of hourly modelled or metered wind speed data to calibrate your wind speed profile. Amun will use this data to derive a statistical relationship between uploaded data and the reanalysis wind speed for the same location and time period uploaded."),(0,n.kt)("h4",{id:"weibull"},"Weibull"),(0,n.kt)("p",null,"Weibull parameters represent the long-term wind speed distribution at the site. Amun will calibrate underlying reanalysis wind speeds distribution to match shape."),(0,n.kt)("h2",{id:"speedatheight-objects"},"SpeedAtHeight Objects"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},"class SpeedAtHeight()\n")),(0,n.kt)("p",null,"The wind speeds at a given height,"),(0,n.kt)("p",null,(0,n.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"height")," ",(0,n.kt)("em",{parentName:"li"},"float")," - The measurement height (m) of the wind speeds."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"speeds")," ",(0,n.kt)("em",{parentName:"li"},"List","[float]")," - A list of wind speeds in m/s.")),(0,n.kt)("h2",{id:"loadfactorbaseparameters-objects"},"LoadFactorBaseParameters Objects"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},"class LoadFactorBaseParameters()\n")),(0,n.kt)("p",null,"Parameters for all wind types."),(0,n.kt)("p",null,(0,n.kt)("strong",{parentName:"p"},"Notes"),":"),(0,n.kt)("p",null,"  Not all regions/locations support Multi-Turbine Power Curve Smoothing."),(0,n.kt)("p",null,(0,n.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"turbineModelId")," (int): The Id of the Turbine to use in the calculation as returned from ",(0,n.kt)("inlineCode",{parentName:"li"},".AmunSession.get_turbines"),"."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"latitude")," (float): The latitude of the point (-90 to 90)."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"longitude")," (float): The latitude of the point (-180 to 180)."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"startTimeUTC")," (str): The time in UTC that the calcution should start from. This must be in the form ","'",(0,n.kt)("em",{parentName:"li"},"2016-07-28T00:00:00.000Z"),"'"," ."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"regionCode")," (str): The code for the region used to set region specific parameters."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"hubHeight")," (float): Given in meters (m)."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"obstacleHeight")," (float): Given in meters (m)."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"numberOfTurbines")," (int): The number of turbines in the site."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"roughnessLength")," (float, optional): Static roughness. If not given, will be derived from reanalysis data. Defaults to None."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"usePowerCurveSmoothing")," (bool, optional): Should Default Multi-Turbine Power Curve Smoothing be used in the calculation if true then a region specific scale factor is used. If None then no smoothing is applied Defaults to None."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"useReanalysisCorrection")," (bool, optional): Should Reanalysis Correctionbe used only valid for ERA5, Defaults to False."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"smoothingCoefficient")," (float): The value to use for smoothing. This will override any region specific values. This has no effect unless ",(0,n.kt)("em",{parentName:"li"},"usePowerCurveSmoothing")," is true."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"lossesWake")," (float, default 0): The percentage to apply for wake loss. (0 ","<","= lossesWake ","<"," 1)"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"lossesAvailability")," (float, default 0): Percentage for external losses.  (0 ","<","= lossesAvailability ","<"," 1)"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"lossesElectrical")," (float, default 0): Percentage for external losses.  (0 ","<","= lossesElectrical ","<"," 1)"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"lossesTurbinePerformance")," (float, default 0): Percentage for external losses.  (0 ","<","= lossesTurbinePerformance ","<"," 1)"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"lossesEnvironmental")," (float, default 0): Percentage for external losses.  (0 ","<","= lossesEnvironmental ","<"," 1)"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("strong",{parentName:"li"},"lossesOtherCurtailment")," (float, default 0): Percentage for external losses.  (0 ","<","= lossesOtherCurtailment ","<"," 1)")),(0,n.kt)("h2",{id:"flowparameters-objects"},"FlowParameters Objects"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},"class FlowParameters()\n")),(0,n.kt)("p",null,"Base class for a flow. Internal Use only."),(0,n.kt)("p",null,(0,n.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"windType")," ",(0,n.kt)("em",{parentName:"li"},"WindType")," - All flows must define a unique windtype as defined by the Amun http API.")),(0,n.kt)("h2",{id:"averagewindspeedparameters-objects"},"AverageWindSpeedParameters Objects"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},"class AverageWindSpeedParameters(FlowParameters)\n")),(0,n.kt)("p",null,"The parameters required for a ",(0,n.kt)("em",{parentName:"p"},"AverageWindSpeed")," calculation."),(0,n.kt)("p",null,(0,n.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"averageWindSpeed")," ",(0,n.kt)("em",{parentName:"li"},"float")," - The average wind speed of your site to use as calibration (m/s)"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"measurementHeight")," ",(0,n.kt)("em",{parentName:"li"},"float")," - The height at which the measurements were taken (m)")),(0,n.kt)("h2",{id:"builtinwindparameters-objects"},"BuiltInWindParameters Objects"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},"class BuiltInWindParameters(FlowParameters)\n")),(0,n.kt)("p",null,"The parameters used for built in wind calculations."),(0,n.kt)("p",null,(0,n.kt)("strong",{parentName:"p"},"Notes"),":"),(0,n.kt)("p",null,"  Not all locations support all wind types and not all locations support Regional Reanalysis Correction."),(0,n.kt)("p",null,(0,n.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"windType")," ",(0,n.kt)("em",{parentName:"li"},"WindType")," - AuroraWindAtlas, Era5, Merra2, or NEWA"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"useReanalysisCorrection")," ",(0,n.kt)("em",{parentName:"li"},"bool, optional")," - Should Regional Reanalysis Correction be enabled.\nIf true then a location specific ",(0,n.kt)("em",{parentName:"li"},"reanalysisScaleCorrectionDelta")," is used. Defaults to None."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"reanalysisScaleCorrectionDelta")," ",(0,n.kt)("em",{parentName:"li"},"float, optional")," - Override the location specific\n",(0,n.kt)("em",{parentName:"li"},"reanalysisScaleCorrectionDelta"),". This has no effect if ",(0,n.kt)("em",{parentName:"li"},"reanalysisScaleCorrectionDelta")," is false. Defaults to None.")),(0,n.kt)("h2",{id:"p50scalingparameters-objects"},"P50ScalingParameters Objects"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},"class P50ScalingParameters(FlowParameters)\n")),(0,n.kt)("p",null,"The parameters required for a ",(0,n.kt)("em",{parentName:"p"},"P50Scaling")," calculation."),(0,n.kt)("p",null,(0,n.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"p50GrossProduction")," ",(0,n.kt)("em",{parentName:"li"},"float, 0 ","<"," p50GrossProduction ","<"," 1")," - the P50 load factor which represents the long-term production potential of this site,\ntypically from an energy assessment report, will be used to calibrate the underlying reanalysis wind speed,\nsuch that the long-term production potential used in Amun-based valuations are the same.")),(0,n.kt)("h2",{id:"p50yieldscalingparameters-objects"},"P50YieldScalingParameters Objects"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},"class P50YieldScalingParameters(FlowParameters)\n")),(0,n.kt)("p",null,"The parameters required for a ",(0,n.kt)("em",{parentName:"p"},"P50YieldScaling")," calculation."),(0,n.kt)("p",null,(0,n.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"annualProductionInGWHours")," ",(0,n.kt)("em",{parentName:"li"},"float, 0 ","<"," annualProductionInGWHours ","<"," 1000000")," - the production expected by the site in a year in Gigawatt Hours.")),(0,n.kt)("h2",{id:"powerdensityparameters-objects"},"PowerDensityParameters Objects"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},"class PowerDensityParameters(FlowParameters)\n")),(0,n.kt)("p",null,"The parameters required for a ",(0,n.kt)("em",{parentName:"p"},"PowerDensity")," calculation."),(0,n.kt)("p",null,(0,n.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"averagePowerDensity")," ",(0,n.kt)("em",{parentName:"li"},"float")," - The average power density of your site to use as calibration (W/m2)"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"measurementHeight")," ",(0,n.kt)("em",{parentName:"li"},"float")," - The height at which the measurements were taken (m)")),(0,n.kt)("h2",{id:"uploadedwindparameters-objects"},"UploadedWindParameters Objects"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},"class UploadedWindParameters(FlowParameters)\n")),(0,n.kt)("p",null,"The parameters required to run a custom (uploaded) load factor calculation.  If ",(0,n.kt)("em",{parentName:"p"},"highHeight"),"\nis specified it must be the same length as the ",(0,n.kt)("em",{parentName:"p"},"lowHeight")," and be measured at a greater height.\nThe speeds upload should be hourly measurements starting at ",(0,n.kt)("em",{parentName:"p"},"uploadedWindStartTime")," and span at least 1 year."),(0,n.kt)("p",null,(0,n.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"uploadedWindStartTime")," ",(0,n.kt)("em",{parentName:"li"},"str")," - The time in UTC that the wind speeds upload start from. This must be in the form ","'",(0,n.kt)("em",{parentName:"li"},"2016-07-28T00:00:00.000Z"),"'"," ."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"lowHeight")," ",(0,n.kt)("em",{parentName:"li"},"SpeedAtHeight")," - The height and speed for the low height wind speed to upload."),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"highHeight")," ",(0,n.kt)("em",{parentName:"li"},"SpeedAtHeight, optional")," - The height and speed for the high height wind speed to upload. Defaults to None.")),(0,n.kt)("h2",{id:"weibullparameters-objects"},"WeibullParameters Objects"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},"class WeibullParameters(FlowParameters)\n")),(0,n.kt)("p",null,"The parameters required for a ",(0,n.kt)("em",{parentName:"p"},"Weibull")," calculation."),(0,n.kt)("p",null,(0,n.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"weibullShape")," ",(0,n.kt)("em",{parentName:"li"},"float")," - The long term shape parameter from your wind report"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"weibullScale")," ",(0,n.kt)("em",{parentName:"li"},"float")," - The long term scale parameter from your wind report"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"measurementHeight")," ",(0,n.kt)("em",{parentName:"li"},"float")," - The height at which the measurements were taken (m)")))}d.isMDXComponent=!0}}]);