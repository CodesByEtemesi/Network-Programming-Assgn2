import socket

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
host = 'localhost'
port = 12345
client_socket.connect((host, port))

# Input two numbers from user
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Send to server
data = f"{num1},{num2}"
client_socket.send(data.encode())

# Receive and display result
result = client_socket.recv(1024).decode()
print(f"Sum received from server: {result}")

# Close socket
client_socket.close()
