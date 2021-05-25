# İyi çalışmalar <3

import random

randomNumber = random.randint(1, 20)
counter = 3

while(True):
    if(counter <= 0):
        print('> Üzgünüz, hakkınız bitti!')
        break
    try: 
        estimation = int(input(f'\n>> Kalan {counter} hak | Tahmininiz: '))
        counter -= 1

        if(estimation == randomNumber):
            print(f'\n>> Tahmin ettiğiniz {estimation} sayısı doğru!')
            break
        elif((estimation > randomNumber)and(counter > 0)):
            print('> Tahmininizi azaltın!')
        elif((estimation < randomNumber)and(counter > 0)):
            print('> Tahmininizi arttırın!')
    except ValueError:
        print('> Sayı girmediniz!')
    
