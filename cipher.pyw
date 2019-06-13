from ceaser_form import ceaser_form

#from vigener import *
from tkinter import *
root = Tk()
root.title('Шифрование')
root.geometry('400x400')

label = Label(root, font = 'Helvetica 14', text = 'Выберите шифр')
label.place(relx = 0.3, rely = 0.1)

btn_c = Button(root, command=ceaser_form, text = 'Шифр Цезаря', font = 'Arial 14', bg = '#66b0ff')
btn_c.place(relx = 0.3, rely = 0.3)

#fix me
btn_v = Button(root, text = 'Шифр Виженера', font = 'Arial 14', bg = '#926eae')
btn_v.place(relx = 0.3, rely = 0.5)
# btn_v.bind('<1>', cipher_v)

root.mainloop()
