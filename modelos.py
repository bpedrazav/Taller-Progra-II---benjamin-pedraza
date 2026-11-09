from decimal import Decimal
from sqlalchemy import String, Numeric, Integer, CheckConstraint, Column, ForeignKey, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Sala(Base):
    __tablename__ = "sala"
    __table_args__ = (
        CheckConstraint("capacidad > 0", name="check_capacidad_positive"),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    capacidad: Mapped[int] = mapped_column(Integer)
    disponible: Mapped[bool] = mapped_column(Boolean, default=True)
    reservas: Mapped[list["Reserva"]] = relationship(back_populates="sala")


class Reserva(Base):
    __tablename__ = "reserva"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    estudiante: Mapped[str] = mapped_column(String(100), nullable=False)
    sala_id: Mapped[int] = mapped_column(ForeignKey("sala.id"))
    fecha: Mapped[str] = mapped_column(String(10), nullable=False)
    sala: Mapped["Sala"] = relationship(back_populates="reservas")
