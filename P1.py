
tasks = []

while True:
    print("\n--- My Task List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks added yet.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        print("Thank you! Goodbye.")
        break

    else:
        print("Invalid choice. Please try again.")
