from tkinter import *
import tkMessageBox


def sndText():
    tkMessageBox.showinfo('Hello brother','Text sent')

root=Tk()

root.title('pTalk Official App')
root.resizable(width=50,height=50)

lbl=Label(root,text='Welcome to pTalk',bg='blue',fg='white')
lbl.pack(side=TOP)


bttmFrame=Frame()
bttmFrame.pack(side=BOTTOM)

btnSend1=Button(bttmFrame,text='Send1',bg='red',command=sndText)
btnSend1.pack(side=BOTTOM)


inp1=StringVar()

lbl2=Label(root,text='Enter Name : ')
lbl2.pack(side=LEFT)
e1=Entry(root,bd=5)
e1.pack(side=LEFT)

e2=Entry(root,bd=5,textvariable=inp1)
e2.pack(side=RIGHT)
mtext=inp1.get()
mlbl2=Label(root,text=inp1).pack()


readInput1=e1.get()
print(readInput1)

root.mainloop()


