from flask import Flask
from Models.dbConnect import db
from Views.view import bp

#1- instanciar flask (crear app)
app = Flask(__name__)
#se registran blueprints de Views
app.register_blueprint(bp)

#2- cadena de conexion con la base de datos
#configura la db con sqlite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

#3- instancia de sqlalchemy
db.init_app(app)

#4- hace la migraciones a la base de datos en automatico
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug = True)