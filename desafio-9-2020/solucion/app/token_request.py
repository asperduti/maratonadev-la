import requests

def token_request():
     # Request an IAM token from IBM Cloud IAM API

    # IAM token request documentation:
    # https://cloud.ibm.com/docs/account?topic=account-iamtoken_from_apikey

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    payload = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": "YOUR_API_KEY" # Se puede usar el API key del servicio Watson Machine Learning que se obtiene en el notebook en el último paso(WML APIKEY)
    }
    req = requests.post(
        "https://iam.cloud.ibm.com/identity/token",
        data=payload,
        headers=headers
    )
    res = req.json()

    return res['access_token']
