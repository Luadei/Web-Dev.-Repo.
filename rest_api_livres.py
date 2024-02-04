from flask import Flask, request, jsonify
from flask_cors import CORS

#Initialiser l'application
app = Flask(__name__)

#Definir une liste de livre
liste_livres = [
    {'id': 1,'title': 'titre 01',},
    {'id': 2,'title': 'titre 02',},
    {'id': 3,'title': 'titre 02',}
]

#Definir une route qui retourne la liste de livre
@app.route('/api/livres', methods=["GET", "POST"])  #Méthodes GET et POST utilisées plus tard pour lire la liste de livre ou écrire dedans
def livres():
  if request.method == "GET":
    return jsonify(liste_livres)  #Retourne la liste de livre en cas de commande GET
  else:  #Comme methods n'a que GET et POST ici, "else" = POST
    nbr_livres = len(liste_livres)  #Stock le nombres de livre dans la liste
    post_id = nbr_livres + 1  #Donne au livre posté un nouvel id

    #Indéxation du nouveau livre
    nv_livre = {'title': request.json['title'], 'id': post_id}

    #Ajouter le nouveau livre à la liste
    liste_livres.append(nv_livre)

    #Retourne la nouvelle liste de livres
    return jsonify(liste_livres), 201


#Definir la route qui retourne uniquement un livre par son id
@app.route('/api/livres/<int:id>', methods=["GET", "DELETE", "PUT"]) #Méthodes GET, DELETE et PUT utilisées plus tard pour afficher un livre correspondant à l'id ou supprimer le livre ou de mettre à jour le titre d'un livre
def livre_id(id):
  
  index = id - 1  #Car le livre avec l'id 1 est en fait en position 0 dans la liste

  if request.method == "GET":
    return jsonify(liste_livres[index])

  elif request.method == "DELETE":
    liste_livres.pop(index)  #Fonction .pop supprime le livre dans la liste
    return jsonify({"msg": "book deleted"})

  elif request.method == "PUT":
    liste_livres[index]['title'] = request.json['title']
    return jsonify({"msg": "book updated"})


app.debug = True
app.run(host='0.0.0.0', port=8080)
