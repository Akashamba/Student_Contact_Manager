import PySimpleGUI as s
from back import *

col = "#343434"

def signup():
    sign_up_layout = [
        [s.Text("Enter Name         ", background_color=col), s.InputText("", key='name', size=(20,10))],
        [s.Text("Enter Username   ", background_color=col), s.InputText("", key='username', size=(20,10))],
        [s.Text("Enter Password   ", background_color=col), s.InputText("", key="password", password_char='*', size=(20,10))],
        [s.Text("Confirm Password", background_color=col), s.InputText("", key="cpassword", password_char='*',size=(20,10))],
        [s.Text("                                   ", key='msg', background_color=col)],
        [s.Button("Create Account", bind_return_key=True,   button_color=('white', 'black')), s.Button("Log In",   button_color=('white', 'black'))]
    ]

    sign_w = s.Window("Sign Up", sign_up_layout, resizable=1, background_color=col)

    while True:
        s_button, s_values = sign_w.Read()

        if s_button == "Create Account":
            if s_values['password'] == s_values['cpassword']:
                if len(s_values['password']) > 7:
                    if create_acc(s_values['name'], s_values['username'], encrypt(s_values['password'])):
                        sign_w.FindElement('msg').update("Account Created", text_color='green')
                    else:
                        sign_w.FindElement('msg').update("Username Taken", text_color='red')

                else:
                    sign_w.FindElement('msg').update("Password too short", text_color='red')
            else:
                sign_w.FindElement('msg').update("Passwords do not match",  text_color='red')

        if s_button == None:
            sign_w.Close()
            break


delete_acc("")
