from flask import Blueprint, render_template, request
from database.models.client import Client

client_route = Blueprint("client", __name__)


@client_route.route("/")
def list_clients():
    """listar todos os clients"""
    clients = Client.select()
    return render_template("list_clients.html", clients=clients)


@client_route.route("/", methods=["POST"])
def insert_client():
    """inserir dados do client"""
    data = request.json

    new_user = Client.create(name=data["name"], email=data["email"])

    return render_template("client_item.html", client=new_user)


@client_route.route("/new")
def client_form():
    """formulario para cadastrar um client"""
    return render_template("client_form.html")


@client_route.route("/<int:client_id>")
def detail_client(client_id):

    client = Client.get_by_id(client_id)
    return render_template("detail_client.html", client=client)


@client_route.route("/<int:client_id>/edit")
def edit_client_form(client_id):

    client = Client.get_by_id(client_id)

    return render_template("client_form.html", client=client)


@client_route.route("/<int:client_id>/update", methods=["PUT"])
def update_client(client_id):
    """update client"""

    data = request.json

    updated_client = Client.get_by_id(client_id)

    updated_client.name = data["name"]
    updated_client.email = data["email"]
    updated_client.save()

    return render_template("client_item.html", client=updated_client)


@client_route.route("/<int:client_id>/delete", methods=["DELETE"])
def delete(client_id):
    """delete client"""
    client = Client.get_by_id(client_id)
    client.delete_instance()

    return {"deleted": "ok"}
