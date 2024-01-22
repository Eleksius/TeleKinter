import tkinter as tk
from telebot import TeleBot
from telebot import *
from tkinter import messagebox
<<<<<<< Updated upstream
=======
from idlelib.tooltip import Hovertip
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
=======

Hovertip(entry, "Enter your message here", hover_delay=500)
Hovertip(entryId, "Enter the user's ID you want to send a message to. \nYou can get it on Telegram from @username_to_id_bot or other", hover_delay=500)
Hovertip(entryToken, "Enter the tag of the bot from which you want to send a message\nIt can be found in Telegram at @BotFather", hover_delay=500)
>>>>>>> Stashed changes

window.mainloop()