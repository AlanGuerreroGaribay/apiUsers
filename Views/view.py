from flask import Blueprint, request
from Models.user import User
from Models.dbConnect import db

bp = Blueprint('bp', __name__)

@bp.route('/users')
def users():
    return {
        "RESPUESTA": "respuesta huevos"
    }

@bp.route("/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
        )
        db.session.add(user)
        db.session.commit()
        return {"hecho"}

    return { "respuesta": "verificar la creacion en la tabla" }