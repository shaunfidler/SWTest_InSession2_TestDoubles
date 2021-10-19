from accounting import accounting
from unittest.mock import call, patch, MagicMock
import unittest

class AccountingTest(unittest.TestCase):
    #mock
    @patch("accounting.accounting.connect_to_db")
    def test_setup_database(self, connect_to_db):
        db_connection = MagicMock()
        connect_to_db.return_value = db_connection

        mock_cursor = MagicMock()
        db_connection.cursor.return_value = mock_cursor

        accounting.create_db_and_tables()
        mock_cursor.execute.assert_has_calls(
            [
            call('CREATE DATABASE accounting'), 
            call('USE accounting'), 
            call('CREATE TABLE customers (customer_id INT, name VARCHAR(255), total_goods INT)'), 
            call('CREATE TABLE orders (customer_id INT, total_goods INT)')
            ]
        )

    #mock
    @patch("accounting.accounting.connect_to_db")
    def test_destroy_database(self, connect_to_db):
        db_connection = MagicMock()
        connect_to_db.return_value = db_connection

        mock_cursor = MagicMock()
        db_connection.cursor.return_value = mock_cursor

        accounting.delete_db_and_tables()
        mock_cursor.execute.assert_called_with('DROP DATABASE accounting')

    #mock
    @patch("accounting.accounting.connect_to_db")
    def test_create_customer_happy_path(self, connect_to_db):
        db_connection = MagicMock()
        connect_to_db.return_value = db_connection

        mock_cursor = MagicMock()
        db_connection.cursor.return_value = mock_cursor

        id = 10
        name = "Name"
        total_goods = 25

        accounting.create_customer(id, name, total_goods)
        mock_cursor.execute.assert_called_with('INSERT INTO customers VALUES({},"{}",{})'.format(id, name, total_goods))
    
    #mock
    @patch("accounting.accounting.connect_to_db")
    def test_create_order_happy_path(self, connect_to_db):
        db_connection = MagicMock()
        connect_to_db.return_value = db_connection

        mock_cursor = MagicMock()
        db_connection.cursor.return_value = mock_cursor

        id = 10
        total_goods = 25

        accounting.create_order(id, total_goods)
        mock_cursor.execute.assert_called_with('INSERT INTO orders VALUES({},{})'.format(id, total_goods))

    #mock
    @patch("accounting.accounting.connect_to_db")
    def test_get_customers(self, connect_to_db):
        db_connection = MagicMock()
        connect_to_db.return_value = db_connection

        mock_cursor = MagicMock()
        db_connection.cursor.return_value = mock_cursor

        mock_cursor.fetchall.return_value = [(10, 'Name', 25)]
        self.assertEqual(accounting.get_all_customers(), [(10, 'Name', 25)])
        mock_cursor.execute.assert_called_with('SELECT * from customers')

    #none
    def test_create_customer_invalid_type_name(self):
        id = 10
        name = 10
        total_goods = 25

        self.assertRaises(TypeError, accounting.create_customer, id, name, total_goods)

    #none
    def test_create_customer_space_in_name(self):
        id = 10
        name = "Name Space"
        total_goods = 25

        self.assertRaises(ValueError, accounting.create_customer, id, name, total_goods)
    
    #none
    def test_create_customer_invalid_type_id(self):
        id = "10"
        name = "Name"
        total_goods = 25

        self.assertRaises(TypeError, accounting.create_customer, id, name, total_goods)
    
    #none
    def test_create_customer_invalid_type_total_goods(self):
        id = 10
        name = "Name"
        total_goods = "25"

        self.assertRaises(TypeError, accounting.create_customer, id, name, total_goods)
    
    #none
    def test_create_order_invalid_type_id(self):
        id = "10"
        total_goods = 25

        self.assertRaises(TypeError, accounting.create_order, id, total_goods)
    
    #none
    def test_create_order_invalid_type_total_goods(self):
        id = 10
        total_goods = "25"

        self.assertRaises(TypeError, accounting.create_order, id, total_goods)

if __name__ == '__main__':
    unittest.main()