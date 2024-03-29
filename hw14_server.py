import json
import socket
import time


class MyServer:
    def __init__(self):
        self.host = "localhost"
        self.port = 9090

        self.clients = []
        self.client_names = {}

        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((self.host, self.port))
        self.quit = False

        print("[SERVER STARTED]")

    def server_works(self):
        while not self.quit:
            try:
                rec_data, addr = self.s.recvfrom(1024)
                if addr not in self.clients:
                    self.clients.append(addr)

                itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

                print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + itsatime + "] / ", end="")

                action, addresate, user_name, message, send_data = self.disassemble_msg(rec_data)
                self.send_answer(action, addresate, user_name, message, send_data, addr)

            except Exception as ex:
                try:
                    for client in self.clients:
                        self.s.sendto(json.dumps({
                            "response": 503,
                            "time": time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
                        }).encode("utf-8"), client)
                except Exception as int_ex:
                    print(int_ex)
                print(ex)
                print("\n[SERVER STOPPED]")
                self.quit = True

    def disassemble_msg(self, rec_data):
        try:
            client_msg = json.loads(rec_data.decode("utf-8"))
            send_data = {k: v for k, v in client_msg.items() if k != "action"}
        except Exception as ex:
            print(ex)
            print(rec_data.decode("utf-8"))
            client_msg = {}
            send_data = {"response": 503}
            self.quit = True

        action = client_msg.get("action")
        addresate = client_msg.get("addresate")
        user_name = client_msg.get("user").get("name")
        message = client_msg.get("message")

        return action, addresate, user_name, message, send_data

    def send_answer(self, action, addresate, user_name, message, send_data, addr):
        if action == "join_chat":
            self.client_joined(user_name, send_data, addr)
        elif action == "leave_chat":
            print(user_name, "<= left chat")
        elif addresate:
            if addresate in self.client_names.keys():
                self.send_private_message(addresate, user_name, message, send_data, addr)
            else:
                self.addresate_not_found(addresate, send_data, addr)
        else:
            self.send_message(user_name, message, send_data, addr)

    def client_joined(self, user_name, send_data, addr):
        print(user_name, "=> join chat")
        send_data["response"] = 201
        for client in self.clients:
            if addr == client:
                self.client_names[user_name] = addr
                self.s.sendto(json.dumps(send_data).encode("utf-8"), client)

    def send_private_message(self, addresate, user_name, message, send_data, addr):
        print(user_name, "to ->", addresate, "::", message)
        for client in self.clients:
            if addr == client:
                send_data["response"] = 202
                self.s.sendto(json.dumps(send_data).encode("utf-8"), client)
        send_data["response"] = 200
        self.s.sendto(json.dumps(send_data).encode("utf-8"), self.client_names[addresate])

    def addresate_not_found(self, addresate, send_data, addr):
        print("client", addresate, "not found")
        send_data["response"] = 404
        for client in self.clients:
            if addr == client:
                self.s.sendto(json.dumps(send_data).encode("utf-8"), client)

    def send_message(self, user_name, message, send_data, addr):
        print(user_name, "::", message)
        for client in self.clients:
            if addr == client:
                send_data["response"] = 202
            else:
                send_data["response"] = 200
            self.s.sendto(json.dumps(send_data).encode("utf-8"), client)


if __name__ == "__main__":
    my_server = MyServer()
    my_server.server_works()
    my_server.s.close()
