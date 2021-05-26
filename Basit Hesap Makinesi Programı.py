# İyi çalışmalar <3

import time

def operation_total():
    print(f'\n>> {number} + {number2} = {number + number2}\n')
def operation_extraction():
    print(f'\n>> {number} - {number2} = {number - number2}\n')
def operation_multiplication():
    print(f'\n>> {number} x {number2} = {number * number2}\n')
def operation_division():
    print(f'\n>> {number} / {number2} = {number / number2}\n')
while(True):
    try:
        operation = int(input("""==========İŞLEMLER==========
1.Toplama(+)
2.Çıkarma(-)
3.Çarpma(x)
4.Bölme(/)
5.Çıkış...
> İşlem seçiniz (örn;1): """))
        if(operation < 1)or(operation > 5):
            print('\n>> Lütfen 1 ile 4 arası seçim yapınız!\n')
        elif(operation == 5):
            print('\n> Çıkış yapılıyor...')
            time.sleep(2)
            break
        else:
            print(f'\n==========İŞLEM YAPILACAK SAYILAR==========')
            number = int(input('> 1.Sayı giriniz: '))
            number2 = int(input('> 2.Sayı griniz: '))

        if(operation == 1):
            operation_total()
        elif(operation == 2):
            operation_extraction()
        elif(operation == 3):
            operation_multiplication()
        elif(operation == 4):
            operation_division()
    except ValueError:
        print('\n>> Sayı giriniz!\n')
    except ZeroDivisionError:
        print('\n>> Bölme işleminde sayı sıfıra bölünemez!\n')

print('>> Başarıyla çıkış yaptınız!')
