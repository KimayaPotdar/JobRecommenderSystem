import sqlite3
import tkinter
from tkinter import *

connStu = None
try:
    connStu = sqlite3.connect("Responses.db")
except Error as e:
    print(e)

curStu = connStu.cursor()
curProff = connStu.cursor()

def exit():
    global root
    root.destroy()

def read_list_from_DB(profession,flag):
    print("Reading from DB")
    curStu.execute("SELECT NAME  FROM Responses where " + flag +" = 1")
    rows = curStu.fetchall()
    print("Students which are suitable for " + profession +"'s Job: ")
    for row in rows:
        print('{0}'.format(row[0]))
    display_List(rows,profession)

def display_List(rows,profession):
    global root

    root = Tk()
    root.geometry('625x625')
    root.title('Candidate List - BizInt')
    frame2 = Frame(root)
    frame2.pack()
    profession="Profile: " + profession
    Profile = Label(frame2, text=profession, font='Times 17').pack()
    l = Label(frame2,
              text="Following is the list of suitable candidates",
              font='Times 15')
    l.pack(side=TOP, pady=(10, 30))
    for row in rows:
        row = row[0]
        Label(frame2,text=str(row), font='bold 15').pack()
    b = Button(frame2, text="Back", command=exit, width=40, font='bold')
    b.pack(side=TOP, padx=(35, 100), pady=(30, 30))
    root.mainloop()

def show_Teacher_Results():
    print("def show_Teacher_Results")
    profession = "Teacher"
    flag = "Is_Teacher"
    read_list_from_DB(profession,flag)


def show_Animator_Results():
    print("def show_Animator(_Results")
    profession = "Animator"
    flag = "Is_Animator"
    read_list_from_DB(profession,flag)

def show_Anchor_Results():
    print("def show_Anchor_Results")
    profession = "Anchor"
    flag = "Is_Anchor"
    read_list_from_DB(profession,flag)

def show_Guide_Results():
    print("def show_Guide_Results")
    profession = "Tourist Guide"
    flag = "Is_Tourist"
    read_list_from_DB(profession,flag)