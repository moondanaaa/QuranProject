from tkinter import *
from tkinter import ttk
import pandas as pd

import pygame


fnt = ('Milkshake', 10)


win = Tk()
pygame.mixer.init()

wrapper1 = LabelFrame(win)
wrapper2 = LabelFrame(win)

mycanvas = Canvas(wrapper1)
mycanvas.pack(side=LEFT, fill="both", expand="yes")

yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

myframe = Frame(mycanvas)
mycanvas.create_window((0, 0), window=myframe, anchor="nw")

label1 = Label(wrapper2, text="Choose Surah for display text")
label1.pack()


wrapper1.pack(fill="both", expand="yes")
wrapper2.pack(fill="both", expand="yes")

win.geometry("600x600")
win.resizable(False, False)
win.title('Quran')


def get_surah_text(number):
    df = pd.read_csv('Quran_data.csv')
    df = df[df['SurahNumber'] == number]

    text = []
    for i in df.values:
        text.append(f'{i[7]}: {i[8]}')

    return "\n".join(text)


def su1():
    pygame.mixer.music.load("surah/001.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(1))


def su2():
    pygame.mixer.music.load("surah/002.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(2))


def su3():
    pygame.mixer.music.load("surah/003.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(3))


def su4():
    pygame.mixer.music.load("surah/004.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(4))


def su5():
    pygame.mixer.music.load("surah/005.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(5))


def su6():
    pygame.mixer.music.load("surah/006.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(6))


def su7():
    pygame.mixer.music.load("surah/007.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(7))


def su8():
    pygame.mixer.music.load("surah/008.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(8))


def su9():
    pygame.mixer.music.load("surah/009.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(9))


def su10():
    pygame.mixer.music.load("surah/010.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(10))


def su11():
    pygame.mixer.music.load("surah/011.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(11))


def su12():
    pygame.mixer.music.load("surah/012.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(12))


def su13():
    pygame.mixer.music.load("surah/013.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(13))


def su14():
    pygame.mixer.music.load("surah/014.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(14))


def su15():
    pygame.mixer.music.load("surah/015.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(15))


def su16():
    pygame.mixer.music.load("surah/016.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(16))


def su17():
    pygame.mixer.music.load("surah/017.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(17))


def su18():
    pygame.mixer.music.load("surah/018.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(18))


def su19():
    pygame.mixer.music.load("surah/019.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(19))


def su20():
    pygame.mixer.music.load("surah/020.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(20))


def su21():
    pygame.mixer.music.load("surah/021.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(21))


def su22():
    pygame.mixer.music.load("surah/022.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(22))


def su23():
    pygame.mixer.music.load("surah/023.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(23))


def su24():
    pygame.mixer.music.load("surah/024.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(24))


def su25():
    pygame.mixer.music.load("surah/025.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(25))


def su26():
    pygame.mixer.music.load("surah/026.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(26))


def su27():
    pygame.mixer.music.load("surah/027.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(27))


def su28():
    pygame.mixer.music.load("surah/028.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(28))


def su29():
    pygame.mixer.music.load("surah/029.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(29))


def su30():
    pygame.mixer.music.load("surah/030.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(30))


def su31():
    pygame.mixer.music.load("surah/031.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(31))


def su32():
    pygame.mixer.music.load("surah/032.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(32))


def su33():
    pygame.mixer.music.load("surah/033.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(33))


def su34():
    pygame.mixer.music.load("surah/034.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(34))


def su35():
    pygame.mixer.music.load("surah/035.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(35))


def su36():
    pygame.mixer.music.load("surah/036.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(36))


def su37():
    pygame.mixer.music.load("surah/037.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(37))


def su38():
    pygame.mixer.music.load("surah/038.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(38))


def su39():
    pygame.mixer.music.load("surah/039.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(39))


def su40():
    pygame.mixer.music.load("surah/040.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(40))


def su41():
    pygame.mixer.music.load("surah/041.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(41))


def su42():
    pygame.mixer.music.load("surah/042.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(42))


def su43():
    pygame.mixer.music.load("surah/043.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(43))


def su44():
    pygame.mixer.music.load("surah/044.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(44))


def su45():
    pygame.mixer.music.load("surah/045.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(45))


def su46():
    pygame.mixer.music.load("surah/046.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(46))


def su47():
    pygame.mixer.music.load("surah/047.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(47))


def su48():
    pygame.mixer.music.load("surah/048.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(48))


def su49():
    pygame.mixer.music.load("surah/049.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(49))


def su50():
    pygame.mixer.music.load("surah/050.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(50))


def su51():
    pygame.mixer.music.load("surah/051.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(51))


def su52():
    pygame.mixer.music.load("surah/052.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(52))


def su53():
    pygame.mixer.music.load("surah/053.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(53))


def su54():
    pygame.mixer.music.load("surah/054.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(54))


def su55():
    pygame.mixer.music.load("surah/055.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(55))


def su56():
    pygame.mixer.music.load("surah/056.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(56))


def su57():
    pygame.mixer.music.load("surah/057.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(57))


def su58():
    pygame.mixer.music.load("surah/058.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(58))


def su59():
    pygame.mixer.music.load("surah/059.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(59))


def su60():
    pygame.mixer.music.load("surah/060.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(6))


def su61():
    pygame.mixer.music.load("surah/061.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(61))


def su62():
    pygame.mixer.music.load("surah/062.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(62))


def su63():
    pygame.mixer.music.load("surah/063.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(63))


def su64():
    pygame.mixer.music.load("surah/064.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(64))


def su65():
    pygame.mixer.music.load("surah/065.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(65))


def su66():
    pygame.mixer.music.load("surah/066.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(66))


def su67():
    pygame.mixer.music.load("surah/067.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(67))


def su68():
    pygame.mixer.music.load("surah/068.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(68))


def su69():
    pygame.mixer.music.load("surah/069.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(69))


def su70():
    pygame.mixer.music.load("surah/070.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(70))


def su71():
    pygame.mixer.music.load("surah/071.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(71))


def su72():
    pygame.mixer.music.load("surah/072.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(72))


def su73():
    pygame.mixer.music.load("surah/073.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(73))


def su74():
    pygame.mixer.music.load("surah/074.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(74))


def su75():
    pygame.mixer.music.load("surah/075.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(75))


def su76():
    pygame.mixer.music.load("surah/076.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(76))


def su77():
    pygame.mixer.music.load("surah/077.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(77))


def su78():
    pygame.mixer.music.load("surah/078.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(78))


def su79():
    pygame.mixer.music.load("surah/079.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(79))


def su80():
    pygame.mixer.music.load("surah/080.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(80))


def su81():
    pygame.mixer.music.load("surah/081.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(81))


def su82():
    pygame.mixer.music.load("surah/082.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(82))


def su83():
    pygame.mixer.music.load("surah/083.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(83))


def su84():
    pygame.mixer.music.load("surah/084.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(84))


def su85():
    pygame.mixer.music.load("surah/085.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(85))


def su86():
    pygame.mixer.music.load("surah/086.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(86))


def su87():
    pygame.mixer.music.load("surah/087.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(87))


def su88():
    pygame.mixer.music.load("surah/088.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(88))


def su89():
    pygame.mixer.music.load("surah/089.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(89))


def su90():
    pygame.mixer.music.load("surah/090.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(90))


def su91():
    pygame.mixer.music.load("surah/091.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(91))


def su92():
    pygame.mixer.music.load("surah/092.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(92))


def su93():
    pygame.mixer.music.load("surah/093.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(93))


def su94():
    pygame.mixer.music.load("surah/094.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(94))


def su95():
    pygame.mixer.music.load("surah/095.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(95))


def su96():
    pygame.mixer.music.load("surah/096.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(96))


def su97():
    pygame.mixer.music.load("surah/097.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(97))


def su98():
    pygame.mixer.music.load("surah/098.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(98))


def su99():
    pygame.mixer.music.load("surah/099.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(99))


def su100():
    pygame.mixer.music.load("surah/100.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(10))


def su101():
    pygame.mixer.music.load("surah/101.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(101))


def su102():
    pygame.mixer.music.load("surah/102.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(102))


def su103():
    pygame.mixer.music.load("surah/103.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(103))


def su104():
    pygame.mixer.music.load("surah/104.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(104))


def su105():
    pygame.mixer.music.load("surah/105.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(105))


def su106():
    pygame.mixer.music.load("surah/106.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(106))


def su107():
    pygame.mixer.music.load("surah/107.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(107))


def su108():
    pygame.mixer.music.load("surah/108.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(108))


def su109():
    pygame.mixer.music.load("surah/109.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(109))


def su110():
    pygame.mixer.music.load("surah/110.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(110))


def su111():
    pygame.mixer.music.load("surah/111.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(111))


def su112():
    pygame.mixer.music.load("surah/112.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(112))


def su113():
    pygame.mixer.music.load("surah/113.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(113))


def su114():
    pygame.mixer.music.load("surah/114.mp3")
    pygame.mixer.music.play(loops=0)
    label1.config(text=get_surah_text(114))


# buttons
fatihah = Button(myframe, text='Al-Fatihah', font=fnt, command=su1).pack()
baqarah = Button(myframe, text='Al-Baqarah', font=fnt, command=su2).pack()
imran = Button(myframe, text='Al-Imran', font=fnt, command=su3).pack()
nisaa = Button(myframe, text='An-Nisaa', font=fnt, command=su4).pack()
maaidah = Button(myframe, text='Al-Maaidah', font=fnt, command=su5).pack()
anaam = Button(myframe, text='Al-Anaam', font=fnt, command=su6).pack()
aaraf = Button(myframe, text='Al-Aaraf', font=fnt, command=su7).pack()
anfal = Button(myframe, text='Al-Anfal', font=fnt, command=su8).pack()
taubah = Button(myframe, text='At-Taubah', font=fnt, command=su9).pack()
yunus = Button(myframe, text='Yunus', font=fnt, command=su10).pack()
hood = Button(myframe, text='Hood', font=fnt, command=su11).pack()
yusuf = Button(myframe, text='Yusuf', font=fnt, command=su12).pack()
raad = Button(myframe, text='Ar-Raad', font=fnt, command=su13).pack()
ibrahim = Button(myframe, text='Ibrahim', font=fnt, command=su14).pack()
hijr = Button(myframe, text='Al-Hijr', font=fnt, command=su15).pack()
nahl = Button(myframe, text='An-NAhl', font=fnt, command=su16).pack()
isra = Button(myframe, text='Al-Isra', font=fnt, command=su17).pack()
kahf = Button(myframe, text='Al-Kahf', font=fnt, command=su18).pack()
maryam = Button(myframe, text='Maryam', font=fnt, command=su19).pack()
taha = Button(myframe, text='TaHa', font=fnt, command=su20).pack()
anbiyaa = Button(myframe, text='Al-Anbiyaa', font=fnt, command=su21).pack()
hajj = Button(myframe, text='Al-Hajj', font=fnt, command=su22).pack()
muminum = Button(myframe, text='Al-Muminum', font=fnt, command=su23).pack()
nur = Button(myframe, text='An-Nur', font=fnt, command=su24).pack()
furqan = Button(myframe, text='Al-Furqan', font=fnt, command=su25).pack()
shuaraa = Button(myframe, text='Ash-Shuaraa', font=fnt, command=su26).pack()
naml = Button(myframe, text='An-Naml', font=fnt, command=su27).pack()
qasas = Button(myframe, text='Al-Qasas', font=fnt, command=su28).pack()
aankabut = Button(myframe, text='Al-Aankabut', font=fnt, command=su29).pack()
arroom = Button(myframe, text='ArRoom', font=fnt, command=su30).pack()
luqman = Button(myframe, text='Luqman', font=fnt, command=su31).pack()
assajdah = Button(myframe, text='AsSajdah', font=fnt, command=su32).pack()
alahzab = Button(myframe, text='AlAhzab', font=fnt, command=su33).pack()
sabaa = Button(myframe, text='Sabaa', font=fnt, command=su34).pack()
fatir = Button(myframe, text='Fatir', font=fnt, command=su35).pack()
yasin = Button(myframe, text='YaSin', font=fnt, command=su36).pack()
saffat = Button(myframe, text='As-Saffat', font=fnt, command=su37).pack()
sad = Button(myframe, text='Sad', font=fnt, command=su38).pack()
zumar = Button(myframe, text='Az-Zumar', font=fnt, command=su39).pack()
ghafir = Button(myframe, text='Ghafir', font=fnt, command=su40).pack()
fussilat = Button(myframe, text='Fussilat', font=fnt, command=su41).pack()
shura = Button(myframe, text='Ash-Shura', font=fnt, command=su42).pack()
zukhruf = Button(myframe, text='Az-Zukhruf', font=fnt, command=su43).pack()
dukhan = Button(myframe, text='Ad-Dukhan', font=fnt, command=su44).pack()
jathiya = Button(myframe, text='Al-Jathiya', font=fnt, command=su45).pack()
ahqaf = Button(myframe, text='Al-Ahqaf', font=fnt, command=su46).pack()
muhammad = Button(myframe, text='Muhammad', font=fnt, command=su47).pack()
fath = Button(myframe, text='Al-Fath', font=fnt, command=su48).pack()
hujurat = Button(myframe, text='Al-Hujurat', font=fnt, command=su49).pack()
qaf = Button(myframe, text='Qaf', font=fnt, command=su50).pack()
zariyat = Button(myframe, text='Az-Zariyat', font=fnt, command=su51).pack()
tur = Button(myframe, text='At-Tur', font=fnt, command=su52).pack()
najm = Button(myframe, text='An-Najm', font=fnt, command=su53).pack()
qamar = Button(myframe, text='Al-Qamar', font=fnt, command=su54).pack()
rahman = Button(myframe, text='Ar-Rahman', font=fnt, command=su55).pack()
waqiah = Button(myframe, text='Al-Waqiyah', font=fnt, command=su56).pack()
hadid = Button(myframe, text='Al-Hadid', font=fnt, command=su57).pack()
mujadilah = Button(myframe, text='Al-Mujadilah', font=fnt, command=su58).pack()
nashr = Button(myframe, text='Al-NAshr', font=fnt, command=su59).pack()
mumtahinah = Button(myframe, text='Al-Mumtahinah', font=fnt, command=su60).pack()
saff = Button(myframe, text='As-Saff', font=fnt, command=su61).pack()
jumuah = Button(myframe, text='Al-Jumuah', font=fnt, command=su62).pack()
munafiqun = Button(myframe, text='Al-Munafiqun', font=fnt, command=su63).pack()
taghabun = Button(myframe, text='At-Taghabun', font=fnt, command=su64).pack()
talaq = Button(myframe, text='at-Talaq', font=fnt, command=su65).pack()
tahrim = Button(myframe, text='At-Tahrim', font=fnt, command=su66).pack()
mulk = Button(myframe, text='Al-Mulk', font=fnt, command=su67).pack()
qalam = Button(myframe, text='Al-Qalam', font=fnt, command=su68).pack()
haqqah = Button(myframe, text='Al-Haqqah', font=fnt, command=su69).pack()
maarij = Button(myframe, text='Al-Maarij', font=fnt, command=su70).pack()
nooh = Button(myframe, text='Nooh', font=fnt, command=su71).pack()
jinn = Button(myframe, text='Al-Jinn', font=fnt, command=su72).pack()
muzzammil = Button(myframe, text='Al-Muzzammil', font=fnt, command=su73).pack()
muddaththir = Button(myframe, text='Al-Muddaththir', font=fnt, command=su74).pack()
qiyamah = Button(myframe, text='Al-Qiyamah', font=fnt, command=su75).pack()
insan = Button(myframe, text='Al-Insan', font=fnt, command=su76).pack()
mursalat = Button(myframe, text='Al-Mursalat', font=fnt, command=su77).pack()
nabaa = Button(myframe, text='An-Nabaa', font=fnt, command=su78).pack()
naziat = Button(myframe, text='An-Naziat', font=fnt, command=su79).pack()
aabasa = Button(myframe, text='Aabasa', font=fnt, command=su80).pack()
takwir = Button(myframe, text='At-Takwir', font=fnt, command=su81).pack()
infitar = Button(myframe, text='Al-Infitar', font=fnt, command=su82).pack()
mutaffifin = Button(myframe, text='Al-Mutaffifin', font=fnt, command=su83).pack()
inshiqaq = Button(myframe, text='Al-Inshiqaq', font=fnt, command=su84).pack()
buruj = Button(myframe, text='Al-Buruj', font=fnt, command=su85).pack()
tariq = Button(myframe, text='At-Tariq', font=fnt, command=su86).pack()
aala = Button(myframe, text='Al-Aala', font=fnt, command=su87).pack()
ghashiyah = Button(myframe, text='Al-Ghashiyah', font=fnt, command=su88).pack()
fajr = Button(myframe, text='Al-Fajr', font=fnt, command=su89).pack()
balad = Button(myframe, text='Al-Balad', font=fnt, command=su90).pack()
shams = Button(myframe, text='Ash-Shams', font=fnt, command=su91).pack()
lail = Button(myframe, text='Al-Lail', font=fnt, command=su92).pack()
duha = Button(myframe, text='Ad-Duha', font=fnt, command=su93).pack()
sharf = Button(myframe, text='Ash-Sharf', font=fnt, command=su94).pack()
tin = Button(myframe, text='At-Tin', font=fnt, command=su95).pack()
aalaq = Button(myframe, text='Al-Aalaq', font=fnt, command=su96).pack()
qadr = Button(myframe, text='Al-Qadr', font=fnt, command=su97).pack()
baiyinah = Button(myframe, text='Al-Baiyinah', font=fnt, command=su98).pack()
zalzalah = Button(myframe, text='Az-Zalzalah', font=fnt, command=su99).pack()
aadiyat = Button(myframe, text='Al-Aadiyat', font=fnt, command=su100).pack()
qariah = Button(myframe, text='Al-Qariyah', font=fnt, command=su101).pack()
takathur = Button(myframe, text='At-Takathur', font=fnt, command=su102).pack()
aasr = Button(myframe, text='Al-Aasr', font=fnt, command=su103).pack()
humazah = Button(myframe, text='Al-Humazah', font=fnt, command=su104).pack()
fil = Button(myframe, text='Al-Fil', font=fnt, command=su105).pack()
quraish = Button(myframe, text='Quraish', font=fnt, command=su106).pack()
maaun = Button(myframe, text='Al-Maaun', font=fnt, command=su107).pack()
kauthar = Button(myframe, text='Al-Kauthar', font=fnt, command=su108).pack()
kafirun = Button(myframe, text='Al-Kafirun', font=fnt, command=su109).pack()
nasr = Button(myframe, text='An-Nasr', font=fnt, command=su110).pack()
masad = Button(myframe, text='Al-Masad', font=fnt, command=su111).pack()
ikhilas = Button(myframe, text='Al-Ikhilas', font=fnt, command=su112).pack()
falaq = Button(myframe, text='Al-Falaq', font=fnt, command=su113).pack()
nas = Button(myframe, text='An-Nas', font=fnt, command=su114).pack()

win.mainloop()
