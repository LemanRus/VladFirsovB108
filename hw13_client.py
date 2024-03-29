import socket
import threading
import time
import json
import re
from hw13_logger import get_logger, log

logger = get_logger(__name__)

shutdown = False
join = False


@log(logger)
def receiving(name, sock):
    global shutdown
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)

                rec_msg = json.loads(data.decode("utf-8"))

                response = rec_msg.get("response")
                if response:
                    if response == 200:
                        print(rec_msg.get("message"))
                    if response == 201:
                        pass
                    elif response == 202:
                        pass
                    elif response == 404:
                        print("User", rec_msg.get("addresate"), "not found")
                    elif response == 503:
                        print("Server shutdown")
                        shutdown = True

                time.sleep(0.2)
        except:
            pass


@log(logger)
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
                    addresate = re.findall(r"^(\w+):", message_text)
                    msg_to_server = {
                        "action": "send_msg",
                        "time": time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()),
                        "message": message_text,
                        "user": {
                            "name": name,
                            "status": "online"}
                        }
                    if addresate:
                        msg_to_server["addresate"] = str(addresate[0])
                        msg_to_server["message"] = "From " + name + ": " + msg_to_server.get("message")
                    json_message = json.dumps(msg_to_server).encode("utf-8")
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