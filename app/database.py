from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = "mysql+pymysql://user:p%40ssw0rd@localhost:3306/a-db"
engine = create_engine(url, echo=False, pool_recycle=10)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
