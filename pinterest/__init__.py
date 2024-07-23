#projeto flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# a url-for prega o nome da função (def) e nao o nome dentro do @app.route("") por exemplo

app = Flask(__name__) # isso é para iniciar a criação do site sempre colocar // criando o nome do app que deve ter  forma padrão
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "d5d69b18773d6420c91ab45ea5c8540a91836475" #CHAVE DE SEGURANÇA DO SITE PARA GARANTIR A SEGURANÇA DO SITE
app.config["UPLOAD_FOLDER"] = "static/fotos.posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app) #encriptador
login_manager = LoginManager(app) #login site
login_manager.login_view = "homepage" #view que gerencia a login

from pinterest import routes