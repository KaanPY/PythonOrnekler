import random

registeredUsers = []

while(True):
    operator = int(input("""\n============Operatörler==========
1.Sisteme Giriş Yap
2.Sisteme Kayıt Ol
3.Sistemden Çıkış...
>> Operatör Seçiminiz: """))

    if(operator == 1):
        randomNumber = random.randint(100,999)

        print(f'Güvenlik Kodu: {randomNumber}')
        userName = input('\nKullanıcı adınız: ')
        userPassword = input('Şifrenizi giriniz: ')
        securityCode = int(input('Güvenlik kodunu giriniz: '))

        for kaan in registeredUsers:
            if((userName == kaan["name"])and(userPassword == kaan["password"])and(securityCode == randomNumber)):
                print('>> Başarılı')
                break
        else:
            print('>> üzgünüz')

    elif(operator == 2):
        randomNumber2 = random.randint(100,999)

        print(f'Güvenlik Kodu: {randomNumber2}')
        name = input('\nKullanıcı adınızı giriniz: ')
        password = input('Şifrenizi giriniz: ')
        securityCode2 = int(input('Güvenlik kodunu giriniz: '))

        if(securityCode2 == randomNumber2):
            registeredUsers.append({
                "name": name,
                "password": password
            })
            print('>> Kayıt başarılı!')
        else:
            print('>> Güvenlik kodu yanlış girildi!')

    elif(operator == 3):
        print('\n>> Sistemden çıkılıyor...')
        break
print('>> Sistemden başarıyla çıkış yapıldı!')
