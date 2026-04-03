import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "..", "db", "test_user.db"))

engine = create_engine(f"sqlite:///" + db_path)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
