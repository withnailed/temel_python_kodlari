from datetime import datetime, timedelta
import pyodbc as db
class Person:
    def __init__(self, tc, ad, soyad, departman, maas, dogum_tarihi, dogum_yeri, yas, telefon, email, ev_adresi, cocuk_sayisi, medeni_durum,yonetici_tc=None):
        self.tc = tc
        self.ad = ad
        self.soyad = soyad
        self.departman = departman
        self.maas = maas
        self.dogum_tarihi = dogum_tarihi
        self.dogum_yeri = dogum_yeri
        self.yas = yas
        self.telefon = telefon
        self.email = email
        self.ev_adresi = ev_adresi
        self.cocuk_sayisi = cocuk_sayisi
        self.medeni_durum = medeni_durum
        self.yonetici_tc = yonetici_tc

class DenizAraci:
    def __init__(self, id, kaptan_bilgisi, murettebat_bilgisi, agirlik, uzunluk, yukseklik, genislik, kategori, park_suresi_gun, park_suresi_saat,aktif_durum,sorumlu_buro,sorumlu_guvenlik,park_yeri):
        self.id = id
        self.kaptan_bilgisi = kaptan_bilgisi
        self.murettebat_bilgisi = murettebat_bilgisi
        self.agirlik = agirlik
        self.uzunluk = uzunluk
        self.yukseklik = yukseklik
        self.genislik = genislik
        self.kategori = kategori
        self.park_suresi_gun = park_suresi_gun
        self.park_suresi_saat = park_suresi_saat
        self.aktif_durum= aktif_durum
        self.sorumlu_buro=sorumlu_buro
        self.sorumlu_guvenlik=sorumlu_guvenlik
        self.park_yeri =park_yeri

    def güverte_basti_hesapla(self):
        """
        Deniz aracının güverte bastı ücretini hesapla.
        Güverte bastı ücreti = (Ağırlık * Genişlik) / Uzunluk
        """
        guverte_basti_ucreti = (self.agirlik * self.genislik) / self.uzunluk

        #return guverte_basti_ucreti

class LimanYonetimiSistemi(DenizAraci):
    def __init__(self, id, kaptan_bilgisi, murettebat_bilgisi, agirlik, uzunluk, yukseklik, genislik, kategori, park_suresi_gun, park_suresi_saat,aktif_durum,sorumlu_buro,sorumlu_guvenlik,park_yeri):
        super().__init__((id, kaptan_bilgisi, murettebat_bilgisi, agirlik, uzunluk, yukseklik, genislik, kategori, park_suresi_gun, park_suresi_saat,aktif_durum,sorumlu_buro,sorumlu_guvenlik,park_yeri))
        self.deniz_aracilari = []
        self.personeller = []

    def deniz_araci_ekle(self):
        bos_alan=0
        conn= veri_baglanti()
        cursor = conn.cursor()
        cursor.execute("select * from DenizAraci")
        for i in cursor:
            if i[10]==1:
                bos_alan+=1
        if bos_alan==5:
            print("Kayıt yapılamaz boş alan yok!!!!")
            return 0
        print("****Deniz aracı ekleme paneli****")
        motor=int(input("Deniz Aracı Motor NUmarasını giriniz:"))
        kategori=input("Aracın Katogorisini giriniz: ")
        sorumlu_buro=input("Sorumlu olacak büro personeli TC'sini giriniz:")
        sorumlu_guvenlik=input("Sorumlu olacak güvenlik personeli TC'sini giriniz:")
        aktif_durum=1
        park_alani=int(input("Park edilecek park alanı numarasını giriniz: "))

        yeni_kayit=DenizAraci(motor,kategori=kategori,sorumlu_buro=sorumlu_buro,sorumlu_guvenlik=sorumlu_guvenlik,aktif_durum=aktif_durum,park_yeri=park_alani)
        cursor = conn.cursor()
        komut = (("insert into DenizAraci(id,kategori,sorumlu_buro,sorumlu_guvenlik,aktif_durum,park_yeri) VALUES(?,?,?,?,?,?)"))
        Valuees = [motor,kategori,sorumlu_buro,sorumlu_guvenlik,aktif_durum,park_alani]

        cursor.execute(komut, Valuees)
        conn.commit()
        conn.close()

    def deniz_araci_guncelle(self, sorumlu_tc ):
        conn = veri_baglanti()
        cursor = conn.cursor()
        cursor.execute("select * from DenizAraci")
        for i in cursor:
            if i[11] == sorumlu_tc:
                print("Güncelleme yapabilirsiniz:")
                kaptan_bilgisi =input("Kaptan bilgisi giriniz: ")
                murettebat_bilgisi =input("Mürettabat bilgisi giriniz: ")
                agirlik =int(input("Deniz aracının ağırlığını giriniz: "))
                uzunluk =int(input("Deniz aracının uzunluğunu giriniz: "))
                yukseklik =int(input("Deniz aracının yüksekliğini giriniz: "))
                genislik =int(input("Deniz aracının genişliğini giriniz: "))
                park_suresi_gun = int(input("Deniz aracının park süresi günü giriniz: "))
                park_suresi_saat = int(input("Deniz aracının park süresi saati giriniz: "))
                cursor = conn.cursor()
                cursor.execute("update DenizAraci set kaptan_bilgisi=?,murettebat_bilgisi=?,agirlik=?,uzunluk=?,yukseklik=?,genislik=?,park_suresi_saat=?,park_suresi_gun=?, where sorumlu_tc=?", kaptan_bilgisi,murettebat_bilgisi,agirlik,uzunluk,yukseklik,genislik,park_suresi_saat,park_suresi_gun,sorumlu_tc)
                conn.commit()
                conn.close()
                print("güncelleme yapılmıştır")

    """personel güncelleme"""
    def personel_guncelle(self, personel_tc, yeni_bilgiler):
        pass


    def deniz_araci_guvenlik_raporu_ekle(self, deniz_araci_id, sorumlu_tc):
        

      """  if deniz_araci.id == deniz_araci_id:
                # Deniz aracına güvenlik raporu ekleme işlemi
                deniz_araci.guvenlik_raporu = input("Güvenlik Raporu")"""





