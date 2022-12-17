import socket
import linecache
import json
import random

# create a socket object
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = "127.0.0.1"

port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)



def signup(username, password):
  user = {username: password}

  with open('database.json', 'a') as f:
    json.dump(user, f, separators=(',', ':'))
    f.write('\n')

    
def login(username, password):
    file = open("database.json", 'r')
 

    json_data = json.load(file)

    realpassword = json_data[username]
    if password == realpassword:
        return random.randint(1, 100000000)
    else:
        return 0

gotres1 = False
while gotres1 == False:
    # establish a connection
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))

    raw_data = clientsocket.recv(1024)
    sign_up_choice = raw_data.decode()
    
    scl = sign_up_choice.split(" ")
    if scl[0] == "Login":
      login_return = str(login(scl[1], scl[2]))
      print(login_return)
      clientsocket.send(login_return.encode())
      print("sent return msg")
    if scl[0] == "Signup":
      signup(scl[1], scl[2])
      clientsocket.send(f"Signed up with the username being{scl[1]} and the password being {scl[2]} :D".encode())

    
        