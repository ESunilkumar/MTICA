from  tkinter import *

master=Tk()
demo_text='this is a sample demo'
msg=Message(master,text=demo_text)
msg.config(bg='lightgreen', font=('times',34,'italic'))
msg.pack()