# /////////////////////güncel

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////

class GuvenlikPersoneli(Person):
    def __init__(self, tc, ad, soyad, departman, maas, dogum_tarihi, dogum_yeri, yas, telefon, email, ev_adresi, cocuk_sayisi, medeni_durum, yonetici_tc=None):
        super().__init__(tc, ad, soyad, departman, maas, dogum_tarihi, dogum_yeri, yas, telefon, email, ev_adresi, cocuk_sayisi, medeni_durum, yonetici_tc=None)

    def guvenlik_durumu_gir(self, deniz_araci_id, durum):
        # Deniz aracının güvenlik durumunu sisteme giriş işlemi
        pass

class Muhasebe:
    def __init__(self, muhasebe_id, personel_tc, odeme_tutari, odeme_tarihi):
        self.muhasebe_id = muhasebe_id
        self.personel_tc = personel_tc
        self.odeme_tutari = odeme_tutari
        self.odeme_tarihi = odeme_tarihi

# yukardaki yapıcıya göre aşşağıyı düzenle
class MuhasebePersoneli(Person):
    def __init__(self, tc, ad, soyad, departman, maas, dogum_tarihi, dogum_yeri, yas, telefon, email, ev_adresi, cocuk_sayisi, medeni_durum, görev_unvani):
        super().__init__(tc, ad, soyad, departman, maas, dogum_tarihi, dogum_yeri, yas, telefon, email, ev_adresi, cocuk_sayisi, medeni_durum, görev_unvani)

    def muhasebe_odeme_hesapla(self, personel_tc):
        for personel in self.personeller:
            if personel.tc == personel_tc:
                # Personelin maaşını ve ek ödemelerini hesapla
                ek_odeme = personel.cocuk_sayisi * 300
                toplam_maas = personel.maas + ek_odeme
                print(f"{personel.ad} {personel.soyad}'ın maaşı: {toplam_maas} TL (Ek ödeme: {ek_odeme} TL)")
                break


    def para_tahsis_et(self, deniz_araci, saatlik_ucret):
        park_suresi_gun = deniz_araci.park_suresi_gun
        park_suresi_saat = deniz_araci.park_suresi_saat
        toplam_saat = (park_suresi_gun * 24) + park_suresi_saat
        tahsis_tutari = toplam_saat * saatlik_ucret

       # muhasebe_id = # Her kayda benzersiz bir ID ekleyin
      #  personel_tc = # Muhasebe işlemini yapan personelin TC kimlik numarası
        odeme_tarihi = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Eğer ödeme yapılacaksa, burada veritabanına kaydedebilirsiniz.

        print(f"{deniz_araci.id} numaralı deniz aracından {tahsis_tutari} TL tahsis edildi.")

