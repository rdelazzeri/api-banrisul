import requests
import http.client

def get_token():
    client_id = ''
    client_secret = ''
    sandbox ='https://apidev.banrisul.com.br/cobranca/v1/'
    producao = 'https://api.banrisul.com.br/cobranca/v1/'
    token_url = 'https://apidev.banrisul.com.br/auth/oauth/v2/token'
    token_url2 = 'https://api.banrisul.com.br/auth/oauth/v2/token'
    url = token_url

    headers = {}
    #headers["Accept"] = "application/json"
    #headers["Content-Type"] = "application/json; charset=utf-8"
    #headers["Accept-Encoding"] = "gzip"

    payload = {}
    payload['client_id'] = client_id
    payload['client_secret'] = client_secret
    payload['grant_type'] = 'client_credentials'

    print('tentando com requests')
    print(payload)
    #rs = requests.post(url, headers=headers, data = payload)
    rs = requests.post(url, data = payload)
    print(rs)
    print(rs.content)
    print(rs.request)

def token_conn():
    client_id = 'l7dae62f11052641bd9a7cc8c9e0174264'
    client_secret = '93a385bc56ac41e4a469c21df2fd541d'
    sandbox ='https://apidev.banrisul.com.br/cobranca/v1/OAuth2 '
    producao = 'https://api.banrisul.com.br/cobranca/v1/'
    token_url = 'https://apidev.banrisul.com.br/auth/oauth/v2/token'
    token_url2 = 'https://api.banrisul.com.br/auth/oauth/v2/token'

    url = token_url

    headers = {}

    #headers["Accept"] = "application/json"
    #headers["Content-Type"] = "application/json; charset=utf-8"
    #headers["Accept-Encoding"] = "gzip"

    payload = {}
    payload['client_id'] = client_id
    payload['client_secret'] = client_secret
    payload['grant_type'] = 'client_credentials'
    print('tentando com http')
    conn = http.client.HTTPSConnection(url)
    conn.request("POST", url, headers, payload)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

get_token()
#token_conn()
