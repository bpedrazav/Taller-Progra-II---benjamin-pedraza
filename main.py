from cancelar import cancelar_reserva
from conexion import engine, Session
from consultar import consultar_salas, consultar_reservas
from modelos import Sala, Reserva, Base
from registrar import registrar_sala, registrar_reserva


def conexion():
    Base.metadata.create_all(engine)

def menuu():
    conexion()

    while True:
        print("1. registrar sala")
        print("2. consultar salas")
        print("3. registrar reserva")
        print("4. consultar reservas")
        print("5. cancelar reserva")
        print("0. salir")

        try:
            opcion = int(input("elige una opcion del menu: "))
        except ValueError:
            print("debes ingresar un numero para el menu")
            continue

        if opcion == 1:
            nombre = input("nombre de la sala: ")
            try:
                capacidad = int(input("capacidad: "))
            except ValueError:
                print("tienes que ingresar un numero")
                continue
            registrar_sala(nombre, capacidad)
        elif opcion == 2:
            consultar_salas()
        elif opcion == 3:
            estudiante = input("ingresa el nombre del estudiante;")
            try:
                sala_id = int(input("id de la sala: "))
            except ValueError:
                print("el id debe ser un numero")
                continue
            fecha = input("fecha: ")
            registrar_reserva(estudiante, sala_id, fecha)
        elif opcion == 4:
            consultar_reservas()
        elif opcion == 5:
            try:
                reserva_id = int(input("id de reserva: "))
            except ValueError:
                print("el id tiene que ser un numero")
                continue
            cancelar_reserva(reserva_id)
        elif opcion == 0:
            print("saliendo")
            break
        else:
            print("opcion incorrecta, pon una del menu porfa")


if __name__ == "__main__":
    menuu()

