import os

ESTOQUE_FILE = "estoque.txt"
VENDAS_FILE = "vendas.txt"


def registrar_venda(id_cliente, id_produto, quantidade):
    with open(VENDAS_FILE, "a") as f:
        f.write(f"{id_produto},{id_cliente},{quantidade}\n")

    print("Venda registrada com sucesso!")
   
def buscar_vendas_por_cliente(id_cliente):
    if not os.path.exists(VENDAS_FILE):
        print("Nenhuma venda registrada ainda.")
        return

    with open(VENDAS_FILE, "r") as f:
        for linha in f:
            partes = linha.strip().split(",")
            if len(partes) >= 2 and partes[1] == id_cliente:
                print("Venda encontrada:", linha.strip())

def menu():
    while True:
        print("1. Registrar venda")
        print("2. Buscar venda por cliente")
        print("3. sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_cliente = input("ID do cliente: ")
            id_produto = input("ID do produto: ")
            quantidade = int(input("Quantidade: "))
            registrar_venda(id_cliente, id_produto, quantidade)
        elif opcao == "2":
            id_cliente = input("ID do cliente para buscar: ")
            buscar_vendas_por_cliente(id_cliente)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
