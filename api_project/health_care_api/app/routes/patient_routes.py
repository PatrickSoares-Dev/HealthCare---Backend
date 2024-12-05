from flask import request
from flask_restx import Namespace, Resource, fields
from app.controllers.patient_controller import create_patient, update_patient, delete_patient

api = Namespace('/Pacientes', description='Operações de gerenciamento de pacientes')

patient_model = api.model('Patient', {
    'nome': fields.String(required=True, description='Nome do paciente'),
    'endereco': fields.String(required=True, description='Endereço do paciente'),
    'telefone': fields.String(required=True, description='Telefone do paciente'),
    'email': fields.String(required=True, description='Email do paciente')
})

@api.route('/')
class PatientList(Resource):
    @api.doc('adicionar_paciente')
    @api.expect(patient_model)
    def post(self):
        """Adiciona um novo paciente"""
        data = request.json
        patient = create_patient(data)
        return {'id': patient.id}, 201

@api.route('/<int:patient_id>')
class Patient(Resource):
    @api.doc('editar_paciente')
    @api.expect(patient_model)
    def put(self, patient_id):
        """Edita os dados de um paciente"""
        data = request.json
        patient = update_patient(patient_id, data)
        if patient:
            return {'message': 'Dados do paciente atualizados'}, 200
        return {'error': 'Paciente não encontrado'}, 404

    @api.doc('remover_paciente')
    @api.response(204, 'Paciente removido')
    def delete(self, patient_id):
        """Remove um paciente"""
        if delete_patient(patient_id):
            return {'message': 'Paciente removido'}, 200
        return {'error': 'Paciente não encontrado'}, 404