from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters+password_numbers+password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pswrd_information():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(password)==0 or len(website)==0 or len(email)==0:
        messagebox.showinfo(message="Dont leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website,message=f"The details entered are :"
                                                                     f"\nEmail:{email}"
                                                                     f"\nPassword:{password}"
                                                                     f"\n Is it ok to save?")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0,END)
                password_input.delete(0,END)

            messagebox.showinfo(title="Confirmation Message",message="Password Saved Successfully...")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50,padx=50)

# canvas
canvas = Canvas(width=200,height=200);
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = lock_image)
canvas.grid(row=0,column=1)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)


# inputs
website_input = Entry(width=36)
website_input.grid(row=1,column=1,columnspan=2,sticky=W+E)
website_input.focus()

email_input = Entry(width=36)
email_input.grid(row=2,column=1,columnspan=2,sticky=W+E)
email_input.insert(0,"default@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1,row=3,sticky=W+E)


# buttons
generate_pswrd_button = Button(text="Generate Password",command=generate_password)
generate_pswrd_button.grid(column=2,row=3,sticky=W+E)

add_button = Button(text="Add",width=36,command=save_pswrd_information)
add_button.grid(row=4,column=1,columnspan=2,sticky=W+E)

window.mainloop()
