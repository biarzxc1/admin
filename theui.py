import os
import sys
import time
import json
import aiohttp
import asyncio
import datetime
import requests
import re
import threading
import socket

try:
    from colorama import init
    init()
except ImportError:
    print("ERROR: colorama not installed. Please run: pip install -r requirements.txt")
    sys.exit(1)

# Check and install espeak if needed
try:
    result = os.system('espeak --version > /dev/null 2>&1')
    if result != 0:
        print("Installing espeak...")
        os.system('pkg install espeak -y > /dev/null 2>&1 || apt-get install espeak -y > /dev/null 2>&1')
except:
    pass

# --- COLOR CODES (Solid Colors) ---
white = "\033[1;97m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
cyan = "\033[1;36m"
blue = "\033[1;34m"
purple = "\033[1;35m"
reset = "\033[0m"

# Background colors
BG_R = '\033[41m'
BG_G = '\033[42m'
BG_C = '\033[46m'
BG_M = '\033[45m'
BG_Y = '\033[43m'
BG_B = '\033[44m'

# Style markers
style = f"{white}[{green}●{white}]"
stylee = f"{white}[{red}!{white}]"

LINE = f"{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{reset}"

# --- API CONFIGURATION ---
API_URL = "https://admindatabase-y4iw.onrender.com/api"
CURRENT_VERSION = "1.1.0"
user_token = None
user_data = None

# --- SOCKET CONFIGURATION ---
socket.setdefaulttimeout(10)

# --- ESPEAK CONFIGURATION ---
def speak(text):
    """Text-to-speech using espeak (non-blocking) - REMOVED"""
    pass

# --- GLOBAL VARIABLES ---
success_count = 0
lock = asyncio.Lock()
current_order = None

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def normalize_facebook_url(url):
    if not url:
        return url
    url = url.strip()
    url = re.sub(r'^https?://', '', url, flags=re.IGNORECASE)
    url = re.sub(r'^(www\.|m\.)', '', url, flags=re.IGNORECASE)
    if not url.startswith('facebook.com'):
        if '/' not in url:
            url = f'facebook.com/{url}'
    return url

def validate_smm_post_link(url):
    """
    Validate if the post link is supported for SMM Panel Boost.
    NOT SUPPORTED formats:
    - https://www.facebook.com/share/p/XXXX/
    - https://www.facebook.com/share/XXXX/
    These formats are REJECTED.
    """
    if not url:
        return True
    
    url = url.strip()
    
    unsupported_patterns = [
        r'^https?://(www\.|m\.)?facebook\.com/share/p/[\w]+/?$',
        r'^https?://(www\.|m\.)?facebook\.com/share/[\w]+/?$',
    ]
    
    for pattern in unsupported_patterns:
        if re.match(pattern, url, re.IGNORECASE):
            return False
    
    return True

def check_version():
    """Check if tool version matches server version"""
    try:
        status, response = api_request("GET", "/version", use_token=False)
        if status == 200 and response.get('success'):
            server_version = response.get('version', '1.0.0')
            if server_version != CURRENT_VERSION:
                clear()
                print(LINE)
                print(f"{stylee} {red}VERSION MISMATCH{reset}")
                print(LINE)
                print(f"{style} {green}Your tool version{reset} {white}:{reset} {red}{CURRENT_VERSION}{reset}")
                print(f"{style} {green}Server version{reset} {white}:{reset} {green}{server_version}{reset}")
                print(LINE)
                print(f"{stylee} {red}Your tool is outdated!{reset}")
                print(f"{style} {green}Please update to the latest version to continue using this tool.{reset}")
                print(LINE)
                input(f"\n{stylee} {red}PRESS ENTER TO EXIT{reset}")
                sys.exit(1)
    except:
        pass

