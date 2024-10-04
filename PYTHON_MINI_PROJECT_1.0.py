from tkinter import *
import tkinter as tk
from tkinter import Button ,ttk, messagebox ,Menu ,colorchooser
import pygame
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import json
import speech_recognition as sr
import pyaudio
import pyttsx3
import time
from colorama import Fore

def destroy():
    r.destroy()
def close_window():
    
    b = Button(r,text="Continue",bg='green',font='arial 20 ',command=destroy)
    b.place(x=375,y=310)

r = tk.Tk()
r.geometry("890x470+300+200")
r.config(bg='red')

def well_come():
    label.config(text="W")
def well_come2():
    label2.config(text="E")
def well_come3():
    label3.config(text="L")
def well_come4():
    label4.config(text="...")
def well_come5():
    come.config(text="C")
def well_come6():
    come2.config(text="O")
def well_come7():
    come3.config(text="M")
def well_come8():
    come4.config(text="E")
    
label = tk.Label(r, text='',font='arial 50 bold',bg='red')
label.place(x=150,y=110)
label.after(1000,well_come)
label2 = tk.Label(r, text='',font='arial 50 bold',bg='red')
label2.place(x=220,y=110)
label2.after(1500,well_come2)
label3 = tk.Label(r, text='',font='arial 50 bold',bg='red')
label3.place(x=270,y=110)
label3.after(2000,well_come3)
label4 = tk.Label(r, text='',font='arial 50 bold',bg='red')
label4.place(x=310,y=110)
label4.after(2500,well_come4)

come = tk.Label(r, text='',font='arial 50 bold',bg='red')
come.place(x=450,y=110)
come.after(1000,well_come5)
come2 = tk.Label(r, text='',font='arial 50 bold',bg='red')
come2.place(x=500,y=110)
come2.after(1500,well_come6)
come3 = tk.Label(r, text='',font='arial 50 bold',bg='red')
come3.place(x=555,y=110)
come3.after(2000,well_come7)
come4 = tk.Label(r, text='',font='arial 50 bold',bg='red')
come4.place(x=610,y=110)
come4.after(2500,well_come8)

r.after(8000, close_window)

r.mainloop()

root=Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="black")
root.resizable(False,False)

pi = PhotoImage(file="C:\\Users\\Nandan\\OneDrive\\Desktop\\avengers.png3.png")
l = Label(image=pi)

recognizer = sr.Recognizer()
def voice_recognizer():
    
    with sr.Microphone() as source:   # Use microphone as source of input
            print("Speak something:")
            audio = recognizer.record(source, duration=5)
            print("Recognizing...")
    try:
            text = recognizer.recognize_google(audio)  # Convert audio into text using Google Speech Recognition
            textfield.delete(0,END)
            textfield.insert(END,text)
            print("You said:", text)
    except:
            messagebox.showinfo("Weather App","Sorry, I could not understand you.")
            print("Sorry, I could not understand you.")
    def close_window():
        newroot.destroy()
    
    newroot = tk.Tk()
    newroot.geometry('200x25+600+400')
    newroot.resizable(False,False)
    newroot.config(bg='#404040')
    ll = Label(newroot,text="Recognizing...",font='arial 20 bold',bg="green",)
    ll.pack()
    newroot.after(5000, close_window)
    newroot.mainloop()
    
