from sqlalchemy.orm import Mapped, mapped_column

from peryl_db.base import Base

class Vehicle(Base):
    __tablename__ = "vehicles"
    __table_args__ = {"schema": "vehicle"}

    id: Mapped[int] = mapped_column(primary_key=True)
    make: Mapped[str]
    model: Mapped[str]
    width_mm: Mapped[int | None]
    length_mm: Mapped[int | None]
    height_mm: Mapped[int | None]
    curb_weight_kg: Mapped[int | None]