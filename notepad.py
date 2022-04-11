from tkinter import *
from PIL import ImageTk, Image
import os 
from tkinter import filedialog
from tkinter import messagebox 

root = Tk()

root.title("Notepad")
root.minsize(650,650)
root.maxsize(650,650)

open1 = ImageTk.PhotoImage(Image.open("open.png"))
save1 = ImageTk.PhotoImage(Image.open("save.png"))
exit1 = ImageTk.PhotoImage(Image.open("exit.jpg"))

lbl1 = Label(root,text = "File Name")
lbl1.place(relx=0.28,rely=0.03,anchor=CENTER)

input1 = Entry(root)
input1.place(relx=0.46,rely=0.03,anchor=CENTER)

note = Text(root,height=35,width=80)
note.place(relx=0.5,rely=0.55,anchor=CENTER)







name = ""

def openfile():
    global name
    note.delete(1.0,END)
    input1.delete(0,END)
    text = filedialog.askopenfilename(title = "Open text file",filetype= (("Text file", "*.txt"),))
    print(text)
    name = os.path.basename(text)
    formated = name.split('.')[0]
    input1.insert(END,formated)
    text = open(name,'r+')
    paragraph = text.read()
    note.insert(END,paragraph)
    text.close()

def savefile():
    input2 = input1.get()
    file = open(input2 + ".txt", "w")
    data = note.get("1.0",END)
    print(data)
    file.write(data)
    note.delete(1.0,END)
    input1.delete(0,END)
    messagebox.showinfo("Update","Success")
    
savebtn = Button(root,image = save1,command = savefile)
savebtn.place(relx=0.12,rely=0.03,anchor=CENTER)

def exit12():
    root.destroy()
    
exitbtn = Button(root,image = exit1,command = exit12)
exitbtn.place(relx=0.19,rely=0.03,anchor=CENTER)    
    
    
    
    
    
    
openbtn = Button(root,image = open1,command = openfile)
openbtn.place(relx=0.05,rely=0.03,anchor=CENTER)    


root.mainloop()