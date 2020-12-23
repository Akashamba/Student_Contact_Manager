import sqlite3
from passlib.hash import sha256_crypt
import time


def encrypt(text):
    return sha256_crypt.encrypt(text)


def verify(encrypted, entry):
    return sha256_crypt.verify(entry, encrypted)


def clean(list):
    return list[0][0]


db = sqlite3.connect('contacts_db')
c = db.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Accounts(Name TEXT, Username TEXT PRIMARY KEY,Password TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS Student(Name TEXT, Register_Number INTEGER PRIMARY KEY, Address TEXT, Contact_Number INTEGER, 
                                    Email_ID TEXT, Parent_Contact_Number INTEGER)''')
db.commit()


def create_acc(name, username, password):
    try:
        c.execute('''INSERT into Accounts(Name, Username, Password) VALUES(?,?,?) ''', (name, username, password))
        db.commit()
        return True
    except:
        return False


def delete_acc(username):
    c.execute('''delete from Accounts where Username=?''', (username,))
    db.commit()


def authenticate(username, password):
    try:
        c.execute('''select Username from Accounts where Username=?''', (username,))
        x = clean(c.fetchall())
        c.execute('''select Password from Accounts where Username=?''', (username,))
        y = clean(c.fetchall())
        db.commit()
        if username == x and verify(y, password):
            return True
    except:
        return False


def search(reg):
    details = []
    columns = ["Name:", "Register Number:", "Address:", "Contact Number:", "Email Id:", "Parent's Contact Number:"]
    c.execute('''select * from Student where Register_Number=?''', (reg,))
    x = c.fetchall()
    for i in range(len(x[0])):
            details.append(str(columns[i]) +" "+ str(x[0][i]))
    return details


# search(311018104001)