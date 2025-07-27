import modultest.Hesapla as h
#from modultest import Hesapla as h

from modultest.testpaketi.altpaket import bilgiver as bilgi

x= h.Ortalama()
print(bilgi.mesaj())



#print("alinin ortalaması" ,x )


#import sys
#print(sys.path)


from selenium import webdriver
webdriver.Chrome()

print(webdriver.__version__)