import hw14_client
import hw14_server
import time
import json
from mockito import when
from mock import Mock
import socket
import sys

sys.stdin = open("test_inputs.txt")

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


def test_client_receiving():
    msg = client_for_test.receiving("test", socket.socket(socket.AF_INET, socket.SOCK_DGRAM)).get("message")
    assert msg == "test_message"


def test_client_compile_message():
    msg = client_for_test.compile_message()
    assert json.loads(msg.decode("utf-8")).get("message") == "test"
