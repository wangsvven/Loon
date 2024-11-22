#!name=AppRaven
#!desc=AppRaven
#!icon=https://github.com/Toperlock/Quantumult/raw/main/icon/Doraemon/Doraemon-1074.png

[Script]
http-response https://appraven.net/appraven/graphql script-path=https://raw.githubusercontent.com/Yu9191/Rewrite/main/AppRaven.js, requires-body=true, timeout=60, tag=AppRaven

[MITM]
hostname = appraven.net
