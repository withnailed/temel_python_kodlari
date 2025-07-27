class salon:
    def __init__(self,salon_ad,koltuk_Say):
        self.salon_ad=salon_ad
        self.koltuk_Say=koltuk_Say
    
   
class bilet:
    sayac=0
    ciro=0
    iptal_sayac=0
    def __init__(self,bilet_tur):
        self.bilet_tur=bilet_tur
        bilet.sayac+=1
        
    def satis(tur):
        if tur=="Tam bilet":
            bilet.ciro+=70
        elif tur=="İndirimli bilet":
            bilet.ciro+=50
            
    def iptal(tur):
        if tur=="Tam bilet":
            bilet.ciro-=70
        elif tur=="İndirimli bilet":
            bilet.ciro-=50
        bilet.iptal_sayac+=1
        
    def iptal_gonder():
        return bilet.iptal_sayac


print("Hoşgeldiniz....")
salonadı=input("Salon adı giriniz:")
koltuksay=int(input("Koltuk Sayısı giriniz:"))
salon1=salon(salonadı,koltuksay)
while True:

    print("""Menüden seçim yapınız:  \n bilet satışı için 1 \n bilet iptali için 2 \n iade edilen bileti öğrenmek için 3 \n boş koltuk öğrenmek için 4 \n sistemden çıkmak için 5 e basınız..""")
    sec=int(input("Seçim yapınız:"))
    if sec==1:
        bil=input("bilet türünü yazınız:")
        yeni= bilet(bil)
        bilet.satis(bil)
    elif sec==2:
        bil=input("bilet türünü yazınız:")
        bilet.iptal(bil)
    elif sec==3:
        print(bilet.iptal_gonder())
    elif sec==4:
        print(salon1.koltuk_Say-bilet.sayac+bilet.iptal_sayac)
        print("burdasın")
    elif sec==5:
        break
        
    




