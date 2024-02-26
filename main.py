import socket

def start_server():
    # 创建一个TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定地址和端口
    server_address = ('localhost', 8888)
    server_socket.bind(server_address)

    # 监听连接
    server_socket.listen(1)
    print('等待连接...')

    while True:
        # 等待客户端连接
        client_socket, client_address = server_socket.accept()
        print('接收到来自 {} 的连接'.format(client_address))

        try:
            # 接收数据
            data = client_socket.recv(1024)
            print('接收到数据:', data.decode('utf-8'))

            # 处理数据（这里可以根据实际需求进行业务逻辑处理）

            # 发送响应数据
            response_data = 'Hello, this is the server response!'
            client_socket.sendall(response_data.encode('utf-8'))

        except Exception as e:
            print('发生异常:', str(e))


if __name__ == "__main__":
    start_server()