class WEATHER:
    def __init__(self) -> None:
         pass
    # i take ti from my TimezoneFinder__2.py (path =C:\Users\Nandan\OneDrive\Desktop\mini_pro_img\TimezoneFinder___2.py)
    def find_timezone(lat, lon):
        tf = TimezoneFinder()
        # Use the `timezone_at` method to find the timezone for a given latitude and longitude
        timezone_str = tf.timezone_at(lat=lat, lng=lon)
        return timezone_str

    def getWeather():
        city=textfield.get()
        from geopy.geocoders import Nominatim
        laptop_user_name = 'nandan'
        API_KEY = '80f4a58a086ed52d461fd91452e604ee'
        user_agent = f"{laptop_user_name}/1.0 (https://yourwebsite.com; your_email@example.com) {API_KEY}"
        # Initialize Nominatim with the constructed user agent
        try:
            global i
            global j
            geolocator = Nominatim(user_agent=user_agent)
            location = geolocator.geocode(city )
            print(location.address)
                #print((location.latitude, location.longitude))
            i = location.latitude
            j =  location.longitude
            print(type(i))
            print(i,j)
            latitude = i
            longitude = j
            timezone = WEATHER.find_timezone(latitude, longitude)
            print(f"The timezone for New York City is: {timezone}")
            timezoneis.config(text=timezone)
            long_lat.config(text=f'{i}°N,{j}°E')
        except:
            messagebox.showinfo("Weather App",f"City not found")
                         
        try:
                #weather 
                api_key =
                api = 
                link=f"https://api.openweathermap.org/data/2.5/weather?lat={i}&lon={j}&cnt=7&units=metric&daily&appid={api}"
                link_1="http://api.openweathermap.org/data/2.5/forecast"
                #base_url = 'http://api.openweathermap.org/data/2.5/weather'
                params = {'q': city, 'appid': api_key, 'units': 'metric'}  # You can change 'units' to 'imperial' for Fahrenheit
                json_data_2 = requests.get(link_1,params=params).json()
                json_data = requests.get(link).json()
                print(json_data)
                #response = requests.get(base_url, params=params)
                #data = response.json() 
                #print("Full API Response:", data)  # Add this line to print the entire response
                if json_data['cod'] == '404':
                    messagebox.showinfo("Weather App",json_data['message'])
                    return"City not found"
                TEMP =[]    ## i can creat dict
                HUM = []
                WIND = []
                DES = []
                PRES = []
                ICON = []
                if 'list' in json_data_2 :
                    datas = json_data_2['list'][:15]
                    for i in datas :
                        temp = i['main']['temp']
                        TEMP.append(temp)
                        hum = i['main']['humidity']
                        HUM.append(hum)
                        des = i['weather'][0]['description']
                        DES.append(des)
                        ico = i['weather'][0]['icon']
                        ICON.append(ico)
                        wid = i['wind']['speed']
                        WIND.append(wid)
                        pres = i['main']['pressure']
                        PRES.append(pres)
                else :
                     print(Fore.BLUE + ' no list')
                print(TEMP)
                print(ICON)
                print(DES)
                temperature = json_data["main"]["temp"]
                humidity = json_data["main"]["humidity"]
                pressure = json_data["main"]["pressure"]
                wind = json_data["wind"]["speed"]
                description = json_data["weather"][0]["description"]

                t.config(text=(temperature,"°C"),font="arial 9")
                h.config(text=(humidity,"%"),font="arial 9")
                p.config(text=(pressure/100000,"bar"),font="arial 9")  
                w.config(text=(wind,"km/hr"),font="arial 9")          
                d.config(text=description,font="arial 9")

                def weather_teller(argument):
                    engine = pyttsx3.init()
                    engine.say(argument)
                    #engine.save_to_file(text, 'hello.mp3')
                    engine.runAndWait()
                lst=["°Celcius","%","bar",'kilometer per hour','']
                lst1=[temperature,humidity,pressure,wind ,description]
                lst2=['tempreture','humiditiy','pressure','wind speed','and weather description']
                city_name = json_data_2['city']['name']
                print(city_name)
                kkkk = "current weather of ", city_name," is  "
                weather_teller(kkkk) 
                if True : 
                    for jj in range(len(lst2)) :
                        oooo = lst2[jj] ,'is' ,lst1[jj],lst[jj]
                        weather_teller(oooo)
                else :
                    print(Fore.RED+erro)

                    #firstcell
                tempday1= temperature
                day1temp.config(text=f"{tempday1}°C\n{description}")

                firstdayimg= json_data['weather'][0]['icon']
                print(firstdayimg)
                photo1=PhotoImage(file=f'C:\\Users\\Nandan\\Downloads\\mini_pro_img\\{firstdayimg}.png')
                firstimage=Label(firstframe,image=photo1,bg='#282829')
                firstimage.image=photo1
                firstimage.place(x=20,y=18)

                #secondcell                
                seconddayimg= ICON[1]
                photo2=ImageTk.PhotoImage(file=f'C:\\Users\\Nandan\\Downloads\\mini_pro_img\\{seconddayimg}.png')
                secondimg = Label(root,image=photo2,bg="#282829")
                secondimg.image=photo2
                secondimg.place(x=305,y=323)
                print(secondimg)
                tempday2= TEMP[1]
                day2temp.config(text=f"{tempday2}°C\n{DES[1]}")

                #3dr cell              
                thirddayimg= ICON[2]
                photo3=ImageTk.PhotoImage(file=f'C:\\Users\\Nandan\\Downloads\\mini_pro_img\\{thirddayimg}.png')
                thirdimg = Label(root,image=photo3,bg="#282829")
                thirdimg.image=photo3
                thirdimg.place(x=405,y=323)
                print(thirdimg)
                tempday3= TEMP[2]
                day3temp.config(text=f"{tempday3}°C\n{DES[2]}")

                #4th cell              
                fourthdayimg= ICON[3]
                photo4=ImageTk.PhotoImage(file=f'C:\\Users\\Nandan\\Downloads\\mini_pro_img\\{fourthdayimg}.png')
                fourthimg = Label(root,image=photo4,bg="#282829")
                fourthimg.image=photo4
                fourthimg.place(x=505,y=323)
                print(fourthimg)
                tempday4= TEMP[3]
                day4temp.config(text=f"{tempday4}°C\n{DES[3]}")

                #5th cell             
                fifthdayimg= ICON[4]
                photo5=ImageTk.PhotoImage(file=f'C:\\Users\\Nandan\\Downloads\\mini_pro_img\\{fifthdayimg}.png')
                fifthimg = Label(root,image=photo5,bg="#282829")
                fifthimg.image=photo5
                fifthimg.place(x=605,y=323)
                print(fifthimg)
                tempday5= TEMP[4]
                day5temp.config(text=f"{tempday5}°C\n{DES[4]}")

                #6th cell             
                sixthdayimg= ICON[5]
                photo6=ImageTk.PhotoImage(file=f'C:\\Users\\Nandan\\Downloads\\mini_pro_img\\{sixthdayimg}.png')
                sixthimage = Label(root,image=photo6,bg="#282829")
                sixthimage.image=photo6
                sixthimage.place(x=705,y=323)
                print(sixthimage)
                tempday6= TEMP[5]
                day6temp.config(text=f"{tempday6}°C\n{DES[5]}")

                #7th cell               
                seventhdayimg= ICON[6]
                photo7=ImageTk.PhotoImage(file=f'C:\\Users\\Nandan\\Downloads\\mini_pro_img\\{seventhdayimg}.png')
                seventhimg = Label(root,image=photo7,bg="#282829")
                seventhimg.image=photo7
                seventhimg.place(x=805,y=323)
                print(seventhimg)
                tempday7= TEMP[6]
                day7temp.config(text=f"{tempday7}°C\n{DES[6]}")

                #order of days in boxes
                first=datetime.now()
                day1.config(text=first.strftime('%A'))

                second=first+timedelta(days=1)
                day2.config(text=second.strftime("%A"))
                
                third=first+timedelta(days=2)
                day3.config(text=third.strftime("%A"))

                fourth=first+timedelta(days=3)
                day4.config(text=fourth.strftime("%A"))

                fifth=first+timedelta(days=4)
                day5.config(text=fifth.strftime("%A"))

                sixth=first+timedelta(days=5)
                day6.config(text=sixth.strftime("%A"))

                seventh=first+timedelta(days=6)
                day7.config(text=seventh.strftime("%A"))

                tt = time.localtime(time.time())
                localtime = time.asctime(tt)
                str = Fore.GREEN+"Current Time:" + time.asctime(tt)
                r = str.split(' ')
                rr = r[4].split(':')
                X = int(rr[2])
                rrr = f'{int(rr[0])}:{int(rr[1])}:{int(rr[2])}'
                #while True:
                clock.config(text=rrr) 
               
        except BaseException as e:
                #if data['cod'] == '404':
                    messagebox.showinfo("Weather App",f"City not found ,,,,{e}")
                    return"City not found"
               
