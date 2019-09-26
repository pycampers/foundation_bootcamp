from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
meta = MetaData()

# SQL Database Schema
Students = Table(
   'Students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

# meta.create_all(engine)

if __name__ == '__main__':
    engine = create_engine('sqlite:///college.db', echo = True)
    insert_query = Students.insert().values(name = 'Vikas', lastname = 'S')
    database_connection = engine.connect()
    result = database_connection.execute(insert_query)