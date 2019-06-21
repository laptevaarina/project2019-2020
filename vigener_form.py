from tkinter import *
import vigener

def vigener_form():
    def cipher_v(event):
        text = txt_int_v.get('1.0', END)
        K = txt_k_v.get('1.0', END)
        text_res = vigener.cipher_v(text, K)
        txt_out_v.delete('1.0', END)
        txt_out_v.insert('1.0', text_res)

    def cipher_v_return(event):
        text = txt_out_v.get('1.0', END)
        K = txt_k_v.get('1.0', END)
        text_res = vigener.cipher_v_return(text, K)
        txt_int_v.delete('1.0', END)
        txt_int_v.insert('1.0', text_res)

    root2 = Tk()
    root2.title('Кодировка шифром Виженера')
    root2.geometry('1000x400')
    root2.resizable(False, False)

    lblt_v = Label(root2, font = 'Helvetica 20', text = 'Кодировка шифром Виженера')
    lblt_v.place(relx = 0.3, rely = 0.1)

    lbl0_v = Label(root2, font = 'Helvetica 14', text = 'Ввод текста для зашифровки')
    lbl0_v.place(relx = 0.05, rely = 0.25)
    txt_int_v = Text(root2, width = 26, height = 5,  font = 'Helvetica 14', wrap = WORD)
    txt_int_v.place(relx = 0.05, rely = 0.4)

    lbl1_v = Label(root2, font = 'Helvetica 14', text = 'Введите ключ(слово)')
    lbl1_v.place(relx = 0.38, rely = 0.25)
    txt_k_v = Text(root2, width = 12, height = 2, font = 'Helvetica 14')
    txt_k_v.place(relx = 0.403, rely = 0.4)
    btn_v = Button(root2, text = 'Зашифровать', width = 12, height = 1, font = 'Arial 14', bg = 'red')
    btn_v.place(relx = 0.4, rely = 0.5)
    btn_v.bind('<1>', cipher_v)
    btn1_v = Button(root2, text = 'Расшифровать', width = 12, height = 1, font = 'Arial 14', bg = 'orange')
    btn1_v.place(relx = 0.4, rely = 0.6)
    btn1_v.bind('<1>', cipher_v_return)

    lbl2_v = Label(root2, font = 'Helvetica 14', text = 'Ввод текста для расшифровки')
    lbl2_v.place(relx = 0.6, rely = 0.25)
    txt_out_v = Text(root2, width = 26, height = 5,  font = 'Helvetica 14', wrap = WORD)
    txt_out_v.place(relx = 0.6, rely = 0.4)
    root2.mainloop()

if __name__ == '__main__':
    vigener_form()
