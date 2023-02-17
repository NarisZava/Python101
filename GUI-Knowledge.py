from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk()# หน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล')# ชื่่อโปรแกรม
GUI.geometry('500x400')# ขนาดโปรแกรม

B1 = ttk.Button(GUI,text='มีเงินกี่บาท')
B1.pack(ipadx=20,ipady=20)
##########################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI)#Board
FB1.place(x=200,y=200)
B2 = ttk.Button(FB1,text='มีเงินกี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)
##########################

GUI.mainloop()
