"use strict";(self.webpackChunkamun_sdk=self.webpackChunkamun_sdk||[]).push([[630],{5395:(e,n,r)=>{r.r(n),r.d(n,{assets:()=>a,contentTitle:()=>i,default:()=>l,frontMatter:()=>s,metadata:()=>u,toc:()=>c});var t=r(5893),o=r(1151);const s={title:"Get a Power Curve for a Turbine"},i=void 0,u={id:"Examples/Turbines/get-power-curve",title:"Get a Power Curve for a Turbine",description:"You will need to know the exact name of the turbine you want to get the power curve for. To see the list of available turbines in Amun, use AmunSession.getturbines.",source:"@site/docs/Examples/04-Turbines/03-get-power-curve.md",sourceDirName:"Examples/04-Turbines",slug:"/Examples/Turbines/get-power-curve",permalink:"/aurora-amun-python-sdk/docs/Examples/Turbines/get-power-curve",draft:!1,unlisted:!1,tags:[],version:"current",sidebarPosition:3,frontMatter:{title:"Get a Power Curve for a Turbine"},sidebar:"docSidebar",previous:{title:"Add Custom Turbine",permalink:"/aurora-amun-python-sdk/docs/Examples/Turbines/add-example-turbine"},next:{title:"parameters",permalink:"/aurora-amun-python-sdk/docs/Reference/parameters"}},a={},c=[];function p(e){const n={a:"a",code:"code",p:"p",pre:"pre",...(0,o.a)(),...e.components};return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsxs)(n.p,{children:["You will need to know the exact name of the turbine you want to get the power curve for. To see the list of available turbines in Amun, use ",(0,t.jsx)(n.a,{href:"/docs/Reference/session#get_turbines",children:(0,t.jsx)(n.code,{children:"AmunSession.get_turbines"})}),"."]}),"\n",(0,t.jsx)(n.pre,{children:(0,t.jsx)(n.code,{className:"language-python",children:'from aurora.amun.client.session import AmunSession\n\nsession = AmunSession()\nturbine = session.get_turbine_by_name("Siemens SWT-4.0-130")\npower_curve = session.get_power_curve(turbine["id"])\n\n# Print the first three points of the power curve\nprint(power_curve[:3])\n'})}),"\n",(0,t.jsx)(n.p,{children:"The output will look like so:"}),"\n",(0,t.jsx)(n.pre,{children:(0,t.jsx)(n.code,{className:"language-powershell",children:"[{'speed': 1, 'power': 0}, {'speed': 2, 'power': 0}, {'speed': 3, 'power': 79}]\n"})})]})}function l(e={}){const{wrapper:n}={...(0,o.a)(),...e.components};return n?(0,t.jsx)(n,{...e,children:(0,t.jsx)(p,{...e})}):p(e)}},1151:(e,n,r)=>{r.d(n,{Z:()=>u,a:()=>i});var t=r(7294);const o={},s=t.createContext(o);function i(e){const n=t.useContext(s);return t.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function u(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(o):e.components||o:i(e.components),t.createElement(s.Provider,{value:n},e.children)}}}]);