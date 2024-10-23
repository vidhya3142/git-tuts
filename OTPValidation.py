from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox  # Add this import for messagebox

class OTPApp(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x550")
        self.resizable(False, False)
        self.n = random.randint(1000, 9999)
        self.client = Client(account_sid, auth_token)
        self.client.messages.create(to="Phone_number", from_="Phone_number", body=str(self.n))

        self.Labels()
        self.Entry()
        self.Buttons()

    def Labels(self):
        self.c = Canvas(self, bg="White", width=400, height=200)
        self.c.place(x=100, y=60)
        self.Login_Title = Label(self, text="OTP VERIFICATION", font=("bold", 20),
                                 bg='white')  # Corrected 'fony' to 'font'
        self.Login_Title.place(x=210, y=90)

    def Entry(self):
        self.User_name = Text(self, borderwidth=2, highlightthickness=0, wrap='word', width=29,
                              height=2, bg='lightblue')  # Changed background color to light blue
        self.User_name.place(x=190, y=200)

    def Buttons(self):
        self.submitButtonImage = PhotoImage(file="submit.png")
        self.submitButton = Button(self, image=self.submitButtonImage, command=self.checkOTP, border=0)
        self.submitButton.place(x=180, y=300)

        self.resendOTPImage = PhotoImage(file="resendotp.png")
        self.resendOTPButton = Button(self, image=self.resendOTPImage, command=self.resendOTP,
                                      border=0)  # Renamed to avoid conflict
        self.resendOTPButton.place(x=180, y=400)

    def checkOTP(self):
        try:
            self.userInput = int(self.User_name.get(1.0, "end-1c"))  # Changed to "end-1c" to avoid trailing newline
            if self.userInput == self.n:
                messagebox.showinfo("Success", "Login Success")
                self.n = "done"
            elif self.n == "done":
                messagebox.showinfo("Info", "Already entered the OTP")
            else:
                messagebox.showinfo("Error", "Wrong OTP")
        except ValueError:
            messagebox.showinfo("Error", "Invalid OTP")

    def resendOTP(self):
        self.n = random.randint(1000, 9999)
        self.client.messages.create(to="Phone_number", from_="Phone_number", body=str(self.n))


if __name__ == "__main__":
    window = OTPApp()
    window.mainloop()
