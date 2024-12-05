# app/models/user_model.py

from app import db

class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    senha = db.Column(db.String(120), nullable=False)
    tipo_usuario = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<User {self.nome} - {self.email}>"