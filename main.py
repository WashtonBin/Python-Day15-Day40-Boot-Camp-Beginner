from tkinter import *
from random import randint, shuffle, choice
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entre.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P



    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entre.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global PASSWORD
    website_data = website_entre.get()
    email_data = email_entre.get()
    password_data = password_entre.get()

    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:

        is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered: \nEmail:{email_data} "
                                                      f"\nPassword: {password_data} \n is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_data} | {email_data} | {password_data}\n")
                password_entre.delete(0, END)
                website_entre.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels

website_label = Label(text="Website")
website_label.grid(column=0,row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0,row=2)


password_label = Label(text="Password")
password_label.grid(column=0,row=3)



#Entries
website_entre = Entry(width=35)
website_entre.grid(column=1,row=1,columnspan=2, sticky="EW")


email_entre = Entry(width=35)
email_entre.grid(column=1,row=2,columnspan=2, stick="EW")
email_entre.insert(0, "angela@gmail.com")

password_entre = Entry(width=21)
password_entre.grid(column=1,row=3, stick="EW")


#Buttons
generate_password = Button(text="Generate Password", bg="white", command=password_generator)
generate_password.grid(column=2,row=3)

add_button = Button(text="Add", width=36, bg="white", command=save)
add_button.grid(column=1,row=4,columnspan=2,sticky="EW")

window.mainloop()