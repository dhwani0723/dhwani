from tkinter import *
import os
def register():             #Registration Screen
    global reg_screen
    reg_screen = Toplevel(main_screen)
    reg_screen.title("Register")
    reg_screen.geometry('350x250')

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(reg_screen,text = "Please enter the details below",font=("classic", 11)).pack()
    Label(reg_screen,text = "").pack()

    username_label = Label(reg_screen , text = "Username*",font = ("classic",11))
    username_label.pack()
    username_entry = Entry(reg_screen , textvariable = username)
    username_entry.pack()
    
    password_label = Label(reg_screen , text = "Password*",font=("classic",11))
    password_label.pack()
    password_entry = Entry(reg_screen , textvariable = password,show = '*')
    password_entry.pack()

    Label(reg_screen,text = "").pack()
    Button(reg_screen,text = "Register" , width = 6, height = 1,font = ("classic",11),bg = "green",command=reg_user).pack()

def login():             #Login Screen
    global login_screen 
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry('350x250')
    Label(login_screen,text = "Please enter details to Login!",font=("classic", 11)).pack()
    Label(login_screen,text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen,text = "Username*",font=("classic",11)).pack()
    username_login_entry = Entry(login_screen,textvariable = username_verify)
    username_login_entry.pack()
    Label(login_screen , text = "").pack()
    Label(login_screen,text="Password*",font = ("classic",11)).pack()
    password_login_entry = Entry(login_screen,textvariable = password_verify,show = '*')
    password_login_entry.pack()
    Label(login_screen , text = "").pack()
    Button(login_screen,text = "Login" ,font = ("classic",11), bg = "green",width = 5, height = 1,command=login_verify).pack()

                                #Implementing event on Register Button

def reg_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info,"w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
                                                                        
    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(reg_screen,text = "Registered Sucessfully!").pack()

    #Implementing event on login button
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0,END)
    password_login_entry.delete(0,END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1,"r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()

    #Pop Up for login sucess

def login_sucess():
    global login_sucess_screen
    login_sucess_screen = Toplevel(login_screen)
    login_sucess_screen.title("Sucess")
    login_sucess_screen.geometry('150x100')
    Label(login_sucess_screen, text = "Login Sucess").pack()
    Button(login_sucess_screen,text = "OK",command = delete_login_sucess).pack()

    #Pop up for invalid password

def password_not_recognised():
    global password_not_recognised_screen
    password_not_recognised_screen = Toplevel(login_screen)
    password_not_recognised_screen.title("Sucess")
    password_not_recognised_screen.geometry('150x100')
    Label(password_not_recognised_screen , text = "Invalid Password").pack()
    Button(password_not_recognised_screen,text="OK",command = delete_password_not_recognised).pack()

    #Pop up for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Sucess")
    user_not_found_screen.geometry('150x100')
    Label(user_not_found_screen, text = "User not found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

    #Deleting popups
def delete_login_sucess():
    login_sucess_screen.destroy()
def delete_password_not_recognised():
    password_not_recognised_screen.destroy()
def delete_user_not_found_screen():
    user_not_found_screen.destroy()


                            #Designing first(main) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry('400x300')
    main_screen.title("Home")
    Label(text = "Select your choice",width = "300" , height="2",font=("classic", 11)).pack()
    Label(text = "").pack()
    Button(text = "Login",height = "2",bg = "black",fg = "white", width = "20",command = login).pack()
    Label(text = "").pack()
    Button(text = "Register",height="2",bg = "white",fg = "black",width="20",command = register).pack()
    main_screen.mainloop()
main_account_screen()
    
