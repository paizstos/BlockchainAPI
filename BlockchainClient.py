#!/usr/env/bin python
#
# Author : Christos DIONG AKETI PAIZANOS
# GitHub : https://www.github.com/paizstos
#
#
#  ___    _      ____    ___     ___    ____   _____         _____    _____    ____   ____   ___     _                
# |   \  | |    |  __|  / __|   / __|  |  __| |  __ \       / ___ \  /  _  \  |  __| |  __| |   \   | |         
# | [] | | |    | |__  | <__   | <__   | |__  | |  \ \     | /   \_| | |_| |  | |__  | |__  | |\ \  | |       
# |   <  | |    |  __| \___ \  \___ \  |  __| | |   | |    | | |---  | >  <   |  __| |  __| | | \ \ | |              
# | [] | | |__  | |__   ___> |  ___> | | |__  | |__/ /     | \ __/ | | | \ \  | |__  | |__  | |  \ \| |          
# |____/ |____| |____| |____/  |____/  |____| |_____/       \_____/  |_|  \_\ |____| |____| |_|   \___|                       
#
# Part : Client



# Print le logo
import requests
import json
from Block import Block


print("""

 =====================================================010=============================================
  ___    _      ____    ___     ___    ____   _____         _____    _____    ____   ____   ___     _                
 |   \  | |    |  __|  / __|   / __|  |  __| |  __ \       / ___ \  /  _  \  |  __| |  __| |   \   | |         
 | [] | | |    | |__  | <__   | <__   | |__  | |  \ \     | /   \_| | |_| |  | |__  | |__  | |\ \  | |       
 |   <  | |    |  __| \___ \  \___ \  |  __| | |   | |    | | |---  | >  <   |  __| |  __| | | \ \ | |              
 | [] | | |__  | |__   ___> |  ___> | | |__  | |__/ /     | \ __/ | | | \ \  | |__  | |__  | |  \ \| |          
 |____/ |____| |____| |____/  |____/  |____| |_____/       \_____/  |_|  \_\ |____| |____| |_|   \___|
 
 =====================================================010=============================================
 
 Part : Client
 Version: 1.0.0
 Author : Tcheetos
 GitHub : https://www.github.com/paizstos
 
""")

# URL du serveur
server_url = "http://localhost:5000"

api_key_client ="X"

# Exemple de bloc à envoyer au serveur
nouveau_bloc = {
    "operation": "debit",
    "amount": 100,
    "account": "compte1",
    "comment": "Transaction 1"
}

# Envoyer un nouveau bloc au serveur en utilisant une requête POST
def envoyer_bloc(nouveau_bloc):
    try:
        url = f"{server_url}/ajouter_bloc"
        headers = {
            'Content-Type': 'application/json',
            'X-API-Key': api_key_client  # Ajouter la clé API dans l'en-tête
        }
        response = requests.post(url, data=json.dumps(nouveau_bloc), headers=headers)

        if response.status_code == 201:
            print("Bloc ajouté avec succès.")
        else:
            print(f"Échec de l'ajout du bloc. Code de statut : {response.status_code}")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

# Récupérer tous les blocs du serveur en utilisant une requête GET
def recuperer_tous_les_blocs():
    try:
        url = f"{server_url}/tous_les_blocs"
        headers = {'X-API-Key': api_key_client}  # Ajouter la clé API dans l'en-tête
        
        response = requests.get(url)

        if response.status_code == 200:
            blocs = response.json()
            print("Liste de tous les blocs:")
            for bloc in blocs:
                print(bloc)
        else:
            print(f"Échec de la récupération des blocs. Code de statut : {response.status_code}")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

# Récupérer un bloc spécifique par son indice en utilisant une requête GET
def recuperer_bloc_par_indice(indice):
    try:
        url = f"{server_url}/bloc/{indice}"
        headers = {'X-API-Key': api_key_client}  # Ajouter la clé API dans l'en-tête
        
        response = requests.get(url)

        if response.status_code == 200:
            bloc = response.json()
            print(f"Bloc à l'indice {indice}:")
            print(bloc)
        elif response.status_code == 404:
            print("Bloc introuvable. Indice invalide.")
        else:
            print(f"Échec de la récupération du bloc. Code de statut : {response.status_code}")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")
        
def menu():
    
    print("Ajouter une transaction, tape 1")
    print("Récupérer un bloc par son numero, tape 2")
    print("Récupérer tous les blocs, tape 3")
    print("Besoin d'aide ? Tape H \n")
    reponse = int(input("Answer :  "))
    
    if reponse == 1 :
        print("\n\n\n Rajoutez des détails \n\n")
        ope = str(input("Opération (Achat - Vente - Location - Débit - Crédit) :  "))
        mont = int(input("\n Montant (eur) :   "))
        acc = int(input("\n Compte :  #"))
        com = int(input("\n Commentaire / Explication:   "))
        envoyer_bloc(Block(1, 0, ope, mont, acc, com))
        
    elif reponse == 2 :
        print("\n\n\n Rajoutez des détails \n\n")
        index = int(input(" Entrez le numero du bloc (qui commence par 0) : "))
        
    elif reponse == 3 :
        recuperer_tous_les_blocs()
        
    elif reponse == 'H' :
        print("\n\n\n Besoin d'aide ? \n\n")
        print("Tapez '1' pour ajouter une transaction.")
        print("Tapez '2' pour récupérer un bloc par son numéro.")
        print("Tapez '3' pour récupérer tous les blocs.")
        print("Tapez 'H' pour afficher l'aide.")
        
    else:
        print("Réponse invalide. Veuillez saisir '1', '2', '3' ou 'H'.")
        


# Exemple d'utilisation des fonctions

while True :
    menu()
