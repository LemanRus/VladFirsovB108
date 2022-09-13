import socket
import threading
import time
import json
import re


class MyClient:
    def __init__(self):
        self.shutdown = False
        self.join = False
        self.server_ok = False

        self.server = ("localhost", 9090)

        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.connect(("localhost", 0))

        self.name = input("Name: ")

    def receiving(self, name, sock):
        while not self.shutdown:
            try:
                while True:
                    data, addr = sock.recvfrom(1024)

                    rec_msg = json.loads(data.decode("utf-8"))

                    response = rec_msg.get("response")
                    if response:
                        if response == 200:
                            print(rec_msg.get("message"))
                            self.server_ok = True
                            return rec_msg.get("message")
                        elif response == 404:
                            print("User", rec_msg.get("addresate"), "not found")
                            self.server_ok = True
                            return "not found"
                        elif response == 503:
                            print("Server shutdown")
                            self.server_ok = False
                            self.shutdown = True
                            return "Server shutdown"
                        time.sleep(0.2)

            except Exception as ex:
                print(ex)
                return ex

    def send_msg(self):
        while not self.shutdown:
            if not self.join:
                self.join_chat()
            else:
                try:
                    message_text = input("[YOU] :: ")
                    if message_text:
                        addresate = re.findall(r"^(\w+):", message_text)
                        msg_to_server = {
                            "action": "send_msg",
                            "time": time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()),
                            "message": message_text,
                            "user": {
                                "name": self.name,
                                "status": "online"}
                            }
                        if addresate:
                            msg_to_server["addresate"] = str(addresate[0])
                            msg_to_server["message"] = "From " + self.name + ": " + msg_to_server.get("message")
                        json_message = json.dumps(msg_to_server).encode("utf-8")
                        sent = self.s.sendto(json_message, self.server)
                        print(sent)
                        if sent != 0:
                            self.server_ok = True
                        return json_message
                    time.sleep(0.2)
                except Exception as ex:
                    print("HERESY!")
                    print(ex)
                    if self.server_ok:
                        json_message = json.dumps({
                            "action": "leave_chat",
                            "time": time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()),
                            "user": {
                                "name": self.name,
                                "status": "offline"
                            }
                        }).encode("utf-8")
                        self.s.sendto(json_message, self.server)
                    self.shutdown = True

    def join_chat(self):
        json_message = json.dumps({
            "action": "join_chat",
            "time": time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()),
            "user": {
                "name": self.name,
                "status": "online"
            }
        }).encode("utf-8")
        sent = self.s.sendto(json_message, self.server)
        if sent != 0:
            self.server_ok = True
        self.join = True
        return json_message


if __name__ == "__main__":
    my_client = MyClient()

    rT = threading.Thread(target=my_client.receiving, args=("RecvThread", my_client.s))
    sT = threading.Thread(target=my_client.send_msg)
    rT.start()
    sT.start()

    sT.join()
    rT.join()

    my_client.s.close()
