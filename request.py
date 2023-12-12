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

def build_link(access_token):

    url = "https://bankaccountdata.gocardless.com/api/v2/requisitions/"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "redirect": "https://7nayy.pythonanywhere.com/menu/",
        "institution_id": "HELLO_BANK_BNPAFRPPXXX",
        "user_language": "FR",
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        response.raise_for_status()
        print("Requête pour créer une réquisition réussie ! Voici la réponse JSON :")
        print(response.json())
        response.json().get("id")
        return response
    except requests.exceptions.HTTPError as err:
        print(f"Échec de la requête pour créer une réquisition avec le code d'état {response.status_code} :")
        print(err)
        print(response.text)




def create_bridge(access_token, response):
    rel = response.json().get("id")
    url_create_requisition = "https://bankaccountdata.gocardless.com/api/v2/requisitions/"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    data_requisition = {
        "redirect": "http://www.yourwebpage.com",
        "institution_id": "HELLO_BANK_BNPAFRPPXXX",
        "user_language": "FR",
    }

    # Utilisez l'ID de la réquisition pour effectuer une nouvelle requête GET pour les transactions
    url_get_transactions = f"https://bankaccountdata.gocardless.com/api/v2/requisitions/{rel}/"

    try:
        response_transactions = requests.get(url_get_transactions, headers=headers)
        response_transactions.raise_for_status()
        print("Requête GET pour les transactions réussie ! Voici la réponse JSON :")
        print(response_transactions.json())
    except requests.exceptions.HTTPError as err:
        print(f"Échec de la requête GET avec le code d'état {response_transactions.status_code} :")
        print(err)
        print(response_transactions.text)



def acces_account(access_token, account_id):
    url = f"https://bankaccountdata.gocardless.com/api/v2/accounts/{account_id}/transactions/"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print("Requête GET réussie ! Voici la réponse JSON :")
        print(response.json())
    except requests.exceptions.HTTPError as err:
        print(f"Échec de la requête GET avec le code d'état {response.status_code} :")
        print(err)
        print(response.text)

def obtenir_transactions(account_id, access_token):
    url = f"https://bankaccountdata.gocardless.com/api/v2/accounts/{account_id}/transactions/"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        # Assurez-vous que la structure des données est conforme à vos attentes
        if 'transactions' in data and 'booked' in data['transactions']:
            transactions = data['transactions']['booked']

            # Utiliser une liste en compréhension pour extraire les champs nécessaires
            transactions_filtrees = [
                {
                    "amount": transaction.get("transactionAmount", {}).get("amount"),
                    "bankTransactionCode": transaction.get("bankTransactionCode"),
                    "bookingDate": transaction.get("bookingDate"),
                }
                for transaction in transactions
            ]

            return transactions_filtrees

    except requests.exceptions.HTTPError as err:
        print(f"Échec de la requête GET avec le code d'état {response.status_code} :")
        print(err)
        print(response.text)
        return None


