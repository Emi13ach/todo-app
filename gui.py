import functions
import PySimpleGUI as sg
import time
import os

BUTTON_SIZE = 10

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("BrownBlue")

clock = sg.Text("", key="clock")
label = sg.Text("Type in to-do.")
input_box = sg.InputText(tooltip="Enter to-do.", key="todo")
add_button = sg.Button("Add", size=BUTTON_SIZE)
list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=[45, 10]
                      )
edit_button = sg.Button("Edit", size=BUTTON_SIZE)
complete_button = sg.Button("Complete", size=BUTTON_SIZE)
exit_button = sg.Button("Exit", size=BUTTON_SIZE)


window = sg.Window("My To-Do app",
                   layout=[[label, clock],
                           [input_box],
                           [list_box],
                           [add_button, edit_button, complete_button, exit_button]],
                   font=("Helvetica", 20))

while True:
    event, value = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%d-%m-%Y  %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value["todo"]
            print(f'This is new_todo {new_todo}')
            todos.append(new_todo + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todos = functions.get_todos()
                editing_todo = value["todos"][0]
                todo_idx = todos.index(editing_todo)
                todos[todo_idx] = value["todo"] + "\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 18))
        case "Complete":
            try:
                todo_to_complete = value["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 18))
        case "todos":
            window["todo"].update(value=value["todos"][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
