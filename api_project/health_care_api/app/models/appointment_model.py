# app/models/appointment_model.py

from app import db

class Appointment(db.Model):
    __tablename__ = 'consultas'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'), nullable=False)
    data_consulta = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    observacoes = db.Column(db.Text)
    
    def __repr__(self):
        return f"<Appointment {self.id} - {self.status}>"