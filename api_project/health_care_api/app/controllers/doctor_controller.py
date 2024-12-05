from app.models.doctor_model import Doctor, db

def create_doctor(data):
    """Cria um novo médico."""
    new_doctor = Doctor(
        id=data['id'],
        numero_licenca=data['numero_licenca'],
        especialidade=data['especialidade'],
        numero_contato=data.get('numero_contato'),
        horario_atendimento=data.get('horario_atendimento')
    )
    db.session.add(new_doctor)
    db.session.commit()
    return new_doctor

def update_doctor(doctor_id, data):
    """Atualiza informações de um médico."""
    doctor = Doctor.query.get(doctor_id)
    if doctor:
        doctor.numero_licenca = data.get('numero_licenca', doctor.numero_licenca)
        doctor.especialidade = data.get('especialidade', doctor.especialidade)
        doctor.numero_contato = data.get('numero_contato', doctor.numero_contato)
        doctor.horario_atendimento = data.get('horario_atendimento', doctor.horario_atendimento)
        db.session.commit()
        return doctor
    return None

def delete_doctor(doctor_id):
    """Remove um médico."""
    doctor = Doctor.query.get(doctor_id)
    if doctor:
        db.session.delete(doctor)
        db.session.commit()
        return True
    return False