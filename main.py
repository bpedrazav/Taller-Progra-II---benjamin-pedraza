from conexion import engine, Session
from consultar import listar_libros, consultar_libros_por_id, listar_usuarios
from modelos import Usuario, Libro, Prestamo, Base
from registrar import registrar_libro, registrar_usuario, registrar_prestamo
from eliminar import eliminar_libro

def conexion():
    Base.metadata.create_all(engine)

def menuu():
    conexion()

    while True:
        print("1. registrar libro")
        print("2. registrar usuario")
        print("3. registrar prestamo")
        print("4. consultar libros")
        print("5. consultar usuarios")
        print("6. consultar prestamos")
        print("7. eliminar libro")
        print("8. actualizar libro")
        print("9. salir")

        opcion = input("seleccione una opción: ")

        if opcion == "1":
            id = int(input("ingrese el id del libro: "))
            titulo = input("ingrese el titulo del libro: ")
            autor = input("ingrese el autor del libro: ")
            ejemplares_disponibles = int(input("ingrese la cantidad de ejemplares disponibles: "))
            if ejemplares_disponibles < 0:
                print("la cantidadd debe ser positiva")
            registrar_libro(id, titulo, autor, ejemplares_disponibles)
        
        elif opcion == "2":
            id = int(input("ingrese el id del usuario: "))
            nombre = input("ingrese el nombre del usuario: ")
            correo = input("ingrese el correo del usuario: ")
            registrar_usuario(id, nombre, correo)
        
        elif opcion == "3":
            usuario_id = int(input("ingrese el id del usuario: "))
            libro_id = int(input("ingrese el id del libro: "))
            fecha = input("ingrese la fecha del prestamo (YYYY-MM-DD): ")
            cantidad = int(input("Ingrese la cantidad de libros a prestar: "))
            registrar_prestamo(usuario_id, libro_id, fecha, cantidad)
        
        elif opcion == "4":
            listar_libros()
        
        elif opcion == "5":
            listar_usuarios()
        
        elif opcion == "6":
            consultar_libros_por_id()
            if not Libro:
                print("no existen libros con ese id")
                return
        
        elif opcion == "7":
            libro_id = int(input("Ingrese el id del libro a eliminar: "))
            eliminar_libro(libro_id)
        
        elif opcion == "8":
            libro_id = int(input("Ingrese el id del libro a actualizar: "))
            titulo = input("Ingrese el nuevo titulo del libro: ")
            autor = input("Ingrese el nuevo autor del libro: ")
            ejemplares_disponibles = int(input("Ingrese la nueva cantidad de ejemplares disponibles: "))
            if ejemplares_disponibles < 0:
                print("la cantidad debe ser positiva")
            actualizar_libro(libro_id, titulo, autor, ejemplares_disponibles)
        
        elif opcion == "9":
            break
        
        else:
            print("numero equivocado, ingreselo denuevo")


if __name__ == "__main__":
    menuu()
