__author__ = 'jamesboyle'

from socket import *

'''
High-level overview

1. Client can connect to custom port and IP. If client input
is invalid or unspecified (e.g. just hit enter), default to
port # 5555 and ip 127.0.0.1

2. In order to receive responses from the server as
separate strings, it is necessary for us to pre-process
the client's message and to send the client's message one
character at a time. This guarantees separate strings

3. Client can send as many queries as they want, spaces or not,
valid characters or invalid characters, until they type -1, at which
point they will receive a session closing message and the
socket closes.

4. Client can also timeout, so be wary of connecting for too long without
actually doing anything.

5. Several clients can be connected at once.

Notes: Fulfills all specifications as outlined in handout
'''

def main():

    ##establishes connection
    clientSocket = establishConnectionToServer()

    ##allows sending of messages to Server through clientSocket
    sendMessagesOnceConnectionBegins(clientSocket)

def sendMessagesOnceConnectionBegins(clientSocket):

    validDict = {"N":0,"C":0,"Z":0,"P":0,"S":0,"M":0}

    print("Type '-1' to exit the query system.")

    ##Enter as many queries as you want;
    ##they will be parsed and sent separately
    ##to guarantee receipt of separate strings
    while True:
        sentence = raw_input('Input String:')
        if sentence == "-1": break
        sentence = [z for z in sentence if z in validDict]
        ##print("SENTENCE: ", sentence)
        for z in sentence:
            clientSocket.send(z)
            modifiedSentence = clientSocket.recv(1024)
            print("From Server:", modifiedSentence)

    print("Client session closing!")
    clientSocket.close()

def establishConnectionToServer():

    ##establishes Port connection
    print("Server port #? (carriage return for default)")
    userPort = raw_input()
    try:
        if 0 <= int(userPort) <65535: serverPort = int(userPort)
    except ValueError:
        serverPort = 5555

    ##establishes IP connection
    print("Server IP address?")
    ipAddress = raw_input()
    clientSocket = socket(AF_INET,SOCK_STREAM)
    try:
        clientSocket.connect((ipAddress, serverPort))
    except:
        try:
            clientSocket.connect(('127.0.0.1',serverPort))
        except:
            print("No server listening at specified port and IP. Client terminating")
            exit(-1)

    ##returns socket
    return clientSocket

if __name__ == '__main__':
    main()