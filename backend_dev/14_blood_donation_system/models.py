from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

meta = MetaData()

# SQL Database Schema
Donors = Table(
   'Donors', meta, 
   Column('id', Integer, primary_key = True),
   Column('name', String), 
   Column('age', Integer), 
   Column('blood_group', String),
   Column('city', String),
   Column('phone_no', String),
   Column('donation_count', String),
   Column('latest_donation', String),
)

if __name__ == "__main__":
    engine = create_engine('sqlite:///blood_bank.db', echo = True)
    meta.create_all(engine)

    # insert_query = Students.insert().values(name = 'Vikas', lastname = 'S')
    # database_connection = engine.connect()
    # result = database_connection.execute(insert_query)
