#criar a estrutura do banco de dados
from pinterest import database, login_manager
from datetime import datetime #api python para pegar a data e horario atual
from flask_login import UserMixin # diz a classe que vai gerenciar a classe de login

@login_manager.user_loader # função que carrega o usuario desse metodo
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario)) #obrigatorio do login_manager para pegar a id do usuario e retorna o id do usuario do banco de dados

class Usuario(database.Model, UserMixin): # o database.Model permite criar o formato que o banco de dados entende
    id = database.Column (database.Integer, primary_key = True)
    nomeusuario = database.Column(database.String, nullable = False, unique = True)
    email = database.Column(database.String, nullable = False, unique = True)
    senha = database.Column(database.String, nullable = False)
    fotos = database.relationship("Foto", backref = "usuario", lazy = True) #nao é uma coluna que cria no banco de dados ele cria tipo uma seta para localizar a imagem pelo nome de usuario

class Foto(database.Model):
    id = database.Column (database.Integer, primary_key = True)
    imagemfoto = database.Column(database.String, nullable = False, default = "default.png") #nome da imagem que fica armazenado no banco de dados porem a imagem vai ficar armazenado na pasta static no projeto para nao carregar demais o banco
    data_criacao = database.Column(database.DateTime, nullable = False, default = datetime.utcnow()) # ele é uma api do python que ele pega a data de criação da pessoa pelo site
    id_usuario = database.Column(database.Integer,database.ForeignKey('usuario.id'),  nullable = False) # a ForeignKey key tem que vim antes do argumento de nome tipo nullable
