import psycopg2
from pprint import pprint

def create_bd(cur):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients(
        id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        lastname VARCHAR(30),
        email VARCHAR(254)
        );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonenumbers(
        id_number SERIAL PRIMARY KEY,
        number VARCHAR(11) unique,
        client_id INTEGER REFERENCES clients(id)
        );
    """)

def add_phone(cur, client_id, phone):
    cur.execute("""
    INSERT INTO phonenumbers(number, client_id)
        VALUES (%s, %s);
    """, (phone, client_id))

def add_new_client(cur, name, lastname, email):
    cur.execute("""
    INSERT INTO clients(name, lastname, email) 
        VALUES(%s, %s, %s);
    """, (name, lastname, email,))

def change_client_data():
    print("Для изменения информации о клиенте, введите нужную Вам команду.\n "
        "1 - изменить имя; 2 - изменить фамилию; 3 - изменить e-mail; 4 - изменить номер телефона")

    while True:
        command_symbol = int(input())
        if command_symbol == 1:
            name1 = input("Введите id клиента имя которого хотите изменить: ")
            name2 = input("Введите имя для изменения: ")
            cur.execute("""
            UPDATE clients SET name=%s WHERE id=%s;
            """, (name2, name1))
            break
        elif command_symbol == 2:
            lastname1 = input("Введите id клиента фамилию которого хотите изменить: ")
            lastname2 = input("Введите фамилию для изменения: ")
            cur.execute("""
            UPDATE clients SET lastname=%s WHERE id=%s;
            """, (lastname2, lastname1))
            break
        elif command_symbol == 3:
            email1 = input("Введите id клиента e-mail которого хотите изменить: ")
            email2 = input("Введите e-mail для изменения: ")
            cur.execute("""
            UPDATE clients SET email=%s WHERE id=%s;
            """, (email2, email1))
            break
        elif command_symbol == 4:
            number1 = input("Введите номер телефона который Вы хотите изменить: ")
            number2 = input("Введите новый номер телефона, который заменит собой старый: ")
            cur.execute("""
            UPDATE phonenumbers SET number=%s WHERE number=%s;
            """, (number2, number1))
            break
        else:
            print("Команда нераспознана, повторите ввод")

def delete_phone():
    del_number1 = input("Введите id клиента номер телефона которого хотите удалить: ")
    del_number2 = input("Введите номер телефона который хотите удалить: ")
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM phonenumbers WHERE client_id=%s AND number=%s
        """, (del_number1, del_number2))

def delete_client():
    del_client1 = input("Введите id клиента которого хотите удалить: ")
    del_client2 = input("Введите фамилию клиента которого хотите удалить: ")
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM phonenumbers WHERE client_id=%s
        """, (del_client1,))
        cur.execute("""
        DELETE FROM clients WHERE id=%s AND lastname=%s
        """, (del_client1, del_client2))

def find_client():
    print("Для поиска информации о клиенте, пожалуйста, введите команду, где:\n "
          "1 - найти по имени; 2 - найти по фамилии; 3 - найти по e-mail; 4 - найти по номеру телефона")
    while True:
        command_finding = int(input("Введите команду для поиска информации о клиенте: "))
        if command_finding == 1:
            name_finding = input("Введите имя для поиска информации о клиенте: ")
            cur.execute("""
            SELECT id, name, lastname, email, number
            FROM clients AS c
            LEFT JOIN phonenumbers AS p ON p.id_number = c.id
            WHERE name=%s
            """, (name_finding,))
            print(cur.fetchall())
        elif command_finding == 2:
            lastname_finding = input("Введите фамилию для поиска информации о клиенте: ")
            cur.execute("""
            SELECT id, name, lastname, email, number
            FROM clients AS c
            LEFT JOIN phonenumbers AS p ON p.id_number = c.id
            WHERE lastname=%s
            """, (lastname_finding,))
            print(cur.fetchall())
        elif command_finding == 3:
            email_finding = input("Введите email для поиска информации о клиенте: ")
            cur.execute("""
            SELECT id, name, lastname, email, number
            FROM clients AS c
            LEFT JOIN phonenumbers AS p ON p.id_number = c.id
            WHERE email=%s
            """, (email_finding,))
            print(cur.fetchall())
        elif command_finding == 4:
            phonenumber_finding = input("Введите номер телефона для поиска информации о клиенте: ")
            cur.execute("""
            SELECT id, name, lastname, email, number
            FROM clients AS c
            LEFT JOIN phonenumbers AS p ON p.id_number = c.id
            WHERE number=%s
            """, (phonenumber_finding,))
            #return cur.fetchone()[0]
            print(cur.fetchall())
        else:
            print("К сожалению, Вы ввели неправильную команду, пожалуйста, повторите ввод")

with psycopg2.connect(database="HomeWork5", user='postgres', password='postgres') as conn:
    with conn.cursor() as cur:
        create_bds(cur)
        add_new_client(cur, "Black", "Whites", "1@g.com")
        add_new_client(cur, "Red", "Blues", "2@g.com")
        add_new_client(cur, "Green", "Yellows", "3@g.com")
        add_new_client(cur, "Pink", "Browns", "4@g.com")
        add_new_client(cur, "Grey", "Limes", "5@g.com")
        add_phone(cur, 1, "79999999991")
        add_phone(cur, 2, "79999999992")
        add_phone(cur, 3, "79999999993")
        add_phone(cur, 4, "79999999994")
        add_phone(cur, 5, "79999999995")
        change_client_data()
        delete_phone()
        delete_client()
        find_client()

conn.close()