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

# Set socket timeout
socket.setdefaulttimeout(10)

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

# --- COLOR SYSTEM (matching auto-create FB style) ---
white="\x1b[1;97m"
green="\x1b[38;5;49m"
G0="\x1b[38;5;155m"
green1='\x1b[38;5;154m'
G2='\x1b[38;5;47m'
G3='\x1b[38;5;48m'
G4='\x1b[38;5;49m'
G5='\x1b[38;5;50m'
red="\x1b[38;5;160m"
cyan="\x1b[1;96m"
yellow="\x1b[1;93m"
purple="\033[1;35m"
blue="\033[1;94m"
orange="\x1b[38;5;208m"
RESET="\033[0m"
W="\033[1;37m"

# Background colors
BG_R = '\033[41m'
BG_G = '\033[42m'
BG_C = '\033[46m'
BG_M = '\033[45m'
BG_Y = '\033[43m'
BG_B = '\033[44m'

# Style indicators
style=f"{W}[{green}●{W}]"
stylee=f"{W}[{red}!{W}]"

LINE = f'{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'

# --- API CONFIGURATION ---
API_URL = "https://admindatabase-y4iw.onrender.com/api"
CURRENT_VERSION = "1.1.0"
user_token =     if status != 200 or not isinstance(response, dict) or not response.get('success'):
        error_msg = response if isinstance(response, str) else 'Failed to load cookies'
        print(f" {stylee} {red}{error_msg}")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    cookies = response.get('cookies', [])
    
    if not cookies:
        refresh_screen()
        print(f" {style} {cyan}No cookies to delete.")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    refresh_screen()
    print(f" {stylee} {red}DELETE COOKIE")
    print(LINE)
    
    for i, cookie_data in enumerate(cookies, 1):
        status_indicator = f'{red}[RESTRICTED]' if cookie_data.get('status') == 'restricted' else f'{green}[ACTIVE]'
        uid_text = f"UID: {cookie_data['uid']}"
        print(f" {W}[{i}]{RESET} {purple}{cookie_data['name']} {W}({cyan}{uid_text}{W}){RESET} {status_indicator}")
    
    print(LINE)
    
    choice = input(f" {W}[{W}➤{W}]{RESET} {cyan}SELECT COOKIE NUMBER (0 to cancel) {W}➤{RESET} ").strip()
    
    if not choice or choice == '0':
        return
    
    try:
        cookie_index = int(choice) - 1
        if cookie_index < 0 or cookie_index >= len(cookies):
            print(f" {stylee} {red}Invalid cookie number")
            time.sleep(1)
            return
        
        selected_cookie = cookies[cookie_index]
    except:
        print(f" {stylee} {red}Invalid input")
        time.sleep(1)
        return
    
    refresh_screen()
    speak("Deleting cookie")
    nice_loader("DELETING")
    
    status, response = api_request("DELETE", f"/user/cookies/{selected_cookie['id']}")
    
    if status == 200 and isinstance(response, dict) and response.get('success'):
        speak("Cookie deleted successfully")
        print(f" {style} {green}Cookie deleted!")
        if user_data:
            user_data['cookieCount'] = response.get('totalCookies', 0)
    else:
        error_msg = response if isinstance(response, str) else 'Failed to delete cookie'
        print(f" {stylee} {red}{error_msg}")
    
    print(LINE)
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

def delete_all_cookies():
    refresh_screen()
    print(f" {stylee} {red}DELETE ALL COOKIES")
    print(LINE)
    
    confirm = input(f" {W}[{W}➤{W}]{RESET} {red}Delete ALL cookies? This cannot be undone! (YES/NO) {W}➤{RESET} ").strip().upper()
    
    if confirm != 'YES':
        return
    
    refresh_screen()
    speak("Deleting all cookies")
    nice_loader("DELETING")
    
    status, response = api_request("DELETE", "/user/cookies")
    
    if status == 200 and response.get('success'):
        speak("All cookies deleted")
        print(f" {style} {green}{response.get('message')}")
        if user_data:
            user_data['cookieCount'] = 0
    else:
        print(f" {stylee} {red}Failed to delete cookies")
    
    print(LINE)
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

def update_tool_logic():
    print(f" {style} {green}CHECKING FOR UPDATES...")
    speak("Checking for updates")
    nice_loader("CHECKING")
    
    print(f" {style} {green}NEW VERSION FOUND! DOWNLOADING...")
    speak("Downloading update")
    nice_loader("UPDATING")
    
    print(f" {style} {green}UPDATE COMPLETE. RESTARTING...")
    speak("Update complete, restarting")
    time.sleep(1)
    
    os.execv(sys.executable, ['python'] + sys.argv)

# ============ ADMIN PANEL FUNCTIONS ============

def admin_panel():
    while True:
        refresh_screen()
        print(f" {style} {purple}ADMIN PANEL")
        print(LINE)
        print(f" {W}[{W}1{W}]{RESET} {green}VIEW ALL USERS")
        print(f" {W}[{W}2{W}]{RESET} {cyan}ACTIVATE USER (Auto: Full Access)")
        print(f" {W}[{W}3{W}]{RESET} {red}DEACTIVATE USER")
        print(f" {W}[{W}4{W}]{RESET} {red}DELETE USER")
        print(f" {W}[{W}5{W}]{RESET} {red}DELETE ALL USERS")
        print(f" {W}[{W}6{W}]{RESET} {cyan}VIEW ACTIVITY LOGS")
        print(f" {W}[{W}7{W}]{RESET} {green}DASHBOARD STATS")
        print(f" {W}[{W}8{W}]{RESET} {purple}VIEW ALL ORDERS")
        print(f" {W}[{W}0{W}]{RESET} {cyan}BACK")
        print(LINE)
        
        choice = input(f" {W}[{W}➤{W}]{RESET} {cyan}CHOICE {W}➤{RESET} ").strip()
        
        if choice == '1':
            view_all_users()
        elif choice == '2':
            activate_user()
        elif choice == '3':
            deactivate_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            delete_all_users()
        elif choice == '6':
            view_activity_logs()
        elif choice == '7':
            dashboard_stats()
        elif choice == '8':
            view_all_orders()
        elif choice == '0':
            return
        else:
            print(f"\n {stylee} {red}INVALID SELECTION")
            time.sleep(0.8)

def view_all_users():
    refresh_screen()
    print(f" {style} {green}LOADING USERS...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/admin/users")
    
    if status == 200 and response.get('success'):
        users = response.get('users', [])
        
        refresh_screen()
        print(f" {style} {green}[ALL USERS] Total: {len(users)}")
        print(LINE)
        
        for i, user in enumerate(users, 1):
            admin_badge = f" {purple}[ADMIN]" if user.get('isAdmin') else ""
            status_badge = f'{green}[ACTIVE]' if user.get('isActive') else f'{red}[INACTIVE]'
            
            print(f" {W}[{i:02d}]{RESET} {cyan}{user['username'].upper()}{admin_badge} {status_badge}")
            print(f"      Country: {green}{user['country']}")
            print(f"      Shares: {green}{str(user['totalShares'])}")
            print(f"      Total Cookies: {cyan}{str(user.get('cookieCount', 0))}")
            print(LINE)
        
    else:
        print(f" {stylee} {red}Failed to get users")
        print(LINE)
    
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

def activate_user():
    refresh_screen()
    print(f" {style} {green}ACTIVATE USER")
    print(f" {style} {cyan}Note: Activating will automatically grant FULL ACCESS")
    print(LINE)
    
    status, response = api_request("GET", "/admin/users")
    
    if status != 200 or not response.get('success'):
        print(f" {stylee} {red}Failed to load users")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    users = [u for u in response.get('users', []) if not u.get('isAdmin') and not u.get('isActive')]
    
    if not users:
        print(f" {style} {cyan}No inactive users to activate.")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    print(f" {style} {green}SELECT USER TO ACTIVATE")
    print(LINE)
    for i, user in enumerate(users, 1):
        print(f" {W}[{i}]{RESET} {cyan}{user['username'].upper()} - {red}[INACTIVE]")
    print(LINE)
    
    user_choice = input(f" {W}[{W}➤{W}]{RESET} {cyan}SELECT USER NUMBER (0 to cancel) {W}➤{RESET} ").strip()
    
    if not user_choice or user_choice == '0':
        return
    
    try:
        user_index = int(user_choice) - 1
        if user_index < 0 or user_index >= len(users):
            print(f" {stylee} {red}Invalid user number")
            time.sleep(1)
            return
        
        selected_user = users[user_index]
    except:
        print(f" {stylee} {red}Invalid input")
        time.sleep(1)
        return
    
    refresh_screen()
    speak("Activating user")
    nice_loader("ACTIVATING")
    
    status, response = api_request("PUT", f"/admin/users/{selected_user['username']}/activate")
    
    if status == 200 and response.get('success'):
        speak("User activated successfully")
        print(f" {style} {green}User activated successfully!")
        print(f" {style} {green}• Account Status: ACTIVE")
        print(f" {style} {green}• Access Level: FULL ACCESS")
    else:
        print(f" {stylee} {red}{response.get('message', 'Failed to activate user')}")
    
    print(LINE)
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

