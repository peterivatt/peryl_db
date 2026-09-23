from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

class MetadataMixin:
    id: Mapped[int] = mapped_column(primary_key=True)
    variable: Mapped[str]
    source_url: Mapped[str | None]
    confidence: Mapped[int | None]
    date_set: Mapped[datetime | None]