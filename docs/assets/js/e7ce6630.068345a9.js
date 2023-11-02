"use strict";(self.webpackChunkamun_sdk=self.webpackChunkamun_sdk||[]).push([[668],{3905:(e,t,n)=>{n.d(t,{Zo:()=>u,kt:()=>y});var r=n(7294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function c(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var i=r.createContext({}),s=function(e){var t=r.useContext(i),n=t;return e&&(n="function"==typeof e?e(t):c(c({},t),e)),n},u=function(e){var t=s(e.components);return r.createElement(i.Provider,{value:t},e.children)},m="mdxType",p={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},d=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,o=e.originalType,i=e.parentName,u=l(e,["components","mdxType","originalType","parentName"]),m=s(n),d=a,y=m["".concat(i,".").concat(d)]||m[d]||p[d]||o;return n?r.createElement(y,c(c({ref:t},u),{},{components:n})):r.createElement(y,c({ref:t},u))}));function y(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=n.length,c=new Array(o);c[0]=d;var l={};for(var i in t)hasOwnProperty.call(t,i)&&(l[i]=t[i]);l.originalType=e,l[m]="string"==typeof e?e:a,c[1]=l;for(var s=2;s<o;s++)c[s]=n[s];return r.createElement.apply(null,c)}return r.createElement.apply(null,n)}d.displayName="MDXCreateElement"},2097:(e,t,n)=>{n.r(t),n.d(t,{contentTitle:()=>d,default:()=>k,frontMatter:()=>p,metadata:()=>y,toc:()=>f});var r=n(7462),a=n(7294),o=n(3905),c=n(6010),l=n(9960),i=n(2263);const s="heroBanner_MZnD",u="buttons_Kv2X",m=()=>{const{siteConfig:e}=(0,i.Z)();return a.createElement("header",{className:(0,c.Z)("hero hero--primary",s)},a.createElement("div",{className:"container"},a.createElement("h1",{className:"hero__title"},e.title),a.createElement("p",{className:"hero__subtitle"},e.tagline),a.createElement("div",{className:u},a.createElement(l.Z,{className:"button button--secondary button--lg margin-right--md",to:"/docs/intro"},"Getting Started"),a.createElement(l.Z,{className:"button button--secondary button--lg margin-right--md",to:"/docs/Examples/Load Factors/common"},"Examples"),a.createElement(l.Z,{className:"button button--secondary button--lg margin-right--md",to:"/docs/Reference/parameters"},"SDK Reference"))))},p={},d=void 0,y={type:"mdx",permalink:"/aurora-amun-python-sdk/",source:"@site/src/pages/index.mdx",description:"---",frontMatter:{}},f=[],b={toc:f},h="wrapper";function k(e){let{components:t,...n}=e;return(0,o.kt)(h,(0,r.Z)({},b,n,{components:t,mdxType:"MDXLayout"}),(0,o.kt)(m,{mdxType:"HomePageHeader"}),(0,o.kt)("hr",null),(0,o.kt)("p",null,"Amun Python SDK allows you use Amun API in your Python applications. Currently, the SDK supports the features like:"),(0,o.kt)("ul",{className:"contains-task-list"},(0,o.kt)("li",{parentName:"ul",className:"task-list-item"},(0,o.kt)("input",{parentName:"li",type:"checkbox",checked:!0,disabled:!0})," ","Calculate load factors"),(0,o.kt)("li",{parentName:"ul",className:"task-list-item"},(0,o.kt)("input",{parentName:"li",type:"checkbox",checked:!0,disabled:!0})," ","Run valuations"),(0,o.kt)("li",{parentName:"ul",className:"task-list-item"},(0,o.kt)("input",{parentName:"li",type:"checkbox",checked:!0,disabled:!0})," ","Access turbine data"),(0,o.kt)("li",{parentName:"ul",className:"task-list-item"},(0,o.kt)("input",{parentName:"li",type:"checkbox",checked:!0,disabled:!0})," ","and more")),(0,o.kt)("p",null,"The SDK and documentation is under active development. Please get in touch with Aurora if you have any questions or feedback."))}k.isMDXComponent=!0}}]);