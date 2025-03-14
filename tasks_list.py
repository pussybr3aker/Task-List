#Libs
import time; import os; import json

#Tasks lists
allTask = {}
incompletedTasks = []
completedTasks = []

#Banner
banner = """
                  _        _  _            
   _             | |      | |(_)       _   
 _| |_ _____  ___| |  _   | | _  ___ _| |_ 
(_   _|____ |/___) |_/ )  | || |/___|_   _)
  | |_/ ___ |___ |  _ (   | || |___ | | |_ 
   \__)_____(___/|_| \_)   \_)_(___/   \__)
                                           
"""

#Clear
def clear():
    os.system("cls")
    print(banner)

# Add a task
def addTask ():
    clear()
    newTask = input("What task do you want to add?\n-> ")
    if newTask in allTask:
        input(f"\nThe task \"{newTask}\" already exists.")
    else:
        allTask[newTask] = "incomplete"
        input(f"\nTask \"{newTask}\" successfully added.\n")

#Delete a task
def deleteTask():
    clear()
    if showAllTasks():
        deletedTask = input("\nWhich task do you want to delete?\n-> ")
        if deletedTask not in allTask:
            input(f"\nThe task \"{deletedTask}\" is not in the task list.")
        else:
            validation = input("\nAre you sure that you want to delete the task? (y/n)\n-> ")
            if validation == "y":
                del allTask[deletedTask]
                input(f"\nThe task \"{deletedTask}\" has been successfully eliminated.")
            else:
                input("\nTask not deleted.")

#Mark task as completed
def taskCompleted():
    clear()
    if showAllTasks():
        taskCompleted = input("\nWhich task do you want to mark as completed?\n-> ")
        if taskCompleted not in allTask:
            input(f"\nThe task \"{taskCompleted}\" is not in the task list.")
        else:
            allTask[taskCompleted] = "completed"
            input(f"\nThe task \"{taskCompleted}\" has been marked as completed successfully.")


#Mark task as incomplete
def taskIncompleted():
    clear()
    if showAllTasks():
        taskIncompleted = input("\nWhich task do you want to mark as incompleted?\n-> ")
        if taskIncompleted not in allTask:
            input(f"\nThe task \"{taskIncompleted}\" is not in the task list.")
        else:
            allTask[taskIncompleted] = "incomplete"
            input(f"\nThe task \"{taskIncompleted}\" has been marked as incompleted successfully")


#Ask for a option
def ask():
    clear()
    option = input("* Add a new task...............................(1)\n* Delete a task................................(2)\n* Mark a task as completed.....................(3)\n* Mark a task as incompleted...................(4)\n* Show tasks...................................(5)\n* Show incompleted tasks.......................(6)\n* Show completed tasks.........................(7)\n* Save data....................................(8)\n\n-> ")
    while option not in ["1", "2", "3", "4", "5","6","7","8"]:
        clear()
        print("* Add a new task...............................(1)\n* Delete a task................................(2)\n* Mark a task as completed.....................(3)\n* Mark a task as incompleted...................(4)\n* Show tasks...................................(5)\n* Show incompleted tasks.......................(6)\n* Show completed tasks.........................(7)\n* Save data....................................(8)\n")
        option = input("[!] Please choose a valid option.\n\n-> ")
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
            print(f"{i} -> {allTask[i]}")
        return True
    else:
        input("[!] You dont have tasks yet.")
        return False

#Show incompleted tasks
def showIncompletedTasks():
    clear()
    if showAllTasks:
        if incompletedTasks:
            print("Incompleted tasks:")
            iteration = 1
            for task in incompletedTasks:
                print(f"{iteration}) -> {task}")
                iteration = iteration + 1
            input()
        else:
            input("[!] You dont have incomplete tasks yet.")
    else:
        input("[!] You dont have tasks yet.")

#Show completed tasks
def showCompletedTasks():
    clear()
    if showAllTasks:
        if completedTasks:
            print("Completed tasks:")
            iteration = 1
            for task in completedTasks:
                print(f"{iteration}) -> {task}")
                iteration = iteration + 1
            input()
        else:
            input("[!] You dont have complete tasks yet.")
    else:
        input("[!] You dont have tasks yet.")

#Save data
def saveData(data):
    if data:
        with open("tasks.json", "w") as f:
            json.dump(data, f)
            clear()
            input("[+] Data saved successfully.")
    else:
        clear()
        input("[!] No data to store.")

#Load saved data
def loadData():
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        input("\n[!] No data found.")
        return ""

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
        showAllTasks()
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
allTask = loadData()

#Main loop
main()