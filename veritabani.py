import pyodbc as db


# =============================================================================
# driver_name="SQL SERVER"
# server_name="Tolga\SQLEXPRESS"
# database_name="BTKPYTHON"
# 
# =============================================================================

conn= db.connect("Driver={SQL Server};"
                 "Server=Tolga\SQLEXPRESS;"
                 "Database=BTKPYTHON;"
                 "Trusted_Connection=yes;")

cursor= conn.cursor()
cursor.execute("select * from musteri")

# =============================================================================
# for i in cursor:
#     print(i.Adi)
# =============================================================================
    
# import pandas as pd
# #data frame= df
# df=pd.read_sql_query("select * from musteri", conn)
# print(df)

# ad=input("Adınızı Giriniz:")
# soyad=input("Soyadınızı Giriniz:")
# dt=input("Doğum Tarihinizi Giriniz:")
# sehir=input("Şehir Giriniz:")
# cinsiyet=input("Cinsiyet Giriniz:")
# puan=input("Puan Giriniz:")

# cursor=conn.cursor()
# SQLCommand=("insert into musteri(Adi,Soyad,DogumTarihi,Sehir,Cinsiyet,Puan) VALUES(?,?,?,?,?,?)"  )
# VALUES=[ad,soyad,dt,sehir,cinsiyet,puan]

# cursor.execute(SQLCommand,VALUES)
# conn.commit()
# print("Data sucsesfully ınserted")
# conn.close()

# cursor= conn.cursor()
# SQLCommand="Delete from musteri where MusteriNo='3'"
# cursor.execute(SQLCommand)
# conn.commit()
# print("Kayıt başarıyla silindi.")
# conn.close()


# ad = input("Adınızı giriniz:")
# soyad= input("Soyadınızı giriniz:")
# MusteriNo=8
# cursor= conn.cursor()
# cursor.execute("update musteri set Adi=?,Soyad=? where MusteriNo=?",ad,soyad,MusteriNo)
# conn.commit()
# print("kayıt başarılı bir şekilde güncellendi...")
# conn.close()

















    