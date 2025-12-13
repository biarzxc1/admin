import os
import sys
import time
import json
import aiohttp
import asyncio
import datetime
import requests
import re

try:
    from colorama import init
    init()
except ImportError:
    print("ERROR: colorama not installed. Please run: pip install -r requirements.txt")
    sys.exit(1)

# --- GRADIENT COLOR SYSTEM ---
def get_gradient_color(progress, color_scheme='purple_cyan'):
    progress = max(0, min(1, progress))
    
    color_schemes = {
        'purple_cyan': [
            (138, 43, 226), (147, 51, 234), (168, 85, 247), (192, 132, 252),
            (216, 180, 254), (147, 197, 253), (125, 211, 252), (34, 211, 238),
        ],
        'green_yellow': [
            (16, 185, 129), (52, 211, 153), (110, 231, 183), (167, 243, 208),
            (253, 224, 71), (250, 204, 21),
        ],
        'red_orange': [
            (220, 38, 38), (239, 68, 68), (248, 113, 113), (251, 146, 60),
            (253, 186, 116), (254, 215, 170),
        ],
        'blue_purple': [
            (37, 99, 235), (59, 130, 246), (96, 165, 250), (147, 197, 253),
            (167, 139, 250), (196, 181, 253),
        ]
    }
    
    levels = color_schemes.get(color_scheme, color_schemes['purple_cyan'])
    
    index = progress * (len(levels) - 1)
    lower_index = int(index)
    upper_index = min(lower_index + 1, len(levels) - 1)
    
    if lower_index == upper_index:
        r, g, b = levels[lower_index]
    else:
        fraction = index - lower_index
        r1, g1, b1 = levels[lower_index]
        r2, g2, b2 = levels[upper_index]
        
        r = int(r1 + (r2 - r1) * fraction)
        g = int(g1 + (g2 - g1) * fraction)
        b = int(b1 + (b2 - b1) * fraction)
    
    return f'\033[38;2;{r};{g};{b}m'

def apply_gradient(text, color_scheme='purple_cyan'):
    if not text.strip():
        return text
    
    result = []
    chars = [c for c in text if c != ' ']
    
    if not chars:
        return text
    
    char_index = 0
    for c in text:
        if c == ' ':
            result.append(c)
        else:
            progress = char_index / max(1, len(chars) - 1)
            color = get_gradient_color(progress, color_scheme)
            result.append(color + c + '\033[0m')
            char_index += 1
    
    return ''.join(result)

# Color helpers
G = lambda text: apply_gradient(str(text), 'green_yellow')
R = lambda text: apply_gradient(str(text), 'red_orange')
C = lambda text: apply_gradient(str(text), 'purple_cyan')
Y = lambda text: apply_gradient(str(text), 'green_yellow')
M = lambda text: apply_gradient(str(text), 'blue_purple')
B = lambda text: apply_gradient(str(text), 'purple_cyan')
W = '\033[1;37m'
RESET = '\033[0m'

BG_R = '\033[41m'
BG_G = '\033[42m'
BG_C = '\033[46m'
BG_M = '\033[45m'
BG_Y = '\033[43m'
BG_B = '\033[44m'

LINE = apply_gradient("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", 'purple_cyan')

# --- API CONFIGURATION ---
API_URL = "https://rpwtools.onrender.com/api"
CURRENT_VERSION = "1.0.6"
user_token = None
user_data = None

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

def check_version():
    try:
        status, response = api_request("GET", "/version", use_token=False)
        if status == 200 and response.get('success'):
            server_version = response.get('version', '1.0.0')
            if server_version != CURRENT_VERSION:
                clear()
                print(LINE)
                print(f" {R('[VERSION MISMATCH]')}")
                print(LINE)
                print(f" {C('Your tool version:')} {R(CURRENT_VERSION)}")
                print(f" {C('Server version:')} {G(server_version)}")
                print(LINE)
                print(f" {R('⚠ Your tool is outdated!')}")
                print(f" {C('Please update to the latest version.')}")
                print(LINE)
                input(f"\n {R('[PRESS ENTER TO EXIT]')}")
                sys.exit(1)
    except:
        pass

def banner_header():
    banner_art = """
    ╦═╗╔═╗╦ ╦╔╦╗╔═╗╔═╗╦  ╔═╗
    ╠╦╝╠═╝║║║ ║ ║ ║║ ║║  ╚═╗
    ╩╚═╩  ╚╩╝ ╩ ╚═╝╚═╝╩═╝╚═╝
    """
    print(apply_gradient(banner_art, 'purple_cyan'))
    print(LINE)
    print(f" {W}[{RESET}•{W}]{RESET} {C('DEVELOPER')}     {W}➤{RESET} {G('KEN DRICK')}")
    print(f" {W}[{RESET}•{W}]{RESET} {C('GITHUB')}        {W}➤{RESET} {G('RYO GRAHHH')}")
    print(f" {W}[{RESET}•{W}]{RESET} {C('VERSION')}       {W}➤{RESET} {G(CURRENT_VERSION)}")
    print(f" {W}[{RESET}•{W}]{RESET} {C('FACEBOOK')}      {W}➤{RESET} {G('facebook.com/ryoevisu')}")
    print(f" {W}[{RESET}•{W}]{RESET} {C('TOOL NAME')}     {W}➤{RESET} {R('[ RPWTOOLS ]')}")
    
    if user_data:
        print(LINE)
        print(f" {W}[{RESET}•{W}]{RESET} {C('USERNAME')}      {W}➤{RESET} {G(user_data['username'].upper())}")
        print(f" {W}[{RESET}•{W}]{RESET} {C('FACEBOOK')}      {W}➤{RESET} {G(user_data.get('facebook', 'N/A'))}")
        print(f" {W}[{RESET}•{W}]{RESET} {C('COUNTRY')}       {W}➤{RESET} {G(user_data.get('country', 'N/A').upper())}")
        
        is_active = user_data.get('isActive', False)
        if is_active:
            status_display = G('[ACTIVE]')
        else:
            status_display = R('[INACTIVE]')
        
        print(f" {W}[{RESET}•{W}]{RESET} {C('STATUS')}        {W}➤{RESET} {status_display}")
        
        if user_data.get('isAdmin'):
            print(f" {W}[{RESET}•{W}]{RESET} {C('ACCESS')}        {W}➤{RESET} {M('[ADMIN]')}")
        
        cookie_count = user_data.get('cookieCount', 0)
        print(f" {W}[{RESET}•{W}]{RESET} {C('COOKIES')}       {W}➤{RESET} {G(str(cookie_count))}")
    
    print(LINE)

