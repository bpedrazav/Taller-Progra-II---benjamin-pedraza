from sqlalchemy import select
from conexion import Session
from modelos import Sala, Reserva

def cancelar_reserva(reserva_id):
    with Session() as session:
        reserva = session.get(Reserva, reserva_id)
        if not reserva:
            print("la reserva no se puede cancelar porque no existe wuadaudj")
            return
        session.delete(reserva)
        reserva.sala.disponible = True
        session.add(reserva.sala)
        session.commit()
        print("la reserva ya se cancelo") #hola