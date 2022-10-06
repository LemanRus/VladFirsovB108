import hw14_client, hw14_server
import time
import json
from mockito import when, unstub
from mock import Mock, patch
import socket


mock_socket = Mock(spec=socket.socket)
attrs = {'recvfrom.return_value': (json.dumps({
                            "response": 200,
                            "time": time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()),
                            "message": "test_message",
                            "user": {
                                "name": "test_name",
                                "status": "online"}
                            }).encode("utf-8"), "0.0.0.0")}
mock_socket.configure_mock(**attrs)
when(socket).socket(socket.AF_INET, socket.SOCK_DGRAM).thenReturn(mock_socket)

server_for_test = hw14_server.MyServer()
client_for_test = hw14_client.MyClient()

server_test_message = {
                            "action": "send_msg",
                            "time": time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()),
                            "message": "test_message",
                            "user": {
                                "name": "test_name",
                                "status": "online"}
                            }


def test_server_disassemble_msg():
    disassembled = server_for_test.disassemble_msg(json.dumps(server_test_message).encode("utf-8"))
    assert disassembled[:-1] == ("send_msg", None, "test_name", "test_message")


def test_server_assemble_answer():
    status_code = server_for_test.assemble_answer("send_msg", None, "test_name", "test_message", None, None)
    assert status_code == 200


def test_server_client_joined():
    status_code = server_for_test.client_joined("Alex", server_test_message, "0.0.0.0")
    assert status_code == 201


def test_server_send_private_message():
    server_for_test.client_names["Alex"] = ("0.0.0.0",)
    status_code = server_for_test.send_private_message("Alex", "me", server_test_message.get("message"),
                                                   server_test_message, "0.0.0.0")
    assert status_code == 200


def test_server_addresate_not_found():
    status_code = server_for_test.addresate_not_found("Alex", server_test_message, "0.0.0.0")
    assert status_code == 404


def test_server_send_message():
    status_code = server_for_test.send_message("Alex", server_test_message.get("message"),
                                               server_test_message, "0.0.0.0")
    assert status_code == 200


def test_server_works():
    server_for_test.server_works()
    assert server_for_test.status == "OK"


def test_client_receiving():
    msg = client_for_test.receiving(socket.socket(socket.AF_INET, socket.SOCK_DGRAM)).get("message")
    assert msg == "test_message"


def test_client_sending():
    client_for_test.join = True
    assert json.dumps({
                    "action": "send_msg",
                    "time": time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()),
                    "message": "test",
                    "user": {
                        "name": client_for_test.name,
                        "status": "online"
                    }}).encode("utf-8") == client_for_test.send_msg()
