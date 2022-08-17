import json
import requests
import conf


def obtener_token(usuario, clave):
    url = "https://10.10.20.14/api/aaaLogin.json"
    body = {
        "aaaUser": {
            "attributes": {
                "name": usuario,
                "pwd": clave
            }
        }
    }
    cabecera = {
        "Content-Type": "application/json"
    }
    requests.packages.urllib3.disable_warnings()
    response = requests.post(url, headers=cabecera, data=json.dumps(body), verify=False).json()

    token = response['imdata'][0]['aaaLogin']['attributes']['token']
    return token

token = obtener_token(conf.usuario, conf.clave)

print(token)