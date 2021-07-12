import socket



class FalconPeer():
    def __init__(self, listen_addr:str="0.0.0.0", port:int=3968) -> None:
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind((listen_addr, port))

    def send(self):
        pass

    def recv(self):
        pass
