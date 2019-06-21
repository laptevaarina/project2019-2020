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

def cipher_v(text, K):
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
        count += 1
        if count == len(K)-1:
            count = 0
    return text_res

def cipher_v_return(text, K):
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
        count += 1
        if count == len(K)-1:
            count = 0
    return text_res
