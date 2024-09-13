user_prompt = "Enter a todo: "
todos = []
while True:
    todo = input(user_prompt)
    todo = todo.capitalize()
    todos.append(todo)
    print(todos)
