import{g as i}from"./_commonjsHelpers.de833af9.js";function e(t,r){return arguments.length===2&&!r?null:(r||document).querySelector(t)}e.exists=function(t,r){return arguments.length===2?!!e(t,r):!!e(t)};e.all=function(t,r){if(arguments.length===2&&!r)return[];if(!r||typeof r.querySelectorAll=="function")return Array.apply(null,(r||document).querySelectorAll(t));var n,o,u,l;for(o=0;o<r.length;o++){if(n=r[o].querySelectorAll(t),!l){l=Array.apply(null,n);continue}for(u=0;u<n.length;u++)l.indexOf(n[u])<0&&l.push(n[u])}return l};var f=e;const a=i(f);export{a as s};