def deactivate_user():
    refresh_screen()
    print(f" {stylee} {red}DEACTIVATE USER")
    print(f" {style} {cyan}Note: Deactivated users can still manage cookies but cannot share")
    print(LINE)
    
    status, response = api_request("GET", "/admin/users")
    
    if status != 200 or not response.get('success'):
        print(f" {stylee} {red}Failed to load users")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    users = [u for u in response.get('users', []) if not u.get('isAdmin') and u.get('isActive')]
    
    if not users:
        print(f" {style} {cyan}No active users to deactivate.")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    print(f" {style} {green}SELECT USER TO DEACTIVATE")
    print(LINE)
    for i, user in enumerate(users, 1):
        print(f" {W}[{i}]{RESET} {cyan}{user['username'].upper()} - {green}[ACTIVE]")
    print(LINE)
    
    user_choice = input(f" {W}[{W}➤{W}]{RESET} {cyan}SELECT USER NUMBER (0 to cancel) {W}➤{RESET} ").strip()
    
    if not user_choice or user_choice == '0':
        return
    
    try:
        user_index = int(user_choice) - 1
        if user_index < 0 or user_index >= len(users):
            print(f" {stylee} {red}Invalid user number")
            time.sleep(1)
            return
        
        selected_user = users[user_index]
    except:
        print(f" {stylee} {red}Invalid input")
        time.sleep(1)
        return
    
    refresh_screen()
    speak("Deactivating user")
    nice_loader("DEACTIVATING")
    
    status, response = api_request("PUT", f"/admin/users/{selected_user['username']}/deactivate")
    
    if status == 200 and response.get('success'):
        speak("User deactivated")
        print(f" {style} {green}User deactivated successfully!")
        print(f" {style} {yellow}• User can still manage cookies")
        print(f" {style} {red}• User cannot use sharing features")
    else:
        print(f" {stylee} {red}{response.get('message', 'Failed to deactivate user')}")
    
    print(LINE)
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

def delete_user():
    refresh_screen()
    print(f" {stylee} {red}DELETE USER")
    print(LINE)
    
    status, response = api_request("GET", "/admin/users")
    
    if status != 200 or not response.get('success'):
        print(f" {stylee} {red}Failed to load users")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    users = [u for u in response.get('users', []) if not u.get('isAdmin')]
    
    if not users:
        print(f" {style} {cyan}No users to delete.")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    print(f" {style} {green}SELECT USER TO DELETE")
    print(LINE)
    
    for i, user in enumerate(users, 1):
        status_badge = f'{green}[ACTIVE]' if user.get('isActive') else f'{red}[INACTIVE]'
        print(f" {W}[{i:02d}]{RESET} {cyan}{user['username'].upper()} - {status_badge}")
    
    print(f" {W}[00]{RESET} {cyan}CANCEL")
    print(LINE)
    
    choice = input(f" {W}[{W}➤{W}]{RESET} {cyan}SELECT USER {W}➤{RESET} ").strip()
    
    if not choice or choice in ['0', '00']:
        return
    
    try:
        user_index = int(choice) - 1
        if user_index < 0 or user_index >= len(users):
            print(f" {stylee} {red}Invalid selection")
            time.sleep(1)
            return
        
        selected_user = users[user_index]
    except:
        print(f" {stylee} {red}Invalid input")
        time.sleep(1)
        return
    
    refresh_screen()
    print(f" {stylee} {red}CONFIRM DELETION")
    print(LINE)
    print(f" User: {cyan}{selected_user['username'].upper()}")
    print(f" Country: {green}{selected_user['country']}")
    print(LINE)
    
    confirm = input(f" {W}[{W}➤{W}]{RESET} {red}Delete this user? This cannot be undone! (YES/NO) {W}➤{RESET} ").strip().upper()
    
    if confirm != 'YES':
        return
    
    speak("Deleting user")
    nice_loader("DELETING")
    
    status, response = api_request("DELETE", f"/admin/users/{selected_user['username']}")
    
    if status == 200 and response.get('success'):
        speak("User deleted")
        print(f" {style} {green}User {selected_user['username']} deleted successfully!")
    else:
        print(f" {stylee} {red}{response.get('message', 'Failed to delete user')}")
    
    print(LINE)
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

def delete_all_users():
    refresh_screen()
    print(f" {stylee} {red}DELETE ALL USERS")
    print(LINE)
    print(f" {stylee} {red}WARNING: This will delete ALL non-admin users!")
    print(f" {stylee} {red}This action CANNOT be undone!")
    print(LINE)
    
    confirm = input(f" {W}[{W}➤{W}]{RESET} {red}Type CONFIRM to proceed {W}➤{RESET} ").strip()
    
    if confirm != 'CONFIRM':
        print(f" {style} {cyan}[CANCELLED]")
        time.sleep(1)
        return
    
    refresh_screen()
    speak("Deleting all users")
    nice_loader("DELETING ALL USERS")
    
    status, response = api_request("DELETE", "/admin/users")
    
    if status == 200 and response.get('success'):
        deleted_count = response.get('deletedCount', 0)
        speak(f"Deleted {deleted_count} users")
        print(f" {style} {green}Deleted {deleted_count} user(s) successfully!")
    else:
        print(f" {stylee} {red}{response.get('message', 'Failed to delete users')}")
    
    print(LINE)
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

def view_activity_logs():
    refresh_screen()
    print(f" {style} {green}LOADING ACTIVITY LOGS...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/admin/logs?limit=20")
    
    if status == 200 and response.get('success'):
        logs = response.get('logs', [])
        
        refresh_screen()
        print(f" {style} {cyan}[ACTIVITY LOGS] Recent 20")
        print(LINE)
        
        for log in logs:
            action_display = f"{green}{log['action'].upper()}" if log['action'] == 'login' else f"{cyan}{log['action'].upper()}"
            print(f" {W}[{log['timestamp']}]{RESET}")
            print(f" User: {cyan}{log['username'].upper()} | Action: {action_display}")
            if log.get('details'):
                print(f" Details: {green}{log['details']}")
            print(LINE)
    else:
        print(f" {stylee} {red}Failed to load logs")
        print(LINE)
    
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

def dashboard_stats():
    refresh_screen()
    print(f" {style} {green}LOADING DASHBOARD...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/admin/dashboard")
    
    if status == 200 and response.get('success'):
        stats = response.get('stats', {})
        
        refresh_screen()
        print(f" {style} {green}ADMIN DASHBOARD")
        print(LINE)
        
        print(f" {style} {cyan}[USER STATISTICS]")
        print(f" Total Users: {green}{str(stats['totalUsers'])}")
        print(f" Active Users: {green}{str(stats['activeUsers'])}")
        print(f" Inactive Users: {red}{str(stats['inactiveUsers'])}")
        print(LINE)
        
        print(f" {style} {cyan}[ORDER STATISTICS]")
        print(f" Pending Orders: {yellow}{str(stats.get('pendingOrders', 0))}")
        print(f" Completed Orders: {green}{str(stats.get('completedOrders', 0))}")
        print(f" Total Revenue: {purple}₱{str(stats.get('totalRevenue', 0))}")
        print(LINE)
        
        print(f" {style} {cyan}[ACTIVITY STATISTICS]")
        print(f" Total Shares: {green}{str(stats['totalShares'])}")
        print(LINE)
        
        print(f" {style} {cyan}[RECENT USERS]")
        for user in stats.get('recentUsers', []):
            status_badge = f'{green}[ACTIVE]' if user.get('isActive') else f'{red}[INACTIVE]'
            print(f" {cyan}{user['username'].upper()} - {status_badge} - {green}{user['country']}")
        print(LINE)
    else:
        print(f" {stylee} {red}Failed to load dashboard")
        print(LINE)
    
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

def view_all_orders():
    refresh_screen()
    print(f" {style} {green}LOADING ORDERS...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/admin/orders")
    
    if status == 200 and response.get('success'):
        orders = response.get('orders', [])
        
        refresh_screen()
        print(f" {style} {purple}[ALL BOOSTER ORDERS] {cyan}Total: {len(orders)}")
        print(LINE)
        
        if not orders:
            print(f" {style} {cyan}No orders found.")
        else:
            for order in orders:
                status_colors = {
                    'pending': yellow,
                    'processing': cyan,
                    'completed': green,
                    'cancelled': red,
                    'refunded': purple
                }
                status_color = status_colors.get(order['status'], cyan)
                status_display = f"{status_color}[{order['status'].upper()}]"
                
                print(f" {W}[{order['orderId']}]{RESET} {status_display}")
                print(f"    Customer: {green}{order['customerName']}")
                print(f"    Post: {cyan}{order['postLink'][:50] + '...' if len(order['postLink']) > 50 else order['postLink']}")
                print(f"    Quantity: {purple}{str(order['quantity'])} | Amount: {green}₱{str(order['amount'])}")
                print(f"    Progress: {green}{str(order['currentCount'])}/{purple}{str(order['quantity'])} ({yellow}{str(order['remainingCount'])} remaining)")
                print(f"    Created: {cyan}{order['createdAt']}")
                if order.get('notes'):
                    print(f"    Notes: {yellow}{order['notes']}")
                print(LINE)
    else:
        print(f" {stylee} {red}Failed to load orders")
        print(LINE)
    
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

