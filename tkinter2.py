from tkinter import *
from tkinter import messagebox

tk=Tk()

# b1= Button(top,text="Balcan kebabı",relief=FLAT)
# b2= Button(top,text="Kuşbaşı kebabı",relief=RAISED)
# b3= Button(top,text="Adana kebabı",relief=SUNKEN)
# b4= Button(top,text="Tavuk kebabı",relief=GROOVE)
# b5= Button(top,text="Ciğer kebabı",relief=RIDGE)
# b1.pack()
# b2.pack()
# b3.pack()
# b4.pack()
# b5.pack()


# top.title("tkinter-buton ekleme")
# top.geometry("400x250")
# def buton():
#     lbl["text"]="1.butona tıklandı"
    
# def buton2():
#     lbl["text"]="2. butona basıldı"
    
# btn= Button(top,text="buton",bg="yellow",padx="20",pady="5",command=buton)
# btn.pack()

def buton():
    girdi = e1.get()
    messagebox.showinfo("girdi",girdi)
l1=Label(tk,text="username") 
l1.pack(side=LEFT)
e1=Entry(tk,bd=8)
e1.pack(side=LEFT)

btn= Button(tk,text="girdiyi göster",bg="yellow",padx="20",pady="5",command=buton)
btn.pack()
   


tk.mainloop()