def show_menu():
    if not user_token:
        print(f" {W}[{RESET}{BG_G}{W}01{RESET}{BG_G}{W}/{RESET}{BG_G}{W}A{RESET}{W}]{RESET} {G('LOGIN')}")
        print(f" {W}[{RESET}{BG_C}{W}02{RESET}{BG_C}{W}/{RESET}{BG_C}{W}B{RESET}{W}]{RESET} {C('REGISTER')}")
        print(f" {W}[{RESET}{BG_R}{W}00{RESET}{BG_R}{W}/{RESET}{BG_R}{W}X{RESET}{W}]{RESET} {R('EXIT')}")
    elif user_data and user_data.get('isAdmin'):
        print(f" {W}[{RESET}{BG_G}{W}01{RESET}{BG_G}{W}/{RESET}{BG_G}{W}A{RESET}{W}]{RESET} {G('AUTO SHARE              — SMM BOOSTER')}")
        print(f" {W}[{RESET}{BG_C}{W}02{RESET}{BG_C}{W}/{RESET}{BG_C}{W}B{RESET}{W}]{RESET} {C('MANAGE COOKIES          — DATABASE')}")
        print(f" {W}[{RESET}{BG_B}{W}03{RESET}{BG_B}{W}/{RESET}{BG_B}{W}C{RESET}{W}]{RESET} {B('MY STATS                — STATISTICS')}")
        print(f" {W}[{RESET}{BG_M}{W}04{RESET}{BG_M}{W}/{RESET}{BG_M}{W}D{RESET}{W}]{RESET} {M('ADMIN PANEL             — MANAGEMENT')}")
        print(f" {W}[{RESET}{BG_G}{W}05{RESET}{BG_G}{W}/{RESET}{BG_G}{W}E{RESET}{W}]{RESET} {G('UPDATE TOOL             — LATEST VERSION')}")
        print(f" {W}[{RESET}{BG_R}{W}00{RESET}{BG_R}{W}/{RESET}{BG_R}{W}X{RESET}{W}]{RESET} {R('LOGOUT')}")
    else:
        print(f" {W}[{RESET}{BG_G}{W}01{RESET}{BG_G}{W}/{RESET}{BG_G}{W}A{RESET}{W}]{RESET} {G('AUTO SHARE              — SMM BOOSTER')}")
        print(f" {W}[{RESET}{BG_Y}{W}02{RESET}{BG_Y}{W}/{RESET}{BG_Y}{W}B{RESET}{W}]{RESET} {C('MANAGE COOKIES          — DATABASE')}")
        print(f" {W}[{RESET}{BG_B}{W}03{RESET}{BG_B}{W}/{RESET}{BG_B}{W}C{RESET}{W}]{RESET} {B('MY STATS                — STATISTICS')}")
        print(f" {W}[{RESET}{BG_G}{W}04{RESET}{BG_G}{W}/{RESET}{BG_G}{W}D{RESET}{W}]{RESET} {G('UPDATE TOOL             — LATEST VERSION')}")
        print(f" {W}[{RESET}{BG_R}{W}00{RESET}{BG_R}{W}/{RESET}{BG_R}{W}X{RESET}{W}]{RESET} {R('LOGOUT')}")
    print(LINE)

def refresh_screen():
    clear()
    banner_header()
    show_menu()

def nice_loader(text="PROCESSING"):
    sys.stdout.write("\033[?25l")
    filled = "■"
    empty = "□"
    width = 20
    
    for i in range(width + 1):
        percent = int((i / width) * 100)
        bar = filled * i + empty * (width - i)
        bar_gradient = apply_gradient(bar, 'purple_cyan')
        
        sys.stdout.write(f"\r {W}[{RESET}•{W}]{RESET} {G(text)} {W}➤{RESET} [{bar_gradient}] {M(f'{percent}%')}")
        sys.stdout.flush()
        time.sleep(0.04)
    
    time.sleep(0.3)
    sys.stdout.write(f"\r{' ' * 80}\r")
    sys.stdout.flush()
    sys.stdout.write("\033[?25h")

def select_progress_display():
    refresh_screen()
    print(f" {C('[SHARING PROGRESS DISPLAY]')}")
    print(LINE)
    print(f" {W}[{RESET}{BG_G}{W}1{RESET}{W}]{RESET} {G('SUCCESS COUNTER (1/100)')}")
    print(f"     {C('• Best for mobile')}")
    print(LINE)
    print(f" {W}[{RESET}{BG_C}{W}2{RESET}{W}]{RESET} {C('DETAILED LOGS')}")
    print(f"     {G('• Best for desktop')}")
    print(LINE)
    
    while True:
        choice = input(f" {W}[{W}➤{W}]{RESET} {C('CHOICE (1 or 2)')} {W}➤{RESET} ").strip()
        if choice == '1':
            return 'minimal'
        elif choice == '2':
            return 'detailed'
        else:
            print(f" {R('[!] Invalid choice')}")
            time.sleep(0.5)
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

def login_user():
    global user_token, user_data
    
    refresh_screen()
    print(f" {G('[!] LOGIN TO RPWTOOLS')}")
    print(LINE)
    
    username = input(f" {W}[{W}➤{W}]{RESET} {C('USERNAME')} {W}➤{RESET} ").strip()
    if not username:
        return
    
    password = input(f" {W}[{W}➤{W}]{RESET} {C('PASSWORD')} {W}➤{RESET} ").strip()
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
        
        print(f" {G('[SUCCESS] Login successful!')}")
        print(LINE)
        print(f" {G('Welcome back,')} {M(user_data['username'].upper())}")
        
        is_active = user_data.get('isActive', False)
        print(f" {G('Status:')} {G('ACTIVE') if is_active else R('INACTIVE')}")
        print(f" {G('Total Cookies:')} {C(str(user_data.get('cookieCount', 0)))}")
        
        if user_data.get('isAdmin'):
            print(f" {M('[ADMIN ACCESS GRANTED]')}")
        
        print(LINE)
    elif status == 403:
        print(f" {R('[ACCESS DENIED]')}")
        print(LINE)
        print(f" {R(response.get('message', 'Account not activated'))}")
        print(f" {C('Please contact an administrator to activate your account.')}")
        print(LINE)
    else:
        print(f" {R('[ERROR]')} {R(response if isinstance(response, str) else response.get('message', 'Login failed'))}")
        print(LINE)
    
    input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")

