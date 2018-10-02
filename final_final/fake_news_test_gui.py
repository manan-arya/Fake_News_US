
# coding: utf-8

# In[13]:


from tkinter import *


# In[14]:


import import_ipynb
import sys
sys.path.append("./")
import fake_news_main_final


# In[15]:


def quit():
    window.destroy()


# In[18]:


def get_entry_fields():
    global t
    t = entry_text.get()


    
window = Tk()
topFrame = Frame(window)
topFrame.pack()

bottomFrame = Frame(window, width =3000, height = 1500)
bottomFrame.pack(side = BOTTOM)

label = Label(topFrame,text = "News:")
label.grid(row= 0,column =0 )

entry_text = Entry(topFrame, text = "Enter text")
entry_text.grid(row= 0, column = 2)

button_submit = Button(bottomFrame, text = "Submit", fg ="red", command = get_entry_fields)
button_submit.grid(row = 2, column = 2)


button_show = Button(bottomFrame, text = "Show", fg ="red", command = quit)
button_show.grid(row = 2, column = 4)

window.mainloop()



# In[17]:


out = fake_news_main_final.func(t)

window2 = Tk()

label_text = Label(window2, text = out, bg = "white")
label_text.grid(row = 4, column = 2)

window2.mainloop()

