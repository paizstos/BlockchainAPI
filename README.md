# BlockchainAPI

### Application de Gestion de Transactions
Cette application est composée d'un serveur API et d'un client qui permettent de gérer des transactions financières sous forme de blocs.

# Serveur API
Le serveur API est conçu pour stocker et gérer des transactions sous forme de blocs. Il utilise une clé d'authentification pour sécuriser l'accès aux opérations de création de blocs.

### Configuration du Serveur
Adresse du serveur : http://localhost:5000 (par défaut)
Clé API du serveur : votre_cle_api (modifiable dans le code du serveur)

### Opérations du Serveur
Ajouter un Bloc : Le serveur permet d'ajouter un nouveau bloc de transaction en utilisant une requête POST à l'URL /ajouter_bloc. Les clients doivent fournir la clé API du serveur dans l'en-tête X-API-Key pour authentifier la demande.

Récupérer un Bloc par son Numéro : Les clients peuvent récupérer un bloc spécifique en utilisant une requête GET à l'URL /bloc/<numéro>, où <numéro> est l'indice du bloc dans la liste.

Récupérer Tous les Blocs : Les clients peuvent récupérer la liste complète de tous les blocs en utilisant une requête GET à l'URL /tous_les_blocs.

# Client
Le client est une application en ligne de commande qui permet aux utilisateurs d'interagir avec le serveur API en ajoutant des transactions, en récupérant des blocs spécifiques ou en affichant la liste complète de tous les blocs.

### Opérations du Client
Ajouter une Transaction : Les utilisateurs peuvent ajouter une transaction en choisissant l'option "1" dans le menu. Ils doivent fournir les détails de la transaction, tels que l'opération, le montant, le compte et le commentaire.

Récupérer un Bloc par son Numéro : Les utilisateurs peuvent récupérer un bloc spécifique en choisissant l'option "2" dans le menu et en saisissant le numéro du bloc.

Récupérer Tous les Blocs : Les utilisateurs peuvent afficher la liste complète de tous les blocs en choisissant l'option "3" dans le menu.

Obtenir de l'Aide : Les utilisateurs peuvent obtenir de l'aide en choisissant l'option "H" dans le menu.

## Prérequis
* Python 3.x
* Bibliothèque requests pour le client (installez-la avec pip install requests)
* Bibliothèque flask (installez-la avec pip install flask)
``` 
$ pip install requests
$ pip install flask
```

## Comment Démarrer l'Application
Clonez ce dépôt sur votre machine locale.
```
$ git clone https://github.com/paizstos/BlockchainAPI.git 
```

Exécutez le serveur en exécutant le script serveur.py.
```
$ python3 serveur.py 
```

Exécutez le client en exécutant le script client.py.
```
$ python3 client.py 
```

Auteur :
 Christos DIONG AKETI PAIZANOS
 
Email : 
 paizstos11012001@gmail.com

Licence :
 Ce projet est sous licence [licence] - voir le fichier LICENSE.md pour plus de détails.


