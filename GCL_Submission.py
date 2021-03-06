import sqlite3
import pandas as pd
import os
import io
import tkinter

from PIL import ImageTk, Image
from PIL import Image, ImageOps

import PIL.Image

import Rendering_quiz
from Rendering_quiz import *

import Results_for_Company
from Results_for_Company import *

import Results_for_students
from Results_for_students import *

from tkinter import *
from tkinter import simpledialog


def show_Candidate_Results():
    root = Tk()
    root.geometry('625x625')
    root.title('EMPLOYER Login - BizInt')
    frame2 = Frame(root)
    frame2.pack()
    l = Label(frame2, text="Following are your company profiles.\n Click on the Profile to know the suitable list of candidates",
              font='Times 15')
    b = Button(frame2, text="Teacher", command=show_Teacher_Results, width=40, font='bold')
    c = Button(frame2, text="Animator", command=show_Animator_Results, width=40, font='bold')
    d = Button(frame2, text="News Anchor", command=show_Anchor_Results, width=40, font='bold')
    e = Button(frame2, text="Tourist Guide", command=show_Guide_Results, width=40, font='bold')
    l.pack(side=TOP,pady=(10, 30))
    c.pack(side=TOP, padx=(35, 100), pady=(50, 30))
    b.pack(side=TOP, padx=(35, 100), pady=(30, 30))
    d.pack(side=TOP, padx=(35, 100), pady=(30, 30))
    e.pack(side=TOP, padx=(35, 100), pady=(30, 30))
    root.mainloop()

def show_Test_Results():
    global u_cand
    print("Show Results")
    read_list_from_DB(u_cand)

def display_questionnaire():
    root = Tk()
    root.geometry('625x625')
    root.title('Candidate Login - BizInt')
    frame2= Frame(root)
    frame2.pack()
    b = Button(frame2, text="View Test Results", command=show_Test_Results, width=20, font='bold')
    c = Button(frame2, text="Start Personality and Interest Mapping Test", command=start_quiz, width=150, font='bold')
    c.pack(side=TOP,padx=(35, 100),pady=(100, 30))
    b.pack(side=TOP,padx=(35, 100),pady=(30, 30))
    root.mainloop()

def candidate_login():
    global u_cand
    u_cand = simpledialog.askstring("CANDIDATE Login", "Please enter your user name: ")
    cnx = sqlite3.connect(r'C:/Users/kimaya pc/PycharmProjects/SmartIndiaHackathon/venv/databases/Job_Recommender_database.db')
    df = pd.read_sql_query("SELECT Username FROM Candidate", cnx)
    val = df[df['Username'].str.match(u_cand)]
    isempty = val.empty
    if isempty == True:
        message = Label(text='Incorrect Username . Try again! \n You may not yet be registered as a candidate! Sign Up first', fg='Red')
        message.pack()
        return
    else:
        print('Thank you! You shall be redirected to password authentication Page')
        # val.drop(df.index, inplace=True)
        p_emp = simpledialog.askstring("Candidate Login", "Please enter your password: ")
        df = pd.read_sql_query("SELECT Password FROM Candidate", cnx)
        val1 = df[df['Password'].str.match(p_emp)]
        isempty1 = val1.empty
        if isempty1 == True:
            # print('Incorrect Password! Please Contact Help Desk!')
            message = Label(text='Incorrect Password. Try again!', fg='Red')
            message.pack()
        else:
            print('Thank you! Your Homepage is being loaded!')
            # val1.drop(df.index, inplace=True)
            display_questionnaire()
    return 0



def employer_login():
    u_empr = simpledialog.askstring("EMPLOYER Login", "Please enter your user name: ")
    cnx = sqlite3.connect(r'C:/Users/kimaya pc/PycharmProjects/SmartIndiaHackathon/venv/databases/Job_Recommender_database.db')
    df = pd.read_sql_query("SELECT Username FROM Employer", cnx)
    val2 = df[df['Username'].str.match(u_empr)]
    isempty = val2.empty
    if isempty == True:
        print('You are not yet registered as an employer! Please contact Help desk')
        message = Label(
            text='Incorrect Username . Try again! \n You may not yet be as an employer! Please contact Help desk',
            fg='Red')
        message.pack()
    else:
        print('Thank you! You shall be redirected to password authentication Page')
        val2.drop(df.index, inplace=True)
        p_empr = simpledialog.askstring("EMPLOYER Login", "Please enter your password: ")
        df = pd.read_sql_query("SELECT Password FROM Employer", cnx)
        val3 = df[df['Password'].str.match(p_empr)]
        isempty1 = val3.empty
        if isempty1 == True:
            print('Incorrect Password! Please Contact Help Desk!')
            message = Label(text='Incorrect Password. Try again!', fg='Red')
            message.pack()
        else:
            print('+++Thank you! Your Homepage is being loaded!')
            val3.drop(df.index, inplace=True)
            show_Candidate_Results()
    return 0


def Startup_Screen():
    """Generate a pop-up window for special messages."""
    root = Tk()
    root.title('BizInt - The Job Recommender System')
    w = 500  # popup window width
    h = 500  # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    frame1 = Frame(root)
    frame1.pack()
    img = PhotoImage(file="BizInt_logo.png")
    Label(frame1, image=img).pack(side=TOP)


    m = "Welcome to BizInt - The Job Recommender System \n Initiative by the Government of Puducherry"
    w = Label(frame1, text=m, width=120, height=10, font='Times 15', padx=20, fg='Blue')
    w.pack(side=TOP)
    b = Button(frame1, text="CANDIDATE LOGIN", command=candidate_login, width=20, font='bold')
    c = Button(frame1, text="EMPLOYER LOGIN", command=employer_login, width=20, font='bold')
    b.pack()
    c.pack()
    # root.destroy()
    mainloop()


if __name__ == '__main__':
    Startup_Screen()