def register_user():
    global user_token, user_data
    
    refresh_screen()
    print(f" {G('[!] REGISTER NEW ACCOUNT')}")
    print(LINE)
    
    username = input(f" {W}[{W}➤{W}]{RESET} {C('USERNAME')} {W}➤{RESET} ").strip()
    if not username:
        return
    
    password = input(f" {W}[{W}➤{W}]{RESET} {C('PASSWORD')} {W}➤{RESET} ").strip()
    if not password:
        return
    
    facebook = input(f" {W}[{W}➤{W}]{RESET} {C('FACEBOOK LINK')} {W}➤{RESET} ").strip()
    if not facebook:
        return
    
    facebook = normalize_facebook_url(facebook)
    
    refresh_screen()
    print(f" {G('[!] DETECTING YOUR COUNTRY...')}")
    nice_loader("DETECTING")
    
    country = get_country_from_ip()
    
    refresh_screen()
    print(f" {G('[!] DETECTED COUNTRY:')} {C(country)}")
    print(LINE)
    confirm = input(f" {W}[{W}➤{W}]{RESET} {G('Is this correct? (Y/N)')} {W}➤{RESET} ").strip().upper()
    
    if confirm == 'N':
        country = input(f" {W}[{W}➤{W}]{RESET} {C('ENTER YOUR COUNTRY')} {W}➤{RESET} ").strip()
    
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
        
        print(f" {G('[SUCCESS] Registration successful!')}")
        print(LINE)
        print(f" {M(user_data['username'].upper())}")
        print(f" {C('Your account has been created!')}")
        print(LINE)
        print(f" {R('⚠ IMPORTANT:')}")
        print(f" {C('Your account is currently INACTIVE.')}")
        print(f" {C('Contact admin to activate your account.')}")
        print(LINE)
    else:
        print(f" {R('[ERROR]')} {R(response if isinstance(response, str) else response.get('message', 'Registration failed'))}")
        print(LINE)
    
    input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")

def show_user_stats():
    refresh_screen()
    print(f" {G('[!] LOADING STATS...')}")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/user/stats")
    
    if status == 200 and response.get('success'):
        stats = response.get('stats')
        
        refresh_screen()
        print(f" {G('[USER STATISTICS]')}")
        print(LINE)
        print(f" {W}[{RESET}•{W}]{RESET} {C('USERNAME')}      {W}➤{RESET} {G(stats['username'].upper())}")
        
        is_active = stats.get('isActive', False)
        status_display = G('ACTIVE') if is_active else R('INACTIVE')
        print(f" {W}[{RESET}•{W}]{RESET} {C('STATUS')}        {W}➤{RESET} {status_display}")
        print(f" {W}[{RESET}•{W}]{RESET} {C('TOTAL SHARES')}  {W}➤{RESET} {M(str(stats['totalShares']))}")
        print(f" {W}[{RESET}•{W}]{RESET} {C('COOKIES')}       {W}➤{RESET} {G(str(stats.get('cookieCount', 0)))}")
        print(LINE)
    else:
        print(f" {R('[ERROR]')} {R('Failed to get stats')}")
        print(LINE)
    
    input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")

def manage_cookies():
    while True:
        refresh_screen()
        print(f" {G('[MANAGE COOKIES]')}")
        print(LINE)
        print(f" {W}[{W}1{W}]{RESET} {G('VIEW ALL COOKIES')}")
        print(f" {W}[{W}2{W}]{RESET} {G('ADD COOKIE')}")
        print(f" {W}[{W}3{W}]{RESET} {R('DELETE COOKIE')}")
        print(f" {W}[{W}4{W}]{RESET} {R('DELETE ALL COOKIES')}")
        print(f" {W}[{W}0{W}]{RESET} {C('BACK')}")
        print(LINE)
        
        choice = input(f" {W}[{W}➤{W}]{RESET} {C('CHOICE')} {W}➤{RESET} ").strip()
        
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
            print(f"\n {R('[!] INVALID')}")
            time.sleep(0.5)

def view_cookies():
    refresh_screen()
    print(f" {G('[!] LOADING COOKIES...')}")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/user/cookies")
    
    if status == 200 and response.get('success'):
        cookies = response.get('cookies', [])
        
        refresh_screen()
        print(f" {G(f'[COOKIES] Total: {len(cookies)}')}")
        print(LINE)
        
        if not cookies:
            print(f" {C('No cookies stored yet.')}")
        else:
            for i, cookie_data in enumerate(cookies, 1):
                status_display = G('[ACTIVE]') if cookie_data['status'] == 'active' else R('[RESTRICTED]')
                uid_text = f"UID: {cookie_data['uid']}"
                print(f" {W}[{i:02d}]{RESET} {M(cookie_data['name'])} {W}({C(uid_text)}){RESET}")
                cookie_preview = cookie_data['cookie'][:50] + "..." if len(cookie_data['cookie']) > 50 else cookie_data['cookie']
                print(f"      Cookie: {C(cookie_preview)}")
                print(f"      Status: {status_display}")
                print(LINE)
    else:
        print(f" {R('[ERROR] Failed to load cookies')}")
        print(LINE)
    
    input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")

