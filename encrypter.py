from datetime import datetime
from time import sleep

data = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
zmienna = int(datetime.utcnow().strftime('%f')[:-3])


def szyfr():
    with open('krzaki.txt', 'w',encoding='utf8') as f:
        f.write('')
        f.close()

    with open('szyfr.txt', 'r', encoding='utf-8') as f:

        d = f.read()
        print(d)
        for c in d:
            a = ord(c) + 1000 + zmienna

            with open('zaszyfrowane.txt', 'a',encoding='utf8') as k:
                k.write(str(a))
                k.close()

    with open('zaszyfrowane.txt', 'r') as file:
        g = file.read()
        print(g)

    with open('zaszyfrowane_wtornie.txt', 'a',encoding='utf8') as lu:
        for i in g:
            lu.write(str(ord(i)))

    with open('zaszyfrowane_wtornie.txt', 'r',encoding='utf8') as w:
        while True:
            czteryznaki = w.read(4)
            with open('krzaki.txt', 'a', encoding='utf-8') as r:
                if czteryznaki == '':
                    break
                c = chr(int(czteryznaki))
                r.write(c)

    with open('zaszyfrowane.txt', 'w',encoding='utf8') as f:
        f.write('')
        f.close()

    with open('zaszyfrowane_wtornie.txt', 'w',encoding='utf8') as f:
        f.write('')
        f.close()


def odszyfr():
    with open('odszyfrowane.txt', 'w',encoding='utf8') as f:
        f.write('')
        f.close()

    with open(f'{plik}.txt', 'r',encoding='utf-8')as pr:
        while True:
            znak = pr.read(1)
            with open('zaszyfrowane_wtornie.txt', 'a',encoding='utf8')as zsz:
                if znak == '':
                    break
                q = str(ord(znak))
                zsz.write(q)

    with open('zaszyfrowane_wtornie.txt', "r",encoding='utf8') as t:
        while True:
            dwaznaki = t.read(2)
            with open('odszyfrowane.txt', 'a',encoding='utf8') as q:
                if dwaznaki == '':
                    break
                e = chr(int(dwaznaki))
                q.write(e)

    with open('odszyfrowane.txt', 'r',encoding='utf8') as w:
        while True:
            trzyznaki = w.read(4)
            with open(f'{data}--{plik}--odszyfrowano.txt', 'a', encoding='utf-8') as r:
                if trzyznaki == '':
                    break
                fr = int(trzyznaki) - 1000 - haslo
                c = chr(fr)
                r.write(c)

    with open('zaszyfrowane.txt', 'w',encoding='utf8') as f:
        f.write('')
        f.close()

    with open('zaszyfrowane_wtornie.txt', 'w',encoding='utf8') as f:
        f.write('')
        f.close()

    with open('krzaki.txt', 'w',encoding='utf8') as f:
        f.write('')
        f.close()


print('program do szyfrowania plików')
sleep(0.5)
print('wybierz działanie:')
sleep(0.5)
x = int(input('1 - szyfrowanie pliku \n2 - odszyfrowanie pliku\n'))

if x == 1:
    print('szyfrujesz plik')
    sleep(0.5)
    plik = input("podaj samą nazwę pliku (bez rozszerzenia .txt)")
    szyfr()
    sleep(0.5)
    print('zaszyfrowałeś plik')
    sleep(0.5)
    print(f'twoje hasło to: {zmienna}')
    sleep(0.5)
    print('będzie ci ono potrzebne do prawidłowego odszyfrowania pliku więc zapisz sobie je gdzieś')

elif x == 2 :
    print('odszyfrowujesz plik')
    sleep(0.5)
    print("podaj samą nazwę pliku (bez rozszerzenia .txt)")
    plik = input('pamiętaj, że musi to być plik zaszyfrowany, w przeciwnym wypadku program nie zadziała\n')
    sleep(0.5)
    haslo = int(input('podaj hasło: '))
    odszyfr()
    sleep(0.5)
    print('odszyfrowałeś plik')
