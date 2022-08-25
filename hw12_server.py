import json
import socket
import time

host = "localhost"
port = 9090

clients = []
client_names = {}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
quit = False
print("[SERVER STARTED]")

while not quit:
    try:
        rec_data, addr = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + itsatime + "] / ", end="")

        try:
            client_msg = json.loads(rec_data.decode("utf-8"))
            send_data = {k: v for k, v in client_msg.items() if k != "action"}
        except Exception as ex:
            print(ex)
            print(rec_data.decode("utf-8"))
            client_msg = {}
            send_data = {"response": 503}

        action = client_msg.get("action")
        addresate = client_msg.get("addresate")
        user_name = client_msg.get("user").get("name")
        message = client_msg.get("message")

        if action == "join_chat":
            print(user_name, "=> join chat")
            send_data["response"] = 201
            for client in clients:
                if addr == client:
                    client_names[user_name] = addr
                    s.sendto(json.dumps(send_data).encode("utf-8"), client)

        elif action == "leave_chat":
            print(user_name, "<= left chat")

        elif addresate:
            if addresate in client_names.keys():
                print(user_name, "to ->", addresate,
                      "::", message)
                for client in clients:
                    if addr == client:
                        send_data["response"] = 202
                        s.sendto(json.dumps(send_data).encode("utf-8"), client)
                send_data["response"] = 200
                s.sendto(json.dumps(send_data).encode("utf-8"), client_names[addresate])
            else:
                print("client", addresate, "not found")
                send_data["response"] = 404
                for client in clients:
                    if addr == client:
                        s.sendto(json.dumps(send_data).encode("utf-8"), client)
        else:
            print(user_name, "::", message)
            for client in clients:
                if addr == client:
                    send_data["response"] = 202
                else:
                    send_data["response"] = 200
                s.sendto(json.dumps(send_data).encode("utf-8"), client)

    except Exception as ex:
        try:
            for client in clients:
                s.sendto(json.dumps({
                    "response": 503,
                    "time": time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
                }).encode("utf-8"), client)
        except Exception as int_ex:
            print(int_ex)
        print(ex)
        print("\n[SERVER STOPPED]")
        quit = True

s.close()
