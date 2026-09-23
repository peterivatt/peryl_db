from datetime import datetime

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship


from peryl_db.base import Base


class Vehicle(Base):
    __tablename__ = "vehicles"
    __table_args__ = (UniqueConstraint("make",
                                       "model",
                                       "model_year",
                                       "trim",
                                       name="uq_vehicle_identity"),
                      {"schema": "vehicle"})

    id: Mapped[int] = mapped_column(primary_key=True)

    make: Mapped[str]
    model: Mapped[str]
    model_year: Mapped[int]
    trim: Mapped[str | None]

    specs: Mapped["VehicleSpecs | None"] = relationship(back_populates="vehicle",
                                                        cascade="all, delete-orphan",
                                                        uselist=False)

class VehicleSpecs(Base):
    __tablename__ = "vehicle_spec"
    __table_args__ = {"schema": "vehicle"}

    id: Mapped[int] = mapped_column(primary_key=True)

    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicle.vehicles.id"),
                                            unique=True,
                                            nullable=False)

    width_mm: Mapped[int | None]
    length_mm: Mapped[int | None]
    height_mm: Mapped[int | None]
    curb_weight_kg: Mapped[int | None]

    vehicle: Mapped["Vehicle"] = relationship(back_populates="specs")

    metadata_entries: Mapped[list["VehicleSpecsMetadata"]] = relationship(back_populates="specs",
                                                                          cascade="all, delete-orphan")


class VehicleSpecsMetadata(Base):
    __tablename__ = "vehicle_specs_metadata"
    __table_args__ = {"schema": "vehicle"}

    id: Mapped[int] = mapped_column(primary_key=True)

    specs_id: Mapped[int] = mapped_column(ForeignKey("vehicle.vehicle_spec.id"),
                                          nullable=False)

    variable: Mapped[str]
    date_set: Mapped[datetime]
    confidence: Mapped[float]
    source_url: Mapped[str]

    specs: Mapped["VehicleSpecs"] = relationship(back_populates="metadata_entries")