# İyi çalışmalar <3

import random

registeredUsers = []

while(True):
    operation = int(input("""\n============İşlemler==========
1.Sisteme Giriş Yap
2.Sisteme Kayıt Ol
3.Sistemden Çıkış...
>> İşlem seçiniz (örn; 1): """))

    if(operation == 1):
        randomNumber = random.randint(100,999)

        print(f'\n>> Güvenlik Kodu: {randomNumber}')
        userName = input('Kullanıcı adınız: ')
        userPassword = input('Şifreniz: ')
        securityCode = int(input('Güvenlik kodu: '))

        for kaan in registeredUsers:
            if((userName == kaan["name"])and(userPassword == kaan["password"])and(securityCode == randomNumber)):
                print(f'>> {userName} hoş geldin!')
                break
        else:
            print('>> Tekrar deneyiniz.')

    elif(operation == 2):
        randomNumber2 = random.randint(100,999)

        print(f'\n>> Güvenlik Kodu: {randomNumber2}')
        name = input('Kullanıcı adı: ')
        password = input('Şifre: ')
        securityCode2 = int(input('Güvenlik kodu: '))

        if(securityCode2 == randomNumber2):
            registeredUsers.append({
                "name": name,
                "password": password
            })
            print('>> Kayıt başarılı!')
        else:
            print('>> Güvenlik kodu yanlış! Lütfen tekrar deneyiniz!')

    elif(operation == 3):
        print('\n>> Sistemden çıkış yapılıyor...')
        break
print('>> Sistemden başarıyla çıkış yaptınız!')
