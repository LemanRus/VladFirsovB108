import hw14_client, hw14_server
import time
import json

server_for_test = hw14_server.MyServer()

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
    assert assembled is None


def test_client():
    pass