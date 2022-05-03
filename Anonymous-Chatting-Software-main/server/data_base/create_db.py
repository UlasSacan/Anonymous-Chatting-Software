from os import listdir, remove
import sqlite3

DB = "user_.db"


def create_db():
    db = open(DB, "w")
    db.close()
    data_base = sqlite3.connect(DB)
    cr = data_base.cursor()
    cr.execute("CREATE TABLE user_info (id,username, password)")
    cr.close()


if __name__ == '__main__':
    while True:
        if DB not in listdir():
            create_db()
            print("DB created!")
        else:
            chosie = input(DB + " is already exists do you want delete and create after (y/n): ")
            if chosie.lower() == "y":
                remove(DB)
                create_db()
                print("DB created!")
                input("\n prees Enter to exit")
                break
            else:
                break
