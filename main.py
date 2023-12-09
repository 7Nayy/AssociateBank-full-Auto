from config import SECRET_ID, SECRET_KEY, ACCOUNT_ID
from request import obtenir_token, actualiser_token, obtenir_informations_institutions, build_link, create_bridge, \
    acces_account

access_token, refresh_token = obtenir_token(SECRET_ID, SECRET_KEY)

if access_token and refresh_token:
    print(f"Access Token initial : {access_token}")

    # Simuler l'expiration du token (à remplacer par votre logique d'expiration)
    # En pratique, vous vérifieriez si le token est expiré avant chaque requête
    access_token = actualiser_token(refresh_token)

    if access_token:
        print(f"Nouveau Access Token : {access_token}")

        # Obtenir des informations sur les institutions avec le nouveau Access Token
        obtenir_informations_institutions(access_token)
else:
    print("Échec de l'obtention des tokens.")

response = build_link(access_token)
print(acces_account(access_token, ACCOUNT_ID))
#print(create_bridge(access_token, response))
