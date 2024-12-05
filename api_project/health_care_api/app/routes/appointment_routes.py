from flask import request
from flask_restx import Namespace, Resource, fields
from app.controllers.appointment_controller import create_appointment, update_appointment, delete_appointment, get_appointments

api = Namespace('/Consultas', description='Operações de gerenciamento de consultas')

# Modelo de agendamento para documentação Swagger
appointment_model = api.model('Appointment', {
    'paciente_id': fields.Integer(required=True, description='ID do paciente'),
    'medico_id': fields.Integer(required=True, description='ID do médico'),
    'data_consulta': fields.String(required=True, description='Data e hora da consulta no formato ISO 8601'),
    'status': fields.String(required=False, description='Status da consulta', default='pendente')
})

@api.route('/')
class AppointmentList(Resource):
    @api.doc('listar_consultas')
    def get(self):
        """Lista todas as consultas"""
        appointments = get_appointments()
        return [{'id': appointment.id, 'status': appointment.status, 'data_consulta': appointment.data_consulta} for appointment in appointments], 200

    @api.doc('adicionar_consulta')
    @api.expect(appointment_model)
    def post(self):
        """Adiciona uma nova consulta"""
        data = request.json
        appointment = create_appointment(data)
        return {'id': appointment.id, 'status': appointment.status}, 201

@api.route('/<int:appointment_id>')
class Appointment(Resource):
    @api.doc('editar_consulta')
    @api.expect(appointment_model)
    def put(self, appointment_id):
        """Edita os dados de uma consulta"""
        data = request.json
        appointment = update_appointment(appointment_id, data)
        if appointment:
            return {'message': 'Consulta atualizada'}, 200
        return {'error': 'Consulta não encontrada'}, 404

    @api.doc('cancelar_consulta')
    @api.response(204, 'Consulta cancelada')
    def delete(self, appointment_id):
        """Cancela uma consulta"""
        if delete_appointment(appointment_id):
            return {'message': 'Consulta cancelada'}, 200
        return {'error': 'Consulta não encontrada'}, 404