from app.models.appointment_model import Appointment, db

def create_appointment(data):
    """Cria uma nova consulta."""
    new_appointment = Appointment(
        paciente_id=data['paciente_id'],
        medico_id=data['medico_id'],
        data_consulta=data['data_consulta'],
        status=data['status'],
        observacoes=data.get('observacoes')
    )
    db.session.add(new_appointment)
    db.session.commit()
    return new_appointment

def update_appointment(appointment_id, data):
    """Atualiza uma consulta."""
    appointment = Appointment.query.get(appointment_id)
    if appointment:
        appointment.data_consulta = data.get('data_consulta', appointment.data_consulta)
        appointment.status = data.get('status', appointment.status)
        appointment.observacoes = data.get('observacoes', appointment.observacoes)
        db.session.commit()
        return appointment
    return None

def delete_appointment(appointment_id):
    """Cancela uma consulta."""
    appointment = Appointment.query.get(appointment_id)
    if appointment:
        db.session.delete(appointment)
        db.session.commit()
        return True
    return False

def get_appointments():
    """Obtem todas as consultas."""
    return Appointment.query.all()