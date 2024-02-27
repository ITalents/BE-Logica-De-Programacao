# Definindo a lista de tarefas
lista_tarefas = []

# Função para adicionar tarefa
def adicionar_tarefa(tarefa):
    lista_tarefas.append({"descricao": tarefa, "concluida": False})

# Função para listar tarefas
def listar_tarefas():
    for index, tarefa in enumerate(lista_tarefas, start=1):
        print(f"{index}. [{'' if tarefa['concluida'] else 'X'}] {tarefa['descricao']}")

# Função para marcar tarefa como concluída
def marcar_tarefa_concluida(index):
    if 1 <= index <= len(lista_tarefas):
        lista_tarefas[index - 1]['concluida'] = True
        print("Tarefa marcada como concluída.")
    else:
        print("Índice inválido.")

# Função para remover tarefa
def remover_tarefa(index):
    if 1 <= index <= len(lista_tarefas):
        del lista_tarefas[index - 1]
        print("Tarefa removida.")
    else:
        print("Índice inválido.")

# Função para limpar lista de tarefas concluídas
def limpar_lista_concluidas():
    global lista_tarefas
    lista_tarefas = [tarefa for tarefa in lista_tarefas if not tarefa['concluida']]
    print("Tarefas concluídas removidas.")

# Função principal
def main():
    while True:
        print("\n=== To-Do List ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Limpar Lista de Tarefas Concluídas")
        print("6. Sair")

        escolha = input("Escolha uma opção (1-6): ")

        if escolha == '1':
            tarefa = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(tarefa)
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            index = int(input("Digite o número da tarefa a ser marcada como concluída: "))
            marcar_tarefa_concluida(index)
        elif escolha == '4':
            index = int(input("Digite o número da tarefa a ser removida: "))
            remover_tarefa(index)
        elif escolha == '5':
            limpar_lista_concluidas()
        elif escolha == '6':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
