##Task Manager - Python Project
Description

This is a Python project that implements a task manager using Object-Oriented Programming (OOP). It allows the user to manage tasks with the following features:

    Add a new task.
    Delete a task.
    Mark a task as completed or incomplete.
    View existing tasks.
    Save and load tasks from a JSON file.

Features

    Add task: Allows the user to add a new task.
    Delete task: Allows the user to remove an existing task.
    Mark task as completed: Changes the task's status to "completed".
    Mark task as incomplete: Changes the task's status to "incomplete".
    Show tasks: Displays all saved tasks and their status.
    Save tasks: Saves the current tasks to a JSON file.
    Load tasks: Loads tasks from a previously saved JSON file.

Requirements

    Python 3.x
    Standard libraries (os, json)

Usage

    Clone the repository:

[git clone https://github.com/pussybr3aker/task-manager.git](https://github.com/pussybr3aker/Task-List)
cd task-manager

Run the script: To run the task manager, simply execute the task_manager.py file in the terminal:

    python task_manager.py

    User interaction: The program will present an interactive menu where you can add, delete, view, and mark tasks. You can also save and load tasks through a JSON file.

Example of usage

Upon running the program, you'll see the following interactive menu in the console:

1) Add task
2) Delete task
3) Mark task as completed
4) Mark task as incompleted
5) Show tasks
6) Save tasks

Select an option and follow the on-screen instructions.
Code structure

    task.py: Contains the Task class, representing an individual task with a name and status.
    task_manager.py: Contains the TaskManager class, which manages the tasks (adding, deleting, marking as completed, etc.) and user interaction.
    task_list.json: JSON file where tasks are saved.

Contributing

If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. Any suggestions or improvements are welcome.
