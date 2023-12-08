import requests

url = "https://bankaccountdata.gocardless.com/api/v2/token/new/"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

# Remplacez ces valeurs par vos vraies clés d'identification
data = {
    "secret_id": "fafac4c1-bdd7-4387-9204-99a444fd664f",
    "secret_key": "d608901a588c95512f1a00241b6a18d9ba7f40a485e14cc3837cafc1525d98b14bae8bdb4faeae271ba7d2836139131bf798881b42d0962ef02a97a44311da09",
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Requête réussie ! Voici la réponse JSON :")
    print(response.json())
else:
    print(f"Échec de la requête avec le code d'état {response.status_code} :")
    print(response.text)
