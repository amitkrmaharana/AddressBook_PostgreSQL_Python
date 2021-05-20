from Addressbook import AddressBook


class TestAddressBook:
    address_book = AddressBook()
    table_name = "contacts"
    field1 = "name"
    field2 = "city"
    field3 = "state"

    def test_create_table(self):
        """

        :return: true if table is created
        """
        result = self.address_book.create_table(self.table_name, self.field1, self.field2, self.field3)
        assert result == True, "Table not created"

    def test_insert_data(self):
        """

        :return: true if row is inserted
        """
        contact1 = ("Amit", "Jamshedpur", "Jharkhand")
        contact2 = ("Manish", "Bangalore", "Karnataka")
        contact3 = ("Peter", "Lakewood", "California")

        result = self.address_book.insert_table(self.table_name, self.field1, self.field2, self.field3, contact1, contact2, contact3)
        assert result == 3, "Data not inserted"
