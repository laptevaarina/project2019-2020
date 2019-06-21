from vigener import *

def tests_coding():
    '''Функция тестирования шифра Виженера'''
    print(tests_coding.__doc__)

    print('testcase #1: ', end='')
    text, K = 'Hello!', 'programming'
    result = 'Wvzrf!'
    print('Ok' if cipher_v(text, K) == result else 'Fail')

    print('testcase #2: ', end='')
    text, K = 'Карл украл у Клары кораллы', 'кларнет'
    result = 'Хлрь бпгкч у Ыщегё цобнрюё'
    print('Ok' if cipher_v(text, K) == result else 'Fail')

    print('testcase #3: ', end='')
    text, K = 'Южно-эфиопский грач увёл мышь за хобот на съезд ящериц', 'панаграмма'
    result = 'Нжыо-аеиыьсъич гурч аоёы мишя ша выбют ыа фкефр яиеюищ'
    print('Ok' if cipher_v(text, K) == result else 'Fail')

    print('testcase #4: ', end='')
    text, K = 'Хорошая погода', 'дождь'
    result = 'Щэчтфдн цтяттж'
    print('Ok' if cipher_v(text, K) == result else 'Fail')

    print('testcase #5: ', end='')
    text, K = 'Pack my box with five dozen liquor jugs', 'pangram'
    result = 'Eapq dy ndx jokh rxvr jfzqc lvwlod yuty'
    print('Ok' if cipher_v(text, K) == result else 'Fail')

def tests_decoding():
    '''Функция тестирования декодирования шифра Виженера'''
    print(tests_decoding.__doc__)

    print("testcase #1: ", end='')
    text, K = 'M cerz xs vewy qc kbesw akpp', 'ege'
    result = 'I want to pass my exams well'
    print('Ok' if cipher_v_return(text, K) == result else 'Fail')

    print("testcase #2: ", end='')
    text, key = 'Ххкь Гыхкк зеыхз ыхкю', 'рак'
    result = 'Ехал Грека через реку'
    print('Ok' if cipher_v_return(text, key) == result else 'Fail')

    print("testcase #3: ", end='')
    text, key = 'Вжчбяч иррчн', 'лето'
    result = 'Цветут цветы'
    print('Ok' if cipher_v_return(text, key) == result else 'Fail')

    print("testcase #4: ", end='')
    text, key = 'Eosa sijigz wtxel suttt cwg hh btf mbnk', 'cat'
    result = 'Cozy sphinx waves quart jug of bad milk'
    print('Ok' if cipher_v_return(text, key) == result else 'Fail')

    print("testcase #5: ", end='')
    text, key = 'Т ксккю звз вуь фм зуыътщ? Як, юв ёсцевзйцф нющцчшхюш!', 'русскийязык'
    result = 'В чащах юга жил бы цитрус? Да, но фальшивый экземпляр!'
    print('Ok' if cipher_v_return(text, key) == result else 'Fail')

if __name__ == '__main__':
    tests_coding()
    tests_decoding()
