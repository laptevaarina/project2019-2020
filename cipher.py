from ceaser_form import ceaser_form
from vigener_form import vigener_form

from tkinter import *
root = Tk()
root.title('Шифрование')
root.geometry('400x400')

label = Label(root, font = 'Helvetica 14', text = 'Выберите шифр')
label.place(relx = 0.3, rely = 0.1)

btn_c = Button(root, command=ceaser_form, text = 'Шифр Цезаря', font = 'Arial 14', bg = '#66b0ff')
btn_c.place(relx = 0.3, rely = 0.3)

btn_v = Button(root, command=vigener_form, text = 'Шифр Виженера', font = 'Arial 14', bg = '#926eae')
btn_v.place(relx = 0.3, rely = 0.5)

root.mainloop()
