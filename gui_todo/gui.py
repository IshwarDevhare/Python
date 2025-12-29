import functions
import FreeSimpleGUI as sg 

label = sg.Text("Type in a todo")
input = sg.InputText(tooltip="Enter todo", key="todo")
addButton = sg.Button('Add')
exitButton = sg.Button("Exit")

layout = [[label],[input, addButton],[exitButton]]

font = ('Tahoma', 20)

window = sg.Window("To-Do App", layout, font=font)

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