class Repeate :
    def repeate_weather():
        WEATHER.getWeather()

def new_window():
    window=Tk()
    window.title('new window')
    window.geometry('200x100')
    window.configure(bg='red')
def menu_command():
    pass  
def ABOUT_US():
     #put file here
    print('hello i am nandan ')
    pass
def HELP_MENU():
    print("you asked for help")
class Change_BG:
    def change_bg():
        c = colorchooser.askcolor()
        cc = c[1]
        root.config(bg=cc)
        timezoneis.config(bg=cc)
        clock.config(bg=cc)
        myimage.config(bg=cc)
        long_lat.config(bg=cc)
        print(c[1])
    def change_bg_img():
        pass
#menu
menu = Menu(root)
file_menu = Menu(menu, tearoff=0)
open_menu = Menu(root,tearoff=0)
open_menu.add_command(label='open new window',command=new_window)
file_menu.add_cascade(label='new window',menu=open_menu)
file_menu.add_command(label="Open", command=menu_command)
file_menu.add_command(label="Save", command=menu_command)
file_menu.add_command(label="change bg", command=Change_BG.change_bg)
file_menu.add_command(label="change bg img", command=Change_BG.change_bg_img)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

about_menu =Menu(root,tearoff=10)
about_menu.add_command(label='About app',command=ABOUT_US)
about_menu.add_command(label='About modulse',command=ABOUT_US)
about_menu.add_command(label='About us',command=ABOUT_US)

