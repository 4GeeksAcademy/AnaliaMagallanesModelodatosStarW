from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    nombre: Mapped[str] = mapped_column(String(120), nullable=True)
    apellido: Mapped[str] = mapped_column(String(120), nullable=True)
    fecha_suscripcion: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    favoritos = relationship("Favorito", back_populates="usuario")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "fecha_suscripcion": self.fecha_suscripcion.isoformat()
        }


class Personaje(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    genero: Mapped[str] = mapped_column(String(50), nullable=True)
    especie: Mapped[str] = mapped_column(String(50), nullable=True)
    origen: Mapped[str] = mapped_column(String(120), nullable=True)

    favoritos = relationship("Favorito", back_populates="personaje")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "genero": self.genero,
            "especie": self.especie,
            "origen": self.origen
        }


class Planeta(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    clima: Mapped[str] = mapped_column(String(120), nullable=True)
    terreno: Mapped[str] = mapped_column(String(120), nullable=True)
    poblacion: Mapped[str] = mapped_column(String(120), nullable=True)

    favoritos = relationship("Favorito", back_populates="planeta")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.clima,
            "terreno": self.terreno,
            "poblacion": self.poblacion
        }


class Favorito(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    personaje_id: Mapped[int] = mapped_column(ForeignKey("personaje.id"), nullable=True)
    planeta_id: Mapped[int] = mapped_column(ForeignKey("planeta.id"), nullable=True)

    usuario = relationship("User", back_populates="favoritos")
    personaje = relationship("Personaje", back_populates="favoritos")
    planeta = relationship("Planeta", back_populates="favoritos")

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personaje_id": self.personaje_id,
            "planeta_id": self.planeta_id
        }