class BuroPersoneli(Person):
    def __init__(self, tc, ad, soyad, departman, maas, dogum_tarihi, dogum_yeri, yas, telefon, email, ev_adresi, cocuk_sayisi, medeni_durum, görev_unvani):
        super().__init__(tc, ad, soyad, departman, maas, dogum_tarihi, dogum_yeri, yas, telefon, email, ev_adresi, cocuk_sayisi, medeni_durum, görev_unvani)

    def kayit(self):
        pass

class LimanYonetici(Person,LimanYonetimiSistemi):
    def __init__(self, tc, ad, soyad, departman, maas, dogum_tarihi, dogum_yeri, yas, telefon, email, ev_adresi, cocuk_sayisi, medeni_durum,):
        super().__init__(tc, ad, soyad, departman, maas, dogum_tarihi, dogum_yeri, yas, telefon, email, ev_adresi, cocuk_sayisi, medeni_durum)

    def yeni_departman_ekle(self, departman_adi):
        print("Oluşturmak istediğiniz departmanı giriniz:")
        yeni=input("İsim:")
        departmans.append(yeni)
        """ÜZERİNE DÜŞÜN"""

    def personel_ekle(self, personel):
        # Personel eklemek için işlem
        conn= veri_baglanti()
        tc = int(input("Personel Tc giriniz: "))
        ad = input("Personel Adını giriniz: ")
        soyad = input("Personel Soyadı girniz: ")
        departman = input("Personel Departmanını girniz: ")
        maas = int(input("Personel maaşını giriniz: "))
        dogum_t = int(input("Personel Doğum tarihini giriniz: "))
        dogum_y = input("Personel Doğum yerini girniz: ")
        yas = int(input("Personel yaşını giriniz: "))
        telefon = int(input("Personel Telefonunu giriniz: "))
        email = input("Personel Emailini giriniz: ")
        adres = input("Personel Ev adresini giriniz: ")
        cocuk_s = int(input("Personel Çocuk Sayısı giriniz: "))
        medeni = input("Personel Medeni durumunu giriniz: ")
        personel = Person(tc, ad, soyad, departman, maas, dogum_t, dogum_y, yas, telefon, email, adres, cocuk_s, medeni)
        cursor= conn.cursor()
        komut=(("insert into Personel(tc,ad,soyad,departman,maas,dogum_tarihi,dogum_yeri,yas,telefon,email,ev_adresi,cocuk_sayisi,medeni_durum,yonetici_tc) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"  ))
        Valuees=[tc, ad, soyad, departman, maas, dogum_t, dogum_y, yas, telefon, email, adres, cocuk_s, medeni]

        cursor.execute(komut,Valuees)
        conn.commit()
        conn.close()

    def personel_cikar(self):
        conn= veri_baglanti()
        print("Silmek istediğiniz personelin bilgilerini giriniz:")
        tc = int(input("Personel Tc giriniz: "))
        komut=("Delete from Personel where tc='?'")
        values=tc
        cursor.execute(komut,values)
        conn.commit()
        conn.close()



"""VERİ BAĞLANTISI"""
def veri_baglanti():
    conn = db.connect("Driver={SQL Server};"
                        "Server=Tolga\SQLEXPRESS;"
                        "Database=BTKproje;"
                        "Trusted_Connection=yes;")
    return conn

conn=veri_baglanti()
departmans=["yönetici","bilgi işlem","muhasebe","güvenlik","büro"]
print("**************Liman Yönetimine Hoşgeldiniz**************")
while True:
    print("Sisteme giriş yapınız:")
    pAd=input("Adınızı girin:")
    pTc=int(input("Tc'nizi giriniz:"))
    cursor = conn.cursor()
    cursor.execute("select * from Personel")
    for i in cursor:
        print("giriş yapıldı.")
        if i[0]==pTc and i[1]==pAd:

        #yönetici başlangıç
            if i[3]==departmans[0]:
                yonetici= LimanYonetici(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12])
                print("Yönetici Hoşgeldiniz")
                while True:
                    pass







            #yönetici bitiş

        # bilgi işlem düşünülecek
            if i[3]==departmans[1]:
                bilgi_islem= Person(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13])
                print("Bilgi işleme Hoşgeldiniz")

            if i[3]==departmans[2]:
                muhasebe= MuhasebePersoneli(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13])
                print("Muhasebeye Hoşgeldiniz")

            if i[3]==departmans[3]:
                guvenlik= GuvenlikPersoneli(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13])
                print("Güvenliğe Hoşgeldiniz")


            if i[3]==departmans[4]:
                buro= BuroPersoneli(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13])
                print("Büroya Hoşgeldiniz")

    conn.close()
    break



