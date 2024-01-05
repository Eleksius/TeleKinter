import tkinter as tk
from telebot import TeleBot
from tkinter import messagebox
#-------------------------
window = tk.Tk()
window.title('Telekinter by @Eleksius')
window.geometry('500x350')
#-------------------------
entryToken = tk.Entry(width = 60)
entryToken.insert(0,"Enter your bot token")

TOKEN = entryToken.get()
bot = TeleBot(TOKEN)

def send():
    try:
        user_id = entryId.get()
        bot.send_message(user_id, entry.get())
    except:
        messagebox.showinfo('error', "Error, please check the entered data", icon = 'error', type = 'ok')

entry = tk.Text(height = 5)
entry.insert(1.0,"Enter message")

btn = tk.Button(
    text = "send message",
    command = send,
    height = 2
)
entryId = tk.Entry(width = 60)
entryId.insert(0, "Enter user id")


entryToken.pack(pady = 10)
entryId.pack(pady = 20)
entry.pack(pady = 10)
btn.pack()

window.mainloop()