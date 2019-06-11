from tkinter import *
from encoder_decoder import *
root1 = Tk()
root1.title('Кодировка шифром Цезаря')
root1.geometry('1000x400')
root1.resizable(False, False)

alphabetA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabeta = 'abcdefghijklmnopqrstuvwxyz'
alphabetR = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabetr = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def cipher(event):
    text = txt_int.get('1.0', END)
    K = int(txt_k.get('1.0', END))
    text_res = ''
    for i in text:
        if i in alphabetA:
            text_res += encoder(i, alphabetA, K)
        elif i in alphabeta:
            text_res += encoder(i, alphabeta, K)
        elif i in alphabetR:
            text_res += encoder(i, alphabetR, K)
        elif i in alphabetr:
            text_res += encoder(i, alphabetr, K)
        else:
            text_res += i
    txt_out.delete('1.0', END)
    txt_out.insert('1.0', text_res)

def cipher_return(event):
    text = txt_out.get('1.0', END)
    K = int(txt_k.get('1.0', END))
    text_res = ''
    for i in text:
        if i in alphabetA:
            text_res += decoder(i, alphabetA, K)
        elif i in alphabeta:
            text_res += decoder(i, alphabeta, K)
        elif i in alphabetR:
            text_res += decoder(i, alphabetR, K)
        elif i in alphabetr:
            text_res += decoder(i, alphabetr, K)
        else:
            text_res += i
    txt_int.delete('1.0', END)
    txt_int.insert('1.0', text_res)

lblt = Label(root1, font = 'Helvetica 20', text = 'Кодировка шифром Цезаря')
lblt.place(relx = 0.3, rely = 0.1)

lbl0 = Label(root1, font = 'Helvetica 14', text = 'Ввод текста для зашифровки')
lbl0.place(relx = 0.05, rely = 0.25)
txt_int = Text(root1, width = 26, height = 5,  font = 'Helvetica 14', wrap = WORD)
txt_int.place(relx = 0.05, rely = 0.4)

lbl1 = Label(root1, font = 'Helvetica 14', text = 'Введите ключ(число)')
lbl1.place(relx = 0.38, rely = 0.25)
txt_k = Text(root1, width = 12, height = 2, font = 'Helvetica 14')
txt_k.place(relx = 0.403, rely = 0.4)
btn = Button(root1, text = 'Зашифровать', width = 12, height = 1, font = 'Arial 14', bg = 'yellow')
btn.place(relx = 0.4, rely = 0.5)
btn.bind('<1>', cipher)
btn1 = Button(root1, text = 'Расшифровать', width = 12, height = 1, font = 'Arial 14', bg = 'green')
btn1.place(relx = 0.4, rely = 0.6)
btn1.bind('<1>', cipher_return)

lbl2 = Label(root1, font = 'Helvetica 14', text = 'Ввод текста для расшифровки')
lbl2.place(relx = 0.6, rely = 0.25)
txt_out = Text(root1, width = 26, height = 5,  font = 'Helvetica 14', wrap = WORD)
txt_out.place(relx = 0.6, rely = 0.4)

root1.mainloop()
