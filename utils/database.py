import sqlite3


class Database:
    def __init__(self, db_name='sqlite.db'):
        self.db_name = db_name 
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.__create_table()

    def __create_table(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY,
                service_name TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        '''
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert(self, service_name, username, password):
        insert_query = '''
            INSERT INTO services (service_name, username, password)
            VALUES (?, ?, ?)
        '''
        self.cursor.execute(insert_query, (service_name, username, password))
        self.connection.commit()

    def update(self, service_id, service_name, username, password):
        update_query = '''
            UPDATE services
            SET service_name = ?, username = ?, password = ?
            WHERE id = ?
        '''
        self.cursor.execute(update_query, (service_name, username, password, service_id))
        self.connection.commit()

    def delete(self, service_id):
        delete_query = '''
            DELETE FROM services
            WHERE id = ?
        '''
        self.cursor.execute(delete_query, (service_id,))
        self.connection.commit()

    def retrieve_all_services(self):
        select_query = '''
            SELECT id, service_name, username FROM services
        '''
        self.cursor.execute(select_query)
        return self.cursor.fetchall()

    def retrieve_by_service_name(self, service_name):
        select_query = '''
            SELECT id, service_name, username
            FROM services
            WHERE service_name = ?
        '''
        self.cursor.execute(select_query, (service_name,))
        return self.cursor.fetchall()
    
    def retrieve_service_by_id(self, service_id):
        select_query = '''
            SELECT service_name, username, password
            FROM services
            WHERE id = ?
        '''
        self.cursor.execute(select_query, (service_id,))
        return self.cursor.fetchone()

    def count(self, **kwargs):
        count_query = '''
            SELECT COUNT(*)
            FROM services
            WHERE %s
        '''

        counter = 0
        filter_query = ''
        for key in kwargs.keys():
            try:
                value = int(kwargs.get(key))
            except ValueError:
                value = f"'{kwargs.get(key)}'"
            
            filter_query += "%s = %s" % (key, value)
            counter += 1
            if counter < len(kwargs.keys()):
                filter_query += ' and '

        count_query = count_query % (filter_query, )
        self.cursor.execute(count_query)
        return self.cursor.fetchone()[0]

    def __del__(self):
        self.connection.close()
