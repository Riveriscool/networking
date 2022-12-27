import socket
import json
import random
import time
file = open("database.json", 'r')
hi = "hallo"
bye = "ballo"
json_data = json.load(file)
# Set the server address and port
server_address = ('127.0.0.1', 9999)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind(server_address)

# Set the maximum number of pending connections
server_socket.listen(1)

# Accept a connection
connection, client_address = server_socket.accept()
def get_time_xor_random():
    nanoseconds = int(time.time() * 1e9)
    random_number = random.randint(1, 100000)
    return nanoseconds ^ random_number
def update_token(username, new_token):
    with open("database.json", "a+") as f:
        data = json.load(f)
        data[username][1] = new_token
        json.dump(data, f)
def login(username, password):
    global json_data


    realpassword = json_data[username][0]
    if password == realpassword:
        token = get_time_xor_random()# can you help with the login function, it works, but it reformats the database in a way that if you try to signup it breaks the database
    else:
        token = "0"
    update_token(username, token)
    return token

    
def signup(username, password):
       
    fd=open("database.json","r")
    d=fd.read()
    fd.close()
    m=d.split("\n")
    s="\n".join(m[:-1])
    fd=open("database.json","w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()
    with open("database.json", "a+") as f:
        usrdata = "," + "\n" + "    " + '"' + username + '"' + ': ' + '["' + password  + '"'+ "," + '"0"' + "]" + "\n" + "}"
        f.write(usrdata)
    
try:
    # Receive the signup request
    signup_request = connection.recv(1024).decode()
    print(f"signup request is {signup_request}")
    # Parse the signup choice, username, and password from the request
    signup_choice, username, password = signup_request.split()
    print(f"signupchoice is {signup_choice}")
    if signup_choice == "Login":
        token = login(username, password)
        print("sending token...")
        print(token)
        connection.sendall(token.encode()) 
    # Generate a token and send it back to the client
    if signup_choice == "Signup":
        signup(username, password)
        connection.send("Sucess".encode())

    # Receive the request with the user apt, token, and want
    
    request = connection.recv(1024).decode().split()
    print(f"request is {request}")
    # Parse the user apt, token, and want from the request
    with open("database.json", "r") as f:
        data = json.load(f)


    realtoken = data[request[0]][1]

    #find realtoken
    received_token = str(request[1])
    want = request[2]
    print(f"real token is {realtoken}")
    print(f"received token which is [{received_token}] and realtoken is {realtoken}")
    
    if received_token == realtoken :
        print("tokens match")
        if want == "hi":
            connection.send("hi".encode())
        elif want == "bye":
            connection.send("bye".encode())
        

    # Echo the received message back to the client
    
finally:
    # Close the connection
    connection.close()