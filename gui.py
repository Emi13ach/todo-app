import functions
import PySimpleGUI as sg

label = sg.Text("Type in to-do.")
input_box = sg.InputText(tooltip="Enter to-do.", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do app", layout=[[label], [input_box, add_button]], font=("Helvetica", 20))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value["todo"]
            todos.append(new_todo + "\n")
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
