class Araba:
    yakit="benzin"
    sayac=0
    def __init__(self,marka,model,yil):
        self.marka=marka
        self.model=model
        self.yil=yil
        Araba.sayac+=1
        
    @classmethod    
    def sayac_ayarla(cls,s):
        cls.sayac=s
    
    def Sur(self):
        print("araba gidiyor...")
    def bilgiver(self):
        print(self.marka , self.model, self.yil,self.yakit)
    @staticmethod
    def Sesver():
        print("Bipppp......")
    @staticmethod    
    def  Mesajver(mesaj):
        print(mesaj)
        

Araba.Sesver()
araba=Araba("bmw", "520", 2023)
araba.Sesver()
Araba.Mesajver("Yavaş sürüyorsunuz....")
