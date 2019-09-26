from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_test import Students
 
engine = create_engine('sqlite:///college.db', echo = False)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()

result = session.query(Students).filter(Students.c.id == 1).first()
# result = session.query(Students).all()
print(result)
