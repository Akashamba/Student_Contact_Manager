import PySimpleGUI as s
from Sign_Up import signup
from back import *
from Search import search_page

def login():
    col = "#343434"

    login_layout = [
        [s.Text("Student Contact Manager", font='courier' '50', background_color=col, justification="left")],
        [s.Text("Username", background_color=col, ), s.InputText("", key='username',size=(20,10))],
        [s.Text("Password", background_color=col), s.InputText("", key="password", password_char='*', size=(20,10))],
        [s.Button("Login", bind_return_key=True, button_color=('white', 'black'))],
        [s.Text("                                                   ", key='msg', background_color=col)],
        [s.Text("Don't have an account?",background_color=col),s.Button("Sign Up",button_color=('green',col),border_width=0)]
    ]

    w = s.Window("Login", login_layout, resizable=1, background_color=col, element_justification="center")

    while True:
        button, values = w.Read()

        if button == "Login":
            if authenticate(values['username'], values['password']):
                w.FindElement('msg').update("Logging in...", text_color='green')
                w.Close()
                search_page()

            else:
                if values["password"] == "":
                    w.FindElement('msg').update("Password required", text_color='red')
                else:
                    w.FindElement('msg').update("Username or password is incorrect", text_color='red')

        if button == "Sign Up":
            w.Close()
            signup()

        if button is None:
            w.Close()
            break
