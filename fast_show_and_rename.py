
#list des imgs
from os import listdir
from os.path import isfile, join
import os


mypath = 'E:\Autre\HQP\A trier'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles.remove("fast_show_and_rename.py")

#create directory named renamed
renamed_dir = "renamed"
try:
    os.mkdir(renamed_dir)
except OSError:
    print ("Creation of the directory %s failed")
else:
    print ("Successfully created the directory %s ")

Windows_size_h = 1920
Windows_size_w = 1080
Windows_multiplier = 0.6
Image_multiplier = 0.5
index_img=0


import sys
from tkinter import * #or Tkinter if you're on Python2.7
from PIL import Image, ImageTk



window = Tk()

window.title("Fast rename")

window.geometry('350x200')

lab1 = Label(window, text="tag1")
lab2 = Label(window, text="tag2")
lab3 = Label(window, text="tag3")
lab4 = Label(window, text="tag4")

lab1.grid(column=0, row=0)
lab2.grid(column=1, row=0)
lab3.grid(column=2, row=0)
lab4.grid(column=3, row=0)

tag1 = Entry(window,width=13)
tag2 = Entry(window,width=13)
tag3 = Entry(window,width=13)
tag4 = Entry(window,width=13)

tag1.grid(column=0, row=1)
tag2.grid(column=1, row=1)
tag3.grid(column=2, row=1)
tag4.grid(column=3, row=1)

def button1():
	if onlyfiles:
		pil_image = Image.open(onlyfiles[0])
		pil_image = pil_image.resize((int(Windows_size_h*Windows_multiplier*Image_multiplier), int(Windows_size_w*Image_multiplier)), Image.ANTIALIAS)    
		novi = Toplevel()
		canvas = Canvas(novi, width = int(Windows_size_w*Windows_multiplier), height = int(Windows_size_h*Windows_multiplier*Image_multiplier))
		canvas.pack(expand = YES, fill = BOTH)
		gif1 =  ImageTk.PhotoImage(pil_image)	
		canvas.create_image(0, 0, image = gif1, anchor = NW)
		#assigned the gif1 to the canvas object
		canvas.gif1 = gif1
        
	nbs_img = Label(window, text="remaning : "+ str(len(onlyfiles)))

	nbs_img.grid(column=2, row=4)
		


    
    
def Rename():
    Tag1 = tag1.get()
    Tag2 = tag2.get()
    Tag3 = tag3.get()
    Tag4 = tag4.get()
    dash = "-"
    new_name = Tag1+dash+Tag2+dash+Tag3+dash+Tag4
	
    if onlyfiles:
        if (os.path.isfile(new_name+".jpg")):
            i=0
            while(os.path.isfile(new_name+str(i)+".jpg")==True):
                i = i +1
            new_name = new_name	+str(i)
            os.rename(onlyfiles[0],renamed_dir+"/"+new_name+".jpg")
        else:
            os.rename(onlyfiles[0],renamed_dir+"/"+new_name+".jpg")
        onlyfiles.pop(0)

def dont():
    onlyfiles.pop(0)
    

    
Rename = Button(window, text="Rename Image", command=Rename)

Rename.grid(column=0, row=3)

Next = Button(window, text="Next image", command=button1)

Next.grid(column=0, row=4)

dontRename = Button(window, text="don't Rename", command=dont)

dontRename.grid(column=0, row=6)

window.mainloop()

