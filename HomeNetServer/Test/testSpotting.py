import unittest


class TestSpotting(unittest.Testcase):
    def test_inputs(self):
        pass

    def test_send_receive(self):
        pass


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