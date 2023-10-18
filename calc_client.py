import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Calculadora Básica")
    print("Opções:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operator = input("Selecione a operação (1/2/3/4): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    message = f"{num1} {num2} {operator}"
    client_socket.send(message.encode())

    result = client_socket.recv(1024).decode()
    print(f"Resultado: {result}")

    client_socket.close()

if __name__ == '__main__':
    main()
