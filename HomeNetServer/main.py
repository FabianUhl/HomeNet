from threading import Thread

from UDPSocket.UdpListener2 import UDPListener
from UDPSocket.ClientFinder import ClientFinder


def DummyLocalTest():
    print("Start testing Device Spotter")
    port = 1000

    udp_client_listener = UDPListener(port=port)
    udp_client_threaded = Thread(name="TestHomeNetClient", target=udp_client_listener.listen, kwargs={'timeout': 5})
    udp_client_threaded.start()

    spotter = ClientFinder(port=port)
    spotter.send()

    udp_client_threaded.join()
    print(udp_client_listener.get_server_address())


if __name__ == '__main__':
    DummyLocalTest()
