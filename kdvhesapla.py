class Urun:
    def __init__(self,ad,tur,fiyat):
        self.ad=ad
        self.tur=tur
        self.fiyat=fiyat
        
    def kdv_hesaplama(self):
        pass
    
class Sut(Urun):
    def kdv_hesaplama(self):
        deger=self.fiyat+self.fiyat*0.01
        return deger

class Kırtasiye(Urun):
    def kdv_hesaplama(self):
        deger=self.fiyat+self.fiyat*0.2
        return deger
        
siparis= Sut("çikolatlı", "süt", 35)
siparis2= Kırtasiye("defter", "kırtasiye", 50)
print(siparis.kdv_hesaplama())
print(siparis2.kdv_hesaplama())