# ============ POST ID EXTRACTION ============

def extract_post_id_from_link(link):
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

async def getid(session, link):
    try:
        async with session.post('https://id.traodoisub.com/api.php', data={"link": link}) as response:
            rq = await response.json()
            if 'success' in rq:
                return rq["id"]
            else:
                print(f" {stylee} {red}Incorrect post link!")
                return async def share_with_eaag(session, cookie, token, post_id):
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'accept-encoding': 'gzip, deflate',
        'host': 'b-graph.facebook.com',
        'cookie': cookie
    }
    
    try:
        url = f'https://b-graph.facebook.com/me/feed?link=https://mbasic.facebook.com/{post_id}&published=0&access_token={token}'
        async with session.post(url, headers=headers, timeout=10) as response:
            json_data = await response.json()
            
            if 'id' in json_data:
                return True, json_data.get('id', 'N/A')
            else:
                error_msg = json_data.get('error', {}).get('message', 'Unknown error')
                return False, error_msg
    except Exception as e:
        return False, str(e)

async def share_loop(session, cookie, token, post_id, account_name, account_uid, cookie_id, display_mode='detailed', target_shares=None):
    global success_count, current_order
    
    while True:
        if target_shares and success_count >= target_shares:
            break
        
        try:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            
            is_success, result = await share_with_eaag(session, cookie, token, post_id)
            
            if is_success:
                async with lock:
                    success_count += 1
                    current_count = success_count
                
                if display_mode == 'minimal':
                    if target_shares:
                        sys.stdout.write(f"\r {W}[{green}{current_count}/{target_shares}{W}]{RESET} {W}[{cyan}UID: {account_uid}{W}]{RESET}                    ")
                    else:
                        sys.stdout.write(f"\r {W}[{green}SUCCESS: {current_count}{W}]{RESET} {W}[{cyan}UID: {account_uid}{W}]{RESET}                    ")
                    sys.stdout.flush()
                else:
                    if target_shares:
                        print(f" {W}[{green}✓{W}]{RESET} {W}[{blue}{current_time}{W}]{RESET} {W}|{RESET} {cyan}UID: {account_uid} {W}|{RESET} {green}{current_count}/{target_shares}")
                    else:
                        print(f" {W}[{green}✓{W}]{RESET} {W}[{blue}{current_time}{W}]{RESET} {W}|{RESET} {cyan}UID: {account_uid} {W}|{RESET} {green}Total: {current_count}")
                
            else:
                if display_mode != 'minimal':
                    error_message = result[:40]
                    print(f" {W}[{red}✗{W}]{RESET} {W}[{blue}{current_time}{W}]{RESET} {W}|{RESET} {cyan}UID: {account_uid} {W}|{RESET} {red}{error_message}")
                break
        
        except asyncio.CancelledError:
            break
        except KeyboardInterrupt:
            break
        except Exception as e:
            error_msg = str(e)
            if "asyncio" not in error_msg.lower() and "event" not in error_msg.lower():
                if display_mode != 'minimal':
                    print(f" {W}[{red}✗{W}]{RESET} {W}[{blue}{datetime.datetime.now().strftime('%H:%M:%S')}{W}]{RESET} {W}|{RESET} {cyan}UID: {account_uid} {W}|{RESET} {red}{error_msg[:40]}")
            break

async def auto_share_main(link_or_id, selected_cookies, order_info=None):
    global success_count, current_order
    success_count = 0
    current_order = order_info
    target_shares = order_info.get('quantity') if order_info else None
    
    start_time = datetime.datetime.now()
    
    refresh_screen()
    print(f" {style} {green}CONVERTING SELECTED ACCOUNTS...")
    nice_loader("CONVERTING")
    
    eaag_tokens = []
    
    for cookie_data in selected_cookies:
        token = cookie_to_eaag(cookie_data['cookie'])
        if token:
            eaag_tokens.append({
                'id': cookie_data['id'],
                'cookie': cookie_data['cookie'],
                'token': token,
                'name': cookie_data['name'],
                'uid': cookie_data['uid'],
                'status': cookie_data.get('status', 'active')
            })
            status_indicator = f'{red}[RESTRICTED]' if cookie_data.get('status') == 'restricted' else f'{green}[ACTIVE]'
            uid_text = f"UID: {cookie_data['uid']}"
            print(f" {W}[{green}✓{W}]{RESET} {cyan}{cookie_data['name']} {W}({cyan}{uid_text}{W}){RESET} {status_indicator}")
        else:
            print(f" {W}[{red}✗{W}]{RESET} {cyan}{cookie_data['name']} {red}Failed to convert account")
    
    if not eaag_tokens:
        print(f" {stylee} {red}No valid accounts converted!")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return start_time
    
    async with aiohttp.ClientSession() as session:
        post_id = extract_post_id_from_link(link_or_id)
        
        if not post_id.isdigit():
            refresh_screen()
            print(f" {style} {green}EXTRACTING POST ID FROM LINK...")
            nice_loader("EXTRACTING")
            
            post_id = await getid(session, link_or_id)
            if not post_id:
                print(f" {stylee} {red}Failed to get post ID")
                input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
                return start_time
    
    display_mode = select_progress_display()
    
    refresh_screen()
    print(f" {style} {green}[SUCCESS] Converted {len(eaag_tokens)} accounts")
    print(LINE)
    print(f" {style} {cyan}Post ID: {green}{post_id}")
    
    if order_info:
        print(LINE)
        print(f" {style} {purple}[BOOSTER ORDER DETAILS]")
        print(f" {style} {cyan}Order ID: {green}{order_info.get('orderId', 'N/A')}")
        print(f" {style} {cyan}Customer: {green}{order_info.get('customerName', 'N/A')}")
        print(f" {style} {cyan}Quantity: {purple}{str(order_info.get('quantity', 0))}")
        print(f" {style} {cyan}Amount: {green}₱{str(order_info.get('amount', 0))}")
        if order_info.get('notes'):
            print(f" {style} {cyan}Notes: {yellow}{order_info.get('notes')}")
    
    print(LINE)
    
    async with aiohttp.ClientSession() as session:
        print(f" {style} {purple}[AUTO SHARE CONFIGURATION]")
        print(LINE)
        print(f" {style} {cyan}Mode: {green}NORMAL SHARING")
        print(f" {style} {cyan}Total Accounts: {green}{str(len(eaag_tokens))}")
        print(f" {style} {cyan}Share Speed: {green}MAXIMUM (ZERO DELAYS)")
        if target_shares:
            print(f" {style} {cyan}Target Shares: {purple}{str(target_shares)}")
        print(LINE)
        print(f" {style} {green}STARTING AUTO SHARE...")
        print(f" {style} {cyan}[TIP] Press Ctrl+C to stop")
        print(LINE)
        
        tasks = []
        for acc in eaag_tokens:
            task = asyncio.create_task(share_loop(
                session,
                acc['cookie'],
                acc['token'],
                post_id,
                acc['name'],
                acc['uid'],
                acc['id'],
                display_mode,
                target_shares
            ))
            tasks.append(task)
        
        print(f" {style} {green}[STARTED] Running {len(tasks)} parallel share threads at MAXIMUM SPEED...")
        print(LINE)
        
        try:
            if target_shares:
                while success_count < target_shares:
                    await asyncio.sleep(0.5)
                    if all(task.done() for task in tasks):
                        break
                
                for task in tasks:
                    if not task.done():
                        task.cancel()
                await asyncio.gather(*tasks, return_exceptions=True)
            else:
                await asyncio.gather(*tasks, return_exceptions=True)
        except Exception as e:
            for task in tasks:
                if not task.done():
                    task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
    
    return start_time

# ============ SMM PANEL BOOST MAIN ============

