from tkinter import *
root = Tk()
root.title('Шифрование')
root.geometry('400x400')

alphabetA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabeta = 'abcdefghijklmnopqrstuvwxyz'
alphabetR = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabetr = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def encoder(l, alph, k):
    res = ''
    if alph.index(l)+k >= len(alph):
        res += alph[k - (len(alph)-alph.index(l))]
    else:
        res += alph[alph.index(l)+k]
    return res

def decoder(l, alph, k):
    res = ''
    if alph.index(l)-k < 0:
        res += alph[len(alph)-(k - alph.index(l))]
    else:
        res += alph[alph.index(l)-k]
    return res

def caesar(event):
    root1 = Toplevel(root)
    root1.title('Кодировка шифром Цезаря')
    root1.geometry('1000x400')

    def cipher(event):
        text = txt_int.get('1.0', END)
        K = int(ent_k.get())
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
        K = int(ent_k.get())
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
    ent_k = Entry(root1, width = 8, justify='right', bd=10, insertwidth=-0.5,  font = 'Helvetica 14')
    ent_k.place(relx = 0.38, rely = 0.4)
    btn = Button(root1, text = 'Зашифровать', font = 'Arial 14', bg = 'yellow')
    btn.place(relx = 0.38, rely = 0.5)
    btn.bind('<1>', cipher)
    btn1 = Button(root1, text = 'Расшифровать', font = 'Arial 14', bg = 'green')
    btn1.place(relx = 0.38, rely = 0.6)
    btn1.bind('<1>', cipher_return)

    lbl2 = Label(root1, font = 'Helvetica 14', text = 'Ввод текста для расшифровки')
    lbl2.place(relx = 0.6, rely = 0.25)
    txt_out = Text(root1, width = 26, height = 5,  font = 'Helvetica 14', wrap = WORD)
    txt_out.place(relx = 0.6, rely = 0.4)

def vigenere(event):
    root2 = Toplevel(root)
    root2.title('Кодировка шифром Виженера')
    root2.geometry('1000x400')

    def cipher_v(event):
        text = txt_int_v.get('1.0', END)
        K = txt_k_v.get('1.0', END)
        text_res = ''
        count = 0
        for i in text:
            if i in alphabetA:
                text_res += encoder(i, alphabetA, alphabetA.index(K[count].upper()))
            elif i in alphabeta:
                text_res += encoder(i, alphabeta, alphabeta.index(K[count].lower()))
            elif i in alphabetR:
                text_res += encoder(i, alphabetR, alphabetR.index(K[count].upper()))
            elif i in alphabetr:
                text_res += encoder(i, alphabetr, alphabetr.index(K[count].lower()))
            else:
                text_res += i
                continue
            if count == len(K)-1:
                count = 0
            else:
                count += 1
        txt_out_v.delete('1.0', END)
        txt_out_v.insert('1.0', text_res)

    def cipher_v_return(event):
        text = txt_out_v.get('1.0', END)
        K = txt_k_v.get('1.0', END)
        text_res = ''
        count = 0
        for i in text:
            if i in alphabetA:
                text_res += decoder(i, alphabetA, alphabetA.index(K[count].upper()))
            elif i in alphabeta:
                text_res += decoder(i, alphabeta, alphabeta.index(K[count].lower()))
            elif i in alphabetR:
                text_res += decoder(i, alphabetR, alphabetR.index(K[count].upper()))
            elif i in alphabetr:
                text_res += decoder(i, alphabetr, alphabetr.index(K[count].lower()))
            else:
                text_res += i
                continue
            if count == len(K)-1:
                count = 0
            else:
                count += 1
        txt_int_v.delete('1.0', END)
        txt_int_v.insert('1.0', text_res)

    lblt_v = Label(root2, font = 'Helvetica 20', text = 'Кодировка шифром Виженера')
    lblt_v.place(relx = 0.3, rely = 0.1)

    lbl0_v = Label(root2, font = 'Helvetica 14', text = 'Ввод текста для зашифровки')
    lbl0_v.place(relx = 0.05, rely = 0.25)
    txt_int_v = Text(root2, width = 26, height = 5,  font = 'Helvetica 14', wrap = WORD)
    txt_int_v.place(relx = 0.05, rely = 0.4)

    lbl1_v = Label(root2, font = 'Helvetica 14', text = 'Введите ключ(слово)')
    lbl1_v.place(relx = 0.38, rely = 0.25)
    txt_k_v = Text(root2, width = 12, height = 3, font = 'Helvetica 14')
    txt_k_v.place(relx = 0.38, rely = 0.4)
    btn_v = Button(root2, text = 'Зашифровать', font = 'Arial 14', bg = 'red')
    btn_v.place(relx = 0.38, rely = 0.5)
    btn_v.bind('<1>', cipher_v)
    btn1_v = Button(root2, text = 'Расшифровать', font = 'Arial 14', bg = 'orange')
    btn1_v.place(relx = 0.38, rely = 0.6)
    btn1_v.bind('<1>', cipher_v_return)

    lbl2_v = Label(root2, font = 'Helvetica 14', text = 'Ввод текста для расшифровки')
    lbl2_v.place(relx = 0.6, rely = 0.25)
    txt_out_v = Text(root2, width = 26, height = 5,  font = 'Helvetica 14', wrap = WORD)
    txt_out_v.place(relx = 0.6, rely = 0.4)

label = Label(root, font = 'Helvetica 14', text = 'Выберите шифр')
label.place(relx = 0.3, rely = 0.1)

btn_c = Button(root, text = 'Шифр Цезаря', font = 'Arial 14', bg = '#66b0ff')
btn_c.place(relx = 0.3, rely = 0.3)
btn_c.bind('<1>', caesar)

btn_v = Button(root, text = 'Шифр Виженера', font = 'Arial 14', bg = '#926eae')
btn_v.place(relx = 0.3, rely = 0.5)
btn_v.bind('<1>', vigenere)

root.mainloop()
