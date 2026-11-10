from sqlalchemy import select
from conexion import Session
from modelos import Libro, Usuario, Prestamo
from registrar import registrar_prestamo

def eliminar_libro(libro_id):
    with Session() as session:
        libro = session.get(Libro, libro_id)
        if not libro:
            print("el libro no se puede eliminar porque no existe")
            return
        elif libro.ejemplares_disponibles < libro.prestamos.count():
            print("no se puede eliminar porque esta prestado")
            return
        session.delete(libro)
        libro.prestamo.estado = False
        session.commit()
        print("el libro se elimino correctamente")
