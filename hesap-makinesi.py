import time

while ("true"):
    
    islemler = {"toplama : ": 1, "çıkarma : ": 2, "çarpma : ": 3, "bölme : ": 4}
    
    print(islemler)
    print("    ")
    
    a= int(input ("Birinci sayıyı giriniz : "))
    time.sleep(2)
    b = int(input ("ikinci sayıyı giriniz : "))
    time.sleep(2)
    c = int(input ("İşleminizi yukarıda verilen numaralara göre yapınız : "))
    time.sleep(2)
    print("İşleminiz hala hesaplanıyor lütfen bekleyiniz.")
    time.sleep(3)
    
    if (c==1):
        sonuc=a+b
        print (sonuc)
    
    elif (c==2):
        sonuc=a-b
        print (sonuc)
    
    elif (c==3):
        sonuc=a*b
        print (sonuc)
    
    elif (c==4):
        sonuc=a/b
        print(sonuc)
    
    else:
        print("hatalı giriş...")
        break