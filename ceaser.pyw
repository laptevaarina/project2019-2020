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

def cipher(text, key):
    text_res = ''
    for i in text:
        if i in alphabetA:
            text_res += encoder(i, alphabetA, key)
        elif i in alphabeta:
            text_res += encoder(i, alphabeta, key)
        elif i in alphabetR:
            text_res += encoder(i, alphabetR, key)
        elif i in alphabetr:
            text_res += encoder(i, alphabetr, key)
        else:
            text_res += i
    return text_res

def cipher_return(text, key):
    text_res = ''
    for i in text:
        if i in alphabetA:
            text_res += decoder(i, alphabetA, key)
        elif i in alphabeta:
            text_res += decoder(i, alphabeta, key)
        elif i in alphabetR:
            text_res += decoder(i, alphabetR, key)
        elif i in alphabetr:
            text_res += decoder(i, alphabetr, key)
        else:
            text_res += i
    return text_res

def tests_coding():
    '''Функция для тестирования шифра Цезаря'''
    print(tests_coding.__doc__)

    print("testcase #1: ", end='')
    text, key = 'Привет', 3
    result = 'Тулезх'
    print('Ok' if cipher(text, key) == result else 'Fail')

    print("testcase #2: ", end='')
    text, key = 'Привет, как ваши дела?', 10
    result = 'Щътлоь, фйф лйвт нохй?'
    print('Ok' if cipher(text, key) == result else 'Fail')

if __name__ == '__main__':
    tests_coding()


