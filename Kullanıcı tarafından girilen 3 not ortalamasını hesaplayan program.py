# kullanıcılar tarafından girilmesini sağlayarak kullanıcının girdiği 3 sınav notuna
# göre ortalamayı hesaplayan ve ekrana yazdıran kodu yazınız.

not1 = int(input('1.Not Giriniz: '))
not2 = int(input('2.Not Giriniz: '))
performans = int(input('Performans Not Giriniz: '))

hesap = ((not1 + not2 + performans) / 3)

print(f"Girilien 3 not'a göre sizin ortalamanız: {hesap}")
