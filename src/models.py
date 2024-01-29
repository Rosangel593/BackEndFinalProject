import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)
    password = Column(String(200), nullable=False)
    rut = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    
class Pets(Base):
    __tablename__ = 'pets'
    pet_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey=True("user.id"))
    image = Column(String(200))
    name = Column(String(250), nullable=False)
    species = Column(String(250), unique=False)
    date_of_birth = Column(String(200), nullable=False)
    age = Column(Integer)
    color = Column(String(50))
    sterilized = Column(bool)
    weigth = Column(float)
    height = Column(float)
    breed = Column(String(200))
    allergies = Column(String(200))
    aditional_info = Column(String(200))
    doctor_notes = Column(String(200))
    status = Column(bool)
    
class Veterinarians(Base):
    __tablename__ = 'veterinarians'
    vet_id = Column(Integer, Primary_key=True)
    user_id = Column(Integer, ForeignKey=True("user.id"))
    specialty = Column(Integer, nullable=False)
    position = Column(Integer, unique=False)
    
class Vaccines(Base):
    __tablename__ = 'vaccines'
    vac_id = Column(Integer, Primary_key=True)
    pet_id = Column(Integer, ForeignKey=True("pets.id"))
    vet_id = Column(Integer, ForeignKey=True("veterinarians.id"))
    user_id = Column(Integer, ForeignKey=True("user.id"))
    appointment_id = Column(Integer, ForeignKey=True("appointment.id"))
    dose = Column(Integer)
    type_of_vaccine = Column(String(200))
    lote = Column(String(200))
    
class Appointment(Base):
    __tablename__ = 'appointment'
    appointment_id = Column(Integer, primary_key=True)
    date = Column(String(200))
    time = Column(String(200))
    vet_id = Column(Integer, ForeignKey=True("veterinarians.id"))
    user_id = Column(Integer, ForeignKey=True("user.id"))
    pet_id = Column(Integer, ForeignKey=True("pets.id"))
    comments = Column(String(200))
    type_of_visit = Column(String(200))
    payment_status = Column(Integer, nullable=False)


class Prescriptions(Base):
    __tablename__ = 'prescriptions'
    prescription_id = Column(Integer, primary_key=True)
    appointment_id = Column(Integer, ForeignKey=True("appointment.id"))
    image = Column(String(200))
    content = Column(String(200))
    

def to_dict(self):
        return {}
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e