from sqlalchemy import select
from conexion import Session
from modelos import Libro, Usuario, Prestamo

def devolucion_libro(id_prestamo):
    with Session() as session:
        prestamo = session.get(Prestamo, id_prestamo)
        if prestamo:
            prestamo.estado = False
            prestamo.libro.ejemplares_disponibles += prestamo.cantidad
            session.commit()
            print("la devolucion se completo")
            print("ahora el libro puede ser prestado denuevo")