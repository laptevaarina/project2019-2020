from tkinter import *
root = Tk()
root.title('Кодировка шифром Цезаря')
root.geometry('1000x400')

def cipher(event):
    text = txt_int.get(1.0, END)
    K = int(ent_k.get())
    alphabetA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabeta = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    text_res = ''
    for i in text:
        if i in alphabetA:
            text_res += alphabetA[alphabetA.index(i)+K]
        elif i in alphabeta:
            text_res += alphabeta[alphabeta.index(i)+K]
        else:
            text_res += i
    lbl['text'] = text_res

lbl0 = Label(root, font = 'Helvetica 14', text = 'Введите текст')
lbl0.place(relx = 0.05, rely = 0.1)
txt_int = Text(root, width = 26, height = 5,  font = 'Helvetica 14', wrap = WORD)
txt_int.place(relx = 0.05, rely = 0.3)


lbl1 = Label(root, font = 'Helvetica 14', text = 'Введите ключ')
lbl1.place(relx = 0.5, rely = 0.1)
ent_k = Entry(root, width = 8, justify='right', bd=10, insertwidth=-0.5,  font = 'Helvetica 14')
ent_k.place(relx = 0.5, rely = 0.3)
btn = Button(root, text = 'Зашифровать', font = 'Arial 14', bg = 'yellow')
btn.place(relx = 0.5, rely = 0.5)
btn.bind('<1>', cipher)

lbl2 = Label(root, font = 'Helvetica 14', text = 'Ответ')
lbl2.place(relx = 0.8, rely = 0.1)
lbl = Label(root, font = 'Helvetica 14', bg = '#ffff99')
lbl.place(relx = 0.8, rely = 0.3)

root.mainloop()
