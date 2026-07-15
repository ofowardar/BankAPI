from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base


#Database URL {postgresql://username:passwod@adres:port/database}
DATABASE_URL = "postgresql://bankuser:bankpassword@localhost:5432/bankdb"


#Create a engine for postgsql
engine = create_engine(
    DATABASE_URL
)


#Create a session
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind=engine
)

#Create a Base
Base = declarative_base()
