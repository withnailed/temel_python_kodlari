# from abc import ABC,abstractmethod
# class Soyut(ABC):
    
#     @abstractmethod
#     def Soyut_sınıf(self):
#         pass
from abc import ABC    
class Calisan(ABC):
    def __init__(self):
        pass
    def bordro_hesapla(self):
        pass
    
    

class Tam_zamanli(Calisan):
    def __init__(self,isim):
        self.isim=isim
    def bordro_hesapla(self):
        return 11400
    
    
class Saatlik_calisan(Calisan):
    def __init__(self,isim,saat_ucret,calisma_saati):
        self.isim=isim
        self.saat_ucret=saat_ucret
        self.calisma_saati=calisma_saati
        
    def bordro_hesapla(self):
        return self.saat_ucret* self.calisma_saati


kisi= Tam_zamanli("tolga")
yari= Saatlik_calisan("sezer", 30, 50)
print(kisi.bordro_hesapla()) 
print(yari.bordro_hesapla())   
    