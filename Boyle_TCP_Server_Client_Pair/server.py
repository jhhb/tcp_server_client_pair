__author__ = 'jamesboyle'
from socket import *
import threading

"""
High-level overview:

1. First we initialize the server with a call to initializeServer.
During this time the user can enter a custom port and IP if they want.
Otherwise we default to 5555 and 127.0.0.1 for port and IP.

2. We then call listenForClients, which perpetually listens for clients until
the user hits "ctrl+c" to exit terminal.

3. listenForClients spawns a new thread for each client that connects and
sets client.daemon = true so that we can kill the server with a keyboard interrupt
if we would like.

4. Once we have the thread, it just perpetually calls the listen function, which listens
for requests from the associated client. IF we get a request, we call parse, which
matches the client query string with values in a dictionary. We then return separate
strings for each query request.

"""

def main():
    serverSocket = initializeServer()
    listenForClients(serverSocket)

#This function perpetually listens for clients and spawns new threads for each one
#It is necessary to set .daemon true for each client so that you can
#kill the server with a keyboard interrupt
def listenForClients(serverSocket):
    while True:
        try:
            connectionSocket, addr = serverSocket.accept()
            connectionSocket.settimeout(60)
            newThread = threading.Thread(target = listenToClient, args = (connectionSocket, addr))
            newThread.daemon = True
            newThread.start()
        except KeyboardInterrupt:
            print("Server exited by Keyboard Interrupt")
            raise SystemExit

##Binds server to (custom) port and (custom) IP
def initializeServer():

    serverPort = 5555
    print("Server port #? (carriage return for default)")
    userPort = raw_input()
    try:
        if 0 <= int(userPort) <65535: serverPort = int(userPort)
    except ValueError:
        pass

    print("Server IP address?")
    ipAddress = raw_input()
    serverSocket = socket(AF_INET,SOCK_STREAM)
    try:
        serverSocket.bind((ipAddress,serverPort))
        print("Bound to IP:" , ipAddress)
        print("Bound to Port:", serverPort)
    except:
        serverSocket.bind(('127.0.0.1',serverPort))
        print("Bound to IP: 127.0.0.1")
        print("Bound to Port:", serverPort)



    print("You may terminate the server with keyboard interrupt ctrl+c")
    print('The server is ready to receive')
    serverSocket.listen(5)
    return serverSocket

##Receive data from client and parse response
def listenToClient(client, address):
    while True:
        try:
            data = client.recv(1024)
            if data:
                print("String received from client: ", data)
                print("Port of client: ",address[1])
                print("Address of client: ", address[0])
                parse(client, data)
        except:
            client.close()
    return False

##Reply to client with response from dictionary
def parse(client, message):
    consts = Constants()
    if message in consts.d:
        client.send(consts.d[message])

class Constants:
    def __init__(self):
        self.d = {"N":"James","C":"Brunswick","Z":"04011","P":"5555","S":"Soccer","M":"Hello!"}

if __name__ == '__main__':
    main()