async def smm_boost_main(selected_cookies, post_link, share_count, order_info=None):
    """SMM Panel Boost with multiple cookies"""
    global success_count
    success_count = 0
    
    start_time = datetime.datetime.now()
    
    async with aiohttp.ClientSession() as session:
        print(f" {style} {green}CONVERTING SELECTED ACCOUNTS...")
        nice_loader("CONVERTING")
        
        valid_tokens = []
        
        for cookie_data in selected_cookies:
            token = await smm_get_token(session, cookie_data['cookie'])
            
            if token:
                valid_tokens.append({
                    'cookie': cookie_data['cookie'],
                    'token': token,
                    'name': cookie_data['name']
                })
                print(f" {W}[{green}✓{W}]{RESET} {cyan}{cookie_data['name']}")
            else:
                print(f" {W}[{red}✗{W}]{RESET} {cyan}{cookie_data['name']} {red}Failed to convert account")
        
        if not valid_tokens:
            print(f" {stylee} {red}No valid accounts converted!")
            print(f" {style} {cyan}Cookies may be invalid or expired.")
            return start_time
        
        print(LINE)
        print(f" {style} {green}[SUCCESS] Converted {len(valid_tokens)} account(s)!")
        print(LINE)
        
        display_mode = select_progress_display()
        
        refresh_screen()
        print(f" {style} {purple}[SMM PANEL — MOST RECOMMENDED]")
        print(LINE)
        print(f" {style} {cyan}Method: {purple}SMM PANEL BOOST")
        print(f" {style} {cyan}Post Link: {green}{post_link[:50] + '...' if len(post_link) > 50 else post_link}")
        print(f" {style} {cyan}Target Shares: {purple}{str(share_count)}")
        print(f" {style} {cyan}Speed: {green}INSTANT (NO DELAYS)")
        print(f" {style} {cyan}Total Cookies: {green}{str(len(valid_tokens))}")
        
        if order_info:
            print(LINE)
            print(f" {style} {purple}[ORDER DETAILS]")
            print(f" {style} {cyan}Order ID: {green}{order_info.get('orderId', 'N/A')}")
            print(f" {style} {cyan}Customer: {green}{order_info.get('customerName', 'N/A')}")
            print(f" {style} {cyan}Amount: {green}₱{str(order_info.get('amount', 0))}")
        
        print(LINE)
        print(f" {style} {green}STARTING SMM PANEL BOOST...")
        print(f" {style} {cyan}[TIP] Press Ctrl+C to stop")
        print(LINE)
        
        tasks = []
        for token_data in valid_tokens:
            task = asyncio.create_task(smm_share(
                session,
                token_data['cookie'],
                token_data['token'],
                post_link,
                token_data['name'],
                display_mode,
                share_count
            ))
            tasks.append(task)
        
        print(f" {style} {green}[STARTED] Running {len(tasks)} parallel share threads...")
        print(LINE)
        
        try:
            while success_count < share_count:
                await asyncio.sleep(0.5)
                if all(task.done() for task in tasks):
                    break
            
            for task in tasks:
                if not task.done():
                    task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
        except Exception as e:
            for task in tasks:
                if not task.done():
                    task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
        
        return start_time

def format_datetime_readable(dt):
    """Format datetime to readable format"""
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    
    month_name = months[dt.month - 1]
    day = dt.day
    year = dt.year
    hours = dt.hour
    minutes = dt.minute
    seconds = dt.second
    
    return f"{month_name} {day}, {year} {hours}Hours {minutes}Minutes {seconds}Sec"

def generate_order_receipt(order_info, shares_completed, start_time, end_time):
    """Generate a receipt for completed order with banner"""
    is_completed = shares_completed >= order_info.get('quantity', 0)
    status_text = "Completed ✓" if is_completed else "Partial"
    
    clear()
    
    banner_art = f"""{green}
    ╦═╗╔═╗╦ ╦╔╦╗╔═╗╔═╗╦  ╔═╗
    ╠╦╝╠═╝║║║ ║ ║ ║║ ║║  ╚═╗
    ╩╚═╩  ╚╩╝ ╩ ╚═╝╚═╝╩═╝╚═╝{RESET}
    """
    print(banner_art)
    print(LINE)
    print(f"{style} {green}DEVELOPER     {W}➤{RESET} {green}KEN DRICK")
    print(f"{style} {green}GITHUB        {W}➤{RESET} {green}RYO GRAHHH")
    print(f"{style} {green}FACEBOOK      {W}➤{RESET} {green}facebook.com/ryoevisu")
    print(f"{style} {green}TOOL NAME     {W}➤{RESET} {red}[ RPWTOOLS ]")
    print(LINE)
    
    print(f" {style} {purple}[ORDER RECEIPT — SMM PANEL BOOST]")
    print(LINE)
    print(f" {style} {cyan}ORDER ID          {W}➤{RESET} {green}{order_info.get('orderId', 'N/A')}")
    print(f" {style} {cyan}CUSTOMER NAME     {W}➤{RESET} {green}{order_info.get('customerName', 'N/A')}")
    print(f" {style} {cyan}POST LINK         {W}➤{RESET} {green}{order_info.get('postLink', 'N/A')[:50]}")
    print(f" {style} {cyan}REQUEST QUANTITY  {W}➤{RESET} {purple}{str(order_info.get('quantity', 0))}")
    print(f" {style} {cyan}STATUS            {W}➤{RESET} {green if is_completed else red}{status_text}")
    print(f" {style} {cyan}AMOUNT            {W}➤{RESET} {yellow}₱{str(order_info.get('amount', 0))}")
    print(LINE)
    
    if is_completed:
        print(f" {style} {green}Thank you for your avail! Your order has been completed 😊")
    else:
        remaining = order_info.get('quantity', 0) - shares_completed
        print(f" {style} {yellow}Order partially completed. Remaining: {remaining} shares")
    
    print(LINE)
    print(f" {style} {cyan}Powered by RPWTOOLS — SMM Panel Boost System")
    print(f" {style} {cyan}GitHub: RYO GRAHHH | Facebook: facebook.com/ryoevisu")
    print(LINE)

def select_cookies_for_sharing():
    refresh_screen()
    print(f" {style} {green}LOADING COOKIES FROM DATABASE...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/user/cookies")
    
    if status != 200 or not response.get('success'):
        print(f" {stylee} {red}Failed to load cookies")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return None
    
    cookies = response.get('cookies', [])
    
    if not cookies:
        print(f" {stylee} {red}No cookies stored in database")
        print(f" {style} {cyan}[TIP] Use option to add cookies first")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return None
    
    refresh_screen()
    print(f" {style} {cyan}[SELECT COOKIES FOR AUTO SHARE]")
    print(LINE)
    print(f" {W}[{RESET}{BG_G}{W}ALL{RESET}{W}]{RESET} {green}USE ALL COOKIES")
    print(LINE)
    
    for i, cookie_data in enumerate(cookies, 1):
        letter = chr(64 + i) if i <= 26 else str(i)
        status_indicator = f'{red}[RESTRICTED]' if cookie_data.get('status') == 'restricted' else f'{green}[ACTIVE]'
        uid_text = f"UID: {cookie_data['uid']}"
        print(f" {W}[{RESET}{BG_C}{W}{i:02d}{RESET}{W}/{RESET}{BG_C}{W}{letter}{RESET}{W}]{RESET} {cyan}{cookie_data['name']} {W}({cyan}{uid_text}{W}){RESET} {status_indicator}")
    
    print(LINE)
    print(f" {style} {cyan}[TIP] Enter numbers separated by commas (e.g., 1,2,3) or type ALL")
    print(LINE)
    
    selection = input(f" {W}[{W}➤{W}]{RESET} {cyan}SELECT {W}➤{RESET} ").strip().upper()
    
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
                elif len(part) == 1 and part.isalpha():
                    idx = ord(part) - 65
                    if 0 <= idx < len(cookies):
                        selected_cookies.append(cookies[idx])
        except:
            print(f" {stylee} {red}Invalid selection")
            time.sleep(1)
            return None
    
    if not selected_cookies:
        print(f" {stylee} {red}No valid cookies selected")
        time.sleep(1)
        return None
    
    refresh_screen()
    print(f" {style} {cyan}[CONFIRM SELECTION]")
    print(LINE)
    print(f" {style} {cyan}Selected {str(len(selected_cookies))} cookie(s):")
    for cookie_data in selected_cookies:
        status_indicator = f'{red}[RESTRICTED]' if cookie_data.get('status') == 'restricted' else f'{green}[ACTIVE]'
        uid_text = f"UID: {cookie_data['uid']}"
        print(f"   • {cyan}{cookie_data['name']} {W}({cyan}{uid_text}{W}){RESET} {status_indicator}")
    print(LINE)
    
    restricted_count = sum(1 for c in selected_cookies if c.get('status') == 'restricted')
    if restricted_count > 0:
        print(f" {stylee} {red}WARNING: {str(restricted_count)} restricted account(s) detected!")
        print(f" {style} {cyan}Restricted accounts may not be able to share posts.")
        print(LINE)
    
    confirm = input(f" {W}[{W}➤{W}]{RESET} {green}Confirm? (Y/N) {W}➤{RESET} ").strip().upper()
    
    if confirm == 'Y':
        return selected_cookies
    else:
        return None

