from datetime import datetime

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from peryl_db.base import Base
from peryl_db.mixins import MetadataMixin

class Vehicle(Base):
    __tablename__ = "vehicles"
    __table_args__ = (UniqueConstraint("make",
                                       "model",
                                       "model_year_start",
                                       "model_year_end",
                                       "trim",
                                       name="uq_vehicle_identity"),
                      {"schema": "vehicle"})

    id: Mapped[int] = mapped_column(primary_key=True)

    make: Mapped[str]
    model: Mapped[str]
    model_year_start: Mapped[int]
    model_year_end: Mapped[int]
    trim: Mapped[str | None]
    research_status: Mapped[str] = mapped_column(default="missing")
    """
    research_status:
        missing: no specs
        incomplete: gaps in spec
        unreliable: populated with at least 1 low confidence values.
        complete: populated with high confidence values.
    """

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
    stock_tire_class: Mapped[int | None]

    vehicle: Mapped["Vehicle"] = relationship(back_populates="specs")

    metadata_entries: Mapped[list["VehicleSpecsMetadata"]] = relationship(back_populates="specs",
                                                                          cascade="all, delete-orphan")


class VehicleSpecsMetadata(MetadataMixin, Base):
    __tablename__ = "vehicle_specs_metadata"
    __table_args__ = {"schema": "vehicle"}

    specs_id: Mapped[int] = mapped_column(ForeignKey("vehicle.vehicle_spec.id"),
                                          nullable=False)

    specs: Mapped["VehicleSpecs"] = relationship(back_populates="metadata_entries")