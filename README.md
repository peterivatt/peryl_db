# Peryl DB

Peryl's SQLAlchemy models, PostgreSQL connection configuration, and Alembic
migrations. Requires Python 3.11 or newer.

## Local development

From this checkout, with your Python environment activated:

```sh
python -m pip install -e .
```

If `.env` does not already exist, copy `.env.example` to `.env` and set the
database credentials. Alembic loads `.env` from this repository; exported
`DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_NAME`, and `DB_PORT` values take
precedence. `DB_PORT` defaults to `5432`, and connections require SSL.

## Models

The Python package lives under `src/peryl_db/`. Other Peryl repositories can
install it with `python -m pip install -e ../peryl_db` and import models using:

```python
from peryl_db.base import Base
from peryl_db.models import Vehicle
```

`Vehicle` maps to `vehicle.vehicles`. The existing model fields and migration
revision history are preserved from `peryl_api`.

## Migrations

Run migrations from this checkout:

```sh
python -m alembic heads
python -m alembic upgrade head
```

To generate SQL for review without connecting to the database:

```sh
python -m alembic upgrade head --sql
```

From another directory, pass the configuration path explicitly:

```sh
python -m alembic -c ../peryl_db/alembic.ini upgrade head
```

The Alembic configuration and migration files live in this repository alongside
the installable model package.
# peryl_db
