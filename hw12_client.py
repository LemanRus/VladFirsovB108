import socket
import threading
import time
import json

shutdown = False
join = False


def receiving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))
                time.sleep(0.2)
        except:
            pass


def send_msg():
    global join, shutdown
    while not shutdown:
        if not join:
            json_message = json.dumps({
                "action": "join_chat",
                "time": time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()),
                "user": {
                    "name": name,
                    "status": "online"
                }
            }).encode("utf-8")
            s.sendto(json_message, server)
            join = True
        else:
            try:
                message_text = input("[YOU] :: ")
                if message_text != "":
                    json_message = json.dumps({
                        "action": "send_msg",
                        "time": time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()),
                        "message": message_text,
                        "user": {
                            "name": name,
                            "status": "online"
                        }
                    }).encode("utf-8")
                    s.sendto(json_message, server)
                time.sleep(0.2)
            except Exception as ex:
                print(ex)
                json_message = json.dumps({
                    "action": "leave_chat",
                    "time": time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()),
                    "user": {
                        "name": name,
                        "status": "offline"
                    }
                }).encode("utf-8")
                s.sendto(json_message, server)
                shutdown = True


server = ("localhost", 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("localhost", 0))

name = input("Name: ")

rT = threading.Thread(target=receiving, args=("RecvThread", s))
sT = threading.Thread(target=send_msg)
rT.start()
sT.start()

sT.join()
rT.join()
s.close()