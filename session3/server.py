# import socket

# HOST = '127.0.0.1'
# PORT = 8080

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #khởi tạo socket TCP/IP
# server_socket.bind((HOST, PORT)) #gán địa chỉ và cổng cho socket
# server_socket.listen() #lắng nghe kết nối, với số lượng kết nối tối
# print("Server is listening on port 8080...")

# conn, addr = server_socket.accept() #chấp nhận kết nối từ client
# print(f"Connected by {addr}")

# data = conn.recv(1024) #nhận dữ liệu từ client
# print(f"Received message: {data.decode()}") #in ra thông điệp nhận được

# response_message = "Hello, Client!"
# conn.send(response_message.encode()) #gửi phản hồi lại cho client   

# conn.close() #đóng kết nối
# # server_socket.close() #đóng socket server


import socket

HOST = '127.0.0.1'
PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #khởi tạo socket TCP/IP
server_socket.bind((HOST, PORT)) #gán địa chỉ và cổng cho socket
server_socket.listen() #lắng nghe kết nối, với số lượng kết nối tối
print("Server is listening on port 8080...")

conn, addr = server_socket.accept() #chấp nhận kết nối từ client
print(f"Connected by {addr}")

received_data = b""
while True:
    data = conn.recv(5000)
    if not data:
        break
    received_data += data

data = conn.recv(1024) #nhận dữ liệu từ client
print(f"Received message: {data.decode()}") #in ra thông điệp nhận được
    
with open('SAVE_FILE', 'wb') as f:
    f.write(received_data)

conn.close() #đóng kết nối
server_socket.close() #đóng socket server