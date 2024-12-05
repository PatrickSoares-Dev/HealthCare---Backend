# app/models/doctor_model.py

from app import db

class Doctor(db.Model):
    __tablename__ = 'medicos'
    
    id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    numero_licenca = db.Column(db.String(50), nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)
    numero_contato = db.Column(db.String(20))
    horario_atendimento = db.Column(db.String(100))
    
    def __repr__(self):
        return f"<Doctor {self.id} - {self.especialidade}>"