from modelos import Libro, Usuario, Prestamo
from conexion import Session 

def registrar_libro(titulo, autor, ejemplares_disponibles):
    session = Session()
    libro = Libro(titulo=titulo, autor=autor, ejemplares_disponibles=ejemplares_disponibles)
    session.add(libro)
    session.commit()
    print("libro registrado correctamente")


def registrar_usuario(nombre, correo):
    session = Session()
    usuario = Usuario(nombre=nombre, correo=correo)
    session.add(usuario)
    session.commit()
    print("usuario registrado correctamente")

def registrar_prestamo(usuario_id, libro_id, fecha, cantidad):
    session = Session()
    usuario = session.get(Usuario, usuario_id)
    libro = session.get(Libro, libro_id)
    fecha = session.get(Prestamo, fecha)
    cantidad = session.get(Prestamo, cantidad)

    if not usuario:
        print("el usuario no existe")
        return
    if not libro:
        print("el libro no existe")
        return
    if libro.ejemplares_disponibles <= 0:
        print("no hay stock en este libro")
        return
    
    prestamo = Prestamo(usuario=usuario, libro=libro)
    libro.ejemplares_disponibles -= 1
    session.add(prestamo)
    session.commit()
    print("prestamo realizado")
