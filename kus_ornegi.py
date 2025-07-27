class kus:
    def intro(self):
        print("birçok kuş türü bulunmaktadır.")
        
    def flight(self):
        print("kuşların büyük kısmı uçabilmekte ancak bazıları uçamaz.")
        
        
class serce(kus):
    def flight(self):
        print("kuşlar uçabiliyor.")
        
        
class devekusu(kus):
    def flight(self):
        print("devekuşu uçmaz.")
        
obj1=kus()
obj2=serce()
obj3=devekusu()

obj1.intro()
obj1.flight()
obj2.flight()
obj2.intro()
