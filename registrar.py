from modelos import Sala, Reserva
from conexion import Session

def registrar_sala(nombre, capacidad):
    with Session() as session:
        if not nombre.strip():
            print("el nombre de la sala no puede estar vacio")
            return
        if capacidad <= 0:
            print("la capacidad debe ser mayor a 0")
            return
        nueva_sala = Sala(nombre=nombre, capacidad=capacidad)
        session.add(nueva_sala)
        session.commit()
        print("sala registrada")


def registrar_reserva(estudiante, sala_id, fecha):
    with Session() as session:
        sala = session.get(Sala, sala_id)
        if not sala:
            print("la sala no existe")
            return
        if not sala.disponible:
            print("sala no disponible o ocupada")
            return
        nueva_reserva = Reserva(estudiante=estudiante, sala=sala, fecha=fecha)
        sala.disponible = False
        session.add(nueva_reserva)
        session.commit()
        print("reserva lista")