def start_auto_share():
    """Normal unlimited sharing"""
    global success_count, current_order
    
    if not user_data.get('isActive') and not user_data.get('isAdmin'):
        refresh_screen()
        speak_with_sync_animation("Access denied, account not activated", f"{stylee} {red}ACCESS DENIED", red, 0.05)
        print(LINE)
        print(f" {stylee} {red}Your account is not activated.")
        print(f" {style} {cyan}Please contact an administrator to activate your account.")
        print(LINE)
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    refresh_screen()
    speak_with_sync_animation("Auto share, normal accounts", f"{stylee} {green}AUTO SHARE - NORMAL ACCOUNTS (UNLIMITED)", green, 0.05)
    print(LINE)
    print(f" {style} {green}[✓] INFORMATION:")
    print(f" {style} {cyan}• Make sure your post is set to PUBLIC")
    print(f" {style} {cyan}• Shares run at MAXIMUM SPEED (zero delays)")
    print(LINE)
    
    speak("Enter post link or ID")
    display_prompt_with_bg("POST LINK OR ID", BG_C)
    link_or_id = input().strip()
    
    if not link_or_id:
        return
    
    selected_cookies = select_cookies_for_sharing()
    
    if not selected_cookies:
        return
    
    try:
        start_time = asyncio.run(auto_share_main(link_or_id, selected_cookies, None))
        
        end_time = datetime.datetime.now()
        
        refresh_screen()
        speak("Auto share completed successfully")
        print(f" {style} {green}AUTO SHARE COMPLETED")
        stop_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f" {style} {cyan}Stop Time: {stop_time}")
        print(f" {style} {green}Total Successful Shares: {str(success_count)}")
        print(LINE)
        
        if success_count > 0:
            api_request("POST", "/share/complete", {"totalShares": success_count})
            print(f" {style} {green}Shares recorded to your account")
        
    except KeyboardInterrupt:
        end_time = datetime.datetime.now()
        
        refresh_screen()
        speak("Auto share stopped by user")
        print(f" {style} {cyan}AUTO SHARE STOPPED BY USER")
        stop_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f" {style} {cyan}Stop Time: {stop_time}")
        print(f" {style} {green}Total Successful Shares: {str(success_count)}")
        print(LINE)
        
        if success_count > 0:
            api_request("POST", "/share/complete", {"totalShares": success_count})
            print(f" {style} {green}Shares recorded to your account")
    
    except Exception as e:
        refresh_screen()
        print(f" {stylee} {red}An unexpected error occurred:")
        print(f" {stylee} {red}{str(e)}")
    
    print(LINE)
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

def start_smm_panel_boost():
    """SMM Panel Boost with order system"""
    global success_count
    
    if not user_data.get('isActive') and not user_data.get('isAdmin'):
        refresh_screen()
        speak_with_sync_animation("Access denied, account not activated", f"{stylee} {red}ACCESS DENIED", red, 0.05)
        print(LINE)
        print(f" {stylee} {red}Your account is not activated.")
        print(f" {style} {cyan}Please contact an administrator to activate your account.")
        print(LINE)
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    refresh_screen()
    speak_with_sync_animation("SMM Panel, most recommended", f"{stylee} {purple}SMM PANEL — MOST RECOMMENDED", purple, 0.05)
    print(LINE)
    print(f" {style} {green}[✓] INFORMATION:")
    print(f" {style} {cyan}• NO DELAYS - Instant sharing")
    print(f" {style} {cyan}• Creates order for tracking")
    print(f" {style} {cyan}• Supports multiple cookies")
    print(LINE)
    print(f" {stylee} {red}[NOT SUPPORTED POST LINK FORMATS]")
    print(f" {stylee} {red}• https://www.facebook.com/share/p/XXXXX/")
    print(f" {stylee} {red}• https://www.facebook.com/share/XXXXX/")
    print(LINE)
    print(f" {style} {green}[All other Facebook post link formats are supported]")
    print(LINE)
    
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
    
    refresh_screen()
    speak_with_sync_animation("Create SMM boost order", f"{stylee} {purple}CREATE SMM BOOST ORDER", purple, 0.05)
    print(LINE)
    
    speak("Enter customer name")
    display_prompt_with_bg("CUSTOMER NAME", BG_C)
    customer_name = input().strip()
    if not customer_name:
        speak("Customer name is required")
        print(f" {stylee} {red}Customer name is required")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    speak("Enter post link")
    display_prompt_with_bg("POST LINK", BG_C)
    post_link = input().strip()
    if not post_link:
        speak("Post link is required")
        print(f" {stylee} {red}Post link is required")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    if not validate_smm_post_link(post_link):
        refresh_screen()
        speak_with_sync_animation("Link format not supported", f"{stylee} {red}LINK FORMAT NOT SUPPORTED", red, 0.05)
        print(LINE)
        print(f" {stylee} {red}⚠ This type of link format is NOT SUPPORTED!")
        print(LINE)
        print(f" {stylee} {red}[NOT SUPPORTED FORMATS]")
        print(f" {stylee} {red}• https://www.facebook.com/share/p/XXXXX/")
        print(f" {stylee} {red}• https://www.facebook.com/share/XXXXX/")
        print(LINE)
        print(f" {style} {green}[SUPPORTED]")
        print(f" {style} {green}All other Facebook post link formats")
        print(LINE)
        print(f" {style} {yellow}ℹ Contact admin for guide on getting the correct link format.")
        print(LINE)
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    speak("Enter share count")
    display_prompt_with_bg("SHARE COUNT", BG_C)
    share_count = input().strip()
    if not share_count or not share_count.isdigit():
        speak("Valid share count is required")
        print(f" {stylee} {red}Valid share count is required")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    share_count = int(share_count)
    
    speak("Enter amount")
    display_prompt_with_bg("AMOUNT (₱)", BG_C)
    amount = input().strip()
    if not amount:
        amount = '0'
    
    speak("Enter notes, optional")
    display_prompt_with_bg("NOTES (optional)", BG_C)
    notes = input().strip()
    
    selected_cookies = select_cookies_for_sharing()
    
    if not selected_cookies:
        return
    
    refresh_screen()
    speak("Creating order, please wait")
    nice_loader("CREATING ORDER")
    
    max_retries = 5
    for attempt in range(max_retries):
        timestamp_suffix = str(int(time.time()))[-4:] if attempt > 0 else ""
        custom_order_id = f"RPW-{customer_name.upper().replace(' ', '')}{timestamp_suffix}"
        
        status, response = api_request("POST", "/admin/orders", {
            "customOrderId": custom_order_id,
            "customerName": customer_name,
            "postLink": post_link,
            "quantity": share_count,
            "amount": float(amount) if amount else 0,
            "notes": notes
        })
        
        if status == 201 and response.get('success'):
            break
        
        if 'duplicate' in str(response.get('message', '')).lower() or 'already' in str(response.get('message', '')).lower():
            if attempt < max_retries - 1:
                print(f" {style} {yellow}Order ID already exists, generating new ID...")
                time.sleep(0.5)
                continue
            else:
                speak("Failed to create order after retries")
                print(f" {stylee} {red}Failed to create unique order ID after multiple attempts")
                input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
                return
        else:
            speak("Failed to create order")
            print(f" {stylee} {red}{response.get('message', 'Failed to create order') if isinstance(response, dict) else 'Failed to create order'}")
            input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
            return
    
    order_info = response.get('order', {})
    order_info['quantity'] = share_count
    order_info['postLink'] = post_link
    order_info['notes'] = notes
    
    speak("Order created successfully")
    print(f" {style} {green}Order created!")
    print(f" {style} {cyan}Order ID: {green}{order_info.get('orderId', 'N/A')}")
    print(LINE)
    
    try:
        start_time = asyncio.run(smm_boost_main(selected_cookies, post_link, share_count, order_info))
        
        end_time = datetime.datetime.now()
        
        speak("Order completed, generating receipt")
        generate_order_receipt(order_info, success_count, start_time, end_time)
        
        status, response = api_request("PUT", f"/admin/orders/{order_info.get('orderId')}", {
            "status": "completed" if success_count >= share_count else "processing",
            "currentCount": success_count
        })
        
        if status == 200:
            print(f" {style} {green}[✓] Order status updated in database")
        
        if success_count > 0:
            api_request("POST", "/share/complete", {"totalShares": success_count})
            print(f" {style} {green}Shares recorded to your account")
        
    except KeyboardInterrupt:
        end_time = datetime.datetime.now()
        
        generate_order_receipt(order_info, success_count, start_time, end_time)
        
        status, response = api_request("PUT", f"/admin/orders/{order_info.get('orderId')}", {
            "status": "processing",
            "currentCount": success_count
        })
        
        if status == 200:
            print(f" {style} {yellow}Order marked as PROCESSING (partial completion)")
        
        if success_count > 0:
            api_request("POST", "/share/complete", {"totalShares": success_count})
            print(f" {style} {green}Shares recorded to your account")
    
    except Exception as e:
        refresh_screen()
        print(f" {stylee} {red}An unexpected error occurred:")
        print(f" {stylee} {red}{str(e)}")
    
    print(LINE)
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

# ============ MAIN FUNCTION ============

