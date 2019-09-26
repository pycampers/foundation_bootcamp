from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
meta = MetaData()

# SQL Database Schema
Students = Table(
   'Students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String),
   Column('country', String),
   Column('phone', String), 
)


if __name__ == '__main__':
      engine = create_engine('sqlite:///user_details.db', echo = True)
      meta.create_all(engine)