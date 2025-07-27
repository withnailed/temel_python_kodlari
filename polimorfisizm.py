class MP3:
    def __init__(self,path):
        self.path=path
        
    def play(self):
        print("mp3 çalıyor")
            
class WAV:
    def __init__(self,path):
        self.path=path
        
    def play(self):
        print("Wav çalışıyor")
        
class WMA:
    def __init__(self,path):
        self.path=path
    def play(self):
        print("Wma çalışıyor")
        
class M4A:
    def __init__(self,path):
        self.path=path
    def play(self):
        print("M4a çalışıyor")
        
def playmucic(p):
    p.play()
    
mp3=MP3("sjefnekn00")

playmucic(mp3)