def main():
    global user_token, user_data
    
    check_version()
    
    clear()
    speak_with_sync_animation("Welcome to RPW Tools by Kendrick", f"{stylee} {green}WELCOME TO RPWTOOLS BY KENDRICK", green, 0.06)
    time.sleep(1)
    
    while True:
        refresh_screen()
        
        prompt = f" {W}[{W}➤{W}]{RESET} {cyan}CHOICE {W}➤{RESET} "
        try:
            choice = input(prompt).upper()
        except KeyboardInterrupt:
            sys.exit()

        refresh_screen()

        if not user_token:
            if choice in ['1', '01', 'A']:
                login_user()
            elif choice in ['2', '02', 'B']:
                register_user()
            elif choice in ['0', '00', 'X']:
                print(f"\n {stylee} {red}EXITING TOOL...")
                sys.exit()
            else:
                print(f"\n {stylee} {red}INVALID SELECTION")
                time.sleep(0.8)
        
        elif user_data and user_data.get('isAdmin'):
            if choice in ['1', '01', 'A']:
                start_auto_share()
            elif choice in ['2', '02', 'B']:
                start_smm_panel_boost()
            elif choice in ['3', '03', 'C']:
                manage_cookies()
            elif choice in ['4', '04', 'D']:
                show_user_stats()
            elif choice in ['5', '05', 'E']:
                admin_panel()
            elif choice in ['6', '06', 'F']:
                update_tool_logic()
            elif choice in ['0', '00', 'X']:
                print(f"\n {style} {cyan}LOGGING OUT...")
                user_token = None
                user_data = None
                time.sleep(1)
            else:
                print(f"\n {stylee} {red}INVALID SELECTION")
                time.sleep(0.8)
        
        elif user_data and user_data.get('isActive'):
            if choice in ['1', '01', 'A']:
                start_auto_share()
            elif choice in ['2', '02', 'B']:
                start_smm_panel_boost()
            elif choice in ['3', '03', 'C']:
                manage_cookies()
            elif choice in ['4', '04', 'D']:
                show_user_stats()
            elif choice in ['5', '05', 'E']:
                update_tool_logic()
            elif choice in ['0', '00', 'X']:
                print(f"\n {style} {cyan}LOGGING OUT...")
                user_token = None
                user_data = None
                time.sleep(1)
            else:
                print(f"\n {stylee} {red}INVALID SELECTION")
                time.sleep(0.8)
        
        else:
            if choice in ['1', '01', 'A']:
                manage_cookies()
            elif choice in ['2', '02', 'B']:
                show_user_stats()
            elif choice in ['0', '00', 'X']:
                print(f"\n {style} {cyan}LOGGING OUT...")
                user_token = None
                user_data = None
                time.sleep(1)
            else:
                print(f"\n {stylee} {red}INVALID SELECTION")
                time.sleep(0.8)

if __name__ == "__main__":
    main()
            
    except Exception as e:
        print(f" {stylee} {red}Failed to get post ID: {e}")
        return None

# ============ NORMAL SHARING (BUSINESS_LOCATIONS METHOD) ============

def cookie_to_eaag(cookie):
    """Normal method using business_locations endpoint"""
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
        'referer': 'https://www.facebook.com/',
        'host': 'business.facebook.com',
        'origin': 'https://business.facebook.com',
        'upgrade-insecure-requests': '1',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'content-type': 'text/html; charset=utf-8',
        'cookie': cookie
    }
    
    try:
        response = requests.get('https://business.facebook.com/business_locations', headers=headers, timeout=15)
        eaag_match = re.search(r'(EAAG\w+)', response.text)
        if eaag_match:
            return eaag_match.group(1)
    except:
        pass
    return None

# ============ SMM PANEL BOOST (CONTENT_MANAGEMENT METHOD) ============

async def smm_get_token(session, cookie):
    """SMM Panel method using content_management endpoint"""
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
        async with session.get('https://business.facebook.com/content_management', headers=headers, timeout=15) as response:
            data = await response.text()
            match = re.search(r'EAAG(.*?)"', data)
            if match:
                return 'EAAG' + match.group(1)
    except Exception as e:
        print(f" {stylee} {red}Token extraction failed: {e}")
    return None

async def smm_share(session, cookie, token, post_link, account_name, display_mode='detailed', target_shares=None):
    """SMM Panel share method - NO DELAYS"""
    global success_count
    
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'accept-encoding': 'gzip, deflate',
        'host': 'b-graph.facebook.com',
        'cookie': cookie
    }
    
    while True:
        if target_shares and success_count >= target_shares:
            break
        
        try:
            url = f'https://b-graph.facebook.com/me/feed?link={post_link}&published=0&access_token={token}'
            
            async with session.post(url, headers=headers, timeout=10) as response:
                data = await response.json()
                
                if 'id' in data:
                    async with lock:
                        success_count += 1
                        current_count = success_count
                    
                    now = datetime.datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    
                    if display_mode == 'minimal':
                        if target_shares:
                            sys.stdout.write(f"\r {W}[{green}{current_count}/{target_shares}{W}]{RESET} {W}[{cyan}{account_name}{W}]{RESET}                    ")
                        else:
                            sys.stdout.write(f"\r {W}[{green}SUCCESS: {current_count}{W}]{RESET} {W}[{cyan}{account_name}{W}]{RESET}                    ")
                        sys.stdout.flush()
                    else:
                        if target_shares:
                            print(f" {W}[{green}✓{W}]{RESET} {W}[{blue}{current_time}{W}]{RESET} {W}|{RESET} {cyan}{account_name} {W}|{RESET} {green}{current_count}/{target_shares}")
                        else:
                            print(f" {W}[{green}✓{W}]{RESET} {W}[{blue}{current_time}{W}]{RESET} {W}|{RESET} {cyan}{account_name} {W}|{RESET} {green}Total: {current_count}")
                else:
                    error_msg = data.get('error', {}).get('message', 'Unknown error')
                    if display_mode != 'minimal':
                        print(f" {W}[{red}✗{W}]{RESET} {W}[{blue}{current_time}{W}]{RESET} {W}|{RESET} {cyan}{account_name} {W}|{RESET} {red}{error_msg[:50]}")
                    break
        
        except asyncio.CancelledError:
            break
        except Exception as e:
            if display_mode != 'minimal':
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                print(f" {W}[{red}✗{W}]{RESET} {W}[{blue}{current_time}{W}]{RESET} {W}|{RESET} {cyan}{account_name} {W}|{RESET} {red}{str(e)[:50]}")
            break

async def share_with_eaag(session, cookie, token, post_id):
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36
user_data = None

# --- ESPEAK CONFIGURATION ---
def speak(text):
    """Text-to-speech using espeak (non-blocking)"""
    try:
        threading.Thread(target=lambda: os.system(f'espeak -a 200 -s 150 "{text}" > /dev/null 2>&1'), daemon=True).start()
    except:
        pass

def animate_text(text, color=green, delay=0.03):
    """Animate text with fade-in effect letter by letter"""
    for i, char in enumerate(text):
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def speak_with_sync_animation(speech_text, display_text, color=green, delay=0.05):
    """Speak text and animate display text synchronized"""
    speak(speech_text)
    animate_text(display_text, color, delay)

def display_prompt_with_bg(display_text, bg_color=BG_C):
    """Display prompt with background color like menu items"""
    print(f" {W}[{W}➤{W}]{RESET} {bg_color}{W} {display_text} {RESET} {W}➤{RESET} ", end='', flush=True)

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
                print(f" {stylee} {red}VERSION MISMATCH")
                print(LINE)
                print(f" {style} {green}Your tool version{W}: {red}{CURRENT_VERSION}")
                print(f" {style} {green}Server version{W}: {green}{server_version}")
                print(LINE)
                print(f" {stylee} {red}Your tool is outdated!")
                print(f" {style} {green}Please update to the latest version to continue using this tool.")
                print(LINE)
                input(f"\n {stylee} {red}PRESS ENTER TO EXIT")
                sys.exit(1)
    except:
        pass

def banner_header():
    banner_art = f"""{green}
    ╦═╗╔═╗╦ ╦╔╦╗╔═╗╔═╗╦  ╔═╗
    ╠╦╝╠═╝║║║ ║ ║ ║║ ║║  ╚═╗
    ╩╚═╩  ╚╩╝ ╩ ╚═╝╚═╝╩═╝╚═╝{RESET}
    """
    print(banner_art)
    print(LINE)
    print(f"{style} {green}DEVELOPER     {W}➤{RESET} {green}KEN DRICK")
    print(f"{style} {green}GITHUB        {W}➤{RESET} {green}RYO GRAHHH")
    print(f"{style} {green}VERSION       {W}➤{RESET} {green}{CURRENT_VERSION}")
    print(f"{style} {green}FACEBOOK      {W}➤{RESET} {green}facebook.com/ryoevisu")
    print(f"{style} {green}TOOL NAME     {W}➤{RESET} {red}[ RPWTOOLS ]")
    
    if user_data:
        print(LINE)
        print(f"{style} {green}USERNAME       {W}➤{RESET} {green}{user_data['username'].upper()}")
        print(f"{style} {green}FACEBOOK       {W}➤{RESET} {green}{user_data.get('facebook', 'N/A')}")
        print(f"{style} {green}COUNTRY        {W}➤{RESET} {green}{user_data.get('country', 'N/A').upper()}")
        
        is_active = user_data.get('isActive', False)
        
        if is_active:
            status_display = f'{green}[ACTIVE - FULL ACCESS]'
        else:
            status_display = f'{red}[INACTIVE - LIMITED]'
        
        print(f"{style} {green}STATUS         {W}➤{RESET} {status_display}")
        
        cookie_count = user_data.get('cookieCount', 0)
        print(f"{style} {green}TOTAL COOKIES  {W}➤{RESET} {green}{str(cookie_count)}")
    
    print(LINE)

