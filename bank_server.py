import socket

class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return 0

    def get_balance(self):
        return self.balance

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Servidor do Banco esperando por conexões em {host}:{port}...")

    conn, addr = server_socket.accept()
    print(f"Conexão estabelecida com {addr}")

    account = BankAccount(1000)  # Saldo inicial de R$ 1000

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        if data == '1':
            deposit_amount = float(conn.recv(1024).decode())
            account.deposit(deposit_amount)
            conn.send(f"Depósito de R$ {deposit_amount} realizado com sucesso.".encode())
        elif data == '2':
            withdraw_amount = float(conn.recv(1024).decode())
            withdrawn = account.withdraw(withdraw_amount)
            if withdrawn > 0:
                conn.send(f"Saque de R$ {withdrawn} realizado com sucesso.".encode())
            else:
                conn.send("Saldo insuficiente para saque.".encode())
        elif data == '3':
            balance = account.get_balance()
            conn.send(f"Saldo disponível: R$ {balance}".encode())

    conn.close()

if __name__ == '__main__':
    main()
