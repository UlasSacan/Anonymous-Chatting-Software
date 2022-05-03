from time import sleep

import requests
from requests import post
from os import system


class Login:

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.URL = "http://localhost"

    def dogrulama(self):
        try:
            self.req = post(self.URL, data=dict(username=self.user_name, password=self.password, message=None)).json()

            if self.req['status'][0]:
                print("[+] Login successful", self.user_name, "!")
                system('cls')
                return True
            else:
                print("[-] Wrong username or password")
                sleep(1)
                system('cls')
                return False
        except requests.exceptions.ConnectionError:
            print("err: Server is down")
            sleep(1)
            system('cls')
            return False

    def send_msg(self, msg: str) -> list:
        self.req = post(self.URL, data=dict(username=self.user_name, password=self.password,message=msg)).json()['msgs']
        return self.req


if __name__ == '__main__':
    while True:
        usr = input("Enter Your Username: ")
        usr_pass = input("Enter Your Password: ")
        bilgi = Login(usr, usr_pass)
        if bilgi.dogrulama():
            while True:
                msg = input("message: ")
                msgs = bilgi.send_msg(msg)
                system('cls')
                for i in msgs:
                    print(i)

        else:
            continue
