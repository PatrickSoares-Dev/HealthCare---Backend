# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from .config import ProductionConfig

# Inicialização global de extensões
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)

    # Inicialização das extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Importação dos modelos após a inicialização do banco de dados
    with app.app_context():
        from app.models import User, Doctor, Patient, Appointment
    
    api = Api(
        app,
        version='1.0',
        title='Health Care API',
        description='Uma API simples para gerenciamento de consultas médicas.',
        doc='/docs'
    )

    # Importa e registra os namespaces
    from app.routes import user_ns, patient_ns, doctor_ns, appointment_ns
    api.add_namespace(user_ns, path='/usuarios')
    api.add_namespace(patient_ns, path='/pacientes')
    api.add_namespace(doctor_ns, path='/medicos')
    api.add_namespace(appointment_ns, path='/consultas')

    return app