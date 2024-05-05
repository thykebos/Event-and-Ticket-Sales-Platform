import tkinter as tk
from tkinter import ttk
from ttkthemes import *
from tkmacosx import *
from PIL import Image, ImageTk
import json
from datetime import datetime
import time

root = tk.Tk()
root.geometry('900x700')
root.title('IBIS TICKET')
style = ThemedStyle(root)
style.theme_use('yaru')


def kisi_bilgi():
    
    kullanici=kullanici_ad.get().strip()
    parola=kullanici_sifre.get()

    if kullanici and parola:
        kisi_bilgileri= {
        "kullanici": kullanici,
        "sifre": parola,
        }
        veri_tabani= json.dumps(kisi_bilgileri,ensure_ascii=False,indent=12)
        with open("kullanici_bilgi.json","a", encoding='utf-8') as file:
            file.write('\n'+veri_tabani+'\n')
        
        menu_ekrani()
    
    else:
        print("KULLANICI HATASI: eksik var")

biletler = ['Biletlerim']
def menu_ekrani():
    alan_kapla=('\n'*46)
    giris_alan=ttk.Label(root,background='#424124',text=alan_kapla,width=150)
    giris_alan.place(x=0,y=0)

    kategori_yazi= ttk.Label(root,text='Kategori Seçenekleri',background='#424124',font=('Verdana',20),foreground='white')
    kategori_yazi.place(x=300,y=70)

    uyari_yazi= ttk.Label(root,text='!!! Sistemimizde Sadece (Basketbol) Seçeneği Açıktır\n         Lütfen Farklı Tercihler Yapmayınız\n\n Alınan Biletler (biletlerim kısmına eklenir)',background='#424124',font=('Verdana',15),foreground='white')
    uyari_yazi.place(x=150,y=500)

    stil = ttk.Style()
    stil.configure("Horizontal.TSeparator", background="#424124")
    cizgi = ttk.Separator(root, orient='horizontal', style="Horizontal.TSeparator")
    cizgi.place(x=200, y=120, width=500)
    
    saat_yazi= ttk.Label(root,text=datetime.today().strftime('%Y-%m-%d | %H:%M'),background='#424124',font=('Verdana',15),foreground='white')
    saat_yazi.place(x=650,y=20)
    
    global secilen_biletler
    global biletler
    secilen_biletler = tk.StringVar()
    bilet_secenek = ttk.OptionMenu(root,secilen_biletler, biletler[0], *biletler)
    bilet_secenek.place(x=60,y=50)

    global secilen_spor
    global sporlar
    secilen_spor = tk.StringVar()
    sporlar = ['SPOR SEÇİNİZ','Basketbol','Futbol','Tenis','Su Topu','Beyzbol','e-Spor','At Yarışı','Kayak','Hentbol']
    spor_secenek = ttk.OptionMenu(root,secilen_spor, sporlar[0], *sporlar)
    spor_secenek.place(x=220,y=200)

    global secilen_muzik
    global muzikler
    secilen_muzik = tk.StringVar()
    muzikler = ['MÜZİK SEÇİNİZ','çok yakında..']
    muzik_secenek = ttk.OptionMenu(root,secilen_muzik, muzikler[0], *muzikler)
    muzik_secenek.place(x=390,y=200)

    global secilen_sahne
    global sahneler
    secilen_sahne = tk.StringVar()
    sahneler = ['SAHNE SEÇİNİZ','çok yakında..']
    sahne_secenek = ttk.OptionMenu(root,secilen_sahne, sahneler[0], *sahneler)
    sahne_secenek.place(x=560,y=200)

    ara_buton= ttk.Button(root,text=' ARA ',command=arama)
    ara_buton.place(x=405,y=430)

