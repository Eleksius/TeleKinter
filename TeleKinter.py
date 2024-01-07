import tkinter as tk
from telebot import TeleBot
from telebot import *
from tkinter import messagebox

#-------------------------
window = tk.Tk()
window.title('Telekinter by @Eleksius')
window.geometry('450x300')
window.config(bg = "pale turquoise")
#-------------------------
entryToken = tk.Entry(width = 65)
entryToken.insert(0,"Enter your bot token")


def send():
    try:
        TOKEN = str(entryToken.get())
        bot = TeleBot(TOKEN)
        window.update()
        user_id = str(entryId.get())
        message = str(entry.get('1.0',tk.END))
        bot.send_message(user_id, message)
    except:
        messagebox.showinfo('error', "Error, please check the entered data", icon = 'error', type = 'ok')

    print(TOKEN)
    print(user_id)
    print(message)

entry = tk.Text(height = 7,
                width = 50)
entry.tag_config('tag_red_text', foreground = 'black')
entry.insert(1.0,"Enter message", 'tag_red_text')

btn = tk.Button(
    text = "send message",
    command = send,
    height = 2,
    width = 25,
    relief = tk.GROOVE,
    bg = "gray90"
)
entryId = tk.Entry(width = 65)
entryId.insert(0, "Enter user id")

scroll = tk.Scrollbar(command = entry.yview, width = 20)
entry.config(yscrollcommand=scroll.set)

entryToken.grid(row = 0, pady = 10, padx = 10, sticky = 'n', columnspan = 3)
entryId.grid(row = 1, columnspan = 3)
entry.grid(row = 2, columnspan = 2, pady = 15, padx=(10,0))
scroll.grid(row = 2, column = 3, sticky = 'ns', pady = 15)
btn.grid(row = 3, column = 0, columnspan = 3, pady = 5)

window.mainloop()