# ENJOY OPEN SOURCE AUTO CREATE FB 
# AUTHOR : ETHAN KLEIN HUILEN
# GITHUB  : MR-ERROR-708
# STATUS  : FREE VERSION - NO RESTRICTIONS
# THANK YOU.

import os,sys,re,time,json,requests,urllib.parse,bs4,string,random,uuid,threading
from faker import Faker
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
import urllib3
import socket
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
socket.setdefaulttimeout(10)

# Color codes
white="\x1b[1;97m";yelloww="\033[1;33m";green="\x1b[38;5;49m";G0="\x1b[38;5;155m";green1='\x1b[38;5;154m';G2='\x1b[38;5;47m';G3='\x1b[38;5;48m';G4='\x1b[38;5;49m';G5='\x1b[38;5;50m';G6="\x1b[38;5;52m";s="\033[0m";W="\033[1;30m";Y="\x1b[1;93m";red="\x1b[38;5;160m";B="\033[1;95m";BE="\x1b[1;35m";X="\x1b[1;96m";Z="\x1b[1;95m";Y="\033[1;93m";U="\033[1;94m";V="\033[38;5;47m";T="\033[38;5;48m";Q="\033[38;5;49m";P="\033[38;5;50m";O="\033[38;5;51m";N="\033[38;5;52m";M="\x1b[38;5;205m";L="\033[96;1m";K="\x1b[1;91m";WH="\033[1;97m";orange="\x1b[38;5;196m";yellow="\x1b[38;5;208m";black="\033[1;30m";rad="\x1b[38;5;160m";YLW="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu="\033[1;47m";pvt="\033[1;0m";gren="\x1b[38;5;154m";gas="\033[1;32m"
style=f"\033[1;37m[\033[1;32m●\033[1;37m]"
stylee=f"\033[1;37m[\033[1;31m!\033[1;37m]"

# Permission check
try:
    os.system('rm -rf /sdcard/.txt');os.system('clear');open('/sdcard/.txt','w').write(' ')
except PermissionError:
    os.system("clear" if os.name == "posix" else "cls")
    print(f"{style} \033[1;32mMRERROR_AUTOFB TOOL IS NOT ALLOW WITHOUT STORAGE PERMISSION");os.system('termux-setup-storage');os.system('clear');exit(f"{style} \033[1;32mRUN AGAIN : python create.py")

# File path
BASE_PATH="/sdcard/MRERROR_AUTOFB/"
os.makedirs(BASE_PATH,exist_ok=True)
def append_line(filename,text):
    with open(os.path.join(BASE_PATH,filename),"a",encoding="utf-8") as f:
        f.write(text+"\n")

# Internet check
try:
    requests.get("https://www.google.com", timeout=5)
except requests.exceptions.ConnectionError:
    os.system("clear" if os.name == "posix" else "cls")
    print(f"{stylee} \033[1;31mNO INTERNET CONNECTION")
    print(f"\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    sys.exit()

# Opening moment
print(f'{style} \033[1;32mCHECKING UPDATED...\033[1;37m');time.sleep(2)
try:
    os.system("git pull")
except:
    pass
time.sleep(2);os.system("clear")

# Module check
try:import pystyle
except ImportError:print(f'{style} \033[1;32mINSTALLING PYSTYLE...\033[1;37m');time.sleep(0.5);os.system('pip install pystyle');import pystyle;os.system('clear')
from pystyle import Colors,Colorate

# User agent functions
def get_fake_desktop_ua():
    desktop_uas = [
        {
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
            "width": 1920,
            "browser": "Microsoft Edge",
            "version": "138",
            "full_version_list": '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.184", "Microsoft Edge";v="138.0.3351.121"'
        },
        {
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) "
                  "Gecko/20100101 Firefox/119.0",
            "width": 1920,
            "browser": "Firefox",
            "version": "119",
            "full_version_list": '"Firefox";v="119.0"'
        },
        {
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/138.0.0.0 Safari/537.36",
            "width": 1920,
            "browser": "Chromium",
            "version": "138",
            "full_version_list": '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.184"'
        }
    ]
    return random.choice(desktop_uas)

def ____useragent____():
    version = random.choice(['14','15','10','13','7.0.0','7.1.1','9','12','11','9.0','8.0.0','7.1.2','7.0','4','5','4.4.2','5.1.1','6.0.1','9.0.1'])
    model = random.choice(['SM-G973F','SM-G965F','SM-A505F','SM-N975F','Pixel 6','Pixel 7','CPH2399','CPH2401','A54','A55','Reno 8','Find X3'])
    build = random.choice(['MMB29Q','R16NW','LRX22C','KTU84P','JLS36C','NJH47F','PPR1.180610.011','QP1A.190711.020','NRD90M','RP1A.200720.012'])
    ver = str(random.choice(range(77,577)))
    ver2 = str(random.choice(range(57,77)))
    return f'Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'

# Fake name generators for all 32 countries
def fake_philippines():
    first=Faker('en_PH').first_name()
    last=Faker('en_PH').last_name()
    return first,last

def fake_indonesia():
    first=Faker('id_ID').first_name()
    last=Faker('id_ID').last_name()
    return first,last

def fake_japanese():
    first=Faker('ja_JP').first_name()
    last=Faker('ja_JP').last_name()
    return first,last

def fake_bangladesh():
    first=Faker('bn_BD').first_name()
    last=Faker('bn_BD').last_name()
    return first,last

def fake_nigeria():
    first=Faker('en_NG').first_name()
    last=Faker('en_NG').last_name()
    return first,last 

def fake_vietnamese():
    first=Faker('vi_VN').first_name()
    last=Faker('vi_VN').last_name()
    return first,last

def fake_chinese():
    first=Faker('zh_CN').first_name()
    last=Faker('zh_CN').last_name()
    return first,last

def fake_spanish():
    first=Faker('es_ES').first_name()
    last=Faker('es_ES').last_name()
    return first,last

def fake_thailand():
    first=Faker('th_TH').first_name()
    last=Faker('th_TH').last_name()
    return first,last

def fake_frenchcanadian():
    first=Faker('fr_CA').first_name()
    last=Faker('fr_CA').last_name()
    return first,last

def fake_australia():
    first=Faker('en_AU').first_name()
    last=Faker('en_AU').last_name()
    return first,last

def fake_turkey():
    first=Faker('tr_TR').first_name()
    last=Faker('tr_TR').last_name()
    return first,last

def fake_iceland():
    first=Faker('is_IS').first_name()
    last=Faker('is_IS').last_name()
    return first,last

def fake_ukraine():
    first=Faker('uk_UA').first_name()
    last=Faker('uk_UA').last_name()
    return first,last

def fake_denmark():
    first=Faker('da_DK').first_name()
    last=Faker('da_DK').last_name()
    return first,last

def fake_russian():
    first=Faker('ru_RU').first_name()
    last=Faker('ru_RU').last_name()
    return first,last

def fake_netherland():
    first=Faker('nl_NL').first_name()
    last=Faker('nl_NL').last_name()
    return first,last

def fake_bhutan():
    first=Faker('en_IN').first_name()
    last=Faker('en_IN').last_name()
    return first,last

def fake_greek():
    first=Faker('el_GR').first_name()
    last=Faker('el_GR').last_name()
    return first,last

def fake_french():
    first=Faker('fr_FR').first_name()
    last=Faker('fr_FR').last_name()
    return first,last

def fake_portugal():
    first=Faker('pt_PT').first_name()
    last=Faker('pt_PT').last_name()
    return first,last

def fake_norwegian():
    first=Faker('no_NO').first_name()
    last=Faker('no_NO').last_name()
    return first,last

def fake_israel():
    first=Faker('he_IL').first_name()
    last=Faker('he_IL').last_name()
    return first,last

def fake_italian():
    first=Faker('it_IT').first_name()
    last=Faker('it_IT').last_name()
    return first,last

def fake_romania():
    first=Faker('ro_RO').first_name()
    last=Faker('ro_RO').last_name()
    return first,last

def fake_unitedkingdom():
    first=Faker('en_GB').first_name()
    last=Faker('en_GB').last_name()
    return first,last

def fake_persian():
    first=Faker('fa_IR').first_name()
    last=Faker('fa_IR').last_name()
    return first,last

def fake_taiwan():
    first=Faker('zh_TW').first_name()
    last=Faker('zh_TW').last_name()
    return first,last

def fake_turkish():
    first=Faker('tr_TR').first_name()
    last=Faker('tr_TR').last_name()
    return first,last

def fake_slovenia():
    first=Faker('sl_SI').first_name()
    last=Faker('sl_SI').last_name()
    return first,last

def fake_finland():
    first=Faker('fi_FI').first_name()
    last=Faker('fi_FI').last_name()
    return first,last

def fake_yemen():
    first=Faker('ar').first_name()
    last=Faker('ar').last_name()
    return first,last

# Extractor
def extractor(data):
    try:
        soup=BeautifulSoup(data,"html.parser")
        data={}
        for inputs in soup.find_all("input"):
            name=inputs.get("name")
            value=inputs.get("value")
            if name:
                data[name]=value
        return data
    except Exception as e:
        return {"error":str(e)}

# Email generator
def fetch_domainss():
    domains = [
        "ketozie.com",
        "everythingispersonal.com",
        "novamails.my",
        "activationn.com",
        "flashmail.my"
    ]
    return domains

def generate_random_username(length: int = 8):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

def generate_random_email():
    domains=fetch_domainss()
    if not domains:
        return None
    username=generate_random_username()
    domain=random.choice(domains)
    return f'{username}@{domain}'

# Special line
def linex():
    print(f'\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# Banner
logo=(Colorate.Horizontal(Colors.green_to_white,r"""
    _  _   _ _____ ___     ___ ___ ___   _ _____ ___ 
   /_\| | | |_   _/ _ \   / __| _ \ __| /_\_   _| __|
  / _ \ |_| | | || (_) | | (__|   / _| / _ \| | | _| 
 /_/ \_\___/  |_| \___/   \___|_|_\___/_/ \_\_| |___|""" + " MR-ERROR"))

info=(f"""{style} \033[1;32mAUTHOR   \033[1;37m: \033[1;32mETHAN KLEIN HUILEN
{style} \033[1;32mTYPE     \033[1;37m: \033[1;32mAUTO CREATE FACEBOOK
{style} \033[1;32mSTATUS   \033[1;37m: \033[1;32mFREE VERSION
{style} \033[1;32mSYSTEM   \033[1;37m: \033[1;32mDATA/WIFI
{style} \033[1;32mVERSION  \033[1;37m: \033[1;32m2.0""")

def clear():
    os.system("clear" if os.name == "posix" else "cls");print(logo);linex();print(info);linex()

# Global variables
proxies_list=[]
proxies_lock=threading.Lock()
oks,loop,ua,ussr,tw,cps,plist,coki=[],0,[],[],[],[],[],[]

# Main menu
def main():
    clear();print(f'\033[1;37m[\033[1;32m01\033[1;37m]\033[1;32m START AUTO CREATE');print(f'\033[1;37m[\033[1;32m00\033[1;37m]\033[1;31m EXIT THIS PROGRAM');linex()
    auto_select=input(f'\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m CHOOSE \033[1;37m: \033[1;32m')
    if auto_select in ['1','01']:____create____()
    elif auto_select in ['0','00']:os.system("exit")
    else:main()

# Cookie parser
def parse_set_cookie(headers):
    raw_cookie=headers.get('Set-Cookie')
    cookies={}
    if not raw_cookie:
        return cookies,""
    parts=raw_cookie.split(',')
    temp=[]
    for part in parts:
        if '=' in part.split(';')[0]:
            temp.append(part.strip())
        else:
            if temp:
                temp[-1]+=','+part.strip()
    for ck in temp:
        kv=ck.split(';',1)[0]
        if '=' in kv:
            k,v=kv.split('=',1)
            cookies[k.strip()]=v.strip()
    cookie_str="sb=Cracked.By-Error_Tool;"+";".join(f"{k}={v}" for k,v in cookies.items())
    return cookies,cookie_str

# Safe extract
def safe_extract(pattern,text,default=""):
    m=re.search(pattern,text)
    return m.group(1) if m else default

# Dummy proxy function (original had get_random_proxy())
def get_random_proxy():
    return None

# Create menu
def ____create____():
    clear()
    print(f'{style} \033[1;32mALL COUNTRY NAMES WORKING')
    linex()
    print('\033[1;37m[\033[1;32m01\033[1;37m]\033[1;32m RANDOM PHILIPPINES NAMES')
    print('\033[1;37m[\033[1;32m02\033[1;37m]\033[1;32m RANDOM INDONESIA NAMES')
    print('\033[1;37m[\033[1;32m03\033[1;37m]\033[1;32m RANDOM JAPANESE NAMES')
    print('\033[1;37m[\033[1;32m04\033[1;37m]\033[1;32m RANDOM BANGLADESH NAMES')
    print('\033[1;37m[\033[1;32m05\033[1;37m]\033[1;32m RANDOM NIGERIA NAMES')
    print('\033[1;37m[\033[1;32m06\033[1;37m]\033[1;32m RANDOM VIETNAMESE NAMES')
    print('\033[1;37m[\033[1;32m07\033[1;37m]\033[1;32m RANDOM CHINESE NAMES')
    print('\033[1;37m[\033[1;32m08\033[1;37m]\033[1;32m RANDOM SPANISH NAMES')
    print('\033[1;37m[\033[1;32m09\033[1;37m]\033[1;32m RANDOM THAILAND NAMES')
    print('\033[1;37m[\033[1;32m10\033[1;37m]\033[1;32m RANDOM FRENCH CANADIAN NAMES')
    print('\033[1;37m[\033[1;32m11\033[1;37m]\033[1;32m RANDOM AUSTRALIA NAMES')
    print('\033[1;37m[\033[1;32m12\033[1;37m]\033[1;32m RANDOM TURKEY NAMES')
    print('\033[1;37m[\033[1;32m13\033[1;37m]\033[1;32m RANDOM ICELAND NAMES')
    print('\033[1;37m[\033[1;32m14\033[1;37m]\033[1;32m RANDOM UKRAINE NAMES')
    print('\033[1;37m[\033[1;32m15\033[1;37m]\033[1;32m RANDOM DENMARK NAMES')
    print('\033[1;37m[\033[1;32m16\033[1;37m]\033[1;32m RANDOM RUSSIAN NAMES')
    print('\033[1;37m[\033[1;32m17\033[1;37m]\033[1;32m RANDOM NETHERLAND NAMES')
    print('\033[1;37m[\033[1;32m18\033[1;37m]\033[1;32m RANDOM BHUTAN NAMES')
    print('\033[1;37m[\033[1;32m19\033[1;37m]\033[1;32m RANDOM GREEK NAMES')
    print('\033[1;37m[\033[1;32m20\033[1;37m]\033[1;32m RANDOM FRENCH NAMES')
    print('\033[1;37m[\033[1;32m21\033[1;37m]\033[1;32m RANDOM PORTUGAL NAMES')
    print('\033[1;37m[\033[1;32m22\033[1;37m]\033[1;32m RANDOM NORWEGIAN NAMES')
    print('\033[1;37m[\033[1;32m23\033[1;37m]\033[1;32m RANDOM ISRAEL NAMES')
    print('\033[1;37m[\033[1;32m24\033[1;37m]\033[1;32m RANDOM ITALIAN NAMES')
    print('\033[1;37m[\033[1;32m25\033[1;37m]\033[1;32m RANDOM ROMANIA NAMES')
    print('\033[1;37m[\033[1;32m26\033[1;37m]\033[1;32m RANDOM UNITED KINGDOM NAMES')
    print('\033[1;37m[\033[1;32m27\033[1;37m]\033[1;32m RANDOM PERSIAN NAMES')
    print('\033[1;37m[\033[1;32m28\033[1;37m]\033[1;32m RANDOM TAIWAN NAMES')
    print('\033[1;37m[\033[1;32m29\033[1;37m]\033[1;32m RANDOM TURKISH NAMES')
    print('\033[1;37m[\033[1;32m30\033[1;37m]\033[1;32m RANDOM SLOVENIA NAMES')
    print('\033[1;37m[\033[1;32m31\033[1;37m]\033[1;32m RANDOM FINLAND NAMES')
    print('\033[1;37m[\033[1;32m32\033[1;37m]\033[1;32m RANDOM YEMEN NAMES')
    linex()
    random_names_select=input(f'\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m CHOOSE \033[1;37m: \033[1;32m')
    clear()
    print(f'\033[1;37m[\033[1;32m01\033[1;37m]\033[1;32m AUTO PASSWORD COUNTRY')
    print(f'\033[1;37m[\033[1;32m02\033[1;37m]\033[1;32m AUTO CUSTOM PASSWORD')
    linex()
    auto_password_select=input(f'\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m CHOOSE \033[1;37m: \033[1;32m')
    
    auto_password_country_select = None
    password = None
    
    if auto_password_select in ['1','01']:
       clear()
       print(f'{style} \033[1;32mALL COUNTRY PASSWORD WORKING')
       linex()
       print('\033[1;37m[\033[1;32m01\033[1;37m]\033[1;32m AUTO PHILIPPINES PASSWORD')
       print('\033[1;37m[\033[1;32m02\033[1;37m]\033[1;32m AUTO INDONESIA PASSWORD')
       print('\033[1;37m[\033[1;32m03\033[1;37m]\033[1;32m AUTO JAPANESE PASSWORD')
       print('\033[1;37m[\033[1;32m04\033[1;37m]\033[1;32m AUTO BANGLADESH PASSWORD')
       print('\033[1;37m[\033[1;32m05\033[1;37m]\033[1;32m AUTO NIGERIA PASSWORD')
       print('\033[1;37m[\033[1;32m06\033[1;37m]\033[1;32m AUTO VIETNAMESE PASSWORD')
       print('\033[1;37m[\033[1;32m07\033[1;37m]\033[1;32m AUTO CHINESE PASSWORD')
       print('\033[1;37m[\033[1;32m08\033[1;37m]\033[1;32m AUTO SPANISH PASSWORD')
       print('\033[1;37m[\033[1;32m09\033[1;37m]\033[1;32m AUTO THAILAND PASSWORD')
       print('\033[1;37m[\033[1;32m10\033[1;37m]\033[1;32m AUTO FRENCH CANADIAN PASSWORD')
       print('\033[1;37m[\033[1;32m11\033[1;37m]\033[1;32m AUTO AUSTRALIA PASSWORD')
       print('\033[1;37m[\033[1;32m12\033[1;37m]\033[1;32m AUTO TURKEY PASSWORD')
       print('\033[1;37m[\033[1;32m13\033[1;37m]\033[1;32m AUTO ICELAND PASSWORD')
       print('\033[1;37m[\033[1;32m14\033[1;37m]\033[1;32m AUTO UKRAINE PASSWORD')
       print('\033[1;37m[\033[1;32m15\033[1;37m]\033[1;32m AUTO DENMARK PASSWORD')
       print('\033[1;37m[\033[1;32m16\033[1;37m]\033[1;32m AUTO RUSSIAN PASSWORD')
       print('\033[1;37m[\033[1;32m17\033[1;37m]\033[1;32m AUTO NETHERLAND PASSWORD')
       print('\033[1;37m[\033[1;32m18\033[1;37m]\033[1;32m AUTO BHUTAN PASSWORD')
       print('\033[1;37m[\033[1;32m19\033[1;37m]\033[1;32m AUTO GREEK PASSWORD')
       print('\033[1;37m[\033[1;32m20\033[1;37m]\033[1;32m AUTO FRENCH PASSWORD')
       print('\033[1;37m[\033[1;32m21\033[1;37m]\033[1;32m AUTO PORTUGAL PASSWORD')
       print('\033[1;37m[\033[1;32m22\033[1;37m]\033[1;32m AUTO NORWEGIAN PASSWORD')
       print('\033[1;37m[\033[1;32m23\033[1;37m]\033[1;32m AUTO ISRAEL PASSWORD')
       print('\033[1;37m[\033[1;32m24\033[1;37m]\033[1;32m AUTO ITALIAN PASSWORD')
       print('\033[1;37m[\033[1;32m25\033[1;37m]\033[1;32m AUTO ROMANIA PASSWORD')
       print('\033[1;37m[\033[1;32m26\033[1;37m]\033[1;32m AUTO UNITED KINGDOM PASSWORD')
       print('\033[1;37m[\033[1;32m27\033[1;37m]\033[1;32m AUTO PERSIAN PASSWORD')
       print('\033[1;37m[\033[1;32m28\033[1;37m]\033[1;32m AUTO TAIWAN PASSWORD')
       print('\033[1;37m[\033[1;32m29\033[1;37m]\033[1;32m AUTO TURKISH PASSWORD')
       print('\033[1;37m[\033[1;32m30\033[1;37m]\033[1;32m AUTO SLOVENIA PASSWORD')
       print('\033[1;37m[\033[1;32m31\033[1;37m]\033[1;32m AUTO FINLAND PASSWORD')
       linex()
       auto_password_country_select=input(f'\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m CHOOSE \033[1;37m: \033[1;32m')
    elif auto_password_select in ['2','02']:
       clear()
       password=input(f'{style} \033[1;32mENTER CUSTOM PASSWORD \033[1;37m:\033[1;32m ')
    
    clear()
    co=input(f'{style} \033[1;32mDO YOU WANT TO SHOW COOKIE \033[1;37m[\033[1;32mY\033[1;37m/\033[1;31mN\033[1;37m] \033[1;37m:\033[1;32m ')
    coki.append('y' if co.lower() in ['y','yes','1'] else 'n')
    clear()
    print(f'{style} \033[1;32mACCOUNT CREATING STARTED')
    print(f'{style} \033[1;31mAUTO SUSPENDED 3 DAYS OR 6-7 DAYS AFTER.')
    print(f'{style} \033[1;32mUSE AIRPLANE MODE FOR GOOD RESULT')
    linex()
    
    while True:
        sys.stdout.write(f"\r\r\033[1;37m[\033[1;32mFINDING-CREATE\033[1;37m]\033[1;37m-\033[1;37m[\033[1;32mOK\033[1;37m•\033[1;32m{len(oks)}\033[1;37m]\033[1;37m-\033[1;37m[\033[1;31mCP\033[1;37m•\033[1;31m{len(cps)}\033[1;37m]\033[1;37m");
        sys.stdout.flush()
        
        ua_data=get_fake_desktop_ua()
        email_account=generate_random_email()
        
        if random_names_select in ['1','01']:
            first_name,last_name=fake_philippines()
        elif random_names_select in ['2','02']:
            first_name,last_name=fake_indonesia()
        elif random_names_select in ['3','03']:
           first_name,last_name=fake_japanese()
        elif random_names_select in ['4','04']:
           first_name,last_name=fake_bangladesh()
        elif random_names_select in ['5','05']:
           first_name,last_name=fake_nigeria()
        elif random_names_select in ['6','06']:
           first_name,last_name=fake_vietnamese()
        elif random_names_select in ['7','07']:
           first_name,last_name=fake_chinese()
        elif random_names_select in ['8','08']:
           first_name,last_name=fake_spanish()
        elif random_names_select in ['9','09']:
           first_name,last_name=fake_thailand()
        elif random_names_select in ['10']:
           first_name,last_name=fake_frenchcanadian()
        elif random_names_select in ['11']:
           first_name,last_name=fake_australia()
        elif random_names_select in ['12']:
           first_name,last_name=fake_turkey()
        elif random_names_select in ['13']:
           first_name,last_name=fake_iceland()
        elif random_names_select in ['14']:
           first_name,last_name=fake_ukraine()
        elif random_names_select in ['15']:
           first_name,last_name=fake_denmark()
        elif random_names_select in ['16']:
           first_name,last_name=fake_russian()
        elif random_names_select in ['17']:
           first_name,last_name=fake_netherland()
        elif random_names_select in ['18']:
           first_name,last_name=fake_bhutan()
        elif random_names_select in ['19']:
           first_name,last_name=fake_greek()
        elif random_names_select in ['20']:
           first_name,last_name=fake_french()
        elif random_names_select in ['21']:
           first_name,last_name=fake_portugal()
        elif random_names_select in ['22']:
           first_name,last_name=fake_norwegian()
        elif random_names_select in ['23']:
           first_name,last_name=fake_israel()
        elif random_names_select in ['24']:
           first_name,last_name=fake_italian()
        elif random_names_select in ['25']:
           first_name,last_name=fake_romania()
        elif random_names_select in ['26']:
           first_name,last_name=fake_unitedkingdom()
        elif random_names_select in ['27']:
           first_name,last_name=fake_persian()
        elif random_names_select in ['28']:
           first_name,last_name=fake_taiwan()
        elif random_names_select in ['29']:
           first_name,last_name=fake_turkish()
        elif random_names_select in ['30']:
           first_name,last_name=fake_slovenia()
        elif random_names_select in ['31']:
           first_name,last_name=fake_finland()
        elif random_names_select in ['32']:
           first_name,last_name=fake_yemen()
        else:
           first_name,last_name=fake_philippines()
        
        valid=[str(i) for i in range(1, 32)]+[f"0{i}" for i in range(1,10)]
        if auto_password_country_select in valid:
           password=f"{first_name.lower()}{last_name.lower()}{random.randint(10,99)}"
        
        proxies_config=get_random_proxy() 
        cookies={'wd': '738x688','locale': 'en_GB'}
        headers={
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en,id;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'dpr': '1',
            'priority': 'u=0, i',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': f'"Not)A;Brand";v="8", "{ua_data["browser"]}";v="{ua_data["version"]}"',
            'sec-ch-ua-full-version-list': ua_data["full_version_list"],
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"19.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ____useragent____(),
            'viewport-width': str(ua_data["width"])
        }
        
        try:
            response=requests.get('https://www.facebook.com/?_rdc=1&_rdr',cookies=cookies,headers=headers,proxies=proxies_config,timeout=10,allow_redirects=True,verify=False)
            cookies.update(dict(response.cookies.get_dict()))
            headers.update({'referer': 'https://www.facebook.com/?_rdc=1&_rdr',})
            signup=requests.get('https://www.facebook.com/r.php?entry_point=login',cookies=cookies,headers=headers).text.replace('\\','')
            
            lsd_token=safe_extract('name="lsd" value="(.*?)"',signup,'AVo86L310qI')
            haste_session=safe_extract('"haste_session":"(.*?)"',signup)
            ccg=safe_extract('"connectionClass":"(.*?)"',signup)
            rev=safe_extract(r'"consistency":{"rev":(\d+)',signup)
            hsi=safe_extract(r'"hsi":"(\d+)"',signup)
            spint=safe_extract(r'"__spin_t":(\d+)',signup)
            
            headers.update({'x-asbd-id': '359341','x-fb-lsd': lsd_token})
            response=requests.get(f'https://web.facebook.com/ajax/registration/validation/contactpoint_invalid/?contactpoint={email_account}&fb_dtsg_ag&__user=0&__a=1&__req=4&__hs={haste_session}&dpr=1&__ccg={ccg}&__rev={rev}&__s=an0im4%3Afuzmdi%3Ahsr1au&__hsi={hsi}&__dyn=7xe6EsK36Q5E5ObwKBWg5S1Dxu13wqovzEdEc8uw9-3K0lW4o3Bw5VCwjE3awdu0FE2awpUO0n24o5-0me1Fw5uwbO0KU3mwaS0zE5W09yyE1582ZwrU1Xo1UU3jwea&__hsdp=hIfEA5EIox0IkE99fxTFBAwNy2wJBCx90NhE4a1nxe0ky0mK0MEMw7W1kwk87Feoqh0&__hblp=0PU2Owjo620kq0k63a0tG1ew9W2a0cZAw3q80zS0-o04XK0Go1pU0OG1uKLDBFoDh80rQw&__spin_r={rev}&__spin_b=trunk&__spin_t={spint}',cookies=cookies,headers=headers,proxies=proxies_config,timeout=10,allow_redirects=True,verify=False)
            
            headers.update({
                'origin':'https://www.facebook.com',
                'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
                'sec-ch-ua-full-version-list': '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.184", "Microsoft Edge";v="138.0.3351.121"',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
                'accept': '*/*',
                'accept-language': 'en,id;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'referer': 'https://www.facebook.com/r.php?entry_point=login'
            })
            
            formula=extractor(signup)
            jazoest=formula.get("jazoest") or safe_extract(r'name="jazoest"\s+value="(\d+)"', signup, "0")
            
            data={
                'jazoest': str(jazoest),
                'lsd': lsd_token,
                'firstname': first_name,
                'lastname': last_name,
                'birthday_day': str(random.randint(1,28)),
                'birthday_month': str(random.randint(1,12)),
                'birthday_year': str(random.randint(1992,2009)),
                'birthday_age': '',
                'did_use_age': 'false',
                'sex': '1',
                'preferred_pronoun': '',
                'custom_gender': '',
                'reg_email__': email_account,
                'reg_email_confirmation__': '',
                'reg_passwd__': f'#PWD_BROWSER:0:{int(time.time())}:{password}',
                'referrer': '',
                'asked_to_login': '0',
                'use_custom_gender': '',
                'terms': 'on',
                'ns': '0',
                'ri': safe_extract(r'name="ri" value="(.*?)"', signup),
                'action_dialog_shown': '',
                'invid': '',
                'a': '',
                'oi': '',
                'locale': 'en_GB',
                'app_bundle': '',
                'app_data': '',
                'reg_data': '',
                'app_id': '',
                'fbpage_id': '',
                'reg_oid': '',
                'reg_instance': safe_extract(r'name="reg_instance" value="(.*?)"', signup),
                'openid_token': '',
                'uo_ip': '',
                'guid': '',
                'key': '',
                're': '',
                'mid': '',
                'fid': '',
                'reg_dropoff_id': '',
                'reg_dropoff_code': '',
                'ignore': 'captcha|reg_email_confirmation__',
                'captcha_persist_data': safe_extract(r'name="captcha_persist_data" value="(.*?)"', signup, ""),
                'captcha_response': '',
                '__user': '0',
                '__a': '1',
                '__req': '5',
                '__hs': haste_session,
                'dpr': '1',
                '__ccg': ccg,
                '__rev': rev,
                '__s': 'an0im4:fuzmdi:hsr1su',
                '__hsi': hsi,
                '__dyn': '7xe6EsK36Q5E5ObwKBWg5S1Dxu13wqovzEdEc8uw9-3K0lW4o3Bw5VCwjE3awdu0FE2awpUO0n24o5-0me1Fw5uwbO0KU3mwaS0zE5W09yyE1582ZwrU1Xo1UU3jwea',
                '__hsdp': 'hIfEA5EIox0IkE99fxTFBAwNy2wJBCx90NhE4a1nxe0ky0mK0MEMw7W1kwk87Feoqh0',
                '__hblp': '0PU2Owjo620kq0k63a0tG1ew9W2a0cZAw3q80zS0-o04XK0Go1pU0OG1uKLDBFoDh80rQw',
                '__spin_r': rev,
                '__spin_b': 'trunk',
                '__spin_t': spint
            }
            
            c=requests.post('https://web.facebook.com/ajax/register.php',headers=headers,data=data,proxies=proxies_config,timeout=10,allow_redirects=True,verify=False)
            
            if '"registration_succeeded":true' in c.text:
                cookie_dict,cookie_str=parse_set_cookie(c.headers)
                first_cok=c.cookies.get_dict()
                ids=str(first_cok.get("c_user","Unknown"))
                print(f'\r\r\033[1;32m[ERROR-SUCCESS💚] {ids} | {password}')
                linex()
                if 'y' in coki:
                   colorx=random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                   print(f'\r\r\033[1;37m[\033[1;32mCOKI\033[1;37m]  : {colorx}{cookie_str}')
                   print(f'\r\r\033[1;37m[\033[1;32mUA\033[1;37m]    : {colorx}{ua_data["ua"]}')
                   linex()
                append_line("MR-ERROR-AUTO-CRATE-M1-COOKIE.txt", f"{ids} | {password} | {cookie_str}")
                append_line("MR-ERROR-AUTO-CRATE-M1-OK.txt", f"{ids} | {password}")
                append_line("MR-ERROR-AUTO-CRATE-M1-EMAIL.txt", f"{email_account}")
                oks.append(ids)
            else:
                cps.append(email_account)
        except Exception:
            continue

# Entry point - FREE VERSION - NO RESTRICTIONS
if __name__ == "__main__":
    clear()
    print(f'{style} \033[1;32mTOOL IS NOW FREE - NO APPROVAL NEEDED!')
    time.sleep(2)
    main()
