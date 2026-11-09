from sqlalchemy import select
from conexion import Session
from modelos import Sala, Reserva

def consultar_salas():
    with Session() as session:
        consulta = select(Sala)
        salas = session.scalars(consulta).all()

        print("Salas disponibles:")
        if not salas:
            print("No existen Salas registradas.")
            return
        for sala in salas:
            print("id_sala : ", sala.id)
            print("nombre_sala: ", sala.nombre)
            print("capacidad : ", sala.capacidad)
            print("disponible : ", sala.disponible)

def consultar_reservas():
    with Session() as session:
        consulta = select(Reserva)
        reservas = session.scalars(consulta).all()

        print("reservas actuales:")
        if not reservas:
            print("No existen reservas registradas.")
            return
        for reserva in reservas:
            print("id_reserva : ", reserva.id)
            print("estudiante : ", reserva.estudiante)
            print("sala : ", reserva.sala_id)
            print("fecha : ", reserva.fecha)
            print("sala:", reserva.sala.nombre)