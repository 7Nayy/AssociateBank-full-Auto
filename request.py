from config import SECRET_ID, SECRET_KEY
import requests

def obtenir_token(secret_id, secret_key):
    url_token = "https://bankaccountdata.gocardless.com/api/v2/token/new/"
    headers_token = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    data_token = {
        "secret_id": secret_id,
        "secret_key": secret_key,
    }

    response_token = requests.post(url_token, headers=headers_token, json=data_token)

    try:
        response_token.raise_for_status()
        access_token = response_token.json().get("access")
        refresh_token = response_token.json().get("refresh")
        print("Token obtenu avec succès.")
        return access_token, refresh_token
    except requests.exceptions.HTTPError as err:
        print(f"Échec de la requête pour obtenir le token avec le code d'état {response_token.status_code} :")
        print(err)
        print(response_token.text)
        return None, None

def actualiser_token(refresh_token):
    url_refresh_token = "https://bankaccountdata.gocardless.com/api/v2/token/refresh/"
    headers_refresh_token = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    data_refresh_token = {
        "refresh": refresh_token,
    }

    response_refresh_token = requests.post(url_refresh_token, headers=headers_refresh_token, json=data_refresh_token)

    try:
        response_refresh_token.raise_for_status()
        access_token = response_refresh_token.json().get("access")
        print("Token rafraîchi avec succès.")
        return access_token
    except requests.exceptions.HTTPError as err:
        print(f"Échec de la requête pour rafraîchir le token avec le code d'état {response_refresh_token.status_code} :")
        print(err)
        print(response_refresh_token.text)

        return None

import requests

def obtenir_informations_institutions(access_token):
    url_institutions = "https://bankaccountdata.gocardless.com/api/v2/institutions/HELLO_BANK_BNPAFRPPXXX"
    headers_institutions = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    response_institutions = requests.get(url_institutions, headers=headers_institutions)

    try:
        response_institutions.raise_for_status()
        print("Requête pour obtenir des informations sur les institutions réussie ! Voici la réponse JSON :")
        print(response_institutions.json())

        # Ajouter cette ligne pour renvoyer la réponse JSON
        return response_institutions.json()
    except requests.exceptions.HTTPError as err:
        print(f"Échec de la requête pour obtenir des informations sur les institutions avec le code d'état {response_institutions.status_code} :")
        print(err)
        print(response_institutions.text)

        # En cas d'échec, renvoyer None ou une valeur par défaut
        return None
