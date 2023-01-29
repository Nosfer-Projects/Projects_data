import random
from tkinter import *
import tkinter.font as tkFont
import psycopg2 as pg2


PASSWORD = 'Your Password to SQL'

def clear_tabs ():
    #Clears all data that has been written from the table
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    email_entry.delete(0, END)
    date_entry.delete(0, END)
    project_entry.delete(0, END)
    hour_entry.delete(0, END)
    new_feature_entry.delete(0, END)
    comments_entery.delete("1.0", END)


def add():
    #Adds data entered in the program to the SQL server after connection to it
    name =first_name_entry.get()
    surname = last_name_entry.get()
    mail= email_entry.get()
    date= date_entry.get()
    project=project_entry.get()
    hour= hour_entry.get()
    feat= new_feature_entry.get()
    com= comments_entery.get("1.0",END)

    if name == "" or surname == "" or mail == ""\
        or date =="" or project =="" or hour==""\
        or feat == "" or com=="":
        messagebox.showwarning(title = "Error", message= "Please fill all fields! ")
    else:
        #If all fields are filled program connect to database and put all data to table in PostgreSQL

        conn = pg2.connect(database='name_of_database', user='your_user_name',password=PASSWORD, host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute(f"INSERT INTO project (first_name, last_name, email, project, hours, new_feature, short_description, date_of_change) VALUES ('{name}', '{surname}', '{mail}', '{project}', '{hour}', '{feat}', '{com}','{date}')")
        conn.commit()
        clear_tabs()

    cur.close()
    conn.close()
    print("PostgreSQL connection is closed")






window = Tk()
#Created proper window for app
window.title("Projects data".center(1))
window.geometry("900x600")
window.resizable(False, False)



canvas = Canvas(width=900, height=600, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')

my_label = Label(window, image=logo_img)
my_label.place(x=-2, y=0)

dotum = tkFont.Font(family="Dotum",weight="bold")
#Adding program interface
first_name = Label(text="Name", width=10, font=dotum)
first_name.place(x= 100, y=175)

first_name_entry = Entry(width=20)
first_name_entry.place (x=220, y=175, height=24.3)


last_name = Label(text="Surname",width=10, font=dotum)
last_name.place(x=100, y=250)

last_name_entry = Entry(width=20)
last_name_entry.place (x=220, y=250, height=24.3)

email = Label(text="E-mail",width=10, font=dotum)
email.place(x=100, y=325)

email_entry = Entry(width=20)
email_entry.place (x=220, y=325, height=24.3)

date = Label(text="Date:\nYYYY-MM-DD", width=10, font=dotum)
date.place(x= 100, y=400)

date_entry = Entry(width=20)
date_entry.place (x=220, y=400, height=24.3)

project = Label(text="Project", width=10, font=dotum)
project.place(x= 600, y=175)

project_entry = Entry(width=20)
project_entry.place (x=720, y=175, height=24.3)

hour = Label(text="Hours", width=10, font=dotum)
hour.place(x= 600, y=250)

hour_entry = Entry(width=20)
hour_entry.place (x=720, y=250, height=24.3)

new_feature = Label(text="New Feature", width=10, font=dotum)
new_feature.place(x= 600, y=325)

new_feature_entry = Entry(width=20)
new_feature_entry.place (x=720, y=325, height=24.3)

comments = Label(text="Comment", width=10, font=dotum)
comments.place(x= 600, y=400)

comments_entery = Text(width=20, height=4)
comments_entery.place(x=720, y=400)

#Combination of buttons with functions above
add_to_sql = Button(text= 'Add', width=35, font=dotum, bg="#54B435", command=add)
add_to_sql.place(x= 40, y= 520, height=60)

clear = Button(text= 'Clear', width=35, font=dotum, bg="#DD5353", command=clear_tabs)
clear.place(x= 500, y= 520, height=60)

window.mainloop()

