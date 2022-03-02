from confi import DATABASE_URI

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = create_engine(DATABASE_URI)


Session = sessionmaker(db)

session = Session()