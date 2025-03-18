import os; import json

class task():
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def completed(self):
        self.status = "completed"

    def incompleted(self):
        self.status = "incompleted"

class task_manager():
    
    def __init__(self):
        self.task_list = []
        self.banner = "Task manager:\n"
    
    def clear(self):
        if os.name == 'nt':
            os.system("cls")
        else:  
            os.system("clear")
        print(self.banner)

    def add_task(self):
        self.clear()
        name = input("[+] Enter task name to add-> ")
        if name == "":
            self.clear()
            input("[!] You cannot add an empty task")
        for i in self.task_list:
            if i.name == name:
                self.clear()
                input(f"[+] Task {name} already exists.")
                return
        self.clear()
        self.task_list.append(task(name, "incomplete"))
        input(f"[+] Task {name} successfully.")

        
    def delete_task(self):
        self.clear()
        self.show_tasks()
        name = input("\n[+] Enter task name to remove->")
        for i in self.task_list:
            if i.name == name:
                self.task_list.remove(i)
                self.clear()
                input(f"[+] Task {name} successfully deleted.")
            else:
                self.clear()
            input(f"[!] Task {name} not exist.")
    
    def mark_as_completed(self):
        self.clear()
        self.show_tasks()
        name = input("\n[+] Enter task name to mark as completed-> ")
        for i in self.task_list:
            if i.name == name:
                i.status = "completed"
                self.clear()
                input(f"[+] Task {name} marked as completed.")
                return
        self.clear()
        input(f"[!] Task {name} not exist.")

    def mark_as_incompleted(self):
        self.clear()
        self.show_tasks()
        name = input("\n[+] Enter task name to mark as incompleted-> ")
        for i in self.task_list:
            if i.name == name:
                i.status = "incomplete"
                self.clear()
                input(f"[+] Task {name} marked as incompleted.")
        else:
            self.clear()
            input(f"[!] Task {name} not exist.")
    
    def show_tasks(self):
        self.clear()
        try:
            for task in self.task_list:
                print(f"* {task.name} -> {task.status}")
        except AttributeError:
            print("[!] You dont have tasks yet.")

    def save_tasks(self):
        self.clear()
        task_dict_list = []
        for i in self.task_list:
            task_dict = {"name": i.name, "status": i.status}
            task_dict_list.append(task_dict)
        with open("task_list.json", "w") as f:
            json.dump(task_dict_list, f, indent=4)
            input("[+] Tasks saved successfully.")

    def load_tasks(self):
        self.clear()
        try:
            with open("task_list.json", "r") as f:
                tasks = json.load(f)
                self.task_list = task_list = []
                for task_dict in tasks:
                    task_list.append(task(task_dict['name'], task_dict['status']))
                input("[+] Tasks loaded successfully.")
        except FileNotFoundError:
            input("[!] No saved tasks found.")
    
    def update_saved_tasks(self):
        self.clear()
        for i in self.task_list:
            task_dict_list = {"name": i.name, "status": i.status}
        with open("task_list.json", "w") as f:
            json.dump(task_dict_list, f, indent=4)
            input("[+] Tasks saved successfully.")
    
    def main(self, selection):
        self.selection = selection
        self.clear()
        if selection == "1":
            self.add_task()
        if selection == "2":
            self.delete_task()
        if selection == "3":
            self.mark_as_completed()
        if selection == "4":
            self.mark_as_incompleted()
        if selection == "5":
            self.show_tasks()
            input()
        if selection == "6":
            self.save_tasks()

task_mgr = task_manager()

menu = """
1) Add task
2) Delete task
3) Mark task as completed
4) Mark task as incompleted
5) Show tasks
6) Save tasks
"""

task_mgr.load_tasks()

while True:
    task_mgr.clear()
    selection = input(menu + "-> ")
    while selection not in ["1", "2", "3", "4", "5", "6"]:
        task_mgr.clear()
        selection = input(menu + "[!] Please select a valid option -> ")
    task_mgr.main(selection)

