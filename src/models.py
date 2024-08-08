import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String,Enum, Float 
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


class GenderEnum(enum.Enum):
    masculino = 'Masculino'
    femenino  = 'Femenino'


class Usuario(Base):
    __tablename__= "usuario"
    id = Column(Integer, primary_key = True)
    nombre_de_usuario = Column(String(15),nullable = False , unique = True)
    correo = Column(String(250),nullable = False , unique = True)
    contrasenia = Column(String(250), nullable = False)
    
    # RELACIONES PARA LOS ENDPOINTS
    Personaje = relationship('Usuario_Personaje')
    Planeta = relationship('Usuario_Planeta')


class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key = True)
    nombre_planeta = Column(String(250), nullable = False)
    clima = Column(String(20), nullable = True) # investigar cuantos tipos de climas hay en el universo star wars
    creacion_planeta = Column(String(50),nullable = True)
    poblacion  = Column(Integer, nullable = True)
    
class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key = True)
    nombre_personaje = Column(String(250), nullable = False)
    anio_nacimiento = Column(Integer, nullable = True)
    gender = Enum(GenderEnum)  
    estatura = Column (Float, nullable = True)
    color_piel = Column(String(250), nullable = True)
    color_cabello = Column(String(250), nullable = True)

class Usuario_Planeta(Base):
    __tablename__ = 'usuarios_planeta'
    id = Column(Integer, primary_key = True)
    usuario_id = Column(Integer,ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'))

    # RELACIONES PARA LOS ENDPOINTS 
    usuario = relationship('Usuario')
    planeta = relationship('Planeta')
    
class Usuario_Personaje(Base):
    __tablename__ = 'usuario_personaje'
    id = Column(Integer, primary_key = True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    personaje_id = Column(Integer, ForeignKey('personaje.id'))

    # RELACIONES PARA LOS ENDPOINTS   
    usuario = relationship('Usuario')
    personaje = relationship('Personaje')


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