def add_cookie():
    refresh_screen()
    print(f" {G('[ADD COOKIE]')}")
    print(LINE)
    
    cookie = input(f" {W}[{W}➤{W}]{RESET} {C('COOKIE')} {W}➤{RESET} ").strip()
    if not cookie:
        return
    
    refresh_screen()
    print(f" {G('[!] VALIDATING COOKIE...')}")
    nice_loader("VALIDATING")
    
    status, response = api_request("POST", "/user/cookies", {"cookie": cookie})
    
    if status == 200 and isinstance(response, dict) and response.get('success'):
        print(f" {G('[SUCCESS]')} {G(response.get('message'))}")
        print(LINE)
        print(f" {C('Name:')} {M(response.get('name', 'Unknown'))}")
        print(f" {C('UID:')} {C(response.get('uid', 'Unknown'))}")
        
        if user_data:
            user_data['cookieCount'] = response.get('totalCookies', 0)
        
        print(LINE)
    else:
        error_msg = response if isinstance(response, str) else response.get('message', 'Failed to add cookie') if isinstance(response, dict) else 'Failed to add cookie'
        print(f" {R('[ERROR]')} {R(error_msg)}")
        print(LINE)
    
    input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")

def delete_cookie():
    refresh_screen()
    print(f" {G('[!] LOADING COOKIES...')}")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/user/cookies")
    
    if status != 200 or not isinstance(response, dict) or not response.get('success'):
        print(f" {R('[ERROR] Failed to load cookies')}")
        input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")
        return
    
    cookies = response.get('cookies', [])
    
    if not cookies:
        refresh_screen()
        print(f" {C('No cookies to delete.')}")
        input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")
        return
    
    refresh_screen()
    print(f" {R('[DELETE COOKIE]')}")
    print(LINE)
    
    for i, cookie_data in enumerate(cookies, 1):
        uid_text = f"UID: {cookie_data['uid']}"
        print(f" {W}[{i}]{RESET} {M(cookie_data['name'])} {W}({C(uid_text)}){RESET}")
    
    print(LINE)
    
    choice = input(f" {W}[{W}➤{W}]{RESET} {C('SELECT (0 to cancel)')} {W}➤{RESET} ").strip()
    
    if not choice or choice == '0':
        return
    
    try:
        cookie_index = int(choice) - 1
        if cookie_index < 0 or cookie_index >= len(cookies):
            print(f" {R('[ERROR] Invalid')}")
            time.sleep(0.5)
            return
        
        selected_cookie = cookies[cookie_index]
    except:
        print(f" {R('[ERROR] Invalid')}")
        time.sleep(0.5)
        return
    
    refresh_screen()
    nice_loader("DELETING")
    
    status, response = api_request("DELETE", f"/user/cookies/{selected_cookie['id']}")
    
    if status == 200 and isinstance(response, dict) and response.get('success'):
        print(f" {G('[SUCCESS] Cookie deleted!')}")
        if user_data:
            user_data['cookieCount'] = response.get('totalCookies', 0)
    else:
        print(f" {R('[ERROR] Failed to delete')}")
    
    print(LINE)
    input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")

def delete_all_cookies():
    refresh_screen()
    print(f" {R('[DELETE ALL COOKIES]')}")
    print(LINE)
    
    confirm = input(f" {W}[{W}➤{W}]{RESET} {R('Delete ALL? (YES/NO)')} {W}➤{RESET} ").strip().upper()
    
    if confirm != 'YES':
        return
    
    refresh_screen()
    nice_loader("DELETING")
    
    status, response = api_request("DELETE", "/user/cookies")
    
    if status == 200 and response.get('success'):
        print(f" {G('[SUCCESS]')} {G(response.get('message'))}")
        if user_data:
            user_data['cookieCount'] = 0
    else:
        print(f" {R('[ERROR] Failed')}")
    
    print(LINE)
    input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")

def update_tool_logic():
    print(f" {G('[!] CHECKING FOR UPDATES...')}")
    nice_loader("CHECKING")
    print(f" {G('[!] You are using the latest version!')}")
    time.sleep(1)

# ============ ADMIN PANEL ============

def admin_panel():
    while True:
        refresh_screen()
        print(f" {M('[ADMIN PANEL]')}")
        print(LINE)
        print(f" {W}[{W}1{W}]{RESET} {G('VIEW ALL USERS')}")
        print(f" {W}[{W}2{W}]{RESET} {C('ACTIVATE USER')}")
        print(f" {W}[{W}3{W}]{RESET} {R('DEACTIVATE USER')}")
        print(f" {W}[{W}4{W}]{RESET} {R('DELETE USER')}")
        print(f" {W}[{W}5{W}]{RESET} {C('VIEW ACTIVITY LOGS')}")
        print(f" {W}[{W}6{W}]{RESET} {G('DASHBOARD STATS')}")
        print(f" {W}[{W}7{W}]{RESET} {M('VIEW ALL ORDERS')}")
        print(f" {W}[{W}0{W}]{RESET} {C('BACK')}")
        print(LINE)
        
        choice = input(f" {W}[{W}➤{W}]{RESET} {C('CHOICE')} {W}➤{RESET} ").strip()
        
        if choice == '1':
            view_all_users()
        elif choice == '2':
            activate_user()
        elif choice == '3':
            deactivate_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            view_activity_logs()
        elif choice == '6':
            dashboard_stats()
        elif choice == '7':
            view_all_orders()
        elif choice == '0':
            return
        else:
            print(f"\n {R('[!] INVALID')}")
            time.sleep(0.5)

def view_all_users():
    refresh_screen()
    print(f" {G('[!] LOADING USERS...')}")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/admin/users")
    
    if status == 200 and response.get('success'):
        users = response.get('users', [])
        
        refresh_screen()
        print(f" {G(f'[ALL USERS] Total: {len(users)}')}")
        print(LINE)
        
        for i, user in enumerate(users, 1):
            admin_badge = f" {M('[ADMIN]')}" if user.get('isAdmin') else ""
            status_badge = G('[ACTIVE]') if user.get('isActive') else R('[INACTIVE]')
            
            print(f" {W}[{i:02d}]{RESET} {C(user['username'].upper())}{admin_badge} {status_badge}")
            print(f"      Country: {G(user['country'])} | Shares: {G(str(user['totalShares']))}")
            print(f"      Cookies: {C(str(user.get('cookieCount', 0)))}")
            print(LINE)
    else:
        print(f" {R('[ERROR] Failed to get users')}")
        print(LINE)
    
    input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")

