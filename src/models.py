import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)
    password = Column(String(200), nullable=False)
    rut = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)

    def serialize_1(self):
        return {
        'user_id': self.user_id,
        'name': self.name,
        'email': self.email,
        'rut': self.rut,
        'address': self.address
        }

    
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

    def serialize_2(self):
        return {
        'pet_id':self.pet_id,
        'user_id':self.user_id,
        'image':self.image,
        'name':self.name,
        'species':self.species,
        'date_of_birth' : self.date_of_birth,
        'age':self.age,
        'color':self.color,
        'sterilized':self.sterilized,
        'weigth':self.weigth,
        'height':self.height,
        'breed':self.breed,
        'allergies':self.allergies,
        'aditional_info':self.aditional_info,
        'doctor_notes':self.doctor_notes,
        'status':self.status
        }
    
class Veterinarians(Base):
    __tablename__ = 'veterinarians'
    vet_id = Column(Integer, Primary_key=True)
    user_id = Column(Integer, ForeignKey=True("user.id"))
    specialty = Column(Integer, nullable=False)
    position = Column(Integer, unique=False)

    def serialize_3(self):
        return {
        'vet_id':self.vet_id,
        'user_id':self.user_id,
        'specialty':self.specialty,
        'position':self.position
        }
    
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

    def serialize_4(self):
        return {
        'vac_id':self.vac_id,
        'pet_id':self.pet_id,
        'vet_id':self.vet_id,
        'user_id':self.user_id,
        'appointment':self.appointment,
        'dose' : self.dose,
        'type_of_vaccine':self.type_of_vaccine,
        'lote':self.lote
        }
    
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


    def serialize_5(self):
        return {
        'appointment_id':self.appointment_id,
        'date':self.date,
        'time':self.time,
        'vet_id':self.vet_id,
        'user_id':self.user_id,
        'pet_id' : self.pet_id,
        'comments':self.comments,
        'type_of_visit':self.type_of_visit,
        'payments_status':self.payments_status
        }

class Prescriptions(Base):
    __tablename__ = 'prescriptions'
    prescription_id = Column(Integer, primary_key=True)
    appointment_id = Column(Integer, ForeignKey=True("appointment.id"))
    image = Column(String(200))
    content = Column(String(200))

    def serialize_6(self):
        return {
        'prescription_id':self.prescription_id,
        'appointment_id':self.appointment_id,
        'image':self.image,
        'content':self.content
        }
