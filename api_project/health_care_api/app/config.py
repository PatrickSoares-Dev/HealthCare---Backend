import os

class ProductionConfig:
    """Configurações para o ambiente de produção."""
    SECRET_KEY = os.environ.get('SECRET_KEY', '6TfqoMhcc1AZxqh')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///HealthPlanner.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False