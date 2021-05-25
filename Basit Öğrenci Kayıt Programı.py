# İyi çalışmalar <3

import os
os.getcwd() # Bu programı kaydettiğiniz yere "kayitliOgrenciler.txt" dosyası açıp kaydetmiş olduğunuz öğrencileri yazmıştır
# os.chdir('bu kod sayesinde "kayitliOgrenciler.txt" dosyasını istediğniiz yere açtırabilirsiniz')

def not_ekle():
    print('\n==========ÖĞRENCİ NOT EKLEME==========')
    ogrenciAdSoy = input('> Öğrenci adı & soyadı: ')
    ogrenciNumara = input('> Öğrenci numarası: ')
    ogrenciNot = int(input('> 1.Öğrenci sınav notu: '))
    ogrenciNot2 = int(input('> 2.Öğrenci sınav notu: '))
    ogrenciPerformans = int(input('Öğrenci performans notu: '))

    with open('kayitliOgrenciler.txt', mode='a', encoding='utf-8') as file:
        file.write(f'1-) Adı & Soyadı: {ogrenciAdSoy}, Numarası: {ogrenciNumara}, 1.Sınav Notu: {ogrenciNot}, 2.Sınav Notu: {ogrenciNot2}, Performans Notu: {ogrenciPerformans}\n')
    print(f'>> {ogrenciAdSoy} adlı öğrenci sisteme başarıyla kaydedildi!\n')

    sayac = 1
    lOgrenciler = []
    with open('kayitliOgrenciler.txt', mode='r', encoding='utf-8') as file2:
        for kaan in file2:
            lOgrenciler.append(str(sayac) + "-" + kaan.split("-")[1])
            sayac += 1
    with open('kayitliOgrenciler.txt', mode='w', encoding='utf-8') as file3:
        file3.writelines(lOgrenciler)

def not_oku():
    with open('kayitliOgrenciler.txt', mode='r', encoding='utf-8') as file:
        print('\n==========KAYITLI ÖĞRENCİLER==========')
        for kaan in file:
            print(kaan)

while(True):
    operation = int(input("""==========İŞLEMLER==========
1.Öğrenci Not Ekle
2.Kayıtlı Öğrenciler
3.Sistemden Çıkış...
İşlem seçiniz (örn;1): """))

    if(operation == 1):
        not_ekle()
    elif(operation == 2):
        not_oku()
    elif(operation == 3):
        print('Sistemden çıkış yapılıyor...')
        break

print('Sistemden başarıyla çıkış yapıldı!')
