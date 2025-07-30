from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pathlib import Path
import os # Still useful for base directory for the db file

# Define the path for your SQLite database file
# It will be created in the root of your project directory
BASE_DIR = Path(__file__).resolve().parent
DATABASE_FILE = BASE_DIR / "boneka.db" # Or any name you prefer, e.g., "mydatabase.db"

# SQLAlchemy database URL for SQLite
# The 'sqlite:///' prefix means it's a relative path to the database file.
# Using f"sqlite:///{DATABASE_FILE}" ensures it's an absolute path.
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

# For SQLite, connect_args are needed to allow multiple threads to access the same connection
# which is common in web applications like FastAPI.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True, # Keep echo=True for now to see SQL logs in console
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# You can optionally add a function to create tables if they don't exist
# This is usually done in main.py or a migration script, but can be here for simplicity
# if you're just starting out and want quick setup.
# from models import Base as ModelBase # Assuming your models' Base is imported here
# def create_db_tables():
#     ModelBase.metadata.create_all(bind=engine)

# Debug print to confirm DB file path
print(f"Using SQLite database at: {DATABASE_FILE}")