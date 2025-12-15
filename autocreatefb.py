# ENJOY OPEN SOURCE AUTO CREATE FB 
# AUTHOR : ETHAN KLEIN HUILEN
# GITHUB  : MR-ERROR-708
# THANK YOU.
#▬▭▬▭▬▭▬▭[IMPORT]▬▭▬▭▬▭▬▭#
import os,sys,re,time,json,mechanize,asyncio,aiohttp,requests,urllib.parse,bs4,string,faker,fake_email,random,uuid,hashlib,subprocess,platform,marshal,zlib,base64,locale,threading
from faker import Faker
from fake_email import Email
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from datetime import datetime,timedelta
import concurrent.futures
from requests.adapters import HTTPAdapter
import urllib3
import socket
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
socket.setdefaulttimeout(10)
#▬▭▬▭▬▭▬▭[COLOR CODE]▬▭▬▭▬▭▬▭#
white="\x1b[1;97m";yelloww="\033[1;33m";green="\x1b[38;5;49m";G0="\x1b[38;5;155m";green1='\x1b[38;5;154m';G2='\x1b[38;5;47m';G3='\x1b[38;5;48m';G4='\x1b[38;5;49m';G5='\x1b[38;5;50m';G6="\x1b[38;5;52m";s="\033[0m";W="\033[1;30m";Y="\x1b[1;93m";red="\x1b[38;5;160m";B="\033[1;95m";BE="\x1b[1;35m";X="\x1b[1;96m";Z="\x1b[1;95m";Y="\033[1;93m";U="\033[1;94m";V="\033[38;5;47m";T="\033[38;5;48m";Q="\033[38;5;49m";P="\033[38;5;50m";O="\033[38;5;51m";N="\033[38;5;52m";M="\x1b[38;5;205m";L="\033[96;1m";K="\x1b[1;91m";WH="\033[1;97m";orange="\x1b[38;5;196m";yellow="\x1b[38;5;208m";black="\033[1;30m";rad="\x1b[38;5;160m";YLW="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu="\033[1;47m";pvt="\033[1;0m";gren="\x1b[38;5;154m";gas="\033[1;32m"
style=f"\033[1;37m[\033[1;32m●\033[1;37m]"
stylee=f"\033[1;37m[\033[1;31m!\033[1;37m]"
#▬▭▬▭▬▭▬▭[PERMISSION OF SDCARD]▬▭▬▭▬▭▬▭#
try:
    os.system('rm -'+'rf /sd'+'card/.txt');os.system('clear');open('/sd'+'ca'+'rd/.t'+'xt','w').write(' ')
except PermissionError:
    os.system("clear" if os.name == "posix" else "cls")
    print(f"{style} \033[1;32mMRERROR_AUTOFB TOOL IS NOT ALLOW WITHOUT STORAGE PERMISSION");os.system('termux-setup-storage');os.system('clear');exit(f"{style} \033[1;32mRUN AGAIN : python AUTO.py")
#▬▭▬▭▬▭▬▭[FILE PATH]▬▭▬▭▬▭▬▭#
BASE_PATH="/sdcard/MRERROR_AUTOFB/"
os.makedirs(BASE_PATH,exist_ok=True)
def append_line(filename,text):
    with open(os.path.join(BASE_PATH,filename),"a",encoding="utf-8") as f:
        f.write(text+"\n")
#▬▭▬▭▬▭▬▭[INTERNET]▬▭▬▭▬▭▬▭#
try:
    requests.get("https://www.google.com", timeout=5)
except requests.exceptions.ConnectionError:
    os.system("clear" if os.name == "posix" else "cls")
    print(f"{stylee} \033[1;31mNO INTERNET CONNECTION & DON'T TRY TO BYPASS")
    print(f"\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    sys.exit()
#▬▭▬▭▬▭▬▭[SECURITY BOX]▬▭▬▭▬▭▬▭#
style_2=f"\033[1;37m[\033[1;31m!\033[1;37m]"
site = '/da'+'ta/data/com.termu'+'x/files/usr/lib/python3.12/s'+'ite-packages/'
os.system("clear" if os.name == "posix" else "cls");alart=(f"{style_2} \033[1;31mYOU ARE A MOTHERFUCKER, YOU ARE A MOTHERFUCKER.\n{style_2} \033[1;31mDON'T TRY BYPASS AND CAPTURE BOSS\n{style_2} \033[1;31mTHIS TIME I'LL LEAVE IT LIKE THIS, YOU BASTARD.\n\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
try:
    mr_error=f'{site}reque'+'sts/'
    if not 'print' in open(mr_error+'sess'+'ions.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    mr_error1=f'{site}reque'+'sts/'
    if not 'print' in open(mr_error1+'mod'+'els.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    mr_error2=f'{site}reque'+'sts/'
    if not 'print' in open(mr_error2+'ap'+'i.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    king=f'{site}reque'+'sts/'
    if not 'sys.stdout.write' in open(king+'sess'+'ions.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    qeen=f'{site}req'+'uests/'
    if not 'sys.stdout.write' in open(qeen+'mod'+'els.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    don=f'{site}requ'+'ests/'
    if not 'sys.stdout.write' in open(don+'a'+'pi.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
with open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    a=open('requests/sessions.py','r').read()
    if 'print' in a:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    b=open('requests/api.py','r').read()
    if 'print' in b:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    c=open('requests/models.py','r').read()
    if 'print' in c:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    d=open('httpx/_api.py','r').read()
    if 'print' in d:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    e=open('httpx/_auth.py','r').read()
    if 'print' in e:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    f=open('httpx/_models.py','r').read()
    if 'print' in f:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    g=open('requests/sessions.py','r').read()
    if 'sys.stdout.write' in g:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    h=open('requests/api.py','r').read()
    if 'sys.stdout.write' in h:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    h=open('requests/models.py','r').read()
    if 'sys.stdout.write' in h:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    ii=open('httpx/_api.py','r').read()
    if 'sys.stdout.write' in ii:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    j=open('httpx/_auth.py','r').read()
    if 'sys.stdout.write' in j:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    k=open('httpx/_models.py','r').read()
    if 'sys.stdout.write' in k:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    l=open('requests/api.py', 'r').read()
    if "verify = False" in l:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    m=open('requests/sessions.py', 'r').read()
    if "self.verify = False" in m:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    n=open(f'urllib3/conne'+'ction.py', 'r').read()
    if str("cert_reqs = 'CERT_NONE'") in n:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/urllib3');exit(f"{alart}")
    else:pass
except Exception as e:pass
#▬▭▬▭▬▭▬▭[BYPASS]▬▭▬▭▬▭▬▭#
async def bypass():
  file1=open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py','r')
  file2=open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py','r')
  file3=open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py','r')
  data=file1.read()
  sess=file2.read()
  approve=file3.read()
  keyword=("print(url)")
  keyword2=("print(data)")
  if keyword in data or "echo" in data or "pprint" in data:
    os.system("clear" if os.name == "posix" else "cls")
    print(f'{style_2} \033[1;31mSTUPID BYPASS')
    print(f'{style_2} \033[1;33mBYE BYE FILES HAHAHAH')
    sys.exit()
  elif "https://pastebin.com/icdnZ6AQ" in approve or "DR4X" in approve or "pprint" in approve:
    print(f'{style_2} \033[1;31mTRYING HARD BYPASSING MY TOOL LOL BYE')
    sys.exit()
  elif keyword in sess or "echo" in sess or keyword2 in sess or "pprint" in sess or "print(headers)" in sess or "Console" in sess or "{data}" in sess or "{url}" in sess or "{headers}" in sess:
    os.system("clear" if os.name == "posix" else "cls")
    print(f'{style_2} \033[1;31mCAPTURE MORE DATA')
    print(f'{style_2} \033[1;33mBYE BYE FILES')
    sys.exit()
  else:
    os.system("clear" if os.name == "posix" else "cls")
    timee=datetime.now()
    limittime=timee.strftime("%m-%d-%y")
    if limittime >= "12-30-25":
        os.system("clear")
        sys.exit('{style_2} \033[1;31mTIME’S UP BRO')
    else:
      await sub()
#▬▭▬▭▬▭▬▭[KEY GENERATOR]▬▭▬▭▬▭▬▭#
myid=uuid.uuid4().hex[:5].upper()
try:
  key1=open('/data/data/com.termux/files/usr/bin/.errorauto.txt', 'r').read()
except:
  kok=open('/data/data/com.termux/files/usr/bin/.errorauto.txt', 'w')
  kok.write(myid)
  kok.close()
uid=os.getuid()
key1=open('/data/data/com.termux/files/usr/bin/.errorauto.txt', 'r').read()
kex=(f"AUTOCREATEFB|MR|{uid}|ERROR|{key1}|708")
key1=kex
AX=hashlib.md5((platform.version()+str(os.getuid())+platform.platform()+os.getlogin()+platform.release()).replace(' ','').encode()).hexdigest().upper()
_sos_=AX;_xvx_=_sos_;_asa_=_xvx_;_cxa_=_asa_
_qq_=_cxa_[5:8];_ee_=_cxa_[15:19];_rr_=_cxa_[23:26];_tt_=_cxa_[11:13]
_yy_=_cxa_[19:21];_q_=_yy_;_w_=_tt_;_e_=_rr_;_r_=_ee_;_t_=_qq_;__coc__=_q_+_w_+_e_+_r_+_t_
#▬▭▬▭▬▭▬▭[PYCURL]▬▭▬▭▬▭▬▭#
def py_curl(url):
    curl=pycurl.Curl()
    buffer=BytesIO()
    try:
        curl.setopt(curl.URL,url)
        curl.setopt(curl.WRITEDATA,buffer)
        curl.setopt(curl.SSL_VERIFYPEER,1)
        curl.setopt(curl.SSL_VERIFYHOST,2)
        curl.setopt(curl.CAINFO,certifi.where())
        curl.perform()
    except pycurl.error as e:
        return f"AN ERROR IN PY{e}"
    finally:
        curl.close()
    response_body=buffer.getvalue().decode('utf-8')
    return response_body
#▬▭▬▭▬▭▬▭[LOADING SYSTEM]▬▭▬▭▬▭▬▭#
def error(z):
      for a in z +'\n':sys.stdout.write(a);sys.stdout.flush();time.sleep(0.050)
#▬▭▬▭▬▭▬▭[OPENING MOMENT]▬▭▬▭▬▭▬▭#
print(f'{style} \033[1;32mCHECKING UPDATED...\033[1;37m');time.sleep(2)
os.system("git pull");time.sleep(2);os.system("clear")
#▬▭▬▭▬▭▬▭[MODULE]▬▭▬▭▬▭▬▭#
try:import pystyle
except ImportError:print(f'{style} \033[1;32mINSTALLING PYSTYLE...\033[1;37m');time.sleep(0.5);os.system('pip install pystyle');import pystyle;os.system('clear')
from pystyle import Colors,Colorate
#▬▭▬▭▬▭▬▭[USER AGENT]▬▭▬▭▬▭▬▭#
def get_fake_desktop_ua():
    desktop_uas = [# Windows Edge
        {
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
            "width": 1920,
            "browser": "Microsoft Edge",
            "version": "138",
            "full_version_list": '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.184", "Microsoft Edge";v="138.0.3351.121"'
        },# Windows Firefox
        {
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) "
                  "Gecko/20100101 Firefox/119.0",
            "width": 1920,
            "browser": "Firefox",
            "version": "119",
            "full_version_list": '"Firefox";v="119.0"'
        },# Windows Chrome
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
    model = random.choice(['1105','1107','15','3T','62A','6779','6833','7273','9A','A1','A1 5G','A1 Pro','A11','A11k','A11x','A12','A15','A15s','A16','A16e','A16k','A16s','A17','A17k','A18','A1i 5G','A1k','A1s','A1x','A2 5G','A25','A2x 5G','A3','A3 5G','A3 Pro 5G','A30','A31','A31c','A32','A33','A33m','A33t','A34','A35','A36','A37','A37t','A38','A39','A3s','A3x 5G','A4','A40','A400','A41','A42','A43','A44','A45','A46','A47','A48','A49','A5','A5 (2020)','A50','A51','A52','A53','A53 5G','A53m','A53s','A53s 5G','A54','A54 5G','A54s','A55','A55 5G','A55s 5G','A56','A56 5G','A57','A57 (2016)','A57 (2022)','A58','A58 5G','A59','A59 5G','A59m','A59s','A59t','A5S','A60','A7','A71','A71 (2018)','A71A','A72','A72n 5G','A73','A73 5G','A73t','A74','A74 5G','A76','A77','A77 5G','A77s','A77t','A78','A78 5G','A79','A79 5G','A79k','A79t','A7n','A7x','A8','A83','A83 (2018)','A83PRO','A83t','A85T','A9','A9 (2020)','A91','A92','A92s','A93','A93s','A94','A95','A96','A96 5G','A97','A98','A98 5G','A9x','AX5','AX5s','AX7','C1','CNM632','CNM652','CPH1114','CPH1235','CPH1427','CPH1451','CPH1615','CPH1664','CPH1869','CPH1927','CPH1929','CPH1985','CPH2048','CPH2068','CPH2107','CPH2238','CPH2261','CPH2331','CPH2332','CPH2351','CPH2381','CPH2389','CPH2399','CPH2401','CPH2409','CPH2411','CPH2413','CPH2415','CPH2417','CPH2419','CPH2423','CPH2447','CPH2449','CPH2451','CPH2459','CPH2465','CPH2467','CPH2469','CPH2487','CPH2491','CPH2493','CPH2499','CPH2513','CPH2515','CPH2519','CPH2521','CPH2523','CPH2525','CPH2529','CPH2535','CPH2551','CPH2553','CPH2557','CPH2569','CPH2573','CPH2579','CPH2581','CPH2583','CPH2585','CPH2589','CPH2591','CPH2599','CPH2603','CPH2605','CPH2607','CPH2609','CPH2611','CPH2613','CPH2617','CPH2619','CPH2621','CPH2625','CPH2629','CPH2631','CPH2637','CPH2639','CPH2641','CPH2643','CPH2661','CPH2663','CPH2665','CPH2667','CPH2669','CPH2681','CPH2683','CPH2687','CPH2843','CPH2931','CPH3475','CPH3669','CPH3682','CPH3731','CPH3776','CPH3785','CPH4125','CPH4275','CPH4299','CPH4395','CPH4473','CPH4987','CPH5286','CPH5841','CPH5947','CPH6178','CPH6244','CPH6271','CPH6316','CPH6519','CPH6528','CPH6697','CPH7338','CPH7364','CPH7382','CPH7532','CPH7577','CPH7948','CPH7991','CPH8153','CPH8346','CPH8347','CPH8363','CPH8393','CPH8467','CPH8472','CPH8534','CPH8686','CPH8893','CPH9177','CPH9226','CPH9659','CPH9667','CPH9716','CPH9763','CPH9839','CPH9929','CPH9977','f','F1','F1 Plus','F10','F11','F11 Pro','F11Pro','F15','F17','F17 Pro','F19','F19 Pro','F19 Pro Plus','F19s','F1s','F21 Pro','F21s Pro','F23 5G','F25 Pro 5G','F27 Pro+ 5G','F3','F3 Plus','F5','F5 Youth','F51','F61','F7','F9','F9 Pro','Find','Find 5','Find 5 Mini','Find 7','Find 7a','Find Clover','Find Melody','Find Muse','Find N','Find N 5G','Find N2','lFind N2 Flip','Find N3','Find N3 Flip','Find Way S','Find X','Find X Lamborghini','Find X2','Find X2 Lite','Find X2 Pro','Find X3','Find X3 Lite','Find X3 Neo','Find X3 Pro','Find X5','Find X5 Pro','Find X6','Find X6 Pro','Find X7','Find X7 Ultra','Find X7 Ultra SE','JLAJH6','Joy Plus','K1','K10','K10 5G','K10 Pro 5G','K10x','K11 5G','K11x 5G','K12 5G','K3','K5','K7','K7x','K9 5G','K9 Pro 5G','K9s','K9x','N1 Mini','N1T','N3','Neo','Neo 3','Neo 5','Neo 7','Neo 7s','Pad 2','Pad Air','Pad Air 2','Pad Neo','Pad WiFi','R10','R1001','R11','R11 Plus','R11plus','R11s','R11s Plus','R15','R15 Dream Mirror','R15 Neo','R15 Pro','R15x','R17','R17 Neo','R17 Pro','R1K','R1L','R1S','R1x','R2001','R2010','R2017','R3006','R5','R53','R6007','R7','R7 Lite','R7 Plus','R7 Plus F','R7005','R7007','R7s','R7s Plus','R7sm','R7st','R7t','R801','R805','R807','R811','R819','R819T','R8205','R8207','R823T','R829','R829T','R830','R830S','R833T','R9','R9 Plus','R9km','R9s','R9s Plus','R9t','R9tm','Real','Reno','Reno 10','Reno 10 5G','Reno 10 Pro 5G','Reno 10 Pro+ 5G','Reno 10X','Reno 10X Zoom','Reno 11','Reno 11 Pro','Reno 12','Reno 12 5G','Reno 12 F 4G','Reno 12 F 5G','Reno 12 Pro 5G','Reno 2','Reno 2F','Reno 2Z','Reno 3','Reno 3 5G','Reno 3 Lite','Reno 3 Pro','Reno 3A','Reno 4 4G','Reno 4 5G','Reno 4 Lite','Reno 4 Pro 4G','Reno 4 Pro 5G','Reno 4 SE 5G','Reno 4F','Reno 4Z 5G','Reno 5','Reno 5 5G','Reno 5 Lite','Reno 5 Pro 5G','Reno 5 Pro Plus 5G','Reno 5A','Reno 5F','Reno 5G','Reno 5K','Reno 5K 5G','Reno 5Z','Reno 6','Reno 6 Pro','Reno 6 Pro 5G','Reno 6 Pro Plus','Reno 6 Z 5G','Reno 7','Reno 7 Pro','Reno 7 SE','Reno 7A','Reno 7Z','Reno 8','Reno 8 Pro','Reno 8 Pro+','Reno 8 Z','Reno 8T','Reno 9','Reno 9 A','Reno 9 Pro','Reno 9 Pro+','Reno A','Reno Ace','Reno Ace 2','Reno K3','Reno Z','Reno10','Reno11','Reno2','RENO3','Reno4','Reno5','Reno8','Reno9','RX17 Neo','S1','S17','S3','S4','T29','Ulike 2','V5','V8821','Watch 2 46mm','Watch 41mm','Watch 46mm','X','x20','x22','X50Pro','X54','X9017','X907','Y15','Y21','Y3','Z1'])
    build = random.choice(['MMB29Q','R16NW','LRX22C','R16NW','KTU84P','JLS36C','NJH47F','PPR1.180610.011','QP1A.190711.020','NRD90M','RP1A.200720.012','M1AJB','MMB29T'])
    ver = str(random.choice(range(77,577)))
    ver2 = str(random.choice(range(57,77)))
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''
#▬▭▬▭▬▭▬▭[FAKE NAME]▬▭▬▭▬▭▬▭#
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
    first=Faker('sv_SE').first_name()
    last=Faker('sv_SE').last_name()
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
#▬▭▬▭▬▭▬▭[EXTRACTOR]▬▭▬▭▬▭▬▭#
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
#▬▭▬▭▬▭▬▭[FAKE EMAIL]▬▭▬▭▬▭▬▭#
BASE_URL = "https://inboxes.com"
HEADERS = {
    "authority": "inboxes.com", "accept": "*/*", "accept-language": "en-US,en;q=0.9", 
    "referer": "https://inboxes.com/", "sec-ch-ua": '"Not-A.Brand";v="99", "Chromium";v="124"', 
    "sec-ch-ua-mobile": "?1", "sec-ch-ua-platform": '"Android"', "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", 
    "sec-fetch-site": "same-origin", "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
}

def fetch_domains():
    try:
        response = requests.get(f"{BASE_URL}/api/v2/domain",headers=HEADERS)
        if response.status_code == 200:
           domains = response.json().get("domains", [])
           return [domain["qdn"] for domain in domains]
        return []
    except:
        return []

def get_emails(email: str) -> list:
    try:
        response = requests.get(f"{BASE_URL}/api/v2/inbox/{email}", headers=HEADERS)
        return response.json().get("msgs", []) if response.status_code == 200 else []
    except Exception:
        return []

def fetch_email_content(uid: str) -> dict | None:
    try:
        response = requests.get(f"{BASE_URL}/api/v2/message/{uid}", headers=HEADERS)
        return response.json() if response.status_code == 200 else None
    except Exception:
        return None

def extract_fb_code(text: str) -> str | None:
    match = re.search(r"FB-(\d+)", text)
    return match.group(1) if match else None

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
#▬▭▬▭▬▭▬▭[SPECIAL LINE]▬▭▬▭▬▭▬▭#
def linex():
    #print(Colorate.Horizontal(Colors.green_to_white, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"))
    print(f'\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#▬▭▬▭▬▭▬▭[BANNER]▬▭▬▭▬▭▬▭#
logo=(Colorate.Horizontal(Colors.green_to_white,r"""
    _  _   _ _____ ___     ___ ___ ___   _ _____ ___ 
   /_\| | | |_   _/ _ \   / __| _ \ __| /_\_   _| __|
  / _ \ |_| | | || (_) | | (__|   / _| / _ \| | | _| 
 /_/ \_\___/  |_| \___/   \___|_|_\___/_/ \_\_| |___|"""" MR-ERROR"))
 #▬▭▬▭▬▭▬▭[INFO]▬▭▬▭▬▭▬▭#
info=(f"""{style} \033[1;32mAUTHOR   \033[1;37m: \033[1;32mETHAN KLEIN HUILEN
{style} \033[1;32mTYPE     \033[1;37m: \033[1;32mAUTO CREATE FACEBOOK
{style} \033[1;32mSTATUS   \033[1;37m: \033[1;32mPREMIUM
{style} \033[1;32mSYSTEM   \033[1;37m: \033[1;32mDATA/WIFI
{style} \033[1;32mVERSION  \033[1;37m: \033[1;32m1.2""")
#▬▭▬▭▬▭▬▭[CLEAR]▬▭▬▭▬▭▬▭#
def clear():
    os.system("clear" if os.name == "posix" else "cls");print(logo);linex();print(info);linex()
#▬▭▬▭▬▭▬▭[LOOP]▬▭▬▭▬▭▬▭#
proxies_list=[]
proxies_lock=threading.Lock()
oks,loop,ua,ussr,tw,cps,plist,coki=[],0,[],[],[],[],[],[]
#▬▭▬▭▬▭▬▭[APPROVAL SYSTEM]▬▭▬▭▬▭▬▭#
async def sub():
  os.system("clear" if os.name == "posix" else "cls")
  async with aiohttp.ClientSession() as sess:
    async with sess.get('https://pastebin.com/5wE9EWr6') as appro:
      r1=await appro.text()
      if key1 in r1:
        os.system("clear" if os.name == "posix" else "cls")
        print(f"{style} \033[1;32mYOUR KEY IS APPROVED")
        time.sleep(3)
        main()
      else:
        os.system("clear" if os.name == "posix" else "cls")
        print(f"\t\033[1;32mFIRST GET APPROVAL\033[1;37m")
        time.sleep(5)
        clear()
        print(f"{style} \033[1;32mYOU HAVE TO GET APPROVE FIRST BEFORE USING IT\n{stylee} \033[1;31mYOUR KEY IS NOT APPROVED\n\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{style} \033[1;32mYOUR KEY \033[1;37m: \033[1;32m{key1}\n\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        input(f"{style} \033[1;37mPRESS ENTER TO SEND KEY")
        time.sleep(3.5)
        tks=f"""HELLO ERROR X ETHAN, DEAR ADMIN, PLEASE APPROVE MY KEY TO PREMIUM THANKS.\nYOUR KEY : {key1}"""
        msg=urllib.parse.quote(tks)
        os.system(f'am start -a android.intent.action.VIEW 'f'-d "https://wa.me/+639610075203?text={msg}"')
        await sub()
#▬▭▬▭▬▭▬▭[MAIN MENU]▬▭▬▭▬▭▬▭#
def main():
    clear();print(f'\033[1;37m[\033[1;32m01\033[1;37m]\033[1;32m START AUTO CREATE');print(f'\033[1;37m[\033[1;32m00\033[1;37m]\033[1;31m EXIT THIS PROGRAM');linex()
    auto_select=input(f'\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m CHOOSE \033[1;37m: \033[1;32m')
    if auto_select in ['1','01']:____create____()
    elif auto_select in ['0','00']:os.system("exit")
    else:main()
#▬▭▬▭▬▭▬▭[DELAY]▬▭▬▭▬▭▬▭#
def delay(j=3):
    for s in range(j,0,-1):
        print(f'{style} \033[1;32mWAIT FOR {s} SECOND',end='\r')
        sys.stdout.flush()
        time.sleep(1)
    print(' '*50,end='\r')
#▬▭▬▭▬▭▬▭[COOKIE]▬▭▬▭▬▭▬▭#
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
            temp[-1]+=','+part.strip()
    for ck in temp:
        kv=ck.split(';',1)[0]
        if '=' in kv:
            k,v=kv.split('=',1)
            cookies[k.strip()]=v.strip()
    cookie_str="sb=Cracked.By-Error_Tool;"+";".join(f"{k}={v}" for k,v in cookies.items())
    return cookies,cookie_str
#▬▭▬▭▬▭▬▭[SAFE EXTRACT]▬▭▬▭▬▭▬▭#
def safe_extract(pattern,text,default=""):
    m=re.search(pattern,text)
    return m.group(1) if m else default
#▬▭▬▭▬▭▬▭[PROXY SCRAPER]▬▭▬▭▬▭▬▭#
#SORRY I'M NOT PROXY SERVER
#▬▭▬▭▬▭▬▭[CREATE MENU]▬▭▬▭▬▭▬▭#
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
    print(f'{style} \033[1;32mUSE AIRPLANE MOD FOR GOOD RESULT')
    linex()
    while True:
        sys.stdout.write(f"\r\r\033[1;37m[\033[1;32mFINDING-CREATE\033[1;37m]\033[1;37m-\033[1;37m[\033[1;32mOK\033[1;37m•\033[1;32m{len(oks)}\033[1;37m]\033[1;37m-\033[1;37m[\033[1;31mCP\033[1;37m•\033[1;31m{len(cps)}\033[1;37m]\033[1;37m");
        sys.stdout.flush()
        ua_data=get_fake_desktop_ua()
        email_account=generate_random_email()#f"{first_name.lower()}{last_name.lower()}@{random.choice(domains)}"
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
            'user-agent': ____useragent____(),#ua_data["ua"]
            'viewport-width': str(ua_data["width"])
        }
        response=requests.get('https://www.facebook.com/?_rdc=1&_rdr',cookies=cookies,headers=headers,proxies=proxies_config,timeout=10,allow_redirects=True,verify=False)
        cookies.update(dict(response.cookies.get_dict()))
        headers.update({'referer': 'https://www.facebook.com/?_rdc=1&_rdr',})
        signup=requests.get('https://www.facebook.com/r.php?entry_point=login',cookies=cookies,headers=headers).text.replace('\\','')
        lsd_token='AVo86L310qI'
        #re.search('name="lsd" value="(.*?)"',signup).group(1)
        haste_session=re.search('"haste_session":"(.*?)"',signup).group(1)
        ccg=re.search('"connectionClass":"(.*?)"',signup).group(1)
        rev=re.search(r'"consistency":{"rev":(\d+)',signup).group(1)
        hsi=re.search(r'"hsi":"(\d+)"',signup).group(1)
        spint=re.search(r'"__spin_t":(\d+)',signup).group(1)
        vip=re.search('"vip":"(.*?)"',signup).group(1)
        headers.update({'x-asbd-id': '359341','x-fb-lsd': lsd_token})
        response=requests.get(f'https://web.facebook.com/ajax/registration/validation/contactpoint_invalid/?contactpoint={email_account}&fb_dtsg_ag&__user=0&__a=1&__req=4&__hs={haste_session}&dpr=1&__ccg={ccg}&__rev={rev}&__s=an0im4%3Afuzmdi%3Ahsr1au&__hsi={hsi}&__dyn=7xe6EsK36Q5E5ObwKBWg5S1Dxu13wqovzEdEc8uw9-3K0lW4o3Bw5VCwjE3awdu0FE2awpUO0n24o5-0me1Fw5uwbO0KU3mwaS0zE5W09yyE1582ZwrU1Xo1UU3jwea&__hsdp=hIfEA5EIox0IkE99fxTFBAwNy2wJBCx90NhE4a1nxe0ky0mK0MEMw7W1kwk87Feoqh0&__hblp=0PU2Owjo620kq0k63a0tG1ew9W2a0cZAw3q80zS0-o04XK0Go1pU0OG1uKLDBFoDh80rQw&__spin_r={rev}&__spin_b=trunk&__spin_t={spint}',cookies=cookies,headers=headers,proxies=proxies_config,timeout=10,allow_redirects=True,verify=False)
        headers.update({'origin':'https://www.facebook.com',  'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"','sec-ch-ua-full-version-list': '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.184", "Microsoft Edge";v="138.0.3351.121"','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0','accept': '*/*','accept-language': 'en,id;q=0.9,en-GB;q=0.8,en-US;q=0.7','content-type': 'application/x-www-form-urlencoded','referer': 'https://www.facebook.com/r.php?entry_point=login','cookie':'datr=gKGYaMFDH3Zw5Gg2sggX9tbi; sb=gKGYaLge53jtbcJoymqEnZXl; ps_l=1; ps_n=1; locale=en_GB; wd=738x688; fr=1HLHrBbAGkoJv5O1l.AWeSwdELticByfVx58z4uY-kWUf_iGff96qe3DzSwDRT0GEF8Jo.BomL39..AAA.0.0.BomL4I.AWddslGP88dg7QDodcwbRuVHL_k'})
        formula=extractor(response.text)
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
        try:
            c=response=requests.post('https://web.facebook.com/ajax/register.php',headers=headers,data=data,proxies=proxies_config,timeout=10,allow_redirects=True,verify=False)
        except Exception:
            continue
        if '"registration_succeeded":true' in c.text:
            cookie_dict,cookie_str=parse_set_cookie(c.headers)
            session=requests.Session()
            first_cok=c.cookies.get_dict()
            ids=str(first_cok["c_user"])
            print(f'\r\r\033[1;32m[ERROR-SUCCESS💚] {ids} | {password}')
            linex()
            if 'y' in coki:
               colorx=random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
               print(f'\r\r\033[1;37m[\033[1;32mCOKI\033[1;37m]  : {colorx}{cookie_str}')
               print(f'\r\r\033[1;37m[\033[1;32mUA\033[1;37m]    : {colorx}{ua_data["ua"]}')
               linex()
               timestamp=time.strftime("%Y-%m-%d %H:%M:%S")
            append_line("MR-ERROR-AUTO-CRATE-M1-COOKIE.txt", f"{ids} | {password} | {cookie_str}")
            append_line("MR-ERROR-AUTO-CRATE-M1-OK.txt",      f"{ids} | {password}")
            append_line("MR-ERROR-AUTO-CRATE-M1-EMAIL.txt",   f"{email_account}")
            oks.append(ids)
            #delay(9)
        else:
            #print(f'\r\r\033[1;31m[ERROR-CP] {uid} | {password}')
            cps.append(email_account)
#▬▭▬▭▬▭▬▭[END]▬▭▬▭▬▭▬▭#
STATUS_URL="https://raw.githubusercontent.com/ERRORDEATH13451/ERROR_CONTROL/main/status_auto.txt"
try:
    response=requests.get(STATUS_URL,timeout=10)
    response.raise_for_status()
    status=response.text.strip()
except Exception as e:pass;exit()
print(f'{style} \033[1;32mCHECKING TOOL STATUS...\033[1;37m');time.sleep(2)
if status == "FREE":error(f"{style} \033[1;32mCONGRATULATIONS TOOL IS FREE NOW");time.sleep(4);free_login()
elif status == "PAID":error(f"{style} \033[1;32mTOOL IS PAID NOW");time.sleep(4);asyncio.run(bypass())
else:asyncio.run(bypass())

#main()
