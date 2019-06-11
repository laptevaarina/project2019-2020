from tkinter import *
root = Tk()
root.title('Шифрование')
root.geometry('400x400')

from ceaser import *
from vigener import *

label = Label(root, font = 'Helvetica 14', text = 'Выберите шифр')
label.place(relx = 0.3, rely = 0.1)

btn_c = Button(root, text = 'Шифр Цезаря', font = 'Arial 14', bg = '#66b0ff')
btn_c.place(relx = 0.3, rely = 0.3)
btn_c.bind('<1>', cipher_c)

btn_v = Button(root, text = 'Шифр Виженера', font = 'Arial 14', bg = '#926eae')
btn_v.place(relx = 0.3, rely = 0.5)
btn_v.bind('<1>', cipher_v)

root.mainloop()
