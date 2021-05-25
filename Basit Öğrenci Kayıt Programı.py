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
    ogrenciPerformans = int(input('> Öğrenci performans notu: '))

    with open('kayitliOgrenciler.txt', mode='a', encoding='utf-8') as file1:
        file1.write(f'1-) Adı & Soyadı: {ogrenciAdSoy}, Numarası: {ogrenciNumara}, 1.Sınav Notu: {ogrenciNot}, 2.Sınav Notu: {ogrenciNot2}, Performans Notu: {ogrenciPerformans}\n')
    print(f'>> {ogrenciAdSoy} adlı öğrenci sisteme başarıyla kaydedildi!\n')

    counter = 1
    lOgrenciler = []
    with open('kayitliOgrenciler.txt', mode='r', encoding='utf-8') as file2:
        for kaan in file2:
            lOgrenciler.append(str(counter) + "-" + kaan.split("-")[1])
            counter += 1
    with open('kayitliOgrenciler.txt', mode='w', encoding='utf-8') as file3:
        file3.writelines(lOgrenciler)

def not_oku():
    with open('kayitliOgrenciler.txt', mode='r', encoding='utf-8') as file4:
        print('\n==========KAYITLI ÖĞRENCİLER==========')
        for kaan in file4:
            print(kaan)

def ogrenci_sil():
    ogrenciListe = []
    with open('kayitliOgrenciler.txt', mode='r', encoding='utf-8') as f:
        for kaan12 in f:
            ogrenciListe.append(kaan12)

    silOgrenci = int(input("""\n==========ÖĞRENCİ SİLME==========
Silmek istediğiniz öğrencinin listede yer aldığı sırayı yazınız (örn; 3)
> Silmek istediğiniz öğrenci: """))

    ogrenciListe.pop(silOgrenci - 1)
    with open('kayitliOgrenciler.txt', mode='w', encoding='utf-8') as f2:
        f2.writelines(ogrenciListe)

    counter3 = 1
    lOgrenciler2 = []
    with open('kayitliOgrenciler.txt', mode='r', encoding='utf-8') as f3:
        for kaan in f3:
            lOgrenciler2.append(str(counter3) + "-" + kaan.split("-")[1])
            counter3 += 1
    with open('kayitliOgrenciler.txt', mode='w', encoding='utf-8') as f4:
        f4.writelines(lOgrenciler2)
    print(f'>> Listede kayıtlı {silOgrenci} sıradaki öğrenci başarıyla silindi!\n')

while(True):
    operation = int(input("""==========İŞLEMLER==========
1.Öğrenci Not Ekle
2.Kayıtlı Öğrenciler
3.Öğrenci Sil
4.Sistemden Çıkış...
> İşlem seçiniz (örn;1): """))

    if(operation == 1):
        not_ekle()
    elif(operation == 2):
        not_oku()
    elif(operation == 3):
        ogrenci_sil()
    elif(operation == 4):
        print('\n> Sistemden çıkış yapılıyor...')
        break

print('>> Sistemden başarıyla çıkış yapıldı!')
