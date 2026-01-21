
def add_task(new_task):
    if new_task in list_of_tasks:
        print("already in list please re enter a new task, no duplicates allowed")
    else:
        list_of_tasks.append(new_task)


def display_tasks():
    for tasks in list_of_tasks:
        print(tasks,"\n")


def delete_task(): 
    list_of_tasks.pop()



list_of_tasks=[]
choice=0
while choice!=4:
    print("\n 1. ad task")
    print("\n 2. view task")
    print("\n 3. delete task ")
    print("\n 4. exit task manager ")
    choice=int(input("\n enter choice now "))

    if choice==1:
        new_task=str(input("enter new task"))
        add_task(new_task)
        continue
    elif choice==2:
        display_tasks()
        continue
    elif choice==3:
        print("deleted most recent task successfully")
        delete_task()
        continue
    elif choice==4:
        print("exit successful ")
    break
