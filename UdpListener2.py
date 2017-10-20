from socket import socket, AF_INET, SOCK_DGRAM, IPPROTO_UDP, timeout, SOL_SOCKET, SO_BROADCAST


class UDPListener:
    def __init__(self, port=1000, ip='localhost'):
        self._socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        self._socket.setsockopt(SOL_SOCKET, SO_BROADCAST, True)
        self._socket.bind((ip, port))
        self._socket.settimeout(5)

    def listen(self):
        msg = ""
        port = 0
        try:
            # msg, port = self._socket.listen()
            msg, port = self._socket.recv(1024)
            print(msg.decode(), "from", port)

        except timeout:
            print("timeout", msg)

if __name__ == '__main__':
    server = UDPListener()
    server.listen()
