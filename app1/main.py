user_prompt = "Type add <todo>, edit <number>, show, complete <number> or exit: "
with open("todos.txt", "r") as file:
    todos = file.readlines()
todos = [todo.strip('\n') for todo in todos] # remove linebreaks from todos
while True:
    userAction = input(user_prompt).strip()
    if userAction.startswith( "add"):
        todo = userAction[3:].strip()
        todos.append(f"{todo}")
        with open("todos.txt", 'w') as file:
            file.writelines([f"{todo}\n" for todo in todos])
    elif userAction == "show":
        for i, item in enumerate(todos):
            print(f"{i+1}. — {item}")
    elif userAction.startswith("edit"):
        strNum = userAction[4:].strip()
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
    elif userAction.startswith("complete"):
        strNum = userAction[8:].strip()
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
    elif userAction == "exit":
        break
    else:
        print("Unknown command:", userAction)
print("Good bye!")
