import socket

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"Servidor UDP esperando por mensagens em {host}:{port}...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        client_ip, client_port = client_address

        message = data.decode()
        inverted_message = message[::-1]

        response = f"Servidor: Mensagem invertida: {inverted_message}"

        server_socket.sendto(response.encode(), (client_ip, client_port))

if __name__ == '__main__':
    main()
