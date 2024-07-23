#criar formularios do site

from flask_wtf import FlaskForm # estrutura da classe do formulario
from wtforms import StringField, PasswordField, SubmitField #campos de texto, senha e botao para login
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError #validadores de campos o DatRequered ele tem o campo obrigatorio, o Equal to é para verificar se o campo tem a mesma senha exemplo
from pinterest.models import Usuario

class Formulariologin(FlaskForm):
    email = StringField("E-mail", validators= [DataRequired(), Email() ])
    senha = PasswordField("Senha", validators= [DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")

class FormularioCriarConta(FlaskForm):
    email =  StringField("E-mail", validators= [DataRequired(), Email() ])
    nomeusuario =  StringField("Nome de Usuário", validators= [DataRequired()])
    senha = PasswordField("Senha", validators= [DataRequired(), Length(6,20)])
    confirmacaosenha = PasswordField("Confirmar Senha", validators= [DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):  #precisa do validade_nome do campo para validaçao
        usuario = Usuario.query.filter_by(email = email.data).first()
        if usuario:
            return ValidationError("Email já cadastrado, faça login para continuar")