def banner_header():
    banner_art = f"""{green}
    ██████╗ ██████╗ ██╗    ██╗████████╗ ██████╗  ██████╗ ██╗     ███████╗
    ██╔══██╗██╔══██╗██║    ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    ██████╔╝██████╔╝██║ █╗ ██║   ██║   ██║   ██║██║   ██║██║     ███████╗
    ██╔══██╗██╔═══╝ ██║███╗██║   ██║   ██║   ██║██║   ██║██║     ╚════██║
    ██║  ██║██║     ╚███╔███╔╝   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
    ╚═╝  ╚═╝╚═╝      ╚══╝╚══╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝{reset}
    """
    print(banner_art)
    print(LINE)
    print(f"{style} {green}DEVELOPER{reset}     {white}:{reset} {green}KEN DRICK{reset}")
    print(f"{style} {green}GITHUB{reset}        {white}:{reset} {green}RYO GRAHHH{reset}")
    print(f"{style} {green}VERSION{reset}       {white}:{reset} {green}{CURRENT_VERSION}{reset}")
    print(f"{style} {green}FACEBOOK{reset}      {white}:{reset} {green}facebook.com/ryoevisu{reset}")
    print(f"{style} {green}TOOL NAME{reset}     {white}:{reset} {red}[ RPWTOOLS ]{reset}")
    
    if user_data:
        print(LINE)
        print(f"{style} {green}USERNAME{reset}       {white}:{reset} {green}{user_data['username'].upper()}{reset}")
        print(f"{style} {green}FACEBOOK{reset}       {white}:{reset} {green}{user_data.get('facebook', 'N/A')}{reset}")
        print(f"{style} {green}COUNTRY{reset}        {white}:{reset} {green}{user_data.get('country', 'N/A').upper()}{reset}")
        
        is_active = user_data.get('isActive', False)
        
        if is_active:
            status_display = f"{green}ACTIVE - FULL ACCESS{reset}"
        else:
            status_display = f"{red}INACTIVE - LIMITED{reset}"
        
        print(f"{style} {green}STATUS{reset}         {white}:{reset} {status_display}")
        
        cookie_count = user_data.get('cookieCount', 0)
        print(f"{style} {green}TOTAL COOKIES{reset}  {white}:{reset} {green}{str(cookie_count)}{reset}")
    
    print(LINE)

def show_menu():
    if not user_token:
        print(f"{white}[{reset}{BG_G}{white}01{reset}{white}/{reset}{BG_G}{white}A{reset}{white}]{reset} {green}LOGIN{reset}")
        print(f"{white}[{reset}{BG_C}{white}02{reset}{white}/{reset}{BG_C}{white}B{reset}{white}]{reset} {cyan}REGISTER{reset}")
        print(f"{white}[{reset}{BG_R}{white}00{reset}{white}/{reset}{BG_R}{white}X{reset}{white}]{reset} {red}EXIT{reset}")
    elif user_data and user_data.get('isAdmin'):
        print(f"{white}[{reset}{BG_G}{white}01{reset}{white}/{reset}{BG_G}{white}A{reset}{white}]{reset} {green}AUTO SHARE              — NORM ACCOUNTS{reset}")
        print(f"{white}[{reset}{BG_M}{white}02{reset}{white}/{reset}{BG_M}{white}B{reset}{white}]{reset} {purple}SMM PANEL               — MOST RECOMMENDED{reset}")
        print(f"{white}[{reset}{BG_C}{white}03{reset}{white}/{reset}{BG_C}{white}C{reset}{white}]{reset} {cyan}MANAGE COOKIES          — DATABASE{reset}")
        print(f"{white}[{reset}{BG_B}{white}04{reset}{white}/{reset}{BG_B}{white}D{reset}{white}]{reset} {blue}MY STATS                — STATISTICS{reset}")
        print(f"{white}[{reset}{BG_Y}{white}05{reset}{white}/{reset}{BG_Y}{white}E{reset}{white}]{reset} {yellow}ADMIN PANEL             — MANAGEMENT{reset}")
        print(f"{white}[{reset}{BG_G}{white}06{reset}{white}/{reset}{BG_G}{white}F{reset}{white}]{reset} {green}UPDATE TOOL             — LATEST VERSION{reset}")
        print(f"{white}[{reset}{BG_R}{white}00{reset}{white}/{reset}{BG_R}{white}X{reset}{white}]{reset} {red}LOGOUT{reset}")
    elif user_data and user_data.get('isActive'):
        print(f"{white}[{reset}{BG_G}{white}01{reset}{white}/{reset}{BG_G}{white}A{reset}{white}]{reset} {green}AUTO SHARE              — NORM ACCOUNTS{reset}")
        print(f"{white}[{reset}{BG_M}{white}02{reset}{white}/{reset}{BG_M}{white}B{reset}{white}]{reset} {purple}SMM PANEL               — MOST RECOMMENDED{reset}")
        print(f"{white}[{reset}{BG_C}{white}03{reset}{white}/{reset}{BG_C}{white}C{reset}{white}]{reset} {cyan}MANAGE COOKIES          — DATABASE{reset}")
        print(f"{white}[{reset}{BG_B}{white}04{reset}{white}/{reset}{BG_B}{white}D{reset}{white}]{reset} {blue}MY STATS                — STATISTICS{reset}")
        print(f"{white}[{reset}{BG_G}{white}05{reset}{white}/{reset}{BG_G}{white}E{reset}{white}]{reset} {green}UPDATE TOOL             — LATEST VERSION{reset}")
        print(f"{white}[{reset}{BG_R}{white}00{reset}{white}/{reset}{BG_R}{white}X{reset}{white}]{reset} {red}LOGOUT{reset}")
    else:
        print(f"{white}[{reset}{BG_C}{white}01{reset}{white}/{reset}{BG_C}{white}A{reset}{white}]{reset} {cyan}MANAGE COOKIES          — DATABASE{reset}")
        print(f"{white}[{reset}{BG_B}{white}02{reset}{white}/{reset}{BG_B}{white}B{reset}{white}]{reset} {blue}MY STATS                — STATISTICS{reset}")
        print(f"{white}[{reset}{BG_R}{white}00{reset}{white}/{reset}{BG_R}{white}X{reset}{white}]{reset} {red}LOGOUT{reset}")
    print(LINE)

