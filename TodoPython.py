#sys module
import sys

#os module
import os

#creating json file and fetching
import json

if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as file:
        task_storage = json.load(file)
else :
    task_storage = {
        "name" : "Tasks",
        "storage" : [],
        "storage_done" : []
}

#welcome message
print('Welcome to To-do program, this program allows you to manage and save your tasks, select one of the options below to continue...')

#option selector

while True :
    print("""

(1) View Saved Tasks
(2) Add Task
(3) Delete a Task
(4)Mark Task as done
(5) View completed tasks
(6) Exit program

""")

    user = input('Select an option - ')

#flow control and logic
    if user == '1':
        if len(task_storage["storage"]) == 0:
            print('----------no tasks saved----------')
        elif len(task_storage["storage"]) != 0:
            print('------------------------------------------------------------------------')
            print(task_storage["storage"])
            print('------------------------------------------------------------------------')
        
    elif user == '2':
        t_add = input('Enter Task - ')
        task_storage["storage"].append(t_add)
        with open ("tasks.json" , "w") as file:
            json.dump(task_storage , file , indent = 4)
        print('------------task added successfully----------')
        
    elif user == '3':
        tIndex = input('Which Task do you want to delete(Enter the index number) - ')
        del task_storage["storage"][int(tIndex)-1]
        with open ("tasks.json" , "w") as file:
            json.dump(task_storage, file, indent=4)
        print('-------------task deleted successfully------------')

    elif user == '4':
        DoneTask = input('Enter the task you wish to mark as done(Enter the index number) - ')
        if int(DoneTask) < 0 or int(DoneTask) > len(task_storage["storage"]) :
                print('----------------Not a valid index number--------------')
        else :
            if "storage_done" not in task_storage:
                task_storage["storage_done"] = []
            task_storage["storage_done"].append(task_storage["storage"][int(DoneTask)-1])
            del task_storage["storage"][int(DoneTask)-1]
            with open ("tasks.json" , "w") as file :
                json.dump(task_storage, file, indent=4)
            print('----------Task has been marked as done-----------')
        
    elif user == '5':
        if len(task_storage["storage_done"]) == 0:
            print('------------------no tasks have been completed----------------')
        if len(task_storage["storage_done"]) != 0:
            print('------------------------------------------------------------------------')
            print(task_storage["storage_done"])
            print('------------------------------------------------------------------------')
                 
    elif user == '6':
        print('Thanks for using the program! have a good day ahead.')
        break

        
        
        
