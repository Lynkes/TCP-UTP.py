import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client_id = input("Digite o identificador do cliente: ")

    while True:
        sale_message = input("Digite a venda (ou 'q' para encerrar): ")
        if sale_message == 'q':
            break

        client_socket.sendto(sale_message.encode(), (host, port))

    end_message = f"{client_id}:LISTAGEM FINALIZADA"
    client_socket.sendto(end_message.encode(), (host, port))

    data, server_address = client_socket.recvfrom(1024)
    response = data.decode()
    print(response)

    client_socket.close()

if __name__ == '__main__':
    main()
