import psycopg2

from logger import logger


class AddressBook:

    def __init__(self):
        # establishing the connection
        self.client = psycopg2.connect(
            database="postgres",
            user='postgres',
            password='robowars@1amit',
            host='127.0.0.1',
            port='5432'
        )
        self.client.autocommit = True
        # Creating a cursor object using the cursor() method
        self.mycursor = self.client.cursor()

    def create_database(self, db_name):
        """

        :param db_name: name of the database to be created
        :return: return True if database is created
        """
        try:
            database_list = []
            sql = "CREATE DATABASE {}".format(str(db_name))
            self.mycursor.execute(sql)
            self.mycursor.execute("SELECT datname FROM pg_database")
            database_tuple = self.mycursor.fetchall()
            for values in database_tuple:
                database_list.append(values[0])
            return db_name in database_list
        except Exception as e:
            logger.exception(e)
