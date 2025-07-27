def divide_numbers(num1,num2):
    
    try:
        result=num1/num2
        print("Sonuç:",result)
    except ZeroDivisionError:
        print("sıfıra bölme hatası")
        
    except TypeError:
        print("tip hatası! iki sayı girmeniz gerekiyor.")
    except Exception as e:
        print("bir hata oluştu,",str(e))
    else:
        print("istisna oluşmadı. else bloğu çalıştı.")
    finally:
        print("işlem tamamlandı. finally bloğu çalıştı.")
        
divide_numbers(int(input("sayı gir:")), int(input("sayı gir:")))