from flask import request
from flask_restx import Namespace, Resource, fields
from app.controllers.user_controller import create_user, get_users, delete_user, authenticate_user

# Criação do namespace para usuários
api = Namespace('/Usuários', description='Operações de gerenciamento de usuários')

user_model = api.model('User', {
    'id': fields.Integer(readOnly=True, description='O identificador único do usuário'),
    'nome': fields.String(required=True, description='Nome do usuário'),
    'email': fields.String(required=True, description='Email do usuário'),
    'senha': fields.String(required=True, description='Senha do usuário', min_length=6)
})

login_model = api.model('UserLogin', {
    'email': fields.String(required=True, description='Email do usuário'),
    'senha': fields.String(required=True, description='Senha do usuário', min_length=6)
})

@api.route('/')
class UserList(Resource):
    @api.doc('listar_usuarios')
    @api.marshal_list_with(user_model)
    def get(self):
        """Lista todos os usuários"""
        users = get_users()
        return users, 200

    @api.doc('criar_usuario')
    @api.expect(user_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """Cria um novo usuário"""
        data = request.json
        user = create_user(data)
        return user, 201

@api.route('/<int:user_id>')
@api.response(404, 'Usuário não encontrado')
class User(Resource):
    @api.doc('deletar_usuario')
    def delete(self, user_id):
        """Remove um usuário"""
        if delete_user(user_id):
            return {'message': 'Usuário removido com sucesso'}, 200
        api.abort(404, 'Usuário não encontrado')

@api.route('/login')
class UserLogin(Resource):
    @api.doc('login_usuario')
    @api.expect(login_model)
    def post(self):
        """Autentica um usuário"""
        data = request.json
        user = authenticate_user(data['email'], data['senha'])
        if user:
            return {'message': 'Login realizado com sucesso'}, 200
        return {'error': 'Credenciais inválidas'}, 401