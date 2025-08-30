To-Do List App (Python)
Overview

A simple command-line To-Do List application in Python.
This project demonstrates basic Python concepts such as:

Functions and modular code

File handling (JSON) for data persistence

Lists and dictionaries

Interactive command-line interface

Features

Add tasks

List all tasks

Mark tasks as completed

Remove tasks

Save tasks to a JSON file for persistence

Project Structure
todo_app/
│
├── main.py        # Main program, handles user input and menu
├── tasks.py       # Functions for managing tasks (add, list, complete, delete)
└── tasks.json     # JSON file to store tasks (created automatically)

How to Run

Clone the repository or download the project files:

git clone <repository-url>
cd todo_app


Make sure you have Python installed (3.6+ recommended).

Run the program:

python main.py


Follow the menu in the terminal:

=== To-Do List Manager ===
1. List tasks
2. Add task
3. Complete task
4. Remove task
5. Exit

Notes

If tasks.json does not exist, it will be created automatically.

The program handles empty JSON files gracefully.

Example Usage
Choose an option: 2
Enter the task: Study Python
Task 'Study Python' added!

Choose an option: 1
1. Study Python [❌]

Choose an option: 3
Enter task number to complete: 1
Task 'Study Python' completed!
