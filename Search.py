import PySimpleGUI as s
from back import search
import Log_In

col = "#343434"
student = []


def search_page():
    layout = [
        [s.Text("Student Contact Manager", font='courier' '50', background_color=col, justification="left"), s.Button("Log Out", button_color=("green", col), border_width=0)],
        [s.Text("Enter Register Number", background_color=col)],
        [s.Text("                    ", key="msg", background_color=col)],
        [s.InputText("", key="reg"), s.Button("Search", button_color=("white", "black"), bind_return_key=True)],
        [s.Listbox(student, size=(50, 6), key='box', background_color="white")],
        []
    ]

    w = s.Window("Student Contact Manager", layout, background_color=col, use_default_focus=False)

    while True:
        button, values = w.Read()

        if button == "Search":
            try:
                details = search(values["reg"])
                w.FindElement("reg").update("")
                w.FindElement("box").update(details)
                w.FindElement("msg").update("")
            except:
                w.FindElement("msg").update("Invalid Number", text_color="red")

        if button == "Log Out":
            w.Close()
            Log_In.login()
            break

        if button is None:
            w.Close()
            break