def show_menu():
    if not user_token:
        print(f" {W}[{RESET}{BG_G}{W}01{RESET}{BG_G}{W}/{RESET}{BG_G}{W}A{RESET}{W}]{RESET} {green}LOGIN")
        print(f" {W}[{RESET}{BG_C}{W}02{RESET}{BG_C}{W}/{RESET}{BG_C}{W}B{RESET}{W}]{RESET} {cyan}REGISTER")
        print(f" {W}[{RESET}{BG_R}{W}00{RESET}{BG_R}{W}/{RESET}{BG_R}{W}X{RESET}{W}]{RESET} {red}EXIT")
    elif user_data and user_data.get('isAdmin'):
        print(f" {W}[{RESET}{BG_G}{W}01{RESET}{BG_G}{W}/{RESET}{BG_G}{W}A{RESET}{W}]{RESET} {green}AUTO SHARE              — NORM ACCOUNTS")
        print(f" {W}[{RESET}{BG_M}{W}02{RESET}{BG_M}{W}/{RESET}{BG_M}{W}B{RESET}{W}]{RESET} {purple}SMM PANEL               — MOST RECOMMENDED")
        print(f" {W}[{RESET}{BG_C}{W}03{RESET}{BG_C}{W}/{RESET}{BG_C}{W}C{RESET}{W}]{RESET} {cyan}MANAGE COOKIES          — DATABASE")
        print(f" {W}[{RESET}{BG_B}{W}04{RESET}{BG_B}{W}/{RESET}{BG_B}{W}D{RESET}{W}]{RESET} {blue}MY STATS                — STATISTICS")
        print(f" {W}[{RESET}{BG_Y}{W}05{RESET}{BG_Y}{W}/{RESET}{BG_Y}{W}E{RESET}{W}]{RESET} {yellow}ADMIN PANEL             — MANAGEMENT")
        print(f" {W}[{RESET}{BG_G}{W}06{RESET}{BG_G}{W}/{RESET}{BG_G}{W}F{RESET}{W}]{RESET} {green}UPDATE TOOL             — LATEST VERSION")
        print(f" {W}[{RESET}{BG_R}{W}00{RESET}{BG_R}{W}/{RESET}{BG_R}{W}X{RESET}{W}]{RESET} {red}LOGOUT")
    elif user_data and user_data.get('isActive'):
        print(f" {W}[{RESET}{BG_G}{W}01{RESET}{BG_G}{W}/{RESET}{BG_G}{W}A{RESET}{W}]{RESET} {green}AUTO SHARE              — NORM ACCOUNTS")
        print(f" {W}[{RESET}{BG_M}{W}02{RESET}{BG_M}{W}/{RESET}{BG_M}{W}B{RESET}{W}]{RESET} {purple}SMM PANEL               — MOST RECOMMENDED")
        print(f" {W}[{RESET}{BG_C}{W}03{RESET}{BG_C}{W}/{RESET}{BG_C}{W}C{RESET}{W}]{RESET} {cyan}MANAGE COOKIES          — DATABASE")
        print(f" {W}[{RESET}{BG_B}{W}04{RESET}{BG_B}{W}/{RESET}{BG_B}{W}D{RESET}{W}]{RESET} {blue}MY STATS                — STATISTICS")
        print(f" {W}[{RESET}{BG_G}{W}05{RESET}{BG_G}{W}/{RESET}{BG_G}{W}E{RESET}{W}]{RESET} {green}UPDATE TOOL             — LATEST VERSION")
        print(f" {W}[{RESET}{BG_R}{W}00{RESET}{BG_R}{W}/{RESET}{BG_R}{W}X{RESET}{W}]{RESET} {red}LOGOUT")
    else:
        print(f" {W}[{RESET}{BG_C}{W}01{RESET}{BG_C}{W}/{RESET}{BG_C}{W}A{RESET}{W}]{RESET} {cyan}MANAGE COOKIES          — DATABASE")
        print(f" {W}[{RESET}{BG_B}{W}02{RESET}{BG_B}{W}/{RESET}{BG_B}{W}B{RESET}{W}]{RESET} {blue}MY STATS                — STATISTICS")
        print(f" {W}[{RESET}{BG_R}{W}00{RESET}{BG_R}{W}/{RESET}{BG_R}{W}X{RESET}{W}]{RESET} {red}LOGOUT")
    print(LINE)

def refresh_screen():
    clear()
    banner_header()
    show_menu()

def nice_loader(text="PROCESSING"):
    """Sweeti-style animated loader"""
    sys.stdout.write("\033[?25l")
    animation = [f"[{red}■{W}□□□□□□□□□]",f"[{green}■■{W}□□□□□□□□]", f"[{yellow}■■■{W}□□□□□□□]", f"[{blue}■■■■{W}□□□□□□]", f"[{purple}■■■■■{W}□□□□□]", f"[{cyan}■■■■■■{W}□□□□]", f"[{green1}■■■■■■■{W}□□□]", f"[{G2}■■■■■■■■{W}□□]", f"[{G3}■■■■■■■■■{W}□]", f"[{G4}■■■■■■■■■■{W}]"]
    
    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write(f"\r {style} {green}{text} {W}➤{RESET} " + animation[i % len(animation)])
        sys.stdout.flush()
    
    sys.stdout.write(f"\r{' ' * 80}\r")
    sys.stdout.flush()
    sys.stdout.write("\033[?25h")

def select_progress_display():
    refresh_screen()
    print(f" {style} {green}SHARING PROGRESS DISPLAY")
    print(LINE)
    print(f" {style} {green}Choose how you want to see sharing progress:")
    print(LINE)
    print(f" {W}[{RESET}{BG_G}{W}1{RESET}{W}]{RESET} {green}SUCCESS COUNTER (1/100)")
    print(f"     {cyan}• Best for smaller screens (mobile)")
    print(LINE)
    print(f" {W}[{RESET}{BG_C}{W}2{RESET}{W}]{RESET} {cyan}DETAILED LOGS")
    print(f"     {green}• Best for larger screens (desktop)")
    print(LINE)
    
    while True:
        choice = input(f" {W}[{W}➤{W}]{RESET} {cyan}CHOICE (1 or 2) {W}➤{RESET} ").strip()
        if choice == '1':
            return 'minimal'
        elif choice == '2':
            return 'detailed'
        else:
            print(f" {stylee} {red}Invalid choice. Please enter 1 or 2")
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

def login_user():
    global user_token, user_data
    
    refresh_screen()
    speak_with_sync_animation("Login to RPW Tools", f"{stylee} {green}LOGIN TO RPWTOOLS", green, 0.05)
    print(LINE)
    
    speak("Enter username")
    display_prompt_with_bg("USERNAME", BG_C)
    username = input().strip()
    if not username:
        return
    
    speak("Enter password")
    display_prompt_with_bg("PASSWORD", BG_C)
    password = input().strip()
    if not password:
        return
    
    refresh_screen()
    speak("Logging in, please wait")
    nice_loader("LOGGING IN")
    
    status, response = api_request("POST", "/auth/login", {
        "username": username,
        "password": password
    }, use_token=False)
    
    if status == 200 and response.get('success'):
        user_token = response.get('token')
        user_data = response.get('user')
        
        speak("Login successful, Welcome back")
        print(f" {style} {green}Login successful!")
        print(LINE)
        print(f" {style} {green}Welcome back, {purple}{user_data['username'].upper()}")
        
        is_active = user_data.get('isActive', False)
        
        if is_active:
            status_text = 'ACTIVE - FULL ACCESS'
            print(f" {style} {green}Status: {green}{status_text}")
        else:
            status_text = 'INACTIVE - LIMITED ACCESS'
            print(f" {style} {green}Status: {red}{status_text}")
            print(f" {stylee} {yellow}You can only manage cookies. Contact admin to activate.")
        
        print(f" {style} {green}Total Cookies: {cyan}{str(user_data.get('cookieCount', 0))}")
        
        if user_data.get('isAdmin'):
            print(f" {style} {purple}[ADMIN ACCESS GRANTED]")
        
        print(LINE)
    elif status == 403:
        if response.get('allowLimited'):
            user_token = response.get('token')
            user_data = response.get('user')
            print(f" {stylee} {yellow}[LIMITED ACCESS]")
            print(LINE)
            print(f" {stylee} {yellow}{response.get('message', 'Account not activated')}")
            print(f" {style} {cyan}You can still manage cookies.")
            print(LINE)
        else:
            print(f" {stylee} {red}[ACCESS DENIED]")
            print(LINE)
            print(f" {stylee} {red}{response.get('message', 'Account not activated')}")
            print(LINE)
    else:
        print(f" {stylee} {red}{response if isinstance(response, str) else response.get('message', 'Login failed')}")
        print(LINE)
    
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

