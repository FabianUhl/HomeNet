import socket
import HomeNetServer.protocol.spotter as prt


class ClientFinder(object):
    def __init__(self):
        # Create a UDP Broadcast socket
        self.lst_Client = ()
        self.hello_msg = prt.server_spotter_keyword
        self.port = 2000
        print("Looking for run UDP clients on port " + str(self.port))

    def search(self):
        print("searching")
        upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        upd_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
        upd_socket.settimeout(5)
        upd_socket.sendto(self.hello_msg.encode(), ("<broadcast>", self.port))
        try:
            print(upd_socket.recv(1024))
        except socket.timeout:
            print("No Device Time out")
        upd_socket.close()

if __name__ == '__main__':
    deviceClients = ClientFinder()
    deviceClients.search()
