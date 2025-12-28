import functions
import FreeSimpleGUI as sg 

label = sg.Text("Type in a todo")
input = sg.InputText(tooltip="Enter todo")
addButton = sg.Button('Add')
exitButton = sg.Button("Exit")

layout = [[label],[input, addButton],[exitButton]]

window = sg.Window("To-Do App", layout)
window.read()
window.close()
