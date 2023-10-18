import socket

def calculate(num1, num2, operator):
    if operator == '1':
        return num1 + num2
    elif operator == '2':
        return num1 - num2
    elif operator == '3':
        return num1 * num2
    elif operator == '4':
        if num2 == 0:
            return "Erro: Divisão por zero"
        return num1 / num2
    else:
        return "Operação inválida"

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Servidor esperando por conexões em {host}:{port}...")

    conn, addr = server_socket.accept()
    print(f"Conexão estabelecida com {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        num1, num2, operator = data.split()
        result = calculate(float(num1), float(num2), operator)
        conn.send(str(result).encode())

    conn.close()

if __name__ == '__main__':
    main()
