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
# Part : ServerAPI



# Print le logo

print("""

 =====================================================010=============================================
  ___    _      ____    ___     ___    ____   _____         _____    _____    ____   ____   ___     _                
 |   \  | |    |  __|  / __|   / __|  |  __| |  __ \       / ___ \  /  _  \  |  __| |  __| |   \   | |         
 | [] | | |    | |__  | <__   | <__   | |__  | |  \ \     | /   \_| | |_| |  | |__  | |__  | |\ \  | |       
 |   <  | |    |  __| \___ \  \___ \  |  __| | |   | |    | | |---  | >  <   |  __| |  __| | | \ \ | |              
 | [] | | |__  | |__   ___> |  ___> | | |__  | |__/ /     | \ __/ | | | \ \  | |__  | |__  | |  \ \| |          
 |____/ |____| |____| |____/  |____/  |____| |_____/       \_____/  |_|  \_\ |____| |____| |_|   \___|
 
 =====================================================010=============================================
 
 Part : ServerAPI
 Version: 1.0.0
 Author : Tcheetos
 GitHub : https://www.github.com/paizstos 
 
""")

from flask import Flask, request, jsonify
import datetime
from Block import Block


app = Flask(__name__)


# Clé API autorisée
API_KEY = "X"

# Middleware pour vérifier la clé API
def verify_api_key():
    api_key = request.headers.get('X-API-Key')
    if api_key != API_KEY:
        return jsonify({"error": "Clé API invalide"}), 401

# Appliquer la vérification de la clé API à toutes les routes
@app.before_request
def before_request():
    if request.endpoint != 'verify_api_key':
        verify_api_key()


# Liste pour stocker les blocs reçus
blocks = []

# Route pour recevoir un objet JSON représentant un bloc
@app.route('/ajouter_bloc', methods=['POST'])
def ajouter_bloc():
    try:
        data = request.json
        numero = blocks[-1].numero + 1
        previous_hash = blocks[-1].hashe
        operation = data['operation']
        amount = data['amount']
        account = data['account']
        comment = data['comment']
        

        # Créer un objet Block à partir des données JSON
        new_block = Block(numero, previous_hash, operation, amount, account, comment)
        blocks.append(new_block)

        return jsonify({"message": "Bloc ajouté avec succès"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route pour récupérer la liste de tous les blocs
@app.route('/tous_les_blocs', methods=['GET'])
def tous_les_blocs():
    blocs_json = []
    for block in blocks:
        blocs_json.append({
            'numero': block.numero,
            'previous_hash': block.previous_hash,
            'operation': block.operation,
            'amount': block.amount,
            'account': block.account,
            'date': block.date.strftime("%Y-%m-%d %H:%M:%S"),
            'comment': block.comment,
            'hashe': block.hashe
        })
    return jsonify(blocs_json), 200

# Route pour récupérer un bloc par son indice
@app.route('/bloc/<int:indice>', methods=['GET'])
def get_bloc_by_indice(indice):
    if indice >= 0 and indice < len(blocks):
        block = blocks[indice]
        bloc_json = {
            'numero': block.numero,
            'previous_hash': block.previous_hash,
            'operation': block.operation,
            'amount': block.amount,
            'account': block.account,
            'date': block.date.strftime("%Y-%m-%d %H:%M:%S"),
            'comment': block.comment,
            'hashe': block.hashe
        }
        return jsonify(bloc_json), 200
    else:
        return jsonify({"error": "Indice de bloc invalide"}), 404

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)



# Enregistrer un bloc en DB

# Encrypter la DB

# Décrypter la DB
