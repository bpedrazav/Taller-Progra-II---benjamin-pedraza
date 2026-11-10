from sqlalchemy import select
from conexion import Session
from modelos import Libro, Usuario, Prestamo

def listar_libros():
    with Session() as session:
        consulta = select(Libro)
        libros = session.scalars(consulta).all()

        print("Libros disponibles:")
        if not libros:
            print("no existen libros registrados")
            return
        for libro in libros:
            print("id_libro : ", libro.id)
            print("titulo: ", libro.titulo)
            print("autor : ", libro.autor)
            print("disponible : ", libro.disponible)

def consultar_libros_por_id(id_libro):
    with Session() as session:
        consultar = select(Libro).where(Libro.id == id_libro)
        libro = session.scalars(consultar).first()
        print("libro encontrado:", libro.titulo)
        print("autor:", libro.autor)

def listar_usuarios():
    with Session() as session:
        consulta = select(Usuario)
        usuarios = session.scalars(consulta).all()

        print("total usuarios registrados:")
        if not usuarios:
            print("no hay usuarios registrados aun")
            return
        for usuario in usuarios:
            print("id_usuario : ", usuario.id)
            print("nombre: ", usuario.nombre)
            print("correo : ", usuario.correo)
