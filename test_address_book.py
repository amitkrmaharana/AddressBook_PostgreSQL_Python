from Addressbook import AddressBook


class TestAddressBook:
    address_book = AddressBook()

    def test_create_table(self):
        """

        :return:
        """
        table_name = "students"
        field1 = "name"
        field2 = "city"
        field3 = "state"
        result = self.address_book.create_table(table_name, field1, field2, field3)
        assert result == True, "Table not created"
