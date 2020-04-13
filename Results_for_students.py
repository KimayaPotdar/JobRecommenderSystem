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

def read_list_from_DB(name):
    print("Reading from DB")
    career_anchor = ['Technical/Functional competence','General Managerial competence','Autonomy/Independence',
                     'Security/Stability','Entrepreneurial Creativity','Service/Dedication to a cause',
                     'Pure Challenge','Lifestyle']
    strengths = []
    weakness = []
    query = "SELECT TF,GM,AU,SE,EC,SV,CH,LS FROM Responses where NAME='" + name +"'"
    curStu.execute(query)
    rows = curStu.fetchall()
    rows = list(rows[0])
    i = 0
    for element in rows:
        if element > 20:
            strengths.append(career_anchor[i])
        elif element < 11:
            weakness.append(career_anchor[i])
        i = i+1
    display_List(name,strengths,weakness)

def display_List(name,strengths,weakness):
    global root
    root = Tk()
    root.geometry('625x625')
    root.title('Candidate Results - BizInt')
    frame2 = Frame(root)
    frame2.pack()
    candidate="Candidate: " + name
    Profile = Label(frame2, text=candidate, font='Times 17').pack()
    l = Label(frame2,
              text="Following are your strengths",
              font='Times 17', fg='Blue')
    l.pack(side=TOP, pady=(30, 30))

    print(weakness)
    print(len(weakness))
    print(type(weakness))

    for row in strengths:
        Label(frame2,text=str(row), font='bold').pack()

    l = Label(frame2,
              text="Following are your areas of your improvement",
              font='Times 17', fg='Red')
    l.pack(side=TOP, pady=(30, 30))

    if len(weakness) != 0:
        for row in weakness:
            Label(frame2, text=str(row), font='bold').pack()
    else:
        print("empty")
        Label(frame2, text="No weakness we could detect. \n Keep improving on your strengths", font='bold').pack()
    b = Button(frame2, text="Back", command=exit, width=40, font='bold')
    b.pack(side=TOP, padx=(35, 100), pady=(30, 30))
        # Label(frame2,text=str(row), font='bold').pack()
    root.mainloop()

# def start():
#     read_list_from_DB("Jay Savla")

if __name__ == '__main__':
    start()