from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry("300x500")
root.title("Ввойти в систему")

def register():
    text = Label(text="Для входа в систему - заргестрируйтесь!")

    textLog = Label(text="Введите логин: ")
    registerLogin = Entry()

    textPass = Label(text="Введите пароль: ")
    registerPass = Entry(show="*")

    textPass1 = Label(text="Повторите пароль: ")
    registerPass1 = Entry(show="*")

    button_register = Button(text="Зарегестирироваться" , command=lambda:saveRegister())

    text.pack()

    textLog.pack()
    registerLogin.pack()

    textPass.pack()
    registerPass.pack()

    textPass1.pack()
    registerPass1.pack()

    button_register.pack()

    def saveRegister():
        login_pass_save = {}
        login_pass_save[registerLogin.get()] = registerPass.get()

        login = open('login.txt','wb')
        password = open('password.txt' , 'wb')

        pickle.dump(login_pass_save , login)
        pickle.dump(login_pass_save , password)

        login.close()
        password.close()

def login():
    textLogin = Label(text="Введите логин: ")
    enterLogin = Entry()

    textPassword = Label(text="Введите пароль")
    enterPassword = Entry(show="*")

    buttonEnter = Button(text="Войти" , command=lambda :logPass())

    textLogin.pack()
    enterLogin.pack()

    textPassword.pack()
    enterPassword.pack()

    buttonEnter.pack()

    def logPass ():
        login = open('login.txt','rb')
        loadLogin = pickle.load(login)

        password = open('password.txt' , 'rb')
        loadPassword = pickle.load(password)

        login.close()
        password.close()

        if enterLogin.get() in loadLogin:
            if enterLogin.get() == login[enterLogin.get()]:
                messagebox.showifnfo("Здравствуйте!")

        if enterPassword.get() in loadPassword:
            if enterPassword.get() == password[enterPassword.get()]:
                print('s')

            else:
                messagebox.showerror("Вы не правильно ввели логин или пароль")


register()
login()

root.mainloop()
