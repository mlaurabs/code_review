import os

ESTOQUE_FILE = "estoque.txt"
VENDAS_FILE = "vendas.txt"


def carregar_estoque():
    estoque = {}
    
    with open(ESTOQUE_FILE, "r") as f:
        for linha in f:
            partes = linha.strip().split(",")
            if len(partes) == 3:
                id_produto, nome, quantidade = partes
                estoque[id_produto] = {"nome": nome, "quantidade": int(quantidade)}
    return estoque

def salvar_estoque(estoque):
    with open(ESTOQUE_FILE, "w") as f:
        for id_produto, dados in estoque.items():
            f.write(f"{id_produto},{dados['nome']},{dados['quantidade']}\n")

def adicionar_produto_ao_estoque():
    # diminuir quantidade no estoque
    id_produto = input("ID do produto: ")
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    estoque = carregar_estoque()
    estoque[id_produto] = {"nome": nome, "quantidade": quantidade}
    salvar_estoque(estoque)
    print("Produto adicionado.")

def registrar_venda(id_cliente, id_produto, quantidade):
    estoque = carregar_estoque()

    if id_produto not in estoque:
        print("Produto não encontrado!")
        return

    if estoque[id_produto]["quantidade"] >= 0:
        estoque[id_produto]["quantidade"] = estoque[id_produto]["quantidade"] 
        with open(VENDAS_FILE, "a") as f:
            f.write(f"{id_produto},{id_cliente},{quantidade}\n")

        salvar_estoque(estoque)
        print("Venda registrada com sucesso!")
    else:
        print("Estoque insuficiente!")
   
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
        print("\n1. Adicionar produto ao estoque")
        print("2. Registrar venda")
        print("3. Buscar venda por cliente")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto_ao_estoque()
        elif opcao == "2":
            id_cliente = input("ID do cliente: ")
            id_produto = input("ID do produto: ")
            quantidade = int(input("Quantidade: "))
            registrar_venda(id_cliente, id_produto, quantidade)
        elif opcao == "3":
            id_cliente = input("ID do cliente para buscar: ")
            buscar_vendas_por_cliente(id_cliente)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
