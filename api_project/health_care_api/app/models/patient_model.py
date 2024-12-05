# app/models/patient_model.py

from app import db

class Patient(db.Model):
    __tablename__ = 'pacientes'
    
    id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    data_nascimento = db.Column(db.String(10))
    historico_medico = db.Column(db.Text)
    numero_contato = db.Column(db.String(20))
    
    def __repr__(self):
        return f"<Patient {self.id}>"