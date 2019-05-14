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
    txt_out.delete('1.0', END)
    txt_out.insert('1.0', text_res)

def cipher_return(event):
    text = txt_out.get(1.0, END)
    K = int(ent_k.get())
    alphabetA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabeta = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    text_res = ''
    for i in text:
        if i in alphabetA:
            text_res += alphabetA[alphabetA.index(i)-K]
        elif i in alphabeta:
            text_res += alphabeta[alphabeta.index(i)-K]
        else:
            text_res += i
    txt_int.delete('1.0', END)
    txt_int.insert('1.0', text_res)

lbl0 = Label(root, font = 'Helvetica 14', text = 'Ввод текста для зашифровки')
lbl0.place(relx = 0.05, rely = 0.1)
txt_int = Text(root, width = 26, height = 5,  font = 'Helvetica 14', wrap = WORD)
txt_int.place(relx = 0.05, rely = 0.3)

lbl1 = Label(root, font = 'Helvetica 14', text = 'Введите ключ')
lbl1.place(relx = 0.4, rely = 0.1)
ent_k = Entry(root, width = 8, justify='right', bd=10, insertwidth=-0.5,  font = 'Helvetica 14')
ent_k.place(relx = 0.4, rely = 0.3)
btn = Button(root, text = 'Зашифровать', font = 'Arial 14', bg = 'yellow')
btn.place(relx = 0.4, rely = 0.4)
btn.bind('<1>', cipher)
btn1 = Button(root, text = 'Расшифровать', font = 'Arial 14', bg = 'green')
btn1.place(relx = 0.4, rely = 0.5)
btn1.bind('<1>', cipher_return)

lbl2 = Label(root, font = 'Helvetica 14', text = 'Ввод текста для расшифровки')
lbl2.place(relx = 0.6, rely = 0.1)
txt_out = Text(root, width = 26, height = 5,  font = 'Helvetica 14', wrap = WORD)
txt_out.place(relx = 0.6, rely = 0.3)

root.mainloop()
