from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
import ssl
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz 
from PIL import Image, ImageTk
root = tk.Tk()
root.title(" Weather Forcast App")
root.geometry("900x500+300+200")

root.resizable(False,False)
def getWeather():
    try:
        city=textfield.get()
   
        #weather section we have used here API key which we have taken from organization its validity is limited 
        
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=01280fe75a89b7fa788a4b107c02af17"
        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']
        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","Feels","Like",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
    
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App","Invalid City !!")

#icon
image_icon=PhotoImage(file="images/1163763.png")
root.iconphoto(False,image_icon)


#logo
Logo_image=PhotoImage(file="images/1163763.png")
logo=Label(image=Logo_image)
logo.place(x=170,y=150)

#search box
Search_image=PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage=Label(image=Search_image)
myimage.place(x=30,y=20)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=100,y=35)
textfield.focus()

Search_icon=PhotoImage(file="images/Layer 6.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=390,y=25)

#Bottom box
Frame_image=PhotoImage(file="images/Copy of box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)


# this section is for labels that checks the exact whether of any city


#Label
label1=Label(root,text="wind m/s",font=("helvitica",15,'bold'),fg="White",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="  humidity %",font=("helvitica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=225,y=400)

label3=Label(root,text=" Description",font=("helvitica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text=" pressure hpa",font=("helvitica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)


t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)
w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)

d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)

p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)


root.mainloop()

