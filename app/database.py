from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = "mysql+pymysql://user:test@localhost:3306/a-db"
engine = create_engine(url, echo=False, pool_recycle=10)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()