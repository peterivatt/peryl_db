# Peryl DB

Peryl's SQLAlchemy models, PostgreSQL connection configuration, and Alembic
migrations. Requires Python 3.11 or newer.

## Local development

From this checkout, with uv installed:

```sh
uv sync --locked
```

Dependencies are declared in `pyproject.toml` and pinned in `uv.lock`.
`uv sync` creates `.venv` and installs the package in editable mode.

If `.env` does not already exist, copy `.env.example` to `.env` and set the
database credentials. Alembic loads `.env` from this repository; exported
`DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_NAME`, and `DB_PORT` values take
precedence. `DB_PORT` defaults to `5432`, and connections require SSL.

## Models

The Python package lives under `src/peryl_db/`. Other Peryl repositories can
install it with `uv add --editable ../peryl_db` and import models using:

```python
from peryl_db.base import Base
from peryl_db.models import Vehicle
```

`Vehicle` maps to `vehicle.vehicles`. The existing model fields and migration
revision history are preserved from `peryl_api`.

## Migrations

Run migrations from this checkout:

```sh
uv run --locked alembic heads
uv run --locked alembic upgrade head
```

To generate SQL for review without connecting to the database:

```sh
uv run --locked alembic upgrade head --sql
```

From another directory, pass the configuration path explicitly:

```sh
uv run --locked --project ../peryl_db alembic -c ../peryl_db/alembic.ini upgrade head
```

The Alembic configuration and migration files live in this repository alongside
the installable model package.
# peryl_db
