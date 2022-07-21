import socket
import time


def test_internet():
    try:
        socket.create_connection(("youtube.com", 80))
        return True
    except OSError:
        return False


def check_internet():
    check_status = test_internet()
    while check_status:
        check_status = test_internet()
        if not check_status:
            raise ConnectionError("No connection detected!")
        print("Internet is connected!")
