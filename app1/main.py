user_prompt = "Type add, show or exit: "
todos = []
while True:
    userAction = input(user_prompt)
    match userAction:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            print(todos)
        case "exit":
            break
print("Good bye!")
