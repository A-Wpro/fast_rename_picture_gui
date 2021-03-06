
#list des imgs
from os import listdir
from os.path import isfile, join
import os
import shutil

mypath = 'E:\Autre\HQP\A trier'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles.remove("fast_show_and_rename.py")
onlyfiles.remove("tag.txt")

#create directory named renamed
renamed_dir = "renamed"
try:
    os.mkdir(renamed_dir)
except OSError:
    print ("Creation of the directory %s failed")
else:
    print ("Successfully created the directory %s ")
    
#create directory named renamed
not_renamed_dir = "notrenamed"
try:
    os.mkdir(not_renamed_dir)
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


tkinter_umlauts=['odiaeresis', 'adiaeresis', 'udiaeresis', 'Odiaeresis', 'Adiaeresis', 'Udiaeresis', 'ssharp']

class AutocompleteEntry(Entry):
    """
    Subclass of tkinter.Entry that features autocompletion.
    To enable autocompletion use set_completion_list(list) to define 
    a list of possible strings to hit.
    To cycle through hits use down and up arrow keys.
    """

    def set_completion_list(self, completion_list):
        self._completion_list = completion_list
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)               

    def autocomplete(self, delta=0):
        """autocomplete the Entry, delta may be 0/1/-1 to cycle through possible hits"""
        if delta: # need to delete selection otherwise we would fix the current position
            self.delete(self.position, END)
        else: # set position to end so selection starts where textentry ended
            self.position = len(self.get())
        # collect hits
        _hits = []
        for element in self._completion_list:
            if element.startswith(self.get().lower()):
                _hits.append(element)
        # if we have a new hit list, keep this in mind
        if _hits != self._hits:
            self._hit_index = 0
            self._hits=_hits
        # only allow cycling if we are in a known hit list
        if _hits == self._hits and self._hits:
            self._hit_index = (self._hit_index + delta) % len(self._hits)
        # now finally perform the auto completion
        if self._hits:
            self.delete(0,END)
            self.insert(0,self._hits[self._hit_index])
            self.select_range(self.position,END)
                        
    def handle_keyrelease(self, event):
        """event handler for the keyrelease event on this widget"""
        if event.keysym == "BackSpace":
            self.delete(self.index(INSERT), END) 
            self.position = self.index(END)
        if event.keysym == "Left":
            if self.position < self.index(END): # delete the selection
                self.delete(self.position, END)
            else:
                self.position = self.position-1 # delete one character
                self.delete(self.position, END)
        if event.keysym == "Right":
            self.position = self.index(END) # go to end (no selection)
        if event.keysym == "Down":
            self.autocomplete(1) # cycle to next hit
        if event.keysym == "Up":
            self.autocomplete(-1) # cycle to previous hit
        # perform normal autocomplete if event is a single key or an umlaut
        if len(event.keysym) == 1 or event.keysym in tkinter_umlauts:
            self.autocomplete()



# file-input.py
f = open('tag.txt','r')
tag_list = f.read()
# Convert String to Tuple 
tag_list = tuple(map(str, tag_list.split('\n')))
f.close()

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



tag1 = AutocompleteEntry(window,width=13)
tag1.set_completion_list(tag_list)
tag2 = AutocompleteEntry(window,width=13)
tag2.set_completion_list(tag_list)
tag3 = AutocompleteEntry(window,width=13)
tag3.set_completion_list(tag_list)
tag4 = AutocompleteEntry(window,width=13)
tag4.set_completion_list(tag_list)

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
        
        if Tag1 not in tag_list:
            f = open('tag.txt','a')
            f.write("\n"+Tag1)
            f.close()
        if Tag2 not in tag_list:
            f = open('tag.txt','a')
            f.write("\n"+Tag2)
            f.close()
        if Tag3 not in tag_list:
            f = open('tag.txt','a')
            f.write("\n"+Tag3)
            f.close()
        if Tag4 not in tag_list:
            f = open('tag.txt','a')
            f.write("\n"+Tag4)
            f.close()
        
        i=0
        renamed_switch =False
        while renamed_switch == False:
            try:
                os.rename(onlyfiles[0],renamed_dir+"/"+new_name+".jpg")
                renamed_switch = True
            
            except FileExistsError:
            
                i=i+1
                new_name = new_name+dash+str(i)

                os.rename(onlyfiles[0],renamed_dir+"/"+new_name+".jpg")
                renamed_switch = os.path.isfile(new_name+".jpg")
            """
            print("Existe déja on ajoute un chiffre")
            i=0
            while(os.path.isfile(new_name+dash+str(i)+".jpg")==True):
                i = i +1
            print(i)
            #new_name = new_name+dash+str(i)
            #print("SO WILL rename :",renamed_dir+"/"+new_name+".jpg")
            #os.rename(onlyfiles[0],renamed_dir+"/"+new_name+".jpg")
            """
    onlyfiles.pop(0)
"""
        if (os.path.isfile(new_name+".jpg")==False):
            os.rename(onlyfiles[0],renamed_dir+"/"+new_name+".jpg")
            print("will rename :",renamed_dir+"/"+new_name+".jpg")
        else:
            print("CANT rename :",renamed_dir+"/"+new_name+".jpg")
            i=0
            while(os.path.isfile(new_name+str(i)+".jpg")==True):
                i = i +1
            new_name = new_name+dash+str(i)
            print("SO WILL rename :",renamed_dir+"/"+new_name+".jpg")
            os.rename(onlyfiles[0],renamed_dir+"/"+new_name+".jpg")
            
            """

def dont():
    os.rename(onlyfiles[0],not_renamed_dir+"/"+onlyfiles[0])
    onlyfiles.pop(0)

    

    
Rename = Button(window, text="Rename Image", command=Rename)

Rename.grid(column=0, row=3)

Next = Button(window, text="Next image", command=button1)

Next.grid(column=0, row=4)

dontRename = Button(window, text="dont Rename", command=dont)

dontRename.grid(column=0, row=6)

window.mainloop()

