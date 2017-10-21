#!/usr/bin/env python3
import socket
#import HomeNetServer.protocol.spotter as prt
from protocol import spotter as prt


class ClientFinder:
    def __init__(self, port=1000):
        # Create a UDP Broadcast socket
        self.lst_Client = ()
        self.hello_msg = prt.server_spotter_keyword
        self.port = port
        print("Looking for run UDP clients on port " + str(self.port))

    def send(self):
        upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        upd_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
        upd_socket.sendto(self.hello_msg.encode(), ("<broadcast>", self.port))

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
#    from ...protocol import spotter as prt
    import sys
    from pathlib import Path
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[3]
    print(top)
    sys.path.append(top)
    try:
        sys.path.remove(str(parent))
    except ValueError:
        pass

    import HomeNetServer.UDPSocket
    __package__ = 'HomeNetServer.UDPSocket.ClientFinder'

    print(__package__)

    deviceClients = ClientFinder()
    deviceClients.search()
