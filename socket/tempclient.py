import socket

# Set the server address and port
server_address = ('127.0.0.1', 9999)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(server_address)

# Get the signup choice, username, and password from the user
signup_choice = input("Enter your signup choice: ")
username = input("Enter your username: ")
password = input("Enter your password: ")

# Concatenate the signup choice, username, and password with spaces in between
signup_request = f"{signup_choice} {username} {password}"

# Send the signup request to the server
print("sending data...")
client_socket.sendall(signup_request.encode())
print("sent data")
# Receive the token from the server
token = client_socket.recv(1024).decode()
print(token)
# Get the user apt and want from the user
user_apt = username
want = input("Enter your want: ")

# Concatenate the user apt, token, and want with spaces in between
request = f"{user_apt} {token} {want}"

# Send the request to the server
print(f"sending request which is {request}")
client_socket.sendall(request.encode())
print("sent")
# Receive the response from the server
response = client_socket.recv(1024).decode()
print("received response which is")

# Print the response
print(response)

# Close the socket
client_socket.close()