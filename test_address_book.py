from Addressbook import AddressBook


class TestAddressBook:
    address_book = AddressBook()

    def test_create_database(self):
        """

        :return: to check if database is created or not
        """
        db_name = "trydb3"
        result = self.address_book.create_database(db_name)
        assert result == True, "Database not created"
