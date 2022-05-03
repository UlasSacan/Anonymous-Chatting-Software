import sqlite3
from random import randint
DATA_BASE = "data_base/user_.db"


def register(username: str, password: str) -> bool:
    data_base = sqlite3.connect(DATA_BASE)
    cr = data_base.cursor()

    def id_generator():
        while True:
            id = randint(1, 1000)
            cr.execute("SELECT * FROM user_info WHERE id == '{}'".format(id))
            data = cr.fetchall()
            if len(data) == 0:
                break
        return id

    def check_username(username: str) -> bool:
        cr.execute(f"SELECT * FROM user_info WHERE username == '{username}'")
        data = cr.fetchall()
        if len(data) == 0:
            return True
        else:
            return False

    if check_username(username):
        cr.execute(f"INSERT INTO user_info VALUES ('{id_generator()}','{username}', '{password}')")
        data_base.commit()
        data_base.close()
        return True
    else:
        return False  # same username is not valid to register


def main():
    usename = input("enter a username: ")
    password = input("Enter a password: ")
    while True:
        if register(usename, password):
            print("registration complete")
            choise = input("Do you want continue (y/n): ")
            if choise.lower() == "y":
                continue
            else:
                break
        else:
            print("registration failed")
            choise = input("Do you want continue (y/n): ")
            if choise.lower() == "y":
                continue
            else:
                break

if __name__ == '__main__':
    main()
