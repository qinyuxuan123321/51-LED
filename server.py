import socket

# 创建TCP套接字，IPv4
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP和端口8080
server_socket.bind(("0.0.0.0", 8080))
# 开启监听，等待客户端连接
server_socket.listen(5)
print("TCP服务端已启动，等待客户端连接，端口8080")

# 等待客户端，这里完成TCP三次握手
conn, addr = server_socket.accept()
print(f"客户端 {addr} 已完成三次握手，连接成功！")

# 循环收发消息
while True:
    # 接收客户端数据，最大1024字节
    data = conn.recv(1024)
    if not data:
        print("客户端断开连接")
        break
    # 二进制转文字
    recv_msg = data.decode("utf-8")
    print(f"【收到客户端】：{recv_msg}")
    # 构造回复消息
    send_msg = "服务端收到：" + recv_msg
    # 文字转二进制发送
    conn.send(send_msg.encode("utf-8"))

# 关闭套接字，触发四次挥手
conn.close()
server_socket.close()