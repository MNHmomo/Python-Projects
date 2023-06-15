from tkinter import *
from tkinter import messagebox
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1200x600+100+100")
        self.root.resizable(False, False)

        #Background Image
        self.bg = PhotoImage(file = "SharpTeefBG.png")
        self.bg_image = Label(self.root, image = self.bg).place(x = 0, y = 0, relwidth = 1, relheight = 1)

        # Login Frame
        Frame_login = Frame(self.root, bg = "brown1")
        Frame_login.place(x = 130, y = 50, width = 500, height = 500)

        # Title & Subtitle
        title = Label(Frame_login, text = "Login Here", font = ("OPTIFuturaDemiBold", 50, "bold"), fg = "white", bg = "brown1").place(x = 70, y = 30)
        subtitle = Label(Frame_login, text = "member login area", font = ("SansSerifFLF", 20, "bold"), fg = "white", bg = "brown1").place(x = 120, y =115)

        # Username
        lbl_user = Label(Frame_login, text = "Username", font = ("SansSerifFLF", 20, "bold"), fg = "azure2", bg = "brown1").place(x = 30, y = 175)
        self.username = Entry(Frame_login, font = ("Arial", 15, "bold"), fg = "black", bg = "azure2")
        self.username.place(x = 30, y = 210, width = 435, height = 35)

        # Password
        lbl_password = Label(Frame_login, text = "Password", font = ("SansSerifFLF", 20, "bold"), fg = "azure2", bg = "brown1").place(x = 30, y = 305)
        self.password = Entry(Frame_login, font = ("Arial", 15, "bold"), fg = "black", bg = "azure2")
        self.password.place(x = 30, y = 340, width = 435, height = 35)

        # Button
        forget = Button(Frame_login, text = "forgot password?", cursor = "hand2", bd = 0, font = ("Arial", 15, "bold"), fg = "black", bg = "azure2").place(x = 30, y = 410)
        submit = Button(Frame_login, command = self.check_function, cursor = "hand2", text = "Login", bd = 0, font = ("Arial", 15, "bold"), fg = "black", bg = "azure2").place(x = 390, y = 410)

    # Conditons
    def check_function(self):
        if self.username.get() == "" or self.password.get()=="":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
        elif self.username.get() != "MNHmomo" or self.password.get() != "Mohamed2006.":
            messagebox.showerror("Error", "Invalid Username or Password", parent = self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")

root = Tk()
obj = Login(root)
root.mainloop()