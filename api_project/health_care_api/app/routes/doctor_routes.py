from flask import request
from flask_restx import Namespace, Resource, fields
from app.controllers.doctor_controller import create_doctor, update_doctor, delete_doctor

api = Namespace('/Medicos', description='Operações de gerenciamento de médicos')

doctor_model = api.model('Doctor', {
    'nome': fields.String(required=True, description='Nome do médico'),
    'especialidade': fields.String(required=True, description='Especialidade do médico'),
    'email': fields.String(required=True, description='Email do médico'),
    'telefone': fields.String(required=True, description='Telefone do médico'),
})

@api.route('/')
class DoctorList(Resource):
    @api.doc('adicionar_medico')
    @api.expect(doctor_model)
    def post(self):
        """Adiciona um novo médico"""
        data = request.json
        doctor = create_doctor(data)
        return {'id': doctor.id, 'especialidade': doctor.especialidade}, 201

@api.route('/<int:doctor_id>')
class Doctor(Resource):
    @api.doc('editar_medico')
    @api.expect(doctor_model)
    def put(self, doctor_id):
        """Edita os dados de um médico"""
        data = request.json
        doctor = update_doctor(doctor_id, data)
        if doctor:
            return {'message': 'Dados do médico atualizados'}, 200
        return {'error': 'Médico não encontrado'}, 404

    @api.doc('remover_medico')
    @api.response(204, 'Médico removido')
    def delete(self, doctor_id):
        """Remove um médico"""
        if delete_doctor(doctor_id):
            return {'message': 'Médico removido'}, 200
        return {'error': 'Médico não encontrado'}, 404