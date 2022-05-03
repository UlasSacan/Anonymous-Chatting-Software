from flask import Flask, request
import sqlite3
import datetime

app = Flask(__name__)
DATA_BASE = "data_base/user_.db"


def add_msg(user: str, msg: str, type="append"):
    an = datetime.datetime.now()
    zaman = datetime.datetime.ctime(an)
    if type == "append":
        with open("data_base/messages.txt", "a+") as filObj:
            filObj.write(zaman + " " + "|" + " " + user + " " + ":" + " " + msg + "\n")
    elif type == "read":
        with open("data_base/messages.txt", "r+") as filObj:
            return filObj.readlines()
    else:
        raise "type must be (append or read)"


def login_server(username: str, password: str) -> bool:
    data_base = sqlite3.connect(DATA_BASE)
    cr = data_base.cursor()
    usr = cr.execute(f"SELECT * FROM user_info WHERE username == '{username}'")
    dUsr = usr.fetchall()  # [(id, username, password)]
    if len(dUsr) != 0 and (username == dUsr[0][1]) and (password == dUsr[0][2]):
        return True
    else:
        return False


@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        msg = request.form.get('message', None)
        is_succes = login_server(str(username), str(password))
        if is_succes:
            if msg != None:
                add_msg(username, msg)
                return dict(msgs=add_msg(username, msg, "read"))
            else:
                return dict(status=(True, "Login succesful"))
        else:
            return dict(status=(False, "Wrong username or password"))


if __name__ == '__main__':
    app.run(port=80, debug=True)
