user_prompt = "Type add, edit, show, complete or exit: "
file = open("todos.txt", "r")
todos = file.readlines()
file.close()
while True:
    userAction = input(user_prompt)
    match userAction.strip():
        case "add":
            todo = input("Enter a todo: ").strip()
            todos.append(f"{todo}\n")
            file = open("todos.txt", 'w')
            file.writelines(todos)
            file.close()
        case "show":
            for i, item in enumerate(todos):
                print(f"{i+1}. — {item}", end='')
        case "edit":
            strNum = input("Number of the todo to edit: ")
            if not strNum.isnumeric():
                print("Not an integer number:", strNum)
                continue
            num = int(strNum) - 1
            if num < 0 or num >= len(todos):
                print("The number you entered is out of range!")
                continue
            print("You are editing", todos[num])
            newTodo = input("Enter a new value for the todo: ").strip()
            todos[num] = newTodo
            file = open("todos.txt", 'w')
            file.writelines(todos)
            file.close()
        case "complete":
            strNum = input("Number of the todo to complete (delete): ")
            if not strNum.isnumeric():
                print("Not an integer number:", strNum)
                continue
            num = int(strNum) - 1
            if num < 0 or num >= len(todos):
                print("The number you entered is out of range!")
                continue
            deleted = todos.pop(num)
            print(f"'{deleted}' todo has been deleted.")
            file = open("todos.txt", 'w')
            file.writelines(todos)
            file.close()
        case "exit":
            break
        case _unknown:
            print("Unknown command:", _unknown)
print("Good bye!")
