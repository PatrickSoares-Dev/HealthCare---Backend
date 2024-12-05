from .user_routes import api as user_ns
from .patient_routes import api as patient_ns
from .doctor_routes import api as doctor_ns
from .appointment_routes import api as appointment_ns

__all__ = ['user_ns', 'patient_ns', 'doctor_ns', 'appointment_ns']