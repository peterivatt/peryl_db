import os

from sqlalchemy import URL, create_engine
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parents[3] / ".env"
load_dotenv(env_path)

database_url = URL.create(drivername="postgresql+psycopg",
                          username=os.environ["DB_USER"],
                          password=os.environ["DB_PASSWORD"],
                          host=os.environ["DB_HOST"],
                          port=int(os.getenv("DB_PORT", "5432")),
                          database=os.environ["DB_NAME"],
                          query={"sslmode": "require"})

engine = create_engine(database_url)