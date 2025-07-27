# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 15:18:01 2023

@author: sezer
"""

from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.title("Tkinter - Messagebox")
tk.geometry("00x250")

def show():
    messagebox.showinfo("Başlık-Inf", "Info örneği mesajiçeriği...")
    messagebox.showerror("Başlık-hata", "hata örneği mesajiçeriği...")
    messagebox.showwarning("Başlık-uyarı", "uyarı örneği mesajiçeriği...")
    
def ask():
    messagebox.askyesno("Başlık", "evet hayır örneği...")
    messagebox.askokcancel("Başlık", "tamam iptal örneği...")
    messagebox.askquestion("Başlık", "ask question")
    messagebox.askretrycancel("Başlık", "ask retry or cancel")
    messagebox.askyesnocancel("Başlık", "yes no cancel")

L1 = Label(tk,text="Messagebox",font="Arial 10 bold")
L1.pack()

B1 = Button(tk, text="göster", padx="20", pady="20", command=show)
B1.pack()

B2 = Button(tk, text="onay al", padx="20", pady="20", command=ask)
B2.pack()

tk.mainloop()