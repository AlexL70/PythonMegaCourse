FILE_PATH = 'todos.txt'

def get_todos(filePath=FILE_PATH) -> list[str]:
    with open(filePath, "r") as file:
        todo_list = file.readlines()
    return [todo_el.strip('\n') for todo_el in todo_list] # remove linebreaks from todos


def write_todos(todo_list: list[str], filePath=FILE_PATH):
    with open(filePath, 'w') as file:
        file.writelines([f"{todo_el}\n" for todo_el in todo_list])


user_prompt = "Type add/new <todo>, edit <number>, show, complete <number> or exit: "
todos = get_todos()
while True:
    userAction = input(user_prompt).strip()
    if userAction.startswith( "add") or userAction.startswith("new"):
        todo = userAction[3:].strip()
        todos.append(f"{todo}")
        write_todos(todos)
    elif userAction == "show":
        for i, item in enumerate(todos):
            print(f"{i+1}. — {item}")
    elif userAction.startswith("edit"):
        try:
            strNum = userAction[4:].strip()
            num = int(strNum) - 1
            print(f"You are editing \"{todos[num]}\"")
            newTodo = input("Enter a new value for the todo: ").strip()
            todos[num] = newTodo
            write_todos(todos)
        except (ValueError, IndexError):
            print("Bad command. After \"edit\" you should enter non-negative number from the list.")
            continue
    elif userAction.startswith("complete"):
        try:
            strNum = userAction[8:].strip()
            num = int(strNum) - 1
            deleted = todos.pop(num)
            print(f"\"{deleted}\" todo has been deleted.")
            write_todos(todos)
        except (ValueError, IndexError):
            print("Bad command. After \"complete\" you should enter non-negative number from the list.")
            continue
    elif userAction == "exit":
        break
    else:
        print("Unknown command:", userAction)
print("Good bye!")
