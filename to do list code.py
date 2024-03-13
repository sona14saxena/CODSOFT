def toadd(t):
    with open('t.txt', 'a') as file:
        file.write(t + '\n')
    print("Added task: {t}")
def tolist():
    try:
        with open('t.txt', 'r') as file:
            t = file.readlines()
            for i, task in enumerate(t, start=1):
                print("{i}. {t.strip()}")
    except FileNotFoundError:
        print("No tasks found.")
def deleting(no):
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        with open('tasks.txt', 'w') as file:
            for i, task in enumerate(tasks, start=1):
                if i != no:
                    file.write(task)
        print("Deleted task {no}.")
    except FileNotFoundError:
        print("no existing tasks")

if __name__ == "__main__":
    while True:
        print("This is TO-DO LIST")
        print("1. add new task")
        print("2. list new task ")
        print("3. delete existing task")
        print("4. finsh editing ")
        n=int(input("enter the no if items you want to add to the list"))
        ch= input("Enter your choice by mentioning numbers from above options:")
        if ch == '1':
            t = input("Enter the task:")
            toadd(t)
        elif ch == '2':
            tolist()
        elif ch == '3':
            no = int(input("mention the no of the item you want to delete:"))
            deleting(no)
        elif ch == '4':
            break
        else:
            print("wrong choice input")
            
