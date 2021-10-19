"""
Database: MySQL
Port: 3306
Version: 8.0.26.0
Download: https://dev.mysql.com/
"""

from typing import Type
import mysql.connector

class accounting:
    @staticmethod
    def connect_to_db():
        db = mysql.connector.connect(
            host = "localhost",
            username = "root",
            password = "admin"
        )
        return db

    @staticmethod
    def create_db_and_tables():
        db = accounting.connect_to_db()
        cur = db.cursor()
        cur.execute('CREATE DATABASE accounting')
        cur.execute('USE accounting')
        cur.execute('CREATE TABLE customers (customer_id INT, name VARCHAR(255), total_goods INT)')
        cur.execute('CREATE TABLE orders (customer_id INT, total_goods INT)')

    @staticmethod
    def delete_db_and_tables():
        db = accounting.connect_to_db()
        cur = db.cursor()
        cur.execute('USE accounting')
        cur.execute('DROP DATABASE accounting')
        
    @staticmethod
    def create_customer(customer_id, name, total_goods):
        if(type(customer_id) != int):
            raise TypeError
        if(type(name) != str):
            raise TypeError
        if(type(total_goods) != int):
            raise TypeError

        if(' ' in name):
            raise ValueError("space in name")

        db = accounting.connect_to_db()
        cur = db.cursor()
        cur.execute('USE accounting')
        cur.execute('INSERT INTO customers VALUES({},"{}",{})'.format(customer_id, name, total_goods))
        db.commit()

    @staticmethod
    def create_order(customer_id, total_goods):
        if(type(customer_id) != int):
            raise TypeError
        if(type(total_goods) != int):
            raise TypeError

        db = accounting.connect_to_db()
        cur = db.cursor()
        cur.execute('USE accounting')
        cur.execute('INSERT INTO orders VALUES({},{})'.format(customer_id, total_goods))
        db.commit()

    @staticmethod
    def get_all_customers():
        db = accounting.connect_to_db()
        cur = db.cursor()
        cur.execute('USE accounting')
        cur.execute('SELECT * from customers')
        customers = cur.fetchall()
        return list(customers)