def register_user():
    global user_token, user_data
    
    refresh_screen()
    speak_with_sync_animation("Register new account", f"{stylee} {green}REGISTER NEW ACCOUNT", green, 0.05)
    print(LINE)
    
    speak("Enter username")
    display_prompt_with_bg("USERNAME", BG_C)
    username = input().strip()
    if not username:
        return
    
    speak("Enter password")
    display_prompt_with_bg("PASSWORD", BG_C)
    password = input().strip()
    if not password:
        return
    
    speak("Enter facebook link")
    display_prompt_with_bg("FACEBOOK LINK", BG_C)
    facebook = input().strip()
    if not facebook:
        return
    
    facebook = normalize_facebook_url(facebook)
    
    refresh_screen()
    print(f" {style} {green}NORMALIZED FACEBOOK URL: {cyan}{facebook}")
    print(LINE)
    
    print(f" {style} {green}DETECTING YOUR COUNTRY...")
    speak("Detecting your country")
    nice_loader("DETECTING")
    
    country = get_country_from_ip()
    
    refresh_screen()
    print(f" {style} {green}DETECTED COUNTRY: {cyan}{country}")
    print(LINE)
    confirm = input(f" {W}[{W}➤{W}]{RESET} {green}Is this correct? (Y/N) {W}➤{RESET} ").strip().upper()
    
    if confirm == 'N':
        country = input(f" {W}[{W}➤{W}]{RESET} {cyan}ENTER YOUR COUNTRY {W}➤{RESET} ").strip()
    
    refresh_screen()
    speak("Registering your account")
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
        
        speak("Registration successful")
        print(f" {style} {green}Registration successful!")
        print(LINE)
        print(f" {style} {purple}{user_data['username'].upper()}")
        print(f" {style} {cyan}Your account has been created!")
        print(LINE)
        print(f" {stylee} {red}IMPORTANT NOTICE:")
        print(f" {style} {cyan}Your account is currently INACTIVE.")
        print(f" {style} {cyan}Please contact an administrator to activate your account.")
        print(f" {style} {cyan}You can still manage cookies while waiting for activation.")
        print(LINE)
    else:
        print(f" {stylee} {red}{response if isinstance(response, str) else response.get('message', 'Registration failed')}")
        print(LINE)
    
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

def show_user_stats():
    refresh_screen()
    print(f" {style} {green}LOADING STATS...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/user/stats")
    
    if status == 200 and response.get('success'):
        stats = response.get('stats')
        
        refresh_screen()
        print(f" {style} {green}USER STATISTICS")
        print(LINE)
        print(f" {style} {cyan}Username: {W}{stats['username'].upper()}{RESET}")
        
        is_active = stats.get('isActive', False)
        status_display = f'{green}ACTIVE - FULL ACCESS' if is_active else f'{red}INACTIVE - LIMITED'
        print(f" {style} {cyan}Account Status: {status_display}")
        
        print(LINE)
        print(f" {style} {cyan}[STATISTICS]")
        print(f" {style} {green}Total Shares: {purple}{str(stats['totalShares'])}")
        print(f" {style} {green}Total Cookies: {cyan}{str(stats.get('cookieCount', 0))}")
        print(LINE)
    else:
        print(f" {stylee} {red}Failed to get stats")
        print(LINE)
    
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

def manage_cookies():
    while True:
        refresh_screen()
        print(f" {style} {green}MANAGE COOKIES")
        print(LINE)
        print(f" {W}[{W}1{W}]{RESET} {green}VIEW ALL COOKIES")
        print(f" {W}[{W}2{W}]{RESET} {green}ADD COOKIE")
        print(f" {W}[{W}3{W}]{RESET} {red}DELETE COOKIE")
        print(f" {W}[{W}4{W}]{RESET} {red}DELETE ALL COOKIES")
        print(f" {W}[{W}0{W}]{RESET} {cyan}BACK")
        print(LINE)
        
        choice = input(f" {W}[{W}➤{W}]{RESET} {cyan}CHOICE {W}➤{RESET} ").strip()
        
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
            print(f"\n {stylee} {red}INVALID SELECTION")
            time.sleep(0.8)

def view_cookies():
    refresh_screen()
    print(f" {style} {green}LOADING COOKIES...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/user/cookies")
    
    if status == 200 and response.get('success'):
        cookies = response.get('cookies', [])
        
        refresh_screen()
        print(f" {style} {green}[COOKIES] Total: {len(cookies)}")
        print(LINE)
        
        if not cookies:
            print(f" {style} {cyan}No cookies stored yet.")
        else:
            for i, cookie_data in enumerate(cookies, 1):
                status_display = f'{green}[ACTIVE]' if cookie_data['status'] == 'active' else f'{red}[RESTRICTED]'
                
                uid_text = f"UID: {cookie_data['uid']}"
                print(f" {W}[{i:02d}]{RESET} {purple}{cookie_data['name']} {W}({cyan}{uid_text}{W}){RESET}")
                cookie_preview = cookie_data['cookie'][:50] + "..." if len(cookie_data['cookie']) > 50 else cookie_data['cookie']
                print(f"      Cookie: {cyan}{cookie_preview}")
                print(f"      Added: {green}{cookie_data['addedAt']}")
                print(f"      Status: {status_display}")
                
                if cookie_data['status'] == 'restricted':
                    print(f"      {stylee} {red}WARNING: This account is restricted!")
                
                print(LINE)
        
    else:
        print(f" {stylee} {red}Failed to load cookies")
        print(LINE)
    
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

def add_cookie():
    refresh_screen()
    speak_with_sync_animation("Add cookie", f"{stylee} {green}ADD COOKIE", green, 0.05)
    print(LINE)
    
    speak("Enter cookie")
    display_prompt_with_bg("COOKIE", BG_C)
    cookie = input().strip()
    if not cookie:
        return
    
    refresh_screen()
    print(f" {style} {green}VALIDATING COOKIE...")
    print(f" {style} {cyan}This may take 10-15 seconds")
    print(LINE)
    speak("Validating cookie, please wait")
    nice_loader("VALIDATING")
    
    status, response = api_request("POST", "/user/cookies", {"cookie": cookie})
    
    if status == 200 and isinstance(response, dict) and response.get('success'):
        speak("Cookie added successfully")
        print(f" {style} {green}{response.get('message')}")
        print(LINE)
        print(f" {style} {cyan}Name: {purple}{response.get('name', 'Unknown')}")
        print(f" {style} {cyan}UID: {cyan}{response.get('uid', 'Unknown')}")
        status_display = f"{green}{response.get('status', 'unknown').upper()}" if response.get('status') == 'active' else f"{red}{response.get('status', 'unknown').upper()}"
        print(f" {style} {cyan}Status: {status_display}")
        
        if response.get('restricted'):
            print(LINE)
            print(f" {stylee} {red}WARNING: This account is RESTRICTED!")
            print(f" {style} {cyan}Restricted accounts may not be able to share posts.")
        
        if user_data:
            user_data['cookieCount'] = response.get('totalCookies', 0)
        
        print(LINE)
    else:
        error_msg = response if isinstance(response, str) else response.get('message', 'Failed to add cookie') if isinstance(response, dict) else 'Failed to add cookie'
        print(f" {stylee} {red}{error_msg}")
        print(LINE)
    
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")

def delete_cookie():
    refresh_screen()
    print(f" {style} {green}LOADING COOKIES...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/user/cookies")
    
    if status != 200 or not isinstance(response, dict) or not response.get('success'):
        error_msg = response if isinstance(response, str) else 'Failed to load cookies'
        print(f" {stylee} {red}{error_msg}")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    cookies = response.get('cookies', [])
    
    if not cookies:
        refresh_screen()
        print(f" {style} {cyan}No cookies to delete.")
        input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
        return
    
    refresh_screen()
    print(f" {stylee} {red}DELETE COOKIE")
    print(LINE)
    
    for i, cookie_data in enumerate(cookies, 1):
        status_indicator = f'{red}[RESTRICTED]' if cookie_data.get('status') == 'restricted' else f'{green}[ACTIVE]'
        uid_text = f"UID: {cookie_data['uid']}"
        print(f" {W}[{i}]{RESET} {purple}{cookie_data['name']} {W}({cyan}{uid_text}{W}){RESET} {status_indicator}")
    
    print(LINE)
    
    choice = input(f" {W}[{W}➤{W}]{RESET} {cyan}SELECT COOKIE NUMBER (0 to cancel) {W}➤{RESET} ").strip()
    
    if not choice or choice == '0':
        return
    
    try:
        cookie_index = int(choice) - 1
        if cookie_index < 0 or cookie_index >= len(cookies):
            print(f" {stylee} {red}Invalid cookie number")
            time.sleep(1)
            return
        
        selected_cookie = cookies[cookie_index]
    except:
        print(f" {stylee} {red}Invalid input")
        time.sleep(1)
        return
    
    refresh_screen()
    speak("Deleting cookie")
    nice_loader("DELETING")
    
    status, response = api_request("DELETE", f"/user/cookies/{selected_cookie['id']}")
    
    if status == 200 and isinstance(response, dict) and response.get('success'):
        speak("Cookie deleted successfully")
        print(f" {style} {green}Cookie deleted!")
        if user_data:
            user_data['cookieCount'] = response.get('totalCookies', 0)
    else:
        error_msg = response if isinstance(response, str) else 'Failed to delete cookie'
        print(f" {stylee} {red}{error_msg}")
    
    print(LINE)
    input(f"\n {style} {green}PRESS ENTER TO CONTINUE")
