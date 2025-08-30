import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Carrega tarefas do arquivo JSON"""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    """Salva tarefas no arquivo JSON"""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    """Adiciona uma nova tarefa"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Tarefa '{task}' adicionada!")

def list_tasks():
    """Lista todas as tarefas"""
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa encontrada!")
        return
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")

def complete_task(index):
    """Marca uma tarefa como concluída"""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Tarefa '{tasks[index]['task']}' concluída!")
    else:
        print("Índice inválido!")

def delete_task(index):
    """Remove uma tarefa"""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Tarefa '{removed['task']}' removida!")
    else:
        print("Índice inválido!")
