from app.models.patient_model import Patient, db

def create_patient(data):
    """Cria um novo paciente."""
    new_patient = Patient(
        id=data['id'],
        data_nascimento=data.get('data_nascimento'),
        historico_medico=data.get('historico_medico'),
        numero_contato=data.get('numero_contato')
    )
    db.session.add(new_patient)
    db.session.commit()
    return new_patient

def update_patient(patient_id, data):
    """Atualiza informações de um paciente."""
    patient = Patient.query.get(patient_id)
    if patient:
        patient.data_nascimento = data.get('data_nascimento', patient.data_nascimento)
        patient.historico_medico = data.get('historico_medico', patient.historico_medico)
        patient.numero_contato = data.get('numero_contato', patient.numero_contato)
        db.session.commit()
        return patient
    return None

def delete_patient(patient_id):
    """Remove um paciente."""
    patient = Patient.query.get(patient_id)
    if patient:
        db.session.delete(patient)
        db.session.commit()
        return True
    return False