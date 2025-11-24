tasks = [] 
task_id = 1 

def add_task(title):
    global task_id
    priority = int(input("Enter priority (1=High, 2=Medium, 3=Low): "))
    task = {
    "id": task_id,
    "title": title,
    "status": "pending",
    "priority": priority,
    "completed_day":None
    }
    tasks.append(task)
    task_id += 1
    print("Task added successfully")


def view():
    if not tasks:
        print("No tasks found")
        return

    print("      TASK LIST ")
    for t in tasks:
        print("ID: ",t['id'],"        ",t['title'],"        Status: ",t['status'],"       Priority: ",t['priority'])


def complete(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "completed"
            print("Task marked as completed")
            return
    print("Task ID not found")


def delete(task_id):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            print("Task deleted")
            return
    print("Task ID not found")


def calculate_stats():
    total = len(tasks)
    completed = sum(1 for t in tasks if t["status"] == "completed")
    if total == 0: rate = 0
    else: rate = round((completed / total) * 100)
    print("      PRODUCTIVITY REPORT ")
    print("Total Tasks       : ",total)
    print("Completed Tasks   : ",completed)
    print("Completion Rate   : ",rate,"%")


def filter(status):
    found = False
    for t in tasks:
        if t["status"] == status:
            found = True
            print("ID: ",t['id'],"        ",t['title'],"        ",status)
    if not found:
        print("No ",status," tasks found.")


def task_by_status(status):
    found = False
    for t in tasks:
        if t["status"] == status:
            if not found:
                print("\n   ",status.upper()," TASKS")
                found = True
            pri_text = "High" if t["priority"] == 1 else ("Medium" if t["priority"] == 2 else "Low")
            print("ID: ",t['id'],"        Title: ",t['title'],"         Priority: ",{pri_text})
    if not found:
        print("No ",status," tasks found.")
    else:
        print()


def edit(task_id):
    for t in tasks:
        if t["id"] == task_id:
            new = input("New title (leave empty to keep): ")
            if new != "":
                t["title"] = new
            p = input("New priority (1/2/3, leave empty to keep): ")
            if p.isdigit() and int(p) in (1,2,3):
                t["priority"] = int(p)
            print("Task updated")
            return
    print("Task ID not found")


def show_menu():
    print("\n      TASK MANAGEMENT APP")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. View Productivity Statistics")
    print("6. View Pending Tasks")
    print("7. View Completed Tasks")
    print("8. Edit Task")
    print("9. Exit")


while True:
    show_menu()
    option = input("Enter your choice: ")
    if option== "1":
        title= input("Enter task title: ")
        add_task(title)

    elif option== "2":
        view()

    elif option== "3":
        tid= int(input("Enter task ID: "))
        complete(tid)

    elif option== "4":
        tid= int(input("Enter task ID to delete: "))
        delete(tid)

    elif option== "5":
        calculate_stats()

    elif option== "6":
        task_by_status("pending")

    elif option== "7":
        task_by_status("completed")

    elif option=="8":
        edit_id = int(input("Enter the ID of the task you want to edit"))
        edit(edit_id)
    
    elif option== "9":
        print("goodbye")
        break

    else:
        print("Invalid choice. Try again.")