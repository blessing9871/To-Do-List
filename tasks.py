def main():
   while True:
       choice = input("Choose : 1 = Add task, 2 = View Task, 3 = Delete Task, 4 = Exit")
       if choice == "1":
           add_task()
       elif choice == "2":
           view_task()
       elif choice == "3":
           delete_task()
       elif choice == "4":
           break
       else:
           print("Invalid Input")
           break


# function to add a task
def add_task():
    task= input("task:")
    with open("tasks.txt", "a") as file:
        with open("tasks.txt", "r") as f:
            lines = f.readlines()
            number = len(lines) + 1
        file.write(f"{number}. {task}\n")
    print(f"Task added: {number}. {task}")

#function to view a task
def view_task():
    with open("tasks.txt", "r") as file:
        lines=file.readlines()
        for line in lines:
            print(line.strip())

#function to delete task
def delete_task():
    with open("tasks.txt", "r") as file:
        lines = file.readlines()
    if not lines:
        print("No task to delete!")
        return
    
    view_task()
    task_to_delete = input("Enter the number of the task to delete:")

    new_lines=[]
    found = False
    for line in lines:
        if not line.startswith(task_to_delete + "."):
            new_lines.append(line)
        else:
            found = True
    if not found:
        print(f"No task with number{task_to_delete} found")
        return
    
    with open("tasks.txt", "w") as file:
        for i, line in enumerate(new_lines, start=1):
            parts = line.split(".",1)
            if len(parts) == 2:
                tasks_text=parts[1].strip()
            else:
                tasks_text=parts[0].strip()
            file.write(f"{i}.{tasks_text}\n")
        print(f"task{task_to_delete} deleted successfully!!!")


main()
