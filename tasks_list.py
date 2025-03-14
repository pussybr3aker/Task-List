#Made by Donerkalash

#Libs
import time; import os; import json; from colorama import Fore; import curses

#Tasks lists
allTask = {}
incompletedTasks = []
completedTasks = []

#Banner
banner = Fore.RED + """
                  _        _  _            
   _             | |      | |(_)       _   
 _| |_ _____  ___| |  _   | | _  ___ _| |_ 
(_   _|____ |/___) |_/ )  | || |/___|_   _)
  | |_/ ___ |___ |  _ (   | || |___ | | |_ 
   \__)_____(___/|_| \_)   \_)_(___/   \__)
                                           
""" + Fore.RESET

#Clear
def clear():
    os.system("cls")
    print(banner)

# Add a task
def addTask ():
    clear()
    newTask = input(f"What task do you want to add?\n{Fore.GREEN}-> "+Fore.RESET)
    if newTask in allTask:
        input(f"\n{Fore.YELLOW}[!]{Fore.RESET}The task {Fore.YELLOW+newTask+Fore.RESET} already exists.")
    elif newTask == "":
        input(f"{Fore.RED}[!]{Fore.RESET} You can't add an empty task.")
    else:
        allTask[newTask] = "incomplete"
        input(f"\n{Fore.GREEN}[+]{Fore.RESET} Task {Fore.GREEN+newTask+Fore.RESET} successfully added.\n")

#Delete a task
def deleteTask():
    clear()
    if showAllTasks():
        deletedTask = input(f"\nWhich task do you want to delete?\n{Fore.GREEN}-> "+Fore.RESET)
        if deletedTask not in allTask:
            input(f"\nThe task {Fore.YELLOW+deletedTask+Fore.RESET} is not in the task list.")
        else:
            validation = input(f"\n{Fore.YELLOW}[!]{Fore.RESET} Are you sure that you want to delete the task? (y/n)\n{Fore.GREEN}-> "+Fore.RESET)
            if validation == "y":
                del allTask[deletedTask]
                input(f"\n{Fore.GREEN}[+]{Fore.RESET} The task {Fore.GREEN+deletedTask+Fore.RESET} has been successfully eliminated.")
            else:
                input(f"\n{Fore.RED}[!]{Fore.RESET} Task not deleted.")

#Mark task as completed
def taskCompleted():
    clear()
    if showAllTasks():
        taskCompleted = input(f"\nWhich task do you want to mark as completed?\n{Fore.GREEN}-> "+Fore.RESET)
        if taskCompleted not in allTask:
            input(f"\n{Fore.YELLOW}[!]{Fore.RESET} The task {Fore.YELLOW+taskCompleted+Fore.RESET} is not in the task list.")
        else:
            allTask[taskCompleted] = "completed"
            input(f"\n{Fore.GREEN}[+]{Fore.RESET} The task {Fore.GREEN+taskCompleted+Fore.RESET} has been marked as completed successfully.")


#Mark task as incomplete
def taskIncompleted():
    clear()
    if showAllTasks():
        taskIncompleted = input(f"\nWhich task do you want to mark as incompleted?\n{Fore.GREEN}-> "+Fore.RESET)
        if taskIncompleted not in allTask:
            input(f"\n{Fore.YELLOW}[!]{Fore.RESET} The task {Fore.YELLOW+taskIncompleted+Fore.RESET} is not in the task list.")
        else:
            allTask[taskIncompleted] = "incomplete"
            input(f"\n{Fore.GREEN}[+]{Fore.RESET} The task {Fore.GREEN+taskIncompleted+Fore.RESET} has been marked as incompleted successfully")


#Ask for a option
def ask():
    clear()
    option = input(f"{Fore.GREEN}*{Fore.RESET} Add a new task...............................(1)\n{Fore.GREEN}*{Fore.RESET} Delete a task................................(2)\n{Fore.GREEN}*{Fore.RESET} Mark a task as completed.....................(3)\n{Fore.GREEN}*{Fore.RESET} Mark a task as incompleted...................(4)\n{Fore.GREEN}*{Fore.RESET} Show tasks...................................(5)\n{Fore.GREEN}*{Fore.RESET} Show incompleted tasks.......................(6)\n{Fore.GREEN}*{Fore.RESET} Show completed tasks.........................(7)\n{Fore.GREEN}*{Fore.RESET} Save data....................................(8)\n\n-> "+Fore.GREEN)
    while option not in ["1", "2", "3", "4", "5","6","7","8"]:
        clear()
        print(f"{Fore.GREEN}*{Fore.RESET} Add a new task...............................(1)\n{Fore.GREEN}*{Fore.RESET} Delete a task................................(2)\n{Fore.GREEN}*{Fore.RESET} Mark a task as completed.....................(3)\n{Fore.GREEN}*{Fore.RESET} Mark a task as incompleted...................(4)\n{Fore.GREEN}*{Fore.RESET} Show tasks...................................(5)\n{Fore.GREEN}*{Fore.RESET} Show incompleted tasks.......................(6)\n{Fore.GREEN}*{Fore.RESET} Show completed tasks.........................(7)\n{Fore.GREEN}*{Fore.RESET} Save data....................................(8)")
        option = input(f"\n{Fore.YELLOW}[!]{Fore.RESET} Please choose a valid option.\n\n-> "+Fore.GREEN)
    return option

#Update incompleted and completedtasks
def updateTasks():
    global incompletedTasks
    global completedTasks
    incompletedTasks = []
    completedTasks = []
    for task, status in allTask.items():
        if status == "incomplete":
            incompletedTasks.append(task)
        elif status == "completed":
            completedTasks.append(task)

#Show tasks
def showAllTasks():
    clear()
    if  allTask:
        print("All tasks:")
        for i in allTask:
            print(f"{Fore.GREEN+"* "+Fore.RESET+i} -> {allTask[i]}")
        return True
    else:
        input(f"{Fore.RED}[!]{Fore.RESET} You dont have tasks yet.")
        return False

#Show incompleted tasks
def showIncompletedTasks():
    clear()
    if incompletedTasks:
        print("Incompleted tasks:")
        for task in incompletedTasks:
            print(f"{Fore.GREEN}*{Fore.RESET} {task}")
        input()
    else:
        input(f"{Fore.RED}[!]{Fore.RESET} You dont have incomplete tasks yet.")

#Show completed tasks
def showCompletedTasks():
    clear()
    if completedTasks:
        print("Completed tasks:")
        for task in completedTasks:
            print(f"{Fore.GREEN}*{Fore.RESET} {task}")
        input()
    else:
        input(f"{Fore.RED}[!]{Fore.RESET} You dont have complete tasks yet.")

#Save data
def saveData(data):
    if data:
        with open("tasks.json", "w") as f:
            json.dump(data, f)
            clear()
            input(f"{Fore.GREEN}[+]{Fore.RESET} Data saved successfully.")
    else:
        clear()
        input(f"{Fore.RED}[!]{Fore.RESET} No data to store.")

#Load saved data
def loadData():
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
            return(loadedData)
    except FileNotFoundError:
        clear()
        input(f"\n{Fore.YELLOW}[!]{Fore.RESET} No data found.")
        return False

#Print menu
def menu():
    updateTasks()
    option = ask()
    if option == "1":
        addTask()
    elif option == "2":
        deleteTask()
    elif option == "3":
        taskCompleted()
    elif option == "4":
        taskIncompleted()
    elif option == "5":
        if showAllTasks():
            input()
    elif option == "6":
        showIncompletedTasks()
    elif option == "7":
        showCompletedTasks()
    elif option == "8":
        saveData(allTask)

#Main code
def  main():
    while True:
        clear()
        menu()
        clear()

#Load data
loadedData = loadData()
if loadedData:
    allTask = loadedData
else:
    pass

#Main loop
main()