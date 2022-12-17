import socket
#this one is different as i know how to do login but not signup
#:(
# create a socket object


socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = "127.0.0.1"

port = 9999

# connection to hostname on the port.
socket.connect((host, port))

# send a thank you message to the client.'


message1 = input("Login or Sign-up?") # unvalidated - what if I input aoudngougandga? it crashes your server.# no it wont, i handle the output on the server side 
if message1 == "Login" or message1 == "Signup":
    # do that on client side too, why not?
    message2 = input("user?")
    message3 = input("password")
    message = message1 + " " + message2 + " " + message3
    socket.send(message.encode())
    token = socket.recv(1024).decode()
    socket.close()
    print(token)



    
else:
    print("kys")