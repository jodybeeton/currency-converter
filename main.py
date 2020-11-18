import requests
from tkinter import *
from datetime import *

root = Tk()
root.title("Real Time Currency converter")
root.geometry('500x500')
root.configure(bg="black")


def action():
    code = currencies.get(ACTIVE)
    number = request['rates'][code]
    ans = float(num.get())*number
    ans = round(ans,2)
    display_label['text'] = ans

def exit():
    root.destroy()

lt = Label(root)
dt_n = datetime.now()
curr = dt_n.strftime("%D %H:%M")
lt.config(text=curr, bg="fuchsia")
url = 'https://api.exchangerate-api.com/v4/latest/USD'
request = requests.get(url).json()
temp = request['rates']
print(temp)
currencies = Listbox(root, width=10)
for item in temp.keys():
    currencies.insert(END, str(item))

num = Entry(root)
convert_btn = Button(root,bg="fuchsia", text='Convert',command=action)
display_label = Label(root)
title_label = Label(root,bg="fuchsia", text="My Currency converter")


title_label.place(x=150,y=0)
lt.place(x=150,y=20)
currencies.place(x=5,y=40)
num.place(x=100,y=41)
convert_btn.place(x=95,y=80)
display_label.place(x=300,y=50)

exit_btn=Button(root,bg="fuchsia", text="Exit",command=exit)
exit_btn.place(x = 10, y = 300)
root.mainloop()


