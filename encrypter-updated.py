from datetime import datetime
from time import sleep
import os

dt_now = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
random = int(datetime.now().strftime('%f')[:-3])


def create():
    encrypt_one = open('zaszyfrowane.txt', 'w', encoding='utf-8')
    encrypt_two = open('zaszyfrowane_wtornie.txt', 'w', encoding='utf-8')

    encrypt_one.write('')
    encrypt_two.write('')

    encrypt_one.close()
    encrypt_two.close()


def decreate():
    decrypt_one = open('odszyfrowane.txt', 'w', encoding='utf-8')
    decrypt_two = open('odszyfrowane_wtornie.txt', 'w', encoding='utf-8')

    decrypt_one.write('')
    decrypt_two.write('')

    decrypt_one.close()
    decrypt_two.close()


def encrypt():
    main_file = open(f'{file}.txt', 'r', encoding='utf-8')
    encrypt_one = open('zaszyfrowane.txt', 'r+', encoding='utf-8')
    encrypt_two = open('zaszyfrowane_wtornie.txt', 'r+', encoding='utf-8')
    result = open(f'{dt_now}--{file}--zaszyfrowano.txt', 'a', encoding='utf-8')

    while True:
        a = main_file.read(1)
        if a == '':
            break
        h = str(ord(a) + 1000 + random)
        encrypt_one.write(str(h))

    encrypt_one.seek(0)

    while True:
        b = encrypt_one.read(1)
        if b == '':
            break
        h = str(ord(b))
        encrypt_two.write(str(h))

    encrypt_two.seek(0)

    while True:
        four = encrypt_two.read(4)
        if four == '':
            break
        d = chr(int(four))
        result.write(d)

    result.seek(0)

    main_file.close()
    encrypt_one.close()
    encrypt_two.close()
    result.close()

    os.remove('zaszyfrowane.txt')
    os.remove('zaszyfrowane_wtornie.txt')


def decrypt():
    main_file = open(f'{file}.txt', 'r', encoding='utf-8')
    decrypt_one = open('odszyfrowane.txt', 'r+', encoding='utf-8')
    decrypt_two = open('odszyfrowane_wtornie.txt', 'r+', encoding='utf-8')
    decrypted = open(f'{dt_now}--{file}--odszyfrowano.txt', 'a', encoding='utf-8')

    while True:
        one = main_file.read(1)
        if one == '':
            break
        e = ord(one)
        decrypt_one.write(str(e))

    decrypt_one.seek(0)

    while True:
        two = decrypt_one.read(2)
        if two == '':
            break
        f = chr(int(two))
        decrypt_two.write(f)

    decrypt_two.seek(0)

    while True:
        four = decrypt_two.read(4)
        if four == '':
            break
        g = int(int(four) - 1000 - password)
        h = chr(g)
        decrypted.write(h)

    main_file.close()
    decrypt_one.close()
    decrypt_two.close()
    decrypted.close()

    os.remove('odszyfrowane.txt')
    os.remove('odszyfrowane_wtornie.txt')


print('program do szyfrowania plików')
sleep(0.5)
print('wybierz działanie:')
sleep(0.5)
x = int(input('1 - szyfrowanie pliku \n2 - odszyfrowanie pliku\n'))

if x == 1:
    print('szyfrujesz plik')
    sleep(0.5)
    file = input("podaj samą nazwę pliku (bez rozszerzenia .txt)\n")
    create()
    encrypt()
    sleep(0.5)
    print('zaszyfrowałeś plik')
    sleep(0.5)
    print(f'twoje hasło to: {random}')
    sleep(0.5)
    print('będzie ci ono potrzebne do prawidłowego odszyfrowania pliku więc zapisz sobie je gdzieś')

elif x == 2:
    print('odszyfrowujesz plik')
    sleep(0.5)
    print("podaj samą nazwę pliku (bez rozszerzenia .txt)")
    file = input('pamiętaj, że musi to być plik zaszyfrowany, w przeciwnym wypadku program nie zadziała\n')
    sleep(0.5)
    password = int(input('podaj hasło: '))
    decreate()
    decrypt()
    sleep(0.5)
    print('odszyfrowałeś plik')
