import functions
import PySimpleGUI as sg

label = sg.Text("Type in to-do.")
input_box = sg.InputText(tooltip="Enter to-do.", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=[45, 10]
                      )
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


window = sg.Window("My To-Do app",
                   layout=[[label],
                           [input_box],
                           [list_box],
                           [add_button, complete_button, exit_button]],
                   font=("Helvetica", 20))

while True:
    event, value = window.read()
    print(f'This is event -> {event}')
    print(f'This is value -> {value}')
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value["todo"]
            print(f'This is new_todo {new_todo}')
            todos.append(new_todo + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todos = functions.get_todos()
            editing_todo = value["todos"][0]
            todo_idx = todos.index(editing_todo)
            todos[todo_idx] = value["todo"] + "\n"
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Complete":
            todo_to_complete = value["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "todos":
            window["todo"].update(value=value["todos"][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