def refresh_screen():
    clear()
    banner_header()
    show_menu()

def nice_loader(text="PROCESSING"):
    """Loader animation"""
    sys.stdout.write("\033[?25l")
    animation = [f"[{red}■{reset}□□□□□□□□□]",f"[{green}■■{reset}□□□□□□□□]", f"[{yellow}■■■{reset}□□□□□□□]", f"[{blue}■■■■{reset}□□□□□□]", f"[{purple}■■■■■{reset}□□□□□]", f"[{cyan}■■■■■■{reset}□□□□]", f"[{white}■■■■■■■{reset}□□□]", f"[{green}■■■■■■■■{reset}□□]", f"[{yellow}■■■■■■■■■{reset}□]", f"[{blue}■■■■■■■■■■{reset}]"]
    
    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write(f"\r{style} {green}{text}{reset} {white}:{reset} " + animation[i % len(animation)])
        sys.stdout.flush()
    
    sys.stdout.write(f"\r{' ' * 80}\r")
    sys.stdout.flush()
    sys.stdout.write("\033[?25h")

def select_progress_display():
    refresh_screen()
    print(f"{style} {green}SHARING PROGRESS DISPLAY{reset}")
    print(LINE)
    print(f"{style} {green}Choose how you want to see sharing progress:{reset}")
    print(LINE)
    print(f"{white}[{reset}{BG_G}{white}1{reset}{white}]{reset} {green}SUCCESS COUNTER (1/100){reset}")
    print(f"     {cyan}• Best for smaller screens (mobile){reset}")
    print(LINE)
    print(f"{white}[{reset}{BG_C}{white}2{reset}{white}]{reset} {cyan}DETAILED LOGS{reset}")
    print(f"     {green}• Best for larger screens (desktop){reset}")
    print(LINE)
    
    while True:
        choice = input(f"{white}[{white}?{white}]{reset} {green}CHOICE (1 or 2){reset} {white}:{reset} {green}").strip()
        if choice == '1':
            return 'minimal'
        elif choice == '2':
            return 'detailed'
        else:
            print(f"{stylee} {red}Invalid choice. Please enter 1 or 2{reset}")
            time.sleep(1)
            sys.stdout.write("\033[F\033[K")
            sys.stdout.flush()

def get_country_from_ip():
    try:
        response = requests.get('http://ip-api.com/json/', timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get('country', 'Unknown')
    except:
        pass
    return 'Unknown'

def api_request(method, endpoint, data=None, use_token=True):
    headers = {"Content-Type": "application/json"}
    
    if use_token and user_token:
        headers["Authorization"] = f"Bearer {user_token}"
    
    url = f"{API_URL}{endpoint}"
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, timeout=10)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers, timeout=10)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=headers, timeout=10)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, timeout=10)
        else:
            return None, "Invalid method"
        
        return response.status_code, response.json()
    except requests.exceptions.ConnectionError:
        return None, "Cannot connect to server"
    except requests.exceptions.Timeout:
        return None, "Request timeout"
    except Exception as e:
        return None, f"Error: {str(e)}"