help_menu = Menu(root,tearoff=0)
help_menu.add_command(label='Help',command=HELP_MENU)

menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="About", menu=about_menu)
menu.add_cascade(label="Help",menu=help_menu)

root.config(menu=menu)

Round_box=PhotoImage(file="Rounded Rectangle 1.png")
Label(root,image=Round_box, bg="black").place(x=30,y=110)

#Label
label1 = Label(root,text="Temprature  :",font=("Helvatica", 10),fg="white",bg='#203243')
label1.place(x=42,y=120)

label2 = Label(root,text="Humidity    :",font=("Helvatica", 10),fg="white", bg='#203243')
label2.place(x=42,y=140)

label3 = Label(root,text="Pressure   :",font=("Helvatica", 10),fg="white", bg='#203243')
label3.place(x=42,y=160)

label4 = Label(root,text="Wind Speed :",font=("Helvatica", 10),fg="white", bg='#203243')
label4.place(x=42,y=180)

label5 = Label(root,text="Description :",font=("Helvatica", 10),fg="white", bg='#203243')
label5.place(x=42,y=200)

#search box
Search_image=PhotoImage(file="Rounded Rectangle 3.png")
myimage=Label(image=Search_image,bg='black')
myimage.place(x=270,y=120)

weat_image=PhotoImage(file="Layer 7.png")
weatherimage = Label(root,image=weat_image,bg='#203243',border=0)
weatherimage.place(x=290,y=127)

textfield=tk.Entry(root,justif='center',width=15,font=('Helvatica',25,'bold'), bg='#203243',border=0,fg='white')
textfield.place(x=370,y=130)
textfield.focus()

Search_icon = PhotoImage(file='Layer 6.png')
myimage_search = Button(image=Search_icon,borderwidth=0,cursor='hand2', bg='#203243', command=WEATHER.getWeather,activebackground='#203243')
myimage_search.place(x=645,y=125)

#voice icon
mike_icon = PhotoImage(file="C:\\Users\\Nandan\\Downloads\\mini_pro_img\\mick_image.png")
myvoice_search = Button(image=mike_icon,borderwidth=0,cursor='hand2', bg='#203243', command=voice_recognizer,activebackground='#203243')
myvoice_search.place(x=613,y=134)

#repeat the weather
rpt = Button(text ='repeat',font='arial 8',bg='red',command=Repeate.repeate_weather)
rpt.place(x=110,y=230)

#Bttom Box
frame=Frame(root,width=900,height=180,bg="#203243")
frame.pack(side=BOTTOM)

#bottom boxes
firstbox=PhotoImage(file='Rounded Rectangle 2.png')
secondbox=PhotoImage(file='Rounded Rectangle 2 copy.png')