def arama():             #BU KISIM AYARLANICAAAKK    GİRİS BUTONUNUN COMMANDINI DEĞİŞTİRECEYİK    
    if secilen_spor.get() == sporlar[1]:
        alan_kapla=('\n'*46)
        giris_alan=ttk.Label(root,background='#424124',text=alan_kapla,width=150)
        giris_alan.place(x=0,y=0)

        global secilen_bilet_yazi
        secilen_bilet_yazi=ttk.Label(root,text='Seçilen Alan',background='#424124',font=('Verdana',15),foreground='white')
        secilen_bilet_yazi.place(x=100,y=500)
        global secilen_bilet
        secilen_bilet=ttk.Label(root,background='#424124',font=('Verdana',12),foreground='white')
        secilen_bilet.place(x=100,y=550)

        cizgi = ttk.Separator(root, orient='horizontal', style="Horizontal.TSeparator")
        cizgi.place(x=65, y=540, width=200)

        cizgi2 = ttk.Separator(root, orient='horizontal', style="Horizontal.TSeparator")
        cizgi2.place(x=210, y=460, width=500)     

        alan_bir=ttk.Label(root,background='#474747',text='\n\n',width=50,relief='raised')
        alan_bir.place(x=300,y=50)

        global bir_a
        bir_a=ttk.Button(root,text='1-A',width=3,command=lambda: bilet_islem(bir_a)) # x-y gibi parametreleri kolay yönetmemizi sağladı
        bir_a.place(x=330,y=55)
        global iki_a
        iki_a=ttk.Button(root,text='2-A',width=3,command=lambda: bilet_islem(iki_a))
        iki_a.place(x=430,y=55)
        global uc_a
        uc_a=ttk.Button(root,text='3-A',width=3,command=lambda: bilet_islem(uc_a))
        uc_a.place(x=530,y=55)

        alan_bir_ekstra=ttk.Label(root,background='#474747',text='\n                               KOMBİNE SAHİPLERİ',width=50,relief='raised',foreground='white')
        alan_bir_ekstra.place(x=300,y=110)
        alan_iki=ttk.Label(root,background='#474747',text='\n\n',width=20,relief='raised')
        alan_iki.place(x=660,y=50)
        alan_uc=ttk.Label(root,background='#474747',text='\n\n\n\n\n\n\n',width=9,relief='raised')
        alan_uc.place(x=780,y=50)

        global bir_u
        bir_u=ttk.Button(root,text='1-U',width=3,command=lambda: bilet_islem(bir_u))
        bir_u.place(x=700,y=55)
        global iki_u
        iki_u=ttk.Button(root,text='2-U',width=3,command=lambda: bilet_islem(iki_u))
        iki_u.place(x=785,y=95)

        alan_dort=ttk.Label(root,background='#474747',text='\n\n',width=20,relief='raised')
        alan_dort.place(x=660,y=375)
        alan_bes=ttk.Label(root,background='#474747',text='\n\n\n\n\n\n\n',width=9,relief='raised')
        alan_bes.place(x=780,y=300)

        global bir_g
        bir_g=ttk.Button(root,text='1-G',width=3,command=lambda: bilet_islem(bir_g))
        bir_g.place(x=700,y=380)
        global iki_g
        iki_g=ttk.Button(root,text='2-G',width=3,command=lambda: bilet_islem(iki_g))
        iki_g.place(x=785,y=345)

        alan_yedi=ttk.Label(root,background='#474747',text='\n\n',width=50,relief='raised')
        alan_yedi.place(x=300,y=375)

        global bir_b
        bir_b=ttk.Button(root,text='1-B',width=3,command=lambda: bilet_islem(bir_b))
        bir_b.place(x=330,y=380)
        global iki_b
        iki_b=ttk.Button(root,text='2-B',width=3,command=lambda: bilet_islem(iki_b))
        iki_b.place(x=430,y=380)
        global uc_b
        uc_b=ttk.Button(root,text='3-B',width=3,command=lambda: bilet_islem(uc_b))
        uc_b.place(x=530,y=380)

        alan_yedi_ekstra=ttk.Label(root,background='#474747',text='\n',width=50,relief='raised')
        alan_yedi_ekstra.place(x=300,y=330)
        alan_sekiz=ttk.Label(root,background='#474747',text='\n\n',width=20,relief='raised')
        alan_sekiz.place(x=120,y=50)
        alan_dokuz=ttk.Label(root,background='#474747',text='\n\n\n\n\n\n\n',width=9,relief='raised')
        alan_dokuz.place(x=65,y=50)
        alan_on=ttk.Label(root,background='#474747',text='\n\n',width=20,relief='raised')
        alan_on.place(x=120,y=375)
        alan_onbir=ttk.Label(root,background='#474747',text='\n\n\n\n\n\n\n',width=9,relief='raised')
        alan_onbir.place(x=65,y=300)
         
        global bir_d
        bir_d=ttk.Button(root,text='1-D',width=3,command=lambda: bilet_islem(bir_d))
        bir_d.place(x=155,y=380)
        global iki_d
        iki_d=ttk.Button(root,text='2-D',width=3,command=lambda: bilet_islem(iki_d))
        iki_d.place(x=73,y=343)
        global bir_c
        bir_c=ttk.Button(root,text='1-C',width=3,command=lambda: bilet_islem(bir_c))
        bir_c.place(x=155,y=55)
        global iki_c
        iki_c=ttk.Button(root,text='2-C',width=3,command=lambda: bilet_islem(iki_c))
        iki_c.place(x=73,y=95)

        saha = Image.open('saha.png')  #PIL kütüphanesi kullanarak panele resim ekledik
        saha_boyut= saha.resize((480,200))
        saha = ImageTk.PhotoImage(saha_boyut)
        saha_label = tk.Label(root, image=saha,bg='#424124')
        saha_label.image = saha      
        saha_label.place(x=210, y=150)
        
        global bilet_al
        bilet_al=ttk.Button(root,text='BİLET AL',command=bilet_ekle)
        bilet_al.place(x=410,y=500)
    else:
        print("KULLANICI HATASI:")

biletlerim=[]
def bilet_islem(x):
    biletlerim.append(f'{x["text"]}')
    secilen_bilet.config(text="/  ".join(biletlerim)) #bilet al butonuna bu kısmı eklicez burdan kaldırıcaz
    x.config(state='disabled')
def bilet_ekle():
    if len(biletlerim) > 0:
        time.sleep(0.5)
        biletler.append(biletlerim)
        menu_ekrani()   

#
alan_kapla=('\n'*46)
giris_alan=ttk.Label(root,background='#424124',text=alan_kapla,width=150)
giris_alan.place(x=0,y=0)

logo = Image.open('logo.png')  #PIL kütüphanesi kullanarak panele resim ekledik
logo_boyut= logo.resize((170,170))
logo = ImageTk.PhotoImage(logo_boyut)
logo_label = tk.Label(root, image=logo,bg='#424124')
logo_label.place(x=340,y=30)

giris_buton= ttk.Button(root,text=' GİRİŞ YAP ',command=kisi_bilgi)
giris_buton.place(x=380,y=500)

ad_yazi= ttk.Label(root,text=' Kullanıcı adı: ',background='#424124',font=('Verdana',12),foreground='white')
ad_yazi.place(x=320,y=315)
kullanici_ad=ttk.Entry(root,width=25,font=('Verdana',10))
kullanici_ad.place(x=320,y=340)

sifre_yazi= ttk.Label(root,text=' Şifre: ',background='#424124',font=('Verdana',12),foreground='white')
sifre_yazi.place(x=320,y=415)
kullanici_sifre=ttk.Entry(root,width=25,font=('Verdana',10),show='*')
kullanici_sifre.place(x=320,y=440)



root.mainloop()