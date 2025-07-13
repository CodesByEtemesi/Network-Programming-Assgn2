import socket

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to host and port
host = 'localhost'
port = 12345
server_socket.bind((host, port))
server_socket.listen(1)
print(f"Server is listening on {host}:{port}...")

# Accept connection
conn, addr = server_socket.accept()
print(f"Connected to {addr}")

# Receive numbers from client
data = conn.recv(1024).decode()
num1, num2 = map(int, data.split(','))

# Calculate sum
result = num1 + num2

# Send result back to client
conn.send(str(result).encode())

# Close connection
conn.close()
