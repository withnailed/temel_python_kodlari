class Araba:
    yakit="benzin"
    def __init__(self,marka,model,yil):
        self.marka=marka
        self.model=model
        self.yil=yil
        
    
    def Sur(self):
        print("araba gidiyor...")
    def bilgiver(self):
        print(self.marka , self.model, self.yil,self.yakit)

class Araba2:
    pass


araba1= Araba("bmw", "g20" ,2022)

araba1.bilgiver()

araba2= Araba("mersedes", "e200", 2023)
araba2.marka="XYZ"
araba2.yakit="elektrik"
print(araba2.yakit,araba2.marka)

