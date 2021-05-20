import psycopg2

from logger import logger


class AddressBook:

    def __init__(self):
        # establishing the connection
        self.client = psycopg2.connect(
            database="address_book",
            user='postgres',
            password='robowars@1amit',
            host='127.0.0.1',
            port='5432'
        )
        self.client.autocommit = True
        # Creating a cursor object using the cursor() method
        self.mycursor = self.client.cursor()

    def create_table(self, table_name, field1, field2, field3):
        """

        :param table_name: table name to be created
        :param field1: 1st field name in table
        :param field2: 2nd field name
        :param field3: 3rd field name
        :return: true if table is created
        """
        try:
            table_list = []
            # Create table
            sql = "CREATE TABLE {}({} CHAR(60), {} CHAR(60), {} CHAR(60))".format(str(table_name), str(field1),
                                                                                  str(field2),
                                                                                  str(field3))
            self.mycursor.execute(sql)
            # Fetching table_schema
            self.mycursor.execute(
                "SELECT * FROM information_schema.tables WHERE table_type='BASE TABLE' AND table_schema='public'")
            schema_list = self.mycursor.fetchall()
            for values in schema_list:
                table_list.append(values[2])  # retrieving table names
            return table_name in table_list
        except Exception as e:
            logger.exception(e)

    def insert_table(self, table_name, field1, field2, field3, contact1, contact2, contact3):
        """

        :param contact1: data1 to be inserted
        :param contact2:data2 to be inserted
        :param contact3:data3 to be inserted
        :param table_name: name of the table
        :param field1: 1st field
        :param field2: 2nd field
        :param field3: 3rd field
        :return: number of rows affected
        """
        try:
            # insert data
            sql = "INSERT INTO {} ({}, {}, {}) VALUES {}, {}, {}" \
                .format(str(table_name), str(field1),
                        str(field2), str(field3), tuple(contact1),
                        tuple(contact2), tuple(contact3))
            self.mycursor.execute(sql)
            self.client.commit()
            return self.mycursor.rowcount # count rows inserted
        except Exception as e:
            logger.exception(e)
