README.txt

TCP client / server pair Readme.

TCP server-client pair for my Computer Networks class (a week or so ago). These work on a local machine.
I think this is in Python 3. Basically the client connects to the server and sends a
few query strings and gets different responses​

Server:
	1. You run by typing "python server.py" in the command line

	2. You are then prompted for a port and IP address in the command line
		2a. Valid custom ports and addresses can be used; all invalid ports and addresses default to
		5555 for port # and 127.0.0.1 for IP address.
		2b. A message displays showing the port and IP you have connected to
			2bi. If you entered a newline for the IP, IP will display as ' ', which is the
			same as 127.0.0.1
	3. Your server will then wait for connections, and will print client port #s, addresses,
	and will reply to client requests with one string per character.

	4. You may exit the server at any point with a ctrl + c keyboard interrupt

Client:
	1. You run by typing "python client.py" in the command line

	2. If the port you enter is invalid (e.g. out of range, or nobody listening), the client
	will attempt to connect and will display an error and exit.
		2a. This means there is no safeguard for you entering the wrong port on the client end

	3. If the IP you enter is invalid or cannot be connected to, the client defaults to 127.0.0.1

	4. You will timeout after 60 seconds, so after 60 seconds, the server resets your connection if you have been inactive.

	4. You can enter as many (capitalized) strings consisting of NCZPSM  (duplicates, space-separated, etc.) and get the response from the 
	server in a separate string for each character

	5. You can close your connection by typing "-1"

Notes:
	(1) Entering an invalid IP will default to 127.0.0.1 for both server and client
	(2) Entering an invalid port as a server will default to 5555
	(3) Entering an invalid port as a client will attempt to connect to the invalid port and will
	result in a response saying no server is listening at the specified port and the client will quit
	(4) Multiple clients can connect to a single server, and can come and go from the server with no affect on other clients.

	(5) Interestingly, localhost and 127.0.0.1 are not exactly the same.




