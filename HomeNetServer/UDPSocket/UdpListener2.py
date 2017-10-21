import socket
import protocol.spotter as prt

# import HomeNetServer.protocol.spotter as prt
#import HomeNetServer.protocol.spotter as spotter
#import HomeNetServer.protocol.spotter as spotter


class UDPListener:
    def __init__(self, port=1000, ip="<broadcast>"):
        self.client_address = (ip, port)
        self.server_address = None
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

        self._socket.bind(self.client_address)

    def listen(self, timeout=0):
        print("listen to", self.client_address, "for", timeout, "s")
        if timeout > 0:
            self._socket.settimeout(timeout)

        self.server_address = None
        msg = ""
        try:
            # msg, port = self._socket.listen()
            msg, self.server_address = self._socket.recvfrom(1024)
            if prt.server_spotter_keyword not in msg.decode('ascii'):
                self.server_address = None
            print(msg.decode(), "from", self.server_address)
        except socket.timeout:
            print("timeout", msg)

    def get_server_address(self):
        return self.server_address

if __name__ == '__main__':
    server = UDPListener(port=1000)
    server.listen()
