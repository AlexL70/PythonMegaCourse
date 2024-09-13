user_prompt = "Type add, show or exit: "
todos = []
while True:
    userAction = input(user_prompt)
    match userAction.strip():
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            for item in todos:
                item = item.title()
                print(item)
        case "exit":
            break
        case _unknown:
            print("Unknown command:", _unknown)
print("Good bye!")
