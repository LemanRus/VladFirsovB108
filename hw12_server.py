import json
import socket
import time

host = "localhost"
port = 9090

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
quit = False
print("[SERVER STARTED]")

while not quit:
    try:
        data, addr = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + itsatime + "] / ", end="")
        client_msg = json.loads(data.decode("utf-8"))
        if client_msg.get("action") == "join_chat":
            print(client_msg.get("user").get("name"), "=> join chat")
        else:
            print(client_msg.get("user").get("name"), "::", client_msg.get("message"))
            # print(data.decode("utf-8"))  # Сервер выводит здесь
            for client in clients:
                if addr != client:
                    s.sendto(data, client)  # А здесь пересылает остальным клиентам, кроме отправившего
    except Exception as ex:
        try:
            for client in clients:
                s.sendto(json.dumps({
                    "response": 503,
                    "time": time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
                }), client)
        except Exception:
            pass
        print(ex)
        print("\n[SERVER STOPPED]")
        quit = True

s.close()
