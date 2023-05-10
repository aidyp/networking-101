import socket 

HOST = '0.0.0.0'
PORT = 8081 

# Create a TCP Socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

while True:
    client_conn, client_addr = server_socket.accept()
    data = client_conn.recv(1024).decode()
    print(data) 
    with open('index.html', 'r') as fd:
        content = fd.read()
    response = "HTTP/1.0 200 OK\n\n" + content
    print(f"Response: {response}")
    client_conn.sendall(response.encode())
    client_conn.close()

server_socket.close()