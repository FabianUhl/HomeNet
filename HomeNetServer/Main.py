import socket
# from socketserver import UDPServer, BaseRequestHandler
import time
# import sys
# import threading


class HomeNetServer(object):
    _port = 1000            # Set PORT
    _epoch = 1              # Time period for stay alive
    _run = True             # run flag
    _timeOut = 3            # time out time in s

    def __init__(self, epoch=1, port=1000, timeOut=10):
        self._epoch = epoch
        self._port = port
        self._tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._timeOut = timeOut
        print("config: \ntime out: ", self._timeOut)

    def start(self):


        # self._tcpSocket.bind(('localhost', self._port))
        start_time = time.time()
        delay_time_s = 0              # s
        print(start_time)
        while self._run:
            delay_time = time.time() - start_time
            # print(delay_time)
            #self._tcpSocket.listen(1)

            if self._timeOut < delay_time:
                self._run = False

            if delay_time_s < delay_time:
                print(int(delay_time), "s")
                delay_time_s += 1


class TCPListener(object):
    def __int__(self, address=('', 1000)):
        self._tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._tcpSocket.bind(address)
        self._tcpSocket.listen(1)
        print(self._tcpSocket.accept())
        print(self._tcpSocket.recv(12).decode())
        self._tcpSocket.close()


class ClientFinder(object):
    def __int__(self):
        print("Looking for UDP clients on port 1000")
        # Create a UDP Broadcast socket
        self.lst_Client = ()
        self.hello_msg = "HomeNetServer"
        self.port = 1000

    def search(self):
        print("searching")
        pass
        #upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        #upd_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
        #upd_socket.settimeout(5)
        #upd_socket.sendto(self.hello_msg.encode(), ("<broadcast>", self.port))
        #try:
        #    print(upd_socket.recv(1024))
        #except socket.timeout:
        #    print("No Device Time out")
        #upd_socket.close()

if __name__ == '__main__':
    #deviceClients = ClientFinder()
    # deviceClients.__int__()
    #deviceClients.search()

    #threading.Thread(target=TCPListener).start()


    TestServer = HomeNetServer()
    TestServer.start()