import PySimpleGUI as s

col = "#343434"
student = []


def search():
    layout = [
        [s.Text("Student Contact Manager", size=(50,1), font='courier' '50', background_color=col, justification="left")],
        [s.Text("Enter Register Number", background_color=col)],
        [s.InputText("", key="reg"), s.Button("Search", button_color=("white", "black"))],
        [s.Listbox(student, size=(50, 5), key='box')]
    ]

    w=s.Window("Student Contact Manager", layout, background_color=col)
    button, values = w.Read()

# define search function to take reg number from textbox and display stud details
search()