def display_prompt_with_bg(display_text, bg_color=BG_C):
    """Display prompt with background color"""
    print(f"{white}[{white}?{white}]{reset} {bg_color}{white} {display_text} {reset} {white}:{reset} {green}", end='', flush=True)

def login_user():
    global user_token, user_data
    
    refresh_screen()
    print(f"{style} {green}LOGIN TO RPWTOOLS{reset}")
    print(LINE)
    
    display_prompt_with_bg("USERNAME", BG_C)
    username = input().strip()
    if not username:
        return
    
    display_prompt_with_bg("PASSWORD", BG_C)
    password = input().strip()
    if not password:
        return
    
    refresh_screen()
    nice_loader("LOGGING IN")
    
    status, response = api_request("POST", "/auth/login", {
        "username": username,
        "password": password
    }, use_token=False)
    
    if status == 200 and response.get('success'):
        user_token = response.get('token')
        user_data = response.get('user')
        
        print(f"{style} {green}Login successful!{reset}")
        print(LINE)
        print(f"{style} {green}Welcome back,{reset} {purple}{user_data['username'].upper()}{reset}")
        
        is_active = user_data.get('isActive', False)
        
        if is_active:
            status_text = 'ACTIVE - FULL ACCESS'
            print(f"{style} {green}Status:{reset} {green}{status_text}{reset}")
        else:
            status_text = 'INACTIVE - LIMITED ACCESS'
            print(f"{style} {green}Status:{reset} {red}{status_text}{reset}")
            print(f"{stylee} {yellow}You can only manage cookies. Contact admin to activate.{reset}")
        
        print(f"{style} {green}Total Cookies:{reset} {cyan}{str(user_data.get('cookieCount', 0))}{reset}")
        
        if user_data.get('isAdmin'):
            print(f"{style} {purple}ADMIN ACCESS GRANTED{reset}")
        
        print(LINE)
    elif status == 403:
        if response.get('allowLimited'):
            user_token = response.get('token')
            user_data = response.get('user')
            print(f"{stylee} {yellow}LIMITED ACCESS{reset}")
            print(LINE)
            print(f"{stylee} {yellow}{response.get('message', 'Account not activated')}{reset}")
            print(f"{style} {cyan}You can still manage cookies.{reset}")
            print(LINE)
        else:
            print(f"{stylee} {red}ACCESS DENIED{reset}")
            print(LINE)
            print(f"{stylee} {red}{response.get('message', 'Account not activated')}{reset}")
            print(LINE)
    else:
        print(f"{stylee} {red}{response if isinstance(response, str) else response.get('message', 'Login failed')}{reset}")
        print(LINE)
    
    input(f"\n{style} {green}PRESS ENTER TO CONTINUE{reset}")

def register_user():
    global user_token, user_data
    
    refresh_screen()
    print(f"{style} {green}REGISTER NEW ACCOUNT{reset}")
    print(LINE)
    
    display_prompt_with_bg("USERNAME", BG_C)
    username = input().strip()
    if not username:
        return
    
    display_prompt_with_bg("PASSWORD", BG_C)
    password = input().strip()
    if not password:
        return
    
    display_prompt_with_bg("FACEBOOK LINK", BG_C)
    facebook = input().strip()
    if not facebook:
        return
    
    facebook = normalize_facebook_url(facebook)
    
    refresh_screen()
    print(f"{style} {green}NORMALIZED FACEBOOK URL:{reset} {cyan}{facebook}{reset}")
    print(LINE)
    
    print(f"{style} {green}DETECTING YOUR COUNTRY...{reset}")
    nice_loader("DETECTING")
    
    country = get_country_from_ip()
    
    refresh_screen()
    print(f"{style} {green}DETECTED COUNTRY:{reset} {cyan}{country}{reset}")
    print(LINE)
    confirm = input(f"{white}[{white}?{white}]{reset} {green}Is this correct? (Y/N){reset} {white}:{reset} {green}").strip().upper()
    
    if confirm == 'N':
        country = input(f"{white}[{white}?{white}]{reset} {cyan}ENTER YOUR COUNTRY{reset} {white}:{reset} {green}").strip()
    
    refresh_screen()
    nice_loader("REGISTERING")
    
    status, response = api_request("POST", "/auth/register", {
        "username": username,
        "password": password,
        "facebook": facebook,
        "country": country
    }, use_token=False)
    
    if status == 201 and response.get('success'):
        user_token = response.get('token')
        user_data = response.get('user')
        
        print(f"{style} {green}Registration successful!{reset}")
        print(LINE)
        print(f"{style} {purple}{user_data['username'].upper()}{reset}")
        print(f"{style} {cyan}Your account has been created!{reset}")
        print(LINE)
        print(f"{stylee} {red}IMPORTANT NOTICE:{reset}")
        print(f"{style} {cyan}Your account is currently INACTIVE.{reset}")
        print(f"{style} {cyan}Please contact an administrator to activate your account.{reset}")
        print(f"{style} {cyan}You can still manage cookies while waiting for activation.{reset}")
        print(LINE)
    else:
        print(f"{stylee} {red}{response if isinstance(response, str) else response.get('message', 'Registration failed')}{reset}")
        print(LINE)
    
    input(f"\n{style} {green}PRESS ENTER TO CONTINUE{reset}")

