user_prompt = "Type add, edit, show, complete or exit: "
with open("todos.txt", "r") as file:
    todos = file.readlines()
todos = [todo.strip('\n') for todo in todos] # remove linebreaks from todos
while True:
    userAction = input(user_prompt)
    match userAction.strip():
        case "add":
            todo = input("Enter a todo: ").strip()
            todos.append(f"{todo}")
            with open("todos.txt", 'w') as file:
                file.writelines([f"{todo}\n" for todo in todos])
        case "show":
            for i, item in enumerate(todos):
                print(f"{i+1}. — {item}")
        case "edit":
            strNum = input("Number of the todo to edit: ")
            if not strNum.isnumeric():
                print("Not an integer number:", strNum)
                continue
            num = int(strNum) - 1
            if num < 0 or num >= len(todos):
                print("The number you entered is out of range!")
                continue
            print(f"You are editing \"{todos[num]}\"")
            newTodo = input("Enter a new value for the todo: ").strip()
            todos[num] = newTodo
            with open("todos.txt", 'w') as file:
                file.writelines([f"{todo}\n" for todo in todos])
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
            print(f"\"{deleted}\" todo has been deleted.")
            with open("todos.txt", 'w') as file:
                file.writelines([f"{todo}\n" for todo in todos])
        case "exit":
            break
        case _unknown:
            print("Unknown command:", _unknown)
print("Good bye!")
