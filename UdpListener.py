from socketserver import ThreadingUDPServer, ThreadingMixIn, BaseRequestHandler, UDPServer
from threading import Thread
from sys import argv
from time import time


class MyUDPHandler(BaseRequestHandler):
    def setup(self):
        print("setup UDP Handler")

    def handle(self):
        print("rec data")
        #data = self.request.recv(1024)
        data = self.request[0].strip()
        socket = self.request[1]
        #print("{} wrote:".format(self.client_address[0]))
        print(data)
        socket.sendto(data.upper(), self.client_address)


#class ThreadedTCPServer(ThreadingMixIn, UDPServer):
#    pass


if __name__ == "__main__":
    HOST, PORT = "localhost", 1000

    lst_argv = argv[1:]
    if lst_argv:
        try:
            PORT = int(lst_argv[0])
        except TypeError:
            print("not int")
        finally:
            PORT = 1000

    UPDListener = UDPServer((HOST, PORT), MyUDPHandler)
    UPDListener.serve_forever()

    #UDPSocket = ThreadingUDPServer((HOST, PORT), MyUDPHandler)

    #UDPSocketThread = Thread(target=UDPSocket.serve_forever)
    #UDPSocketThread.daemon = True

    #start_time = time()
    #UDPSocketThread.start()
    #print("start server", "on Port:", PORT, "at", start_time)
    #UDPSocketThread.join(5)
    #while time() < start_time + 10.0:
     #   pass

    #print("stop server")
    #UDPSocket.shutdown()