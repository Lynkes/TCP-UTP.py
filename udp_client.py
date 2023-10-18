import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Digite uma mensagem (ou 'q' para sair): ")

        if message == 'q':
            break

        client_socket.sendto(message.encode(), (host, port))

        data, server_address = client_socket.recvfrom(1024)
        response = data.decode()

        print(response)

    client_socket.close()

if __name__ == '__main__':
    main()
