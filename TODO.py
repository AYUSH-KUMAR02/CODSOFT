def menu():
    print("\nTo-Do List")
    print("1. View")
    print("2. Add")
    print("3. Remove")
    print("4. Exit")

def view(tasks):
    if not tasks:
        print("\nNo tasks.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add(tasks):
    task = input("\nTask: ")
    tasks.append(task)
    print(f"Added: {task}")

def remove(tasks):
    view(tasks)
    if tasks:
        try:
            num = int(input("\nRemove #: "))
            if 1 <= num <= len(tasks):
                task = tasks.pop(num - 1)
                print(f"Removed: {task}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a number.")

def main():
    tasks = []
    while True:
        menu()
        choice = input("Choice (1-4): ")
        if choice == '1':
            view(tasks)
        elif choice == '2':
            add(tasks)
        elif choice == '3':
            remove(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()