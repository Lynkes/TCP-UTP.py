import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Banco Online")
    print("Opções:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Consultar Saldo")

    while True:
        choice = input("Selecione a operação (1/2/3, ou 'q' para sair): ")
        client_socket.send(choice.encode())

        if choice == 'q':
            break
        elif choice == '1':
            deposit_amount = float(input("Digite o valor do depósito: "))
            client_socket.send(str(deposit_amount).encode())
            response = client_socket.recv(1024).decode()
            print(response)
        elif choice == '2':
            withdraw_amount = float(input("Digite o valor do saque: "))
            client_socket.send(str(withdraw_amount).encode())
            response = client_socket.recv(1024).decode()
            print(response)
        elif choice == '3':
            client_socket.send("3".encode())
            balance = client_socket.recv(1024).decode()
            print(balance)

    client_socket.close()

if __name__ == '__main__':
    main()
