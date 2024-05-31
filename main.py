from tkinter import *
from random import randint, shuffle, choice
from tkinter import messagebox
import pyperclip
import json
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
    website = website_entre.get().title()
    email = email_entre.get().lower()
    password = password_entre.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #saving upsated data
                json.dump(data, data_file, indent=4)

        finally:
            password_entre.delete(0, END)
            website_entre.delete(0, END)


def find_password():
    website = website_entre.get().title()
    try:
        with open("data.json", "r") as data_file:
            # reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found!")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for Facebook exists")
    finally:
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
website_entre = Entry(width=21)
website_entre.grid(column=1,row=1, sticky="EW")


email_entre = Entry(width=35)
email_entre.grid(column=1,row=2,columnspan=2, stick="EW")
email_entre.insert(0, "angela@gmail.com")

password_entre = Entry(width=21)
password_entre.grid(column=1,row=3, stick="EW")


#Buttons
search_button = Button(text="Search", bg="white", width=14, command=find_password)
search_button.grid(column=2,row=1)

generate_password = Button(text="Generate Password", bg="white", command=password_generator)
generate_password.grid(column=2,row=3)

add_button = Button(text="Add", width=36, bg="white", command=save)
add_button.grid(column=1,row=4,columnspan=2,sticky="EW")

window.mainloop()