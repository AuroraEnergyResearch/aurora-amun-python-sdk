"use strict";(self.webpackChunkamun_sdk=self.webpackChunkamun_sdk||[]).push([[671],{3905:(e,t,n)=>{n.d(t,{Zo:()=>p,kt:()=>f});var r=n(7294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var l=r.createContext({}),c=function(e){var t=r.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},p=function(e){var t=c(e.components);return r.createElement(l.Provider,{value:t},e.children)},u="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},m=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,o=e.originalType,l=e.parentName,p=s(e,["components","mdxType","originalType","parentName"]),u=c(n),m=a,f=u["".concat(l,".").concat(m)]||u[m]||d[m]||o;return n?r.createElement(f,i(i({ref:t},p),{},{components:n})):r.createElement(f,i({ref:t},p))}));function f(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=n.length,i=new Array(o);i[0]=m;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s[u]="string"==typeof e?e:a,i[1]=s;for(var c=2;c<o;c++)i[c]=n[c];return r.createElement.apply(null,i)}return r.createElement.apply(null,n)}m.displayName="MDXCreateElement"},9881:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>l,contentTitle:()=>i,default:()=>d,frontMatter:()=>o,metadata:()=>s,toc:()=>c});var r=n(7462),a=(n(7294),n(3905));const o={sidebar_position:1,sidebar_label:"Installation",title:"Installation",description:"Getting the SDK installed and authenticated"},i="Installation",s={unversionedId:"intro",id:"intro",title:"Installation",description:"Getting the SDK installed and authenticated",source:"@site/docs/intro.md",sourceDirName:".",slug:"/intro",permalink:"/aurora-amun-python-sdk-docs/docs/intro",draft:!1,tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1,sidebar_label:"Installation",title:"Installation",description:"Getting the SDK installed and authenticated"},sidebar:"docSidebar",next:{title:"Common Examples",permalink:"/aurora-amun-python-sdk-docs/docs/Examples/Load Factors/common"}},l={},c=[],p={toc:c},u="wrapper";function d(e){let{components:t,...n}=e;return(0,a.kt)(u,(0,r.Z)({},p,n,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"installation"},"Installation"),(0,a.kt)("ol",null,(0,a.kt)("li",{parentName:"ol"},"Install the package from the git repository")),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"pip install git+https://github.com/AuroraEnergyResearch/aurora-amun-python-sdk\n")),(0,a.kt)("ol",{start:2},(0,a.kt)("li",{parentName:"ol"},(0,a.kt)("p",{parentName:"li"},"In order to use the Amun API a user token is required and can be created in ",(0,a.kt)("a",{parentName:"p",href:"https://eos.auroraer.com/dragonfly/settings"},"EOS settings"),". Add your Aurora API key to the file $home/.aurora-api-key. for example ",(0,a.kt)("inlineCode",{parentName:"p"},"C:\\Users\\Joe Bloggs\\.aurora-api-key")," or set as the environment variable ",(0,a.kt)("inlineCode",{parentName:"p"},"AURORA_API_KEY"),". ")),(0,a.kt)("li",{parentName:"ol"},(0,a.kt)("p",{parentName:"li"},"Once the key is set up the ",(0,a.kt)("inlineCode",{parentName:"p"},"AmunSession")," object can be created to access the API. Examples of methods available can be found in ",(0,a.kt)("a",{parentName:"p",href:"/docs/Reference/session"},"AmunSession")," for details on usage."))),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},'from aurora.amun.client.session import AmunSession\nsession  = AmunSession()\nresult  = session.get_scenarios("gbr")\nprint(result[0])\n')),(0,a.kt)("p",null,"Output to expect:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-powershell"},"{'id': 3, 'name': '2019 Smart Power Scenario', 'description': 'To examine the impact of a smarter power system with more flexible capacity and demand', 'isRetired': True, 'region': 'gbr', 'S3uri': None, 'currency': 'GBP', 'currencyYear': 2018, 'publicationDate': '2020-01-09T17:02:05.000Z', 'type': 'legacy', 'scenarioVersion': 0, 'hash': 'a5da31ed-f72d-424e-9d41-a81873269dbc', 'hasFile': False}\n")))}d.isMDXComponent=!0}}]);