from flask import Blueprint, render_template, request
from database.client import CLIENTS

client_route = Blueprint("client", __name__)


@client_route.route("/")
def list_clients():
    """listar todos os clients"""
    return render_template("list_clients.html", clients=CLIENTS)


@client_route.route("/", methods=["POST"])
def insert_client():
    """inserir dados do client"""
    data = request.json

    new_user = {"id": len(CLIENTS) + 1, "name": data["name"], "email": data["email"]}

    CLIENTS.append(new_user)

    return render_template("client_item.html", client=new_user)


@client_route.route("/new")
def client_form():
    """formulario para cadastrar um client"""
    return render_template("client_form.html")


@client_route.route("/<int:client_id>")
def detail_client(client_id):

    client = list(filter(lambda c: c['id'] == client_id, CLIENTS))[0]
    return render_template("detail_client.html", client=client)


@client_route.route("/<int:client_id>/edit")
def edit_client_form(client_id):

    client = None
    for c in CLIENTS:
        if c["id"] == client_id:
            client = c

    return render_template("client_form.html", client=client)


@client_route.route("/<int:client_id>/update", methods=["PUT"])
def update_client(client_id):
    """update client"""

    client = None
    data = request.json

    for c in CLIENTS:
        if c["id"] == client_id:
            c["name"] = data['name']
            c["email"] = data['email']

            updated_client = c

    return render_template('client_item.html', client=updated_client)


@client_route.route("/<int:client_id>/delete", methods=["DELETE"])
def delete(client_id):
    """delete client"""
    global CLIENTS
    CLIENTS = [c for c in CLIENTS if c["id"] != client_id]

    return {"deleted": "ok"}
