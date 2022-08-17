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
    print(response)
    token = response['imdata'][0]['aaaLogin']['attributes']['token']

    return token

token = obtener_token(conf.usuario, conf.clave)

def top_level_system():
    sandbox = "https://10.10.20.14/api/aaaLogin.json"
    url = sandbox + "/api/class/topSystem.json"
    cabecera = {
        "Content-Type": "application/json"
    }
    galletas = {
        "APIC-Cookie": token
    }
    respuesta = requests.get(url, headers=cabecera, cookies=galletas, verify=False)
    print(respuesta.json())


top_level_system()

#GET http://apic-ip-address/api/mo/topology/pod-1/node-1/sys/ch/bslot/board/sensor-3.json

def about_node():
    url = "https://10.10.20.14/api/aaaLogin.json"

    cabecera = {
        "Content-Type": "application/json"
    }
    requests.packages.urllib3.disable_warnings()
    print(requests)
    respuesta = requests.get(url+"api/mo/topology/pod-1/node-1/sys/ch/bslot/board/sensor-3.json", headers=cabecera, verify=False)
    print(respuesta.json())

about_node()