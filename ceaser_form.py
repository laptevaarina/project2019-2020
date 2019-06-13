from tkinter import *
import ceaser

def ceaser_form():
    def cipher(event):
        text = txt_int.get('1.0', END)
        key = int(txt_k.get('1.0', END))
        text_res = ceaser.cipher(text, key)
        txt_out.delete('1.0', END)
        txt_out.insert('1.0', text_res)

    def cipher_return(event):
        text = txt_out.get('1.0', END)
        key = int(txt_k.get('1.0', END))
        text_res = ceaser.cipher_return(text, key)
        txt_int.delete('1.0', END)
        txt_int.insert('1.0', text_res)

    root1 = Tk()
    root1.title('Кодировка шифром Цезаря')
    root1.geometry('1000x400')
    root1.resizable(False, False)

    lblt = Label(root1, font='Helvetica 20', text='Кодировка шифром Цезаря')
    lblt.place(relx=0.3, rely=0.1)

    lbl0 = Label(root1, font='Helvetica 14', text='Ввод текста для зашифровки')
    lbl0.place(relx=0.05, rely=0.25)
    txt_int = Text(root1, width=26, height=5, font='Helvetica 14', wrap=WORD)
    txt_int.place(relx=0.05, rely=0.4)

    lbl1 = Label(root1, font='Helvetica 14', text='Введите ключ(число)')
    lbl1.place(relx=0.38, rely=0.25)
    txt_k = Text(root1, width=12, height=2, font='Helvetica 14')
    txt_k.place(relx=0.403, rely=0.4)
    btn = Button(root1, text='Зашифровать', width=12, height=1, font='Arial 14', bg='yellow')
    btn.place(relx=0.4, rely=0.5)
    btn.bind('<1>', cipher)
    btn1 = Button(root1, text='Расшифровать', width=12, height=1, font='Arial 14', bg='green')
    btn1.place(relx=0.4, rely=0.6)
    btn1.bind('<1>', cipher_return)

    lbl2 = Label(root1, font='Helvetica 14', text='Ввод текста для расшифровки')
    lbl2.place(relx=0.6, rely=0.25)
    txt_out = Text(root1, width=26, height=5, font='Helvetica 14', wrap=WORD)
    txt_out.place(relx=0.6, rely=0.4)
    root1.mainloop()

if __name__ == '__main__':
    ceaser_form()