Label(frame,image=firstbox,bg='red').place(x=30, y=20)       ####  bg = red        #########################################################################################
Label(frame,image=secondbox,bg='#203243').place(x=300, y=10)
Label(frame,image=secondbox,bg='#203243').place(x=400, y=10)
Label(frame,image=secondbox,bg='#203243').place(x=500, y=10)
Label(frame,image=secondbox,bg='#203243').place(x=600, y=10)
Label(frame,image=secondbox,bg='#203243').place(x=700, y=10)
Label(frame,image=secondbox,bg='#203243').place(x=800, y=10)    

#clock(time)
clock = Label(root,text=' ',font=('Helvatica',30,'bold'), fg='white',bg='black')
clock.place(x=30,y=20) 
timezoneis = Label(root,font=('Helvatica',20), fg='white',bg='black')
timezoneis.place(x=680,y=20)

long_lat = Label(root,font=('Helvatica',10), fg='white',bg='black')
long_lat.place(x=680,y=50)

#thwpd
t=Label(root,font="Helvetica,11",fg="white",bg="#203243")
t.place(x=126,y=120)
h=Label(root,font="Helvetica,11",fg="white",bg="#203243")
h.place(x=126,y=140)
p=Label(root,font="Helvetica,11",fg="white",bg="#203243")
p.place(x=126,y=160)
w=Label(root,font="Helvetica,11",fg="white",bg="#203243")
w.place(x=126,y=180)
d=Label(root,font="Helvetica,11",fg="white",bg="#203243")
d.place(x=126,y=200)

#the first cell
firstframe=Frame(root,width=230,height=130,bg="#282829")
firstframe.place(x=35,y=315)

day1=Label(firstframe,font="arial 17",bg="#282829",fg="#fff")
day1.place(x=97,y=5)

day1temp=Label(firstframe,bg='#282829',fg="#57adff",font="arial 13 bold")
day1temp.place(x=80,y=57)

#seconf cell
secondframe=Frame(root,width=70,height=113,bg="#282829")
secondframe.place(x=305,y=306)

day2=Label(secondframe,font="arial 8",bg="#282829",fg="#fff")
day2.place(x=6,y=0)

day2temp=Label(secondframe,bg='#282829',fg="#57adff",font="arial 8 ")
day2temp.place(x=1,y=83)

#third cell
thirdframe=Frame(root,width=70,height=113,bg="#282829")
thirdframe.place(x=405,y=306)

day3=Label(thirdframe,font="arial 8",bg="#282829",fg="#fff")
day3.place(x=6,y=0)

day3temp=Label(thirdframe,bg='#282829',fg="#57adff",font="arial 8 ")
day3temp.place(x=1,y=83)

#fourthcell
fourthframe=Frame(root,width=70,height=113,bg="#282829")
fourthframe.place(x=505,y=306)

day4=Label(fourthframe,font="arial 8",bg="#282829",fg="#fff")
day4.place(x=6,y=0)

day4temp=Label(fourthframe,bg='#282829',fg="#57adff",font="arial 8 ")
day4temp.place(x=1,y=83)

#fifthcell
fifthframe=Frame(root,width=70,height=113,bg="#282829")
fifthframe.place(x=605,y=306)

day5=Label(fifthframe,font="arial 8",bg="#282829",fg="#fff")
day5.place(x=6,y=0)

day5temp=Label(fifthframe,bg='#282829',fg="#57adff",font="arial 8 ")
day5temp.place(x=1,y=83)

#sixthcell
sixthframe=Frame(root,width=70,height=113,bg="#282829")
sixthframe.place(x=705,y=306)

day6=Label(sixthframe,font="arial 8",bg="#282829",fg="#fff")
day6.place(x=6,y=0)

day6temp=Label(sixthframe,bg='#282829',fg="#57adff",font="arial 8 ")
day6temp.place(x=1,y=83)

#seventhcell
seventhframe=Frame(root,width=69,height=113,bg="#282829")
seventhframe.place(x=806,y=306)

day7=Label(seventhframe,font="arial 8",bg="#282829",fg="#fff")
day7.place(x=6,y=0)

day7temp=Label(seventhframe,bg='#282829',fg="#57adff",font="arial 8 ")
day7temp.place(x=1,y=83)

#l.place(x=90,y=8)


root.mainloop()#maybe paste code above -c