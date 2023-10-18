import socket
import threading

def send_message(client_socket):
    while True:
        message = input("Digite uma mensagem (ou 'q' para sair): ")

        if message == 'q':
            break

        client_socket.send(message.encode())

def receive_message(client_socket):
    while True:
        data = client_socket.recv(1024)
        response = data.decode()
        print(response)

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))

    send_thread.start()
    receive_thread.start()

if __name__ == '__main__':
    main()
