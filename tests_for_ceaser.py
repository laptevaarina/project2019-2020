from ceaser import *

def tests_coding():
    '''Функция для тестирования шифра Цезаря'''
    print(tests_coding.__doc__)

    print("testcase #1: ", end='')
    text, key = 'Привет', 3
    result = 'Тулезх'
    print('Ok' if cipher(text, key) == result else 'Fail')

    print("testcase #2: ", end='')
    text, key = 'В следующей фразе есть все буквы алфавита', 10
    result = 'Л ыхонэзгоу юъйсо оыьё лыо кэфле йхюйлтьй'
    print('Ok' if cipher(text, key) == result else 'Fail')

    print("testcase #3: ", end='')
    text, key = 'Шифровальщица попросту забыла ряд ключевых множителей и тэгов', 7
    result = 'Япычхижтгапэж цхцчхшщъ ожзвтж чёк стеюливь уфхнпщлтлр п щдйхи'
    print('Ok' if cipher(text, key) == result else 'Fail')

    print("testcase #4: ", end='')
    text, key = 'Crazy Fredrick bought many very exquisite opal jewels', 23
    result = 'Zoxwv Cobaofzh ylrdeq jxkv sbov bunrfpfqb lmxi gbtbip'
    print('Ok' if cipher(text, key) == result else 'Fail')

    print("testcase #5: ", end='')
    text, key = "These were Caesar's encryption tests", 15
    result = "Iwtht ltgt Rpthpg'h tcrgneixdc ithih"
    print('Ok' if cipher(text, key) == result else 'Fail')

def tests_decoding():
    '''Функция для тестирования декодирования по шифру Цезаря'''
    print(tests_decoding.__doc__)

    print("testcase #1: ", end='')
    text, key = 'Х стёяр жтзтр!!!', 4
    result = 'С новым годом!!!'
    print('Ok' if cipher_return(text, key) == result else 'Fail')

    print("testcase #2: ", end='')
    text, key = 'К ъфнмьжвсю эщирию ъчмнщпиыъз кън йьукд ифэиксычк', 9
    result = 'В следующих фразах содержатся все буквы алфавитов'
    print('Ok' if cipher_return(text, key) == result else 'Fail')

    print("testcase #3: ", end='')
    text, key = 'Яьпнунснрщелйя кямгчяуся тёд бъюбзкя ждлкз анвяцди з опнхбдсяэшзф йпдрсыюм', 32
    result = 'Аэрофотосъёмка ландшафта уже выявила земли богачей и процветающих крестьян'
    print('Ok' if cipher_return(text, key) == result else 'Fail')

    print("testcase #4: ", end='')
    text, key = 'Znk lobk hudotm cofgxjy pasv waoiqre', 6
    result = 'The five boxing wizards jump quickly'
    print('Ok' if cipher_return(text, key) == result else 'Fail')

    print("testcase #5: ", end='')
    text, key = 'Cn cm hywymmuls ni fyulh Yhafcmb', 20
    result = 'It is necessary to learn English'
    print('Ok' if cipher_return(text, key) == result else 'Fail')

if __name__ == '__main__':
    tests_coding()
    tests_decoding()
