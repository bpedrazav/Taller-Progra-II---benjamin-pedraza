# Sistema de reservas de salas de estudio

Proyecto correspondiente al **Taller Evaluado de Programación II (ICINF1109)**.
La aplicación permite administrar salas de estudio y sus reservas mediante un
menú por consola. La información se guarda de forma persistente en una base de
datos SQLite utilizando SQLAlchemy ORM.

## Tecnologías

- Python 3.10 o superior
- SQLAlchemy 2.x
- SQLite

## Funcionalidades

- Registrar salas indicando nombre y capacidad.
- Consultar todas las salas y su disponibilidad.
- Registrar una reserva para una sala disponible.
- Consultar las reservas registradas junto con la sala asociada.
- Cancelar una reserva y liberar nuevamente la sala.
- Validar nombres vacíos, capacidades inválidas, salas inexistentes y salas ya ocupadas.

## Estructura del proyecto

| Archivo | Descripción |
| --- | --- |
| `main.py` | Menú principal y flujo de la aplicación. |
| `modelos.py` | Modelos ORM `Sala` y `Reserva`, además de la relación 1:N. |
| `conexion.py` | Configuración del motor SQLite y las sesiones. |
| `crear_tablas.py` | Creación de las tablas de la base de datos. |
| `registrar.py` | Registro de salas y reservas. |
| `consultar.py` | Consulta de salas y reservas. |
| `cancelar.py` | Cancelación de reservas y liberación de salas. |
| `reservas.db` | Base de datos SQLite de demostración. |

## Instalación

Desde la carpeta del proyecto, crear opcionalmente un entorno virtual e
instalar la dependencia:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install "SQLAlchemy>=2.0,<3.0"
```

En Windows, la activación del entorno virtual se realiza con:

```powershell
.venv\Scripts\activate
```

## Ejecución

Ejecutar la aplicación con:

```bash
python3 main.py
```

Al iniciar, el programa crea las tablas automáticamente si todavía no existen.
También es posible crearlas directamente con:

```bash
python3 crear_tablas.py
```

La base de datos se genera o utiliza como `reservas.db` dentro de esta misma
carpeta.

## Menú de opciones

```text
1. Registrar sala
2. Consultar salas
3. Registrar reserva
4. Consultar reservas
5. Cancelar reserva
0. Salir
```

## Modelo de datos

### Sala

- `id`: clave primaria entera.
- `nombre`: nombre obligatorio, de hasta 100 caracteres.
- `capacidad`: cantidad de cupos, debe ser mayor que cero.
- `disponible`: indica si la sala puede recibir una nueva reserva; comienza en `True`.

### Reserva

- `id`: clave primaria entera.
- `estudiante`: nombre obligatorio, de hasta 100 caracteres.
- `sala_id`: clave foránea hacia `Sala`.
- `fecha`: fecha de la reserva.

Una sala puede tener varias reservas a lo largo del tiempo, pero solo una
reserva activa simultáneamente. Al reservar, `disponible` cambia a `False`; al
cancelar, vuelve a `True`.

## Casos de prueba de la pauta

1. Registrar `Sala A` con capacidad `6` y `Sala B` con capacidad `4`.
2. Reservar `Sala A` para `Ana`; la reserva debe registrarse y la sala quedar ocupada.
3. Intentar reservar nuevamente `Sala A` para `Pedro`; la operación debe rechazarse.
4. Consultar reservas y comprobar que aparece la reserva de Ana.
5. Cancelar la reserva de Ana; `Sala A` debe volver a estar disponible.
6. Reservar nuevamente `Sala A` para `Pedro`; la operación debe aceptarse.

## Autor

**Benjamín Pedraza**

Taller Evaluado — Programación II
