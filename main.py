import PySimpleGUI as s
from Log_In import login
from Sign_Up import signup

col = "#343434"

layout = [
    [s.Text("Student Contact Manager", background_color=col, justification="left")],
    [s.Text("", background_color=col)],
    [s.Button("Log In", button_color=('white', 'black')), s.Button("Sign Up", button_color=('white', 'black'))]
]
w = s.Window("Student Contact Manager", layout, background_color=col, use_default_focus=False, element_justification="center")
while True:
    button, values = w.Read()

    if button == "Log In":
        w.Close()
        login()
        break

    if button == "Sign Up":
        w.Close()
        signup()
        break

    if button is None:
        w.Close()
        break
