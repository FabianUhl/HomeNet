import socket
import HomeNetServer.protocol.spotter as prt
#import HomeNetServer.protocol.spotter as spotter
#import HomeNetServer.protocol.spotter as spotter


class UDPListener:
    def __init__(self, port=1000, ip='localhost', timeout=0):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        # self._socket.setsockopt(SOL_SOCKET, SO_BROADCAST, True)
        self._socket.bind((ip, port))
        if timeout > 0:
            self._socket.settimeout(timeout)

    def listen(self):
        server_address = None
        msg = ""
        try:
            # msg, port = self._socket.listen()
            msg, server_address = self._socket.recvfrom(1024)
            if prt.server_spotter_keyword not in msg.decode('ascii'):
                server_address = None
            print(msg.decode(), "from", server_address)
        except socket.timeout:
            print("timeout", msg)

        return server_address

if __name__ == '__main__':
    server = UDPListener(port=1000, ip="<broadcast>")
    server.listen()
