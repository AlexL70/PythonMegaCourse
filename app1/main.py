from PIL.ImImagePlugin import number

user_prompt = "Type add, edit, show or exit: "
todos = []
while True:
    userAction = input(user_prompt)
    match userAction.strip():
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            for item in todos:
                item = item
                print(item)
        case "edit":
            num = int(input("Number of the todo to edit: "))
            num -= 1
            print("You are editing", todos[num])
            newTodo = input("Enter a new value for the todo: ")
            todos[num] = newTodo
        case "exit":
            break
        case _unknown:
            print("Unknown command:", _unknown)
print("Good bye!")