def activate_user():
    refresh_screen()
    print(f" {G('[ACTIVATE USER]')}")
    print(LINE)
    
    status, response = api_request("GET", "/admin/users")
    
    if status != 200 or not response.get('success'):
        print(f" {R('[ERROR] Failed to load users')}")
        input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")
        return
    
    users = [u for u in response.get('users', []) if not u.get('isAdmin') and not u.get('isActive')]
    
    if not users:
        print(f" {C('No inactive users.')}")
        input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")
        return
    
    for i, user in enumerate(users, 1):
        print(f" {W}[{i}]{RESET} {C(user['username'].upper())} - {R('[INACTIVE]')}")
    print(LINE)
    
    user_choice = input(f" {W}[{W}➤{W}]{RESET} {C('SELECT (0 to cancel)')} {W}➤{RESET} ").strip()
    
    if not user_choice or user_choice == '0':
        return
    
    try:
        user_index = int(user_choice) - 1
        if user_index < 0 or user_index >= len(users):
            print(f" {R('[ERROR] Invalid')}")
            time.sleep(0.5)
            return
        
        selected_user = users[user_index]
    except:
        print(f" {R('[ERROR] Invalid')}")
        time.sleep(0.5)
        return
    
    refresh_screen()
    nice_loader("ACTIVATING")
    
    status, response = api_request("PUT", f"/admin/users/{selected_user['username']}/activate")
    
    if status == 200 and response.get('success'):
        print(f" {G('[SUCCESS] User activated!')}")
    else:
        print(f" {R('[ERROR]')} {R(response.get('message', 'Failed'))}")
    
    print(LINE)
    input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")

def deactivate_user():
    refresh_screen()
    print(f" {R('[DEACTIVATE USER]')}")
    print(LINE)
    
    status, response = api_request("GET", "/admin/users")
    
    if status != 200 or not response.get('success'):
        print(f" {R('[ERROR] Failed to load users')}")
        input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")
        return
    
    users = [u for u in response.get('users', []) if not u.get('isAdmin') and u.get('isActive')]
    
    if not users:
        print(f" {C('No active users.')}")
        input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")
        return
    
    for i, user in enumerate(users, 1):
        print(f" {W}[{i}]{RESET} {C(user['username'].upper())} - {G('[ACTIVE]')}")
    print(LINE)
    
    user_choice = input(f" {W}[{W}➤{W}]{RESET} {C('SELECT (0 to cancel)')} {W}➤{RESET} ").strip()
    
    if not user_choice or user_choice == '0':
        return
    
    try:
        user_index = int(user_choice) - 1
        if user_index < 0 or user_index >= len(users):
            print(f" {R('[ERROR] Invalid')}")
            time.sleep(0.5)
            return
        
        selected_user = users[user_index]
    except:
        print(f" {R('[ERROR] Invalid')}")
        time.sleep(0.5)
        return
    
    refresh_screen()
    nice_loader("DEACTIVATING")
    
    status, response = api_request("PUT", f"/admin/users/{selected_user['username']}/deactivate")
    
    if status == 200 and response.get('success'):
        print(f" {G('[SUCCESS] User deactivated!')}")
    else:
        print(f" {R('[ERROR]')} {R(response.get('message', 'Failed'))}")
    
    print(LINE)
    input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")

def delete_user():
    refresh_screen()
    print(f" {R('[DELETE USER]')}")
    print(LINE)
    
    status, response = api_request("GET", "/admin/users")
    
    if status != 200 or not response.get('success'):
        print(f" {R('[ERROR] Failed to load users')}")
        input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")
        return
    
    users = [u for u in response.get('users', []) if not u.get('isAdmin')]
    
    if not users:
        print(f" {C('No users to delete.')}")
        input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")
        return
    
    for i, user in enumerate(users, 1):
        status_badge = G('[ACTIVE]') if user.get('isActive') else R('[INACTIVE]')
        print(f" {W}[{i:02d}]{RESET} {C(user['username'].upper())} {status_badge}")
    print(LINE)
    
    choice = input(f" {W}[{W}➤{W}]{RESET} {C('SELECT (0 to cancel)')} {W}➤{RESET} ").strip()
    
    if not choice or choice == '0':
        return
    
    try:
        user_index = int(choice) - 1
        if user_index < 0 or user_index >= len(users):
            print(f" {R('[ERROR] Invalid')}")
            time.sleep(0.5)
            return
        
        selected_user = users[user_index]
    except:
        print(f" {R('[ERROR] Invalid')}")
        time.sleep(0.5)
        return
    
    confirm = input(f" {W}[{W}➤{W}]{RESET} {R('Delete? (YES/NO)')} {W}➤{RESET} ").strip().upper()
    
    if confirm != 'YES':
        return
    
    nice_loader("DELETING")
    
    status, response = api_request("DELETE", f"/admin/users/{selected_user['username']}")
    
    if status == 200 and response.get('success'):
        print(f" {G('[SUCCESS] User deleted!')}")
    else:
        print(f" {R('[ERROR]')} {R(response.get('message', 'Failed'))}")
    
    print(LINE)
    input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")

def view_activity_logs():
    refresh_screen()
    print(f" {G('[!] LOADING LOGS...')}")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/admin/logs?limit=20")
    
    if status == 200 and response.get('success'):
        logs = response.get('logs', [])
        
        refresh_screen()
        print(f" {C('[ACTIVITY LOGS] Recent 20')}")
        print(LINE)
        
        for log in logs:
            action_display = G(log['action'].upper()) if log['action'] == 'login' else C(log['action'].upper())
            print(f" {W}[{log['timestamp']}]{RESET}")
            print(f" User: {C(log['username'].upper())} | Action: {action_display}")
            if log.get('details'):
                print(f" Details: {G(log['details'])}")
            print(LINE)
    else:
        print(f" {R('[ERROR] Failed to load logs')}")
        print(LINE)
    
    input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")

def dashboard_stats():
    refresh_screen()
    print(f" {G('[!] LOADING DASHBOARD...')}")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/admin/dashboard")
    
    if status == 200 and response.get('success'):
        stats = response.get('stats', {})
        
        refresh_screen()
        print(f" {G('[ADMIN DASHBOARD]')}")
        print(LINE)
        print(f" {W}[{RESET}•{W}]{RESET} {C('TOTAL USERS')}     {W}➤{RESET} {G(str(stats['totalUsers']))}")
        print(f" {W}[{RESET}•{W}]{RESET} {C('ACTIVE USERS')}    {W}➤{RESET} {G(str(stats['activeUsers']))}")
        print(f" {W}[{RESET}•{W}]{RESET} {C('INACTIVE USERS')}  {W}➤{RESET} {R(str(stats['inactiveUsers']))}")
        print(f" {W}[{RESET}•{W}]{RESET} {C('TOTAL SHARES')}    {W}➤{RESET} {M(str(stats['totalShares']))}")
        print(f" {W}[{RESET}•{W}]{RESET} {C('PENDING ORDERS')}  {W}➤{RESET} {Y(str(stats.get('pendingOrders', 0)))}")
        print(f" {W}[{RESET}•{W}]{RESET} {C('COMPLETED')}       {W}➤{RESET} {G(str(stats.get('completedOrders', 0)))}")
        print(f" {W}[{RESET}•{W}]{RESET} {C('TOTAL REVENUE')}   {W}➤{RESET} {M('₱' + str(stats.get('totalRevenue', 0)))}")
        print(LINE)
    else:
        print(f" {R('[ERROR] Failed to load dashboard')}")
        print(LINE)
    
    input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")

def view_all_orders():
    refresh_screen()
    print(f" {G('[!] LOADING ORDERS...')}")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/admin/orders")
    
    if status == 200 and response.get('success'):
        orders = response.get('orders', [])
        
        refresh_screen()
        print(f" {M('[ALL ORDERS]')} {C(f'Total: {len(orders)}')}")
        print(LINE)
        
        if not orders:
            print(f" {C('No orders found.')}")
        else:
            for order in orders:
                status_colors = {
                    'pending': Y,
                    'processing': C,
                    'completed': G,
                    'cancelled': R
                }
                status_color = status_colors.get(order['status'], C)
                status_display = status_color(f"[{order['status'].upper()}]")
                
                print(f" {W}[{order['orderId']}]{RESET} {status_display}")
                print(f"    Customer: {G(order['customerName'])}")
                print(f"    Qty: {M(str(order['quantity']))} | ₱{G(str(order['amount']))}")
                print(f"    Progress: {G(str(order['currentCount']))}/{M(str(order['quantity']))}")
                print(LINE)
    else:
        print(f" {R('[ERROR] Failed to load orders')}")
        print(LINE)
    
    input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")

# ============ SMM BOOSTER SHARING (ALTERNATIVE METHOD) ============

async def get_token_alt(session, cookie):
    """Get EAAG token using content_management method - NO DELAYS"""
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'cookie': cookie
    }
    
    try:
        async with session.get('https://business.facebook.com/content_management', headers=headers, timeout=aiohttp.ClientTimeout(total=15)) as response:
            data = await response.text()
            match = re.search(r'EAAG(\w+)', data)
            if match:
                return 'EAAG' + match.group(1)
    except:
        pass
    return None

async def share_alt(session, cookie, token, post_id):
    """Share using b-graph method - MAXIMUM SPEED NO DELAYS"""
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'accept-encoding': 'gzip, deflate',
        'host': 'b-graph.facebook.com',
        'cookie': cookie
    }
    
    try:
        url = f'https://b-graph.facebook.com/me/feed?link=https://mbasic.facebook.com/{post_id}&published=0&access_token={token}'
        async with session.post(url, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as response:
            data = await response.json()
            if 'id' in data:
                return True, data.get('id', 'N/A')
            else:
                error_msg = data.get('error', {}).get('message', 'Unknown error')
                return False, error_msg
    except Exception as e:
        return False, str(e)

async def share_loop_smm(session, cookie, token, post_id, account_uid, display_mode, target_shares=None):
    """Share loop - MAXIMUM SPEED NO DELAYS"""
    global success_count
    
    while True:
        if target_shares and success_count >= target_shares:
            break
        
        try:
            is_success, result = await share_alt(session, cookie, token, post_id)
            
            if is_success:
                async with lock:
                    success_count += 1
                    current_count = success_count
                
                if display_mode == 'minimal':
                    if target_shares:
                        sys.stdout.write(f"\r {apply_gradient(f'[{current_count}/{target_shares}]', 'green_yellow')} {W}|{RESET} {apply_gradient('SUCCESS', 'green_yellow')} {W}|{RESET} {apply_gradient(account_uid, 'purple_cyan')}          ")
                    else:
                        sys.stdout.write(f"\r {apply_gradient(f'[{current_count}]', 'green_yellow')} {W}|{RESET} {apply_gradient('SUCCESS', 'green_yellow')} {W}|{RESET} {apply_gradient(account_uid, 'purple_cyan')}          ")
                    sys.stdout.flush()
                else:
                    current_time = datetime.datetime.now().strftime("%H:%M:%S")
                    if target_shares:
                        print(f" {G('[SUCCESS]')} {W}|{RESET} {C(current_time)} {W}|{RESET} {M(account_uid)} {W}|{RESET} {G(f'{current_count}/{target_shares}')}")
                    else:
                        print(f" {G('[SUCCESS]')} {W}|{RESET} {C(current_time)} {W}|{RESET} {M(account_uid)} {W}|{RESET} {G(f'Total: {current_count}')}")
            else:
                if display_mode != 'minimal':
                    current_time = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f" {R('[ERROR]')} {W}|{RESET} {C(current_time)} {W}|{RESET} {M(account_uid)} {W}|{RESET} {R(result[:30])}")
        
        except asyncio.CancelledError:
            break
        except KeyboardInterrupt:
            break
        except:
            pass

def extract_post_id(link):
    """Extract post ID from link"""
    link = link.strip()
    
    if link.isdigit():
        return link
    
    link = re.sub(r'^https?://', '', link)
    link = re.sub(r'^(www\.|m\.)', '', link)
    
    patterns = [
        r'facebook\.com/.*?/posts/(\d+)',
        r'facebook\.com/.*?/photos/.*?/(\d+)',
        r'facebook\.com/permalink\.php\?story_fbid=(\d+)',
        r'facebook\.com/story\.php\?story_fbid=(\d+)',
        r'facebook\.com/photo\.php\?fbid=(\d+)',
        r'/(\d+)/?$'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, link)
        if match:
            return match.group(1)
    
    return link

async def getid_online(session, link):
    """Get post ID from online service"""
    try:
        async with session.post('https://id.traodoisub.com/api.php', data={"link": link}, timeout=aiohttp.ClientTimeout(total=10)) as response:
            rq = await response.json()
            if 'id' in rq:
                return rq["id"]
    except:
        pass
    return None

def generate_order_receipt(order_info, shares_completed):
    """Generate receipt - Clean format"""
    is_completed = shares_completed >= order_info.get('quantity', 0)
    status_text = "Completed ✓" if is_completed else "Partial"
    
    clear()
    print(LINE)
    print(f" {W}[{RESET}•{W}]{RESET} {C('ORDER ID')}          {W}➤{RESET} {G(order_info.get('orderId', 'N/A'))}")
    print(f" {W}[{RESET}•{W}]{RESET} {C('CUSTOMER NAME')}     {W}➤{RESET} {G(order_info.get('customerName', 'N/A'))}")
    print(f" {W}[{RESET}•{W}]{RESET} {C('POST LINK')}         {W}➤{RESET} {G(order_info.get('postLink', 'N/A'))}")
    print(f" {W}[{RESET}•{W}]{RESET} {C('REQUEST QUANTITY')}  {W}➤{RESET} {M(str(order_info.get('quantity', 0)))}")
    print(f" {W}[{RESET}•{W}]{RESET} {C('STATUS')}            {W}➤{RESET} {G(status_text) if is_completed else R(status_text)}")
    print(f" {W}[{RESET}•{W}]{RESET} {C('AMOUNT')}            {W}➤{RESET} {Y('₱' + str(order_info.get('amount', 0)))}")
    print(LINE)
    
    if is_completed:
        print(f" {G('Thank you for your avail! Your order has been completed 😊')}")
    else:
        remaining = order_info.get('quantity', 0) - shares_completed
        print(f" {Y(f'Order partially completed. Remaining: {remaining} shares')}")
    
    print(LINE)

async def smm_share_main(post_link, selected_cookies, order_info=None):
    """Main SMM sharing - MAXIMUM SPEED"""
    global success_count
    success_count = 0
    target_shares = order_info.get('quantity') if order_info else None
    
    refresh_screen()
    print(f" {C('[!] EXTRACTING TOKENS...')}")
    nice_loader("EXTRACTING")
    
    valid_accounts = []
    
    async with aiohttp.ClientSession() as session:
        for cookie_data in selected_cookies:
            token = await get_token_alt(session, cookie_data['cookie'])
            if token:
                valid_accounts.append({
                    'cookie': cookie_data['cookie'],
                    'token': token,
                    'uid': cookie_data['uid'],
                    'name': cookie_data['name']
                })
                print(f" {G('✓')} {C(cookie_data['name'])} {W}({C(cookie_data['uid'])}){RESET}")
            else:
                print(f" {R('✗')} {C(cookie_data['name'])} {R('Failed')}")
    
    if not valid_accounts:
        print(f" {R('[ERROR] No valid tokens!')}")
        input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")
        return
    
    post_id = extract_post_id(post_link)
    
    if not post_id.isdigit():
        async with aiohttp.ClientSession() as session:
            post_id = await getid_online(session, post_link)
            if not post_id:
                print(f" {R('[ERROR] Failed to get post ID')}")
                input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")
                return
    
    display_mode = select_progress_display()
    
    refresh_screen()
    print(f" {G('[SMM BOOSTER - MAXIMUM SPEED]')}")
    print(LINE)
    print(f" {W}[{RESET}•{W}]{RESET} {C('POST ID')}       {W}➤{RESET} {G(post_id)}")
    print(f" {W}[{RESET}•{W}]{RESET} {C('ACCOUNTS')}      {W}➤{RESET} {G(str(len(valid_accounts)))}")
    print(f" {W}[{RESET}•{W}]{RESET} {C('SPEED')}         {W}➤{RESET} {M('MAXIMUM (NO DELAYS)')}")
    if target_shares:
        print(f" {W}[{RESET}•{W}]{RESET} {C('TARGET')}        {W}➤{RESET} {M(str(target_shares))}")
    print(LINE)
    print(f" {C('[TIP] Press Ctrl+C to stop')}")
    print(LINE)
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for acc in valid_accounts:
            task = asyncio.create_task(share_loop_smm(
                session,
                acc['cookie'],
                acc['token'],
                post_id,
                acc['uid'],
                display_mode,
                target_shares
            ))
            tasks.append(task)
        
        try:
            if target_shares:
                while success_count < target_shares:
                    await asyncio.sleep(0.1)
                    if all(task.done() for task in tasks):
                        break
                
                for task in tasks:
                    if not task.done():
                        task.cancel()
                await asyncio.gather(*tasks, return_exceptions=True)
            else:
                await asyncio.gather(*tasks, return_exceptions=True)
        except:
            for task in tasks:
                if not task.done():
                    task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)

def select_cookies_for_sharing():
    refresh_screen()
    print(f" {G('[!] LOADING COOKIES...')}")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/user/cookies")
    
    if status != 200 or not response.get('success'):
        print(f" {R('[ERROR] Failed to load cookies')}")
        input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")
        return None
    
    cookies = response.get('cookies', [])
    
    if not cookies:
        print(f" {R('[ERROR] No cookies!')}")
        print(f" {C('[TIP] Add cookies first')}")
        input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")
        return None
    
    refresh_screen()
    print(f" {C('[SELECT COOKIES]')}")
    print(LINE)
    print(f" {W}[{RESET}{BG_G}{W}ALL{RESET}{W}]{RESET} {G('USE ALL COOKIES')}")
    print(LINE)
    
    for i, cookie_data in enumerate(cookies, 1):
        print(f" {W}[{RESET}{BG_C}{W}{i:02d}{RESET}{W}]{RESET} {C(cookie_data['name'])} {W}({C(cookie_data['uid'])}){RESET}")
    
    print(LINE)
    
    selection = input(f" {W}[{W}➤{W}]{RESET} {C('SELECT')} {W}➤{RESET} ").strip().upper()
    
    if not selection:
        return None
    
    selected_cookies = []
    
    if selection == 'ALL':
        selected_cookies = cookies
    else:
        try:
            parts = selection.replace(',', ' ').split()
            for part in parts:
                if part.isdigit():
                    idx = int(part) - 1
                    if 0 <= idx < len(cookies):
                        selected_cookies.append(cookies[idx])
        except:
            return None
    
    if not selected_cookies:
        return None
    
    return selected_cookies

def start_auto_share():
    global success_count
    
    refresh_screen()
    
    print(f" {C('[!] SMM BOOSTER - AUTO SHARE')}")
    print(LINE)
    print(f" {W}[{RESET}{BG_G}{W}1{RESET}{W}]{RESET} {G('BOOSTER ORDER (With Receipt)')}")
    print(f" {W}[{RESET}{BG_C}{W}2{RESET}{W}]{RESET} {C('UNLIMITED SHARING')}")
    print(LINE)
    
    order_choice = input(f" {W}[{W}➤{W}]{RESET} {C('CHOICE')} {W}➤{RESET} ").strip()
    
    order_info = None
    
    if order_choice == '1':
        refresh_screen()
        print(f" {M('[CREATE BOOSTER ORDER]')}")
        print(LINE)
        
        customer_name = input(f" {W}[{W}➤{W}]{RESET} {C('CUSTOMER NAME')} {W}➤{RESET} ").strip()
        if not customer_name:
            return
        
        post_link = input(f" {W}[{W}➤{W}]{RESET} {C('POST LINK')} {W}➤{RESET} ").strip()
        if not post_link:
            return
        
        quantity = input(f" {W}[{W}➤{W}]{RESET} {C('QUANTITY')} {W}➤{RESET} ").strip()
        if not quantity or not quantity.isdigit():
            print(f" {R('[ERROR] Invalid quantity')}")
            input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")
            return
        
        amount = input(f" {W}[{W}➤{W}]{RESET} {C('AMOUNT (₱)')} {W}➤{RESET} ").strip()
        if not amount:
            amount = '0'
        
        refresh_screen()
        nice_loader("CREATING ORDER")
        
        status, response = api_request("POST", "/admin/orders", {
            "customerName": customer_name,
            "postLink": post_link,
            "quantity": int(quantity),
            "amount": float(amount) if amount else 0
        })
        
        if status == 201 and response.get('success'):
            order_info = response.get('order', {})
            order_info['quantity'] = int(quantity)
            order_info['postLink'] = post_link
            
            print(f" {G('[SUCCESS] Order created!')}")
            print(f" {C('Order ID:')} {G(order_info.get('orderId', 'N/A'))}")
            print(LINE)
        else:
            print(f" {R('[ERROR]')} {R(response.get('message', 'Failed') if isinstance(response, dict) else 'Failed')}")
            input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")
            return
    else:
        refresh_screen()
        print(f" {C('[UNLIMITED SHARING]')}")
        print(LINE)
        
        post_link = input(f" {W}[{W}➤{W}]{RESET} {C('POST LINK')} {W}➤{RESET} ").strip()
        if not post_link:
            return
    
    selected_cookies = select_cookies_for_sharing()
    if not selected_cookies:
        return
    
    try:
        asyncio.run(smm_share_main(post_link if not order_info else order_info.get('postLink'), selected_cookies, order_info))
        
        if order_info:
            generate_order_receipt(order_info, success_count)
            
            api_request("PUT", f"/admin/orders/{order_info.get('orderId')}", {
                "status": "completed" if success_count >= order_info.get('quantity', 0) else "processing",
                "currentCount": success_count
            })
        else:
            print()
            print(LINE)
            print(f" {G(f'[COMPLETED] Total Shares: {success_count}')}")
            print(LINE)
        
        if success_count > 0:
            api_request("POST", "/share/complete", {"totalShares": success_count})
        
    except KeyboardInterrupt:
        print()
        print(LINE)
        
        if order_info:
            generate_order_receipt(order_info, success_count)
            api_request("PUT", f"/admin/orders/{order_info.get('orderId')}", {
                "status": "processing",
                "currentCount": success_count
            })
        else:
            print(f" {C(f'[STOPPED] Total Shares: {success_count}')}")
        
        if success_count > 0:
            api_request("POST", "/share/complete", {"totalShares": success_count})
    
    except Exception as e:
        print(f" {R(f'[ERROR] {str(e)}')}")
    
    print(LINE)
    input(f"\n {G('[PRESS ENTER TO CONTINUE]')}")

# ============ MAIN ============

def main():
    global user_token, user_data
    
    check_version()
    
    while True:
        refresh_screen()
        
        try:
            choice = input(f" {W}[{W}➤{W}]{RESET} {C('CHOICE')} {W}➤{RESET} ").strip().upper()
        except KeyboardInterrupt:
            sys.exit()

        refresh_screen()

        if not user_token:
            if choice in ['1', '01', 'A']:
                login_user()
            elif choice in ['2', '02', 'B']:
                register_user()
            elif choice in ['0', '00', 'X']:
                print(f"\n {R('[!] EXIT')}")
                sys.exit()
            else:
                print(f"\n {R('[!] INVALID')}")
                time.sleep(0.5)
        else:
            if choice in ['1', '01', 'A']:
                start_auto_share()
            elif choice in ['2', '02', 'B']:
                manage_cookies()
            elif choice in ['3', '03', 'C']:
                show_user_stats()
            elif choice in ['4', '04', 'D']:
                if user_data and user_data.get('isAdmin'):
                    admin_panel()
                else:
                    update_tool_logic()
            elif choice in ['5', '05', 'E']:
                if user_data and user_data.get('isAdmin'):
                    update_tool_logic()
                else:
                    print(f"\n {R('[!] INVALID')}")
                    time.sleep(0.5)
            elif choice in ['0', '00', 'X']:
                print(f"\n {C('[!] LOGOUT')}")
                user_token = None
                user_data = None
                time.sleep(0.5)
            else:
                print(f"\n {R('[!] INVALID')}")
                time.sleep(0.5)

if __name__ == "__main__":
    main()
