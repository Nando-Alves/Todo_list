from tasks import add_task, list_tasks, complete_task, delete_task

def menu():
    print("\n=== Gerenciador de Tarefas ===")
    print("1. Listar tarefas")
    print("2. Adicionar tarefa")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")

while True:
    menu()
    choice = input("Escolha uma opção: ")

    if choice == "1":
        list_tasks()
    elif choice == "2":
        task = input("Digite a tarefa: ")
        add_task(task)
    elif choice == "3":
        index = int(input("Número da tarefa a concluir: ")) - 1
        complete_task(index)
    elif choice == "4":
        index = int(input("Número da tarefa a remover: ")) - 1
        delete_task(index)
    elif choice == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")
