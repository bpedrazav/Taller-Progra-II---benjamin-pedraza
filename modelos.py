from decimal import Decimal
from email.policy import default
from sqlalchemy import String, Numeric, Integer, CheckConstraint, Column, ForeignKey, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Libro(Base):
    __tablename__ = "libro"
    __table_args__ = (
        CheckConstraint("ejemplares_disponibles >= 0", name="check_ejemplares_disponibles_non_negative"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String, nullable=False)
    autor: Mapped[str] = mapped_column(String, nullable=False)
    ejemplares_disponibles: Mapped[int] = mapped_column(Integer, nullable=False)


class Usuario(Base):
    __tablename__ = "usuario"
    __table_args__ = (
        CheckConstraint("correo != correo", name="check_correo_not_duplicate"),)

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    correo: Mapped[str] = mapped_column(String, nullable=False)

class Prestamo(Base):
    __tablename__ = "prestamo"
    __table_args__ = (
        CheckConstraint("cantidad > 0", name="check_cantidad_positive"),)

    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    libro_id: Mapped["Libro"] = relationship("Libro", backref="prestamos")
    usuario_id: Mapped["Usuario"] = relationship("Usuario", backref="prestamos")
    fecha: Mapped[str] = mapped_column(String, nullable=False)
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    estado: Mapped[bool] = mapped_column(Boolean, default=True)
