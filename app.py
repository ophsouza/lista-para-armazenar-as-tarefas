# Definir uma lista para armazenar as tarefas
tarefas = []

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        print("Lista de Tarefas:")
        for index, tarefa in enumerate(tarefas, start=1):
            print(f"{index}. {tarefa}")

# Função para remover uma tarefa
def remover_tarefa():
    listar_tarefas()
    if tarefas:
        try:
            index = int(input("Digite o número da tarefa a ser removida: "))
            if 1 <= index <= len(tarefas):
                tarefa_removida = tarefas.pop(index - 1)
                print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
            else:
                print("Número de tarefa inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    else:
        print("Não há tarefas para remover.")

# Loop principal para interação com o usuário
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        adicionar_tarefa()
    elif escolha == "2":
        listar_tarefas()
    elif escolha == "3":
        remover_tarefa()
    elif escolha == "4":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