def show_user_stats():
    refresh_screen()
    print(f"{style} {green}LOADING STATS...{reset}")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/user/stats")
    
    if status == 200 and response.get('success'):
        stats = response.get('stats')
        
        refresh_screen()
        print(f"{style} {green}USER STATISTICS{reset}")
        print(LINE)
        print(f"{style} {cyan}Username:{reset} {white}{stats['username'].upper()}{reset}")
        
        is_active = stats.get('isActive', False)
        status_display = f"{green}ACTIVE - FULL ACCESS{reset}" if is_active else f"{red}INACTIVE - LIMITED{reset}"
        print(f"{style} {cyan}Account Status:{reset} {status_display}")
        
        print(LINE)
        print(f"{style} {cyan}STATISTICS{reset}")
        print(f"{style} {green}Total Shares:{reset} {purple}{str(stats['totalShares'])}{reset}")
        print(f"{style} {green}Total Cookies:{reset} {cyan}{str(stats.get('cookieCount', 0))}{reset}")
        print(LINE)
    else:
        print(f"{stylee} {red}Failed to get stats{reset}")
        print(LINE)
    
    input(f"\n{style} {green}PRESS ENTER TO CONTINUE{reset}")

def manage_cookies():
    while True:
        refresh_screen()
        print(f"{style} {green}MANAGE COOKIES{reset}")
        print(LINE)
        print(f"{white}[{white}1{white}]{reset} {green}VIEW ALL COOKIES{reset}")
        print(f"{white}[{white}2{white}]{reset} {green}ADD COOKIE{reset}")
        print(f"{white}[{white}3{white}]{reset} {red}DELETE COOKIE{reset}")
        print(f"{white}[{white}4{white}]{reset} {red}DELETE ALL COOKIES{reset}")
        print(f"{white}[{white}0{white}]{reset} {cyan}BACK{reset}")
        print(LINE)
        
        choice = input(f"{white}[{white}?{white}]{reset} {cyan}CHOICE{reset} {white}:{reset} {green}").strip()
        
        if choice == '1':
            view_cookies()
        elif choice == '2':
            add_cookie()
        elif choice == '3':
            delete_cookie()
        elif choice == '4':
            delete_all_cookies()
        elif choice == '0':
            return
        else:
            print(f"\n{stylee} {red}INVALID SELECTION{reset}")
            time.sleep(0.8)

