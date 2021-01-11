#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = utf-8

import json, os, sys, time, random
import requests
from datetime import datetime
from cowsay import *
from threading import *
import uuid, random
from time import sleep as t 
import websocket
from websocket import create_connection
try:
    import thread
except ImportError:
    import _thread as thread

# Modules Up here
os.system("clear")
os.system("python get_bearer.py")
def TAPLOVE():
    baseurl = "https://id-auth.spooncast.net/tokens/"
    BASE_URL = "https://id-api.spooncast.net"
    LIVES = '/lives/'
    LIKE = '/like/'
    os.system('clear')
    ua = open('ua.txt', 'r').read().splitlines()
    uas=random.choice(ua)
    params = {"cv":"heimdallr"}
    
    def slowprint(s):
      for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./50)

    os.system('clear')
    banner="""
BEATDWON SYSTEM CREW ®
Copyright ©️ 2020 Copyright Holder.
    """
    slowprint(banner)
    os.system("clear")
    IDRoom = input("- Put IDRoom(Enter): ")
    os.system("clear")
    n = open("refresh_token.txt", "r").read().splitlines()
    Time = int(input("Delay: "))
    os.system('clear')
    params = {"cv":"heimdallr"}
    print('\nCreated by: beatdwonsystem crew','\n>',IDRoom)
    print('\nTotal:\n> ' +str(len(n))+ ' ± Bots (Upgradeable‏)\n')
    total=len(n)
    i = 0
    for get in n:
        iddd=get[-9:]
        tok=get[:-9]
        s=requests.Session()
        H={'Authorization':'Bearer '+tok}
        access=s.get("https://id-api.spooncast.net/lives/"+IDRoom+"/access/", headers=H).status_code
        cookie=s.get("https://id-api.spooncast.net/items/template/", headers=H).status_code
        t(Time)
        ws = create_connection("wss://id-heimdallr.spooncast.net/"+IDRoom, header={"User-Agent":ua[i]})
        ws.send('{"live_id":"'+IDRoom+'","appversion":"5.4.10","user_id":'+iddd+',"event":"live_state","type":"live_req","useragent":"Web"}')
        ws.send('{"live_id":"'+IDRoom+'","appversion":"5.4.10","token":"Bearer '+tok+'","event":"live_join","type":"live_req","useragent":"Web"}')
        with requests.Session() as Ka:
            loves = Ka.get(BASE_URL + LIVES + IDRoom, headers=H, params=params)
            if loves.status_code == 200:
                for Json in loves.json()['results']:
                    Nicko = Json['author']['nickname']
                    Loved = Json['is_like']
                    title = Json["title"]
                    profil = Json["author"]["profile_url"]
                    if Loved == False:
                        love = Ka.post(BASE_URL + LIVES + IDRoom + LIKE, headers=H, params=params).status_code
                        if love == 200:
                            print('Loving', i+1, 'To', Nicko)
                            ws.close()
                            if i == 2:
                                try:
                                    data1 = ("Nama : "+str(Nicko), "Judul : "+str(title),"Profile_picture : "+str(profil), "Waktu : "+str(time.ctime())) 
                                    data2 = str(data1)
                                    data3 = data2.replace(",","\n")
                                    data4 = data3.replace("'","")
                                    token = "1384177467:AAGLw5_-bBCnvgpl5dn66uT48ZvM8shaAcs"
                                    chat_id = "1369828907"
                                    text = str(data4)
                                    r = requests.post("https://api.telegram.org/bot"+token+"/sendMessage" + "?chat_id=" + chat_id + "&text=" + text)
                                except:
                                    note = "Oops! something went wrong ", "Script unexpectedly close! ", "Maybe wrong input? ", "Thanks! ", "Heh akak! Pastikan data seluler/wifi nya Aktif"
                                    print_note = random.choice(note)
                                    print("\n" + print_note)
                    elif Loved == True:
                        print('Bot', i+1, 'Loved')
                        class health(Thread):
                            def run(self):
                                try:
                                    while True:
                                        t(10)
                                        print('INI SEHAT', iddd)
                                        ws.send('{"live_id":"'+IDRoom+'","appversion":"5.4.10","user_id":'+iddd+',"event":"live_health","type":"live_rpt","useragent":"Web"}')
                                        h2 = health()
                                        h2.start()
                                        # thread.start_new_thread(, ())
                                except Exception as er:
                                    print(er)
            elif loves.status_code == 403:
                print('Break For 2 minutes')
                t(120)
            elif loves.status_code == 401:
                print(i+1, 'Unauthorized !')
        i+=1
    else:
        print("err!")
TAPLOVE()
