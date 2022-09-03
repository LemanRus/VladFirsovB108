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


def test_server_disassemble_msg():
    disassembled = server_for_test.disassemble_msg(json.dumps({
                            "action": "send_msg",
                            "time": time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()),
                            "message": "test_message",
                            "user": {
                                "name": "test_name",
                                "status": "online"}
                            }).encode("utf-8"))
    assert disassembled[:-1] == ("send_msg", None, "test_name", "test_message")


def test_server_assemble_answer():
    assembled = server_for_test.assemble_answer("send_msg", None, "test_name", "test_message", None, None)
    assert assembled == 200


def test_client_receiving():
    msg = client_for_test.receiving("test", socket.socket(socket.AF_INET, socket.SOCK_DGRAM))
    assert msg == "test_message"


def test_client_sending():
    assert json.dumps({
                    "action": "join_chat",
                    "time": time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()),
                    "user": {
                        "name": client_for_test.name,
                        "status": "online"
                    }}).encode("utf-8") == client_for_test.send_msg()