def view_cookies():
    refresh_screen()
    print(f"{style} {green}LOADING COOKIES...{reset}")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/user/cookies")
    
    if status == 200 and response.get('success'):
        cookies = response.get('cookies', [])
        
        refresh_screen()
        print(f"{style} {green}COOKIES Total: {len(cookies)}{reset}")
        print(LINE)
        
        if not cookies:
            print(f"{style} {cyan}No cookies stored yet.{reset}")
        else:
            for i, cookie_data in enumerate(cookies, 1):
                status_display = f"{green}[ACTIVE]{reset}" if cookie_data['status'] == 'active' else f"{red}[RESTRICTED]{reset}"
                
                uid_text = f"UID: {cookie_data['uid']}"
                print(f"{white}[{i:02d}]{reset} {purple}{cookie_data['name']}{reset} {white}({cyan}{uid_text}{reset}){reset}")
                cookie_preview = cookie_data['cookie'][:50] + "..." if len(cookie_data['cookie']) > 50 else cookie_data['cookie']
                print(f"      Cookie: {cyan}{cookie_preview}{reset}")
                print(f"      Added: {green}{cookie_data['addedAt']}{reset}")
                print(f"      Status: {status_display}")
                
                if cookie_data['status'] == 'restricted':
                    print(f"      {stylee} {red}WARNING: This account is restricted!{reset}")
                
                print(LINE)
        
    else:
        print(f"{stylee} {red}Failed to load cookies{reset}")
        print(LINE)
    
    input(f"\n{style} {green}PRESS ENTER TO CONTINUE{reset}")

def add_cookie():
    refresh_screen()
    print(f"{style} {green}ADD COOKIE{reset}")
    print(LINE)
    
    display_prompt_with_bg("COOKIE", BG_C)
    cookie = input().strip()
    if not cookie:
        return
    
    refresh_screen()
    print(f"{style} {green}VALIDATING COOKIE...{reset}")
    print(f"{style} {cyan}This may take 10-15 seconds{reset}")
    print(LINE)
    nice_loader("VALIDATING")
    
    status, response = api_request("POST", "/user/cookies", {"cookie": cookie})
    
    if status == 200 and isinstance(response, dict) and response.get('success'):
        print(f"{style} {green}{response.get('message')}{reset}")
        print(LINE)
        print(f"{style} {cyan}Name:{reset} {purple}{response.get('name', 'Unknown')}{reset}")
        print(f"{style} {cyan}UID:{reset} {cyan}{response.get('uid', 'Unknown')}{reset}")
        status_display = f"{green}{response.get('status', 'unknown').upper()}{reset}" if response.get('status') == 'active' else f"{red}{response.get('status', 'unknown').upper()}{reset}"
        print(f"{style} {cyan}Status:{reset} {status_display}")
        
        if response.get('restricted'):
            print(LINE)
            print(f"{stylee} {red}WARNING: This account is RESTRICTED!{reset}")
            print(f"{style} {cyan}Restricted accounts may not be able to share posts.{reset}")
        
        if user_data:
            user_data['cookieCount'] = response.get('totalCookies', 0)
        
        print(LINE)
    else:
        error_msg = response if isinstance(response, str) else response.get('message', 'Failed to add cookie') if isinstance(response, dict) else 'Failed to add cookie'
        print(f"{stylee} {red}{error_msg}{reset}")
        print(LINE)
    
    input(f"\n{style} {green}PRESS ENTER TO CONTINUE{reset}")

def delete_cookie():
    refresh_screen()
    print(f"{style} {green}LOADING COOKIES...{reset}")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/user/cookies")
    
    if status != 200 or not isinstance(response, dict) or not response.get('success'):
        error_msg = response if isinstance(response, str) else 'Failed to load cookies'
        print(f"{stylee} {red}{error_msg}{reset}")
        input(f"\n{style} {green}PRESS ENTER TO CONTINUE{reset}")
        return
    
    cookies = response.get('cookies', [])
    
    if not cookies:
        refresh_screen()
        print(f"{style} {cyan}No cookies to delete.{reset}")
        input(f"\n{style} {green}PRESS ENTER TO CONTINUE{reset}")
        return
    
    refresh_screen()
    print(f"{stylee} {red}DELETE COOKIE{reset}")
    print(LINE)
    
    for i, cookie_data in enumerate(cookies, 1):
        status_indicator = f"{red}[RESTRICTED]{reset}" if cookie_data.get('status') == 'restricted' else f"{green}[ACTIVE]{reset}"
        uid_text = f"UID: {cookie_data['uid']}"
        print(f"{white}[{i}]{reset} {purple}{cookie_data['name']}{reset} {white}({cyan}{uid_text}{reset}){reset} {status_indicator}")
    
    print(LINE)
    
    choice = input(f"{white}[{white}?{white}]{reset} {cyan}SELECT COOKIE NUMBER (0 to cancel){reset} {white}:{reset} {green}").strip()
    
    if not choice or choice ==
