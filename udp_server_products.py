import socket

# Dicionário para armazenar as vendas de cada cliente
sales_data = {}

def process_sale(sale):
    # Formato da mensagem: "identificador_do_cliente:nome_do_produto:quantidade_vendida"
    parts = sale.split(':')
    if len(parts) == 3:
        client_id, product_name, quantity = parts
        quantity = int(quantity)

        if client_id not in sales_data:
            sales_data[client_id] = {}

        if product_name in sales_data[client_id]:
            sales_data[client_id][product_name] += quantity
        else:
            sales_data[client_id][product_name] = quantity

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"Servidor UDP de Vendas esperando por mensagens em {host}:{port}...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        client_message = data.decode()

        if ":LISTAGEM FINALIZADA" in client_message:
            client_id = client_message.split(':')[0]
            total_sales = sales_data.get(client_id, {})
            total_amount = sum([quantity for quantity in total_sales.values()])
            response = f"Total de vendas para Cliente {client_id}: R$ {total_amount}"
            server_socket.sendto(response.encode(), client_address)
        else:
            process_sale(client_message)

if __name__ == '__main__':
    main()
