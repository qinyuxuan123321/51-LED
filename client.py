import socket

# 创建TCP套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 发起连接，执行TCP三次握手
client_socket.connect(("127.0.0.1", 8080))

while True:
    # 输入要发送的消息
    msg = input("请输入发给服务端的消息：")
    # 编码后发送
    client_socket.send(msg.encode("utf-8"))
    # 接收服务端返回消息
    recv_data = client_socket.recv(1024)
    print("【收到服务端回复】：", recv_data.decode("utf-8"))

# 关闭连接，触发四次挥手
client_socket.close()