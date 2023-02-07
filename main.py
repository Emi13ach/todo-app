from functions import get_todos, write_todos
import time

now = time.strftime("%d-%b-%Y, %H:%M:%S")
print(f'It is {now}')

while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.title()
    print(" ".join(user_action.split(" ")[1:]))

    if user_action.startswith("Add") or user_action.startswith("New"):
        todo = " ".join(user_action.split(" ")[1:])
        todos = get_todos()
        todos.append(todo + "\n")
        write_todos(todos)

    elif user_action.startswith("Show"):
            todos = get_todos()
            for num, item in enumerate(todos):
                item  = item.strip("\n")
                print(f'{num + 1}. {item}')

    elif user_action.startswith("Edit"):
        try:
            number = int(" ".join(user_action.split(" ")[1:]))
            todos = get_todos()
            new_todo = input("Enter a new todo: ").title() +"\n"
            todos[number - 1] = new_todo
            write_todos(todos)

        except ValueError as err:
            print(f'Your command is not valid - {err}.')
            continue

    elif user_action.startswith("Complete"):
        try:
            complete_num = int(" ".join(user_action.split(" ")[1:]))
            todos = get_todos()
            todos.pop(complete_num - 1)
            write_todos(todos)

        except (ValueError, IndexError) as err:
            print(f'Your command is not valid - {err}.')
            continue

    elif user_action.startswith("Exit"):
        break

    else:
        print("Command is not valid")
