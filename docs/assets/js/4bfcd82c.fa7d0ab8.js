"use strict";(self.webpackChunkamun_sdk=self.webpackChunkamun_sdk||[]).push([[852],{3905:(e,a,t)=>{t.d(a,{Zo:()=>c,kt:()=>f});var r=t(7294);function n(e,a,t){return a in e?Object.defineProperty(e,a,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[a]=t,e}function s(e,a){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);a&&(r=r.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),t.push.apply(t,r)}return t}function o(e){for(var a=1;a<arguments.length;a++){var t=null!=arguments[a]?arguments[a]:{};a%2?s(Object(t),!0).forEach((function(a){n(e,a,t[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):s(Object(t)).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(t,a))}))}return e}function i(e,a){if(null==e)return{};var t,r,n=function(e,a){if(null==e)return{};var t,r,n={},s=Object.keys(e);for(r=0;r<s.length;r++)t=s[r],a.indexOf(t)>=0||(n[t]=e[t]);return n}(e,a);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);for(r=0;r<s.length;r++)t=s[r],a.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(n[t]=e[t])}return n}var l=r.createContext({}),u=function(e){var a=r.useContext(l),t=a;return e&&(t="function"==typeof e?e(a):o(o({},a),e)),t},c=function(e){var a=u(e.components);return r.createElement(l.Provider,{value:a},e.children)},m="mdxType",d={inlineCode:"code",wrapper:function(e){var a=e.children;return r.createElement(r.Fragment,{},a)}},p=r.forwardRef((function(e,a){var t=e.components,n=e.mdxType,s=e.originalType,l=e.parentName,c=i(e,["components","mdxType","originalType","parentName"]),m=u(t),p=n,f=m["".concat(l,".").concat(p)]||m[p]||d[p]||s;return t?r.createElement(f,o(o({ref:a},c),{},{components:t})):r.createElement(f,o({ref:a},c))}));function f(e,a){var t=arguments,n=a&&a.mdxType;if("string"==typeof e||n){var s=t.length,o=new Array(s);o[0]=p;var i={};for(var l in a)hasOwnProperty.call(a,l)&&(i[l]=a[l]);i.originalType=e,i[m]="string"==typeof e?e:n,o[1]=i;for(var u=2;u<s;u++)o[u]=t[u];return r.createElement.apply(null,o)}return r.createElement.apply(null,t)}p.displayName="MDXCreateElement"},6553:(e,a,t)=>{t.r(a),t.d(a,{assets:()=>l,contentTitle:()=>o,default:()=>d,frontMatter:()=>s,metadata:()=>i,toc:()=>u});var r=t(7462),n=(t(7294),t(3905));const s={title:"Advanced Features"},o=void 0,i={unversionedId:"Examples/Load Factors/advanced",id:"Examples/Load Factors/advanced",title:"Advanced Features",description:"There are cases where you could benefit from running multiple load factor simulations in bulk using runloadfactorsforparametersbatch. In cases where you need to produce results for over 100 iterations, it will be faster than using common functions.",source:"@site/docs/Examples/01-Load Factors/02-advanced.md",sourceDirName:"Examples/01-Load Factors",slug:"/Examples/Load Factors/advanced",permalink:"/aurora-amun-python-sdk/docs/Examples/Load Factors/advanced",draft:!1,tags:[],version:"current",sidebarPosition:2,frontMatter:{title:"Advanced Features"},sidebar:"docSidebar",previous:{title:"Common Examples",permalink:"/aurora-amun-python-sdk/docs/Examples/Load Factors/common"},next:{title:"Common Examples",permalink:"/aurora-amun-python-sdk/docs/Examples/Valuations/common"}},l={},u=[{value:"Calculating load factors for all wind types",id:"calculating-load-factors-for-all-wind-types",level:3},{value:"Iterating though parameter values",id:"iterating-though-parameter-values",level:3}],c={toc:u},m="wrapper";function d(e){let{components:a,...t}=e;return(0,n.kt)(m,(0,r.Z)({},c,t,{components:a,mdxType:"MDXLayout"}),(0,n.kt)("p",null,"There are cases where you could benefit from running multiple load factor simulations in bulk using ",(0,n.kt)("a",{parentName:"p",href:"/docs/Reference/session#run_load_factors_for_parameters_batch"},(0,n.kt)("inlineCode",{parentName:"a"},"run_load_factors_for_parameters_batch")),". In cases where you need to produce results for over 100 iterations, it will be faster than using common functions."),(0,n.kt)("h3",{id:"calculating-load-factors-for-all-wind-types"},"Calculating load factors for all wind types"),(0,n.kt)("p",null,"In this example, you can see how you can run load factor calculation iterating through different wind types. You can do it by creating a base parameters objects that all the calculations will use (",(0,n.kt)("inlineCode",{parentName:"p"},"base_parameters"),") and create a list of parameters for individual requests (",(0,n.kt)("inlineCode",{parentName:"p"},"list_of_parameters"),"). After this, you can send all the requests. Be aware that you will need to provide the same number of base parameters and flow parameters because they are paired with each other."),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},'from datetime import datetime\nfrom aurora.amun.client.parameters import (\n    AverageWindSpeedParameters,\n    BuiltInWindParameters,\n    LoadFactorBaseParameters,\n    P50ScalingParameters,\n    PowerDensityParameters,\n    WeibullParameters,\n    P50YieldScalingParameters,\n)\nfrom aurora.amun.client.session import AmunSession\nfrom aurora.amun.client.utils import save_to_json\n\nsession = AmunSession()\nturbine = session.get_turbine_by_name("Siemens SWT-4.0-130")\n\nbase_parameters = LoadFactorBaseParameters(\n    turbineModelId=turbine["id"],\n    latitude=59.59,\n    longitude=0,\n    startTimeUTC="2018-01-01T00:00:00.000Z",\n    regionCode="GBR",\n    hubHeight=90,\n    obstacleHeight=0,\n    lossesAvailability=0.1,\n    lossesWake=0,\n    numberOfTurbines=12,\n    roughnessLength=0.02,\n    usePowerCurveSmoothing=False,\n    useReanalysisCorrection=False,\n)\n\nlist_of_parameters = [\n    BuiltInWindParameters("era5"),\n    WeibullParameters(measurementHeight=90, weibullScale=12, weibullShape=6),\n    PowerDensityParameters(measurementHeight=90, averagePowerDensity=400.1),\n    AverageWindSpeedParameters(measurementHeight=90, averageWindSpeed=6.43),\n    P50ScalingParameters(p50GrossProduction=0.4),\n    P50YieldScalingParameters(annualProductionInGWHours=200)\n]\n\nprint("Running load factor calculations. This will take a few minutes...")\nresults = session.run_load_factors_for_parameters_batch(\n    list_of_parameters,\n    [base_parameters] * len(list_of_parameters) # We must match every flow parameter with a base parameter\n)\n\n# Save each result individually pairing it with the request parameters\n# (the results come in the same order as the requests)\nfor result, params in zip(results, list_of_parameters):\n    \n    # If you want, you can use a unique identifier for each request in the name of your file\n    # You can later use this ID to request the results of this specific request again later\n    loadFactorRequestId = result["parameters"]["loadFactorRequestId"]\n\n    timestamp = datetime.now().isoformat().replace(\':\',\'_\')\n    save_to_json(\n        f"load_factors/load_factors_{timestamp}_{params.windType}_{loadFactorRequestId}.json",\n        result,\n    )\n')),(0,n.kt)("p",null,"You will see 6 result files in the ",(0,n.kt)("inlineCode",{parentName:"p"},"out/load_factors/")," directory. This approach will be faster than using ",(0,n.kt)("a",{parentName:"p",href:"/docs/Reference/session#run_load_factor_for_parameters"},(0,n.kt)("inlineCode",{parentName:"a"},"AmunSession.run_load_factors_for_parameters"))," in a for-loop"),(0,n.kt)("h3",{id:"iterating-though-parameter-values"},"Iterating though parameter values"),(0,n.kt)("p",null,"You can iterate though values to conduct studies. For example, you can submit a large number of requests to see what results different average wind speed values produce"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},'from aurora.amun.client.parameters import AverageWindSpeedParameters, LoadFactorBaseParameters\nfrom aurora.amun.client.session import AmunSession\nfrom aurora.amun.client.utils import save_to_json\n\nsession = AmunSession()\nturbine = session.get_turbine_by_name("Siemens SWT-4.0-130")\n\nbase_parameters = LoadFactorBaseParameters(\n    turbineModelId=turbine["id"],\n    latitude=59.59,\n    longitude=0,\n    startTimeUTC="2018-01-01T00:00:00.000Z",\n    regionCode="GBR",\n    hubHeight=90,\n    obstacleHeight=0,\n    lossesAvailability=0.1,\n    lossesWake=0,\n    numberOfTurbines=12,\n    roughnessLength=0.02,\n    usePowerCurveSmoothing=False,\n    useReanalysisCorrection=False,\n)\n\n# Wind speeds from 1.0 to 15.0 m/s in 0.1 m/s increments\nvariants = []\nfor speedTimes10 in range(10, 150, 1):\n    speed = speedTimes10 / 10   # So that we could interate more granularly\n    variants.append(AverageWindSpeedParameters(measurementHeight=90, averageWindSpeed=speed))\n\nprint("Running load factor calculations. This will take a few minutes...")\nresults = session.run_load_factors_for_parameters_batch(\n    variants,\n    [base_parameters] * len(variants) # This is needed to match every variant of wind speed with a base parameter\n)\n\nfor result, variant in zip(results, variants):\n    save_to_json(\n        f"load_factors/load_factors_for_avg_wind_speed_{variant.averageWindSpeed}.json",\n        result,\n    )\n')),(0,n.kt)("p",null,"At the time this example was written, it took 29 minutes to run these 100 calculations."))}d.isMDXComponent=!0}}]);