from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


class Manager:
    '''
        db_manager = Manager('user_details.db')
        db_manager.save_to_database(user_data, models.Students)
        result = db_manager.read_all_data_from_database(models.Students)

    '''
    def __init__(self, file_name):
        engine = create_engine(f'sqlite:///{file_name}', echo = False)
        self.database_connection = engine.connect()
        
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def save_to_database(self, data_to_insert, table_object):
        result = self.database_connection.execute(table_object.insert(), data_to_insert)
        return result

    def read_from_database_filter(self, filter_query, table_object):
        result = self.session.query(table_object).filter(filter_query).first()
        return result

    def read_from_database_two_filter(self, first_filter_query, second_filter_query, table_object):
        result = self.session.query(table_object).filter(first_filter_query).filter(second_filter_query)
        return result


    def read_all_data_from_database(self, table_object):
        result = self.session.query(table_object).all()
        return result

# result = read_all_data_from_database(Students)
# print(result)

# result = read_from_database_filter(Students.c.name == 'hasan', Students)
# print(result)


# my_info =  [{'name':'Lorenzo', 
#             'lastname': 'L',
#             'country': 'Italy',
#             'phone':'567890123'}]

# save_to_database(my_info, Students)