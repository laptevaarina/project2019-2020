from tkinter import *
root = Tk()
root.title('Кодировка шифром Цезаря')

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

ent_k = Entry(root, width = 8, justify='right', bd=10, insertwidth=-0.5,  font = 'Helvetica 14')
ent_k.pack()
txt_int = Text(root, width = 26, height = 5,  font = 'Helvetica 14', wrap = WORD)
txt_int.pack(padx = 5, pady = 5)


btn = Button(root, text = 'Зашифровать', font = 'Arial 14', bg = 'yellow')
btn.pack()
btn.bind('<1>', cipher)

lbl = Label(root, font = 'Helvetica 14', bg = '#ffff99')
lbl.pack()

root.mainloop()
