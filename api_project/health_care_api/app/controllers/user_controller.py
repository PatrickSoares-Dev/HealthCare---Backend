from app.models.user_model import User, db
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(data):
    """Cria um novo usuário."""
    hashed_password = generate_password_hash(data['senha'], method='sha256')
    new_user = User(
        nome=data['nome'],
        email=data['email'],
        senha=hashed_password,
        tipo_usuario=data['tipo_usuario']
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_users():
    """Obtem todos os usuários."""
    return User.query.all()

def delete_user(user_id):
    """Deleta um usuário."""
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False

def authenticate_user(email, password):
    """Autentica um usuário com base no email e senha."""
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.senha, password):
        return user
    return None