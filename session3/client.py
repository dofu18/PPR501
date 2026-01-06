# import socket

# HOST = '127.0.0.1'
# PORT = 8080

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #khởi tạo socket TCP/IP
# client_socket.connect((HOST, PORT)) #kết nối đến server tại địa chỉ và cổng đã cho

# message = "Hello, Server!"
# client_socket.send(message.encode()) #gửi dữ liệu đến server

# data_from_server = client_socket.recv(1024) #nhận dữ liệu từ server
# print(f"Received from server: {data_from_server.decode('utf-8')}")

# client_socket.close() #đóng kết nối

import socket

HOST = '127.0.0.1'
PORT = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #khởi tạo socket TCP/IP
client_socket.connect((HOST, PORT)) #kết nối đến server tại địa chỉ và cổng đã cho

with open('sample_5mb.txt', 'r') as file:
    data = file.read()
    client_socket.send(data.encode()) #gửi dữ liệu đến server

with open('error_log.txt', 'r') as file:
    data = file.read()
    client_socket.send(data.encode()) #gửi dữ liệu đến server

client_socket.close() #đóng kết nối