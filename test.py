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

# Socket timeout
socket.setdefaulttimeout(10)

# --- COLOR CODES (FROM AUTO CREATE) ---
white="\x1b[1;97m"
green="\x1b[38;5;49m"
G0="\x1b[38;5;155m"
green1='\x1b[38;5;154m'
red="\x1b[38;5;160m"
yellow="\x1b[38;5;208m"
cyan="\033[1;36m"
purple="\033[1;35m"
blue="\033[38;5;6m"
gas="\033[1;32m"
RESET="\033[0m"

# Style markers
style=f"\033[1;37m[\033[1;32m●\033[1;37m]"
stylee=f"\033[1;37m[\033[1;31m!\033[1;37m]"

# --- API CONFIGURATION ---
API_URL = "https://admindatabase-y4iw.onrender.com/api"
CURRENT_VERSION = "1.1.0"
user_token =     try:
        async with session.get('https://business.facebook.com/content_management', headers=headers, timeout=15) as response:
            data = await response.text()
            match = re.search(r'EAAG(.*?)"', data)
            if match:
                return 'EAAG' + match.group(1)
    except Exception as e:
        print(f" {stylee} \033[1;31mToken extraction failed: {e}")
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
                            sys.stdout.write(f"\r\033[1;37m[\033[1;32m{current_count}/{target_shares}\033[1;37m] \033[1;32m[{account_name}]\033[1;37m                    ")
                        else:
                            sys.stdout.write(f"\r\033[1;37m[\033[1;32mSUCCESS: {current_count}\033[1;37m] \033[1;32m[{account_name}]\033[1;37m                    ")
                        sys.stdout.flush()
                    else:
                        if target_shares:
                            print(f"\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;37m{current_time} \033[1;37m| \033[1;32m{account_name} \033[1;37m| \033[1;32m{current_count}/{target_shares}")
                        else:
                            print(f"\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;37m{current_time} \033[1;37m| \033[1;32m{account_name} \033[1;37m| \033[1;32mTotal: {current_count}")
                else:
                    error_msg = data.get('error', {}).get('message', 'Unknown error')
                    if display_mode != 'minimal':
                        print(f"\033[1;37m[\033[1;31m✗\033[1;37m] \033[1;37m{current_time} \033[1;37m| \033[1;32m{account_name} \033[1;37m| \033[1;31m{error_msg[:50]}")
                    break
        
        except asyncio.CancelledError:
            break
        except Exception as e:
            if display_mode != 'minimal':
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"\033[1;37m[\033[1;31m✗\033[1;37m] \033[1;37m{current_time} \033[1;37m| \033[1;32m{account_name} \033[1;37m| \033[1;31m{str(e)[:50]}")
            break

async def share_with_eaag(session, cookie, token, post_id):
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
                        sys.stdout.write(f"\r\033[1;37m[\033[1;32m{current_count}/{target_shares}\033[1;37m] \033[1;32m[UID: {account_uid}]\033[1;37m                    ")
                    else:
                        sys.stdout.write(f"\r\033[1;37m[\033[1;32mSUCCESS: {current_count}\033[1;37m] \033[1;32m[UID: {account_uid}]\033[1;37m                    ")
                    sys.stdout.flush()
                else:
                    if target_shares:
                        print(f"\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;37m{current_time} \033[1;37m| \033[1;32mUID: {account_uid} \033[1;37m| \033[1;32m{current_count}/{target_shares}")
                    else:
                        print(f"\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;37m{current_time} \033[1;37m| \033[1;32mUID: {account_uid} \033[1;37m| \033[1;32mTotal: {current_count}")
                
            else:
                if display_mode != 'minimal':
                    error_message = result[:40]
                    print(f"\033[1;37m[\033[1;31m✗\033[1;37m] \033[1;37m{current_time} \033[1;37m| \033[1;32mUID: {account_uid} \033[1;37m| \033[1;31m{error_message}")
                break
        
        except asyncio.CancelledError:
            break
        except KeyboardInterrupt:
            break
        except Exception as e:
            error_msg = str(e)
            if "asyncio" not in error_msg.lower() and "event" not in error_msg.lower():
                if display_mode != 'minimal':
                    print(f"\033[1;37m[\033[1;31m✗\033[1;37m] \033[1;37m{datetime.datetime.now().strftime('%H:%M:%S')} \033[1;37m| \033[1;32mUID: {account_uid} \033[1;37m| \033[1;31m{error_msg[:40]}")
            break

async def auto_share_main(link_or_id, selected_cookies, order_info=None):
    global success_count, current_order
    success_count = 0
    current_order = order_info
    target_shares = order_info.get('quantity') if order_info else None
    
    start_time = datetime.datetime.now()
    
    refresh_screen()
    print(f" {style} \033[1;32mCONVERTING SELECTED ACCOUNTS...")
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
            status_indicator = '\033[1;31m[RESTRICTED]' if cookie_data.get('status') == 'restricted' else '\033[1;32m[ACTIVE]'
            uid_text = f"UID: {cookie_data['uid']}"
            print(f" \033[1;32m✓ {cookie_data['name']} \033[1;37m({uid_text}) {status_indicator}\033[1;37m")
        else:
            print(f" \033[1;31m✗ {cookie_data['name']} \033[1;31mFailed to convert account")
    
    if not eaag_tokens:
        print(f" {stylee} \033[1;31mNo valid accounts converted!")
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return start_time
    
    async with aiohttp.ClientSession() as session:
        post_id = extract_post_id_from_link(link_or_id)
        
        if not post_id.isdigit():
            refresh_screen()
            print(f" {style} \033[1;32mEXTRACTING POST ID FROM LINK...")
            nice_loader("EXTRACTING")
            
            post_id = await getid(session, link_or_id)
            if not post_id:
                print(f" {stylee} \033[1;31mFailed to get post ID")
                input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
                return start_time
    
    display_mode = select_progress_display()
    
    refresh_screen()
    print(f" {style} \033[1;32mConverted {len(eaag_tokens)} accounts")
    linex()
    print(f" {style} \033[1;32mPost ID: \033[1;37m{post_id}")
    
    if order_info:
        linex()
        print(f" {style} \033[1;32mBOOSTER ORDER DETAILS")
        print(f" {style} \033[1;32mOrder ID: \033[1;37m{order_info.get('orderId', 'N/A')}")
        print(f" {style} \033[1;32mCustomer: \033[1;37m{order_info.get('customerName', 'N/A')}")
        print(f" {style} \033[1;32mQuantity: \033[1;37m{order_info.get('quantity', 0)}")
        print(f" {style} \033[1;32mAmount: \033[1;32m₱{order_info.get('amount', 0)}")
        if order_info.get('notes'):
            print(f" {style} \033[1;32mNotes: \033[1;37m{order_info.get('notes')}")
    
    linex()
    
    async with aiohttp.ClientSession() as session:
        print(f" {style} \033[1;32mAUTO SHARE CONFIGURATION")
        linex()
        print(f" {style} \033[1;32mMode: \033[1;37mNORMAL SHARING")
        print(f" {style} \033[1;32mTotal Accounts: \033[1;37m{len(eaag_tokens)}")
        print(f" {style} \033[1;32mShare Speed: \033[1;32mMAXIMUM (ZERO DELAYS)")
        if target_shares:
            print(f" {style} \033[1;32mTarget Shares: \033[1;37m{target_shares}")
        linex()
        print(f" {style} \033[1;32mSTARTING AUTO SHARE...")
        print(f" {style} \033[1;37mPress Ctrl+C to stop")
        linex()
        
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
        
        print(f" {style} \033[1;32mRunning {len(tasks)} parallel share threads at MAXIMUM SPEED...")
        linex()
        
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
        print(f" {style} \033[1;32mCONVERTING SELECTED ACCOUNTS...")
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
                print(f" \033[1;32m✓ {cookie_data['name']}")
            else:
                print(f" \033[1;31m✗ {cookie_data['name']} \033[1;31mFailed to convert account")
        
        if not valid_tokens:
            print(f" {stylee} \033[1;31mNo valid accounts converted!")
            print(f" {style} \033[1;32mCookies may be invalid or expired.")
            return start_time
        
        linex()
        print(f" {style} \033[1;32mConverted {len(valid_tokens)} account(s)!")
        linex()
        
        display_mode = select_progress_display()
        
        refresh_screen()
        print(f" {style} \033[1;32mSMM PANEL — MOST RECOMMENDED")
        linex()
        print(f" {style} \033[1;32mMethod: \033[1;37mSMM PANEL BOOST")
        print(f" {style} \033[1;32mPost Link: \033[1;37m{post_link[:50] + '...' if len(post_link) > 50 else post_link}")
        print(f" {style} \033[1;32mTarget Shares: \033[1;37m{share_count}")
        print(f" {style} \033[1;32mSpeed: \033[1;32mINSTANT (NO DELAYS)")
        print(f" {style} \033[1;32mTotal Cookies: \033[1;37m{len(valid_tokens)}")
        
        if order_info:
            linex()
            print(f" {style} \033[1;32mORDER DETAILS")
            print(f" {style} \033[1;32mOrder ID: \033[1;37m{order_info.get('orderId', 'N/A')}")
            print(f" {style} \033[1;32mCustomer: \033[1;37m{order_info.get('customerName', 'N/A')}")
            print(f" {style} \033[1;32mAmount: \033[1;32m₱{order_info.get('amount', 0)}")
        
        linex()
        print(f" {style} \033[1;32mSTARTING SMM PANEL BOOST...")
        print(f" {style} \033[1;37mPress Ctrl+C to stop")
        linex()
        
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
        
        print(f" {style} \033[1;32mRunning {len(tasks)} parallel share threads...")
        linex()
        
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

def generate_order_receipt(order_info, shares_completed, start_time, end_time):
    """Generate a receipt for completed order with banner"""
    is_completed = shares_completed >= order_info.get('quantity', 0)
    status_text = "Completed ✓" if is_completed else "Partial"
    
    clear()
    
    banner_art = """
 ╦═╗╔═╗╦ ╦╔╦╗╔═╗╔═╗╦  ╔═╗
 ╠╦╝╠═╝║║║ ║ ║ ║║ ║║  ╚═╗
 ╩╚═╩  ╚╩╝ ╩ ╚═╝╚═╝╩═╝╚═╝"""
    
    print(f"\033[1;32m{banner_art}\033[1;37m")
    linex()
    print(f"{style} \033[1;32mDEVELOPER   \033[1;37m: \033[1;32mKEN DRICK")
    print(f"{style} \033[1;32mGITHUB      \033[1;37m: \033[1;32mRYO GRAHHH")
    print(f"{style} \033[1;32mFACEBOOK    \033[1;37m: \033[1;32mfacebook.com/ryoevisu")
    print(f"{style} \033[1;32mTOOL NAME   \033[1;37m: \033[1;32m[ RPWTOOLS ]")
    linex()
    
    print(f" {style} \033[1;32mORDER RECEIPT — SMM PANEL BOOST")
    linex()
    print(f" {style} \033[1;32mORDER ID          \033[1;37m: \033[1;32m{order_info.get('orderId', 'N/A')}")
    print(f" {style} \033[1;32mCUSTOMER NAME     \033[1;37m: \033[1;32m{order_info.get('customerName', 'N/A')}")
    print(f" {style} \033[1;32mPOST LINK         \033[1;37m: \033[1;37m{order_info.get('postLink', 'N/A')[:50]}")
    print(f" {style} \033[1;32mREQUEST QUANTITY  \033[1;37m: \033[1;37m{order_info.get('quantity', 0)}")
    
    if is_completed:
        print(f" {style} \033[1;32mSTATUS            \033[1;37m: \033[1;32m{status_text}")
    else:
        print(f" {style} \033[1;31mSTATUS            \033[1;37m: \033[1;31m{status_text}")
    
    print(f" {style} \033[1;32mAMOUNT            \033[1;37m: \033[1;32m₱{order_info.get('amount', 0)}")
    linex()
    
    if is_completed:
        print(f" {style} \033[1;32mThank you for your avail! Your order has been completed 😊")
    else:
        remaining = order_info.get('quantity', 0) - shares_completed
        print(f" {style} \033[1;37mOrder partially completed. Remaining: {remaining} shares")
    
    linex()
    print(f" {style} \033[1;32mPowered by RPWTOOLS — SMM Panel Boost System")
    print(f" {style} \033[1;32mGitHub: RYO GRAHHH | Facebook: facebook.com/ryoevisu")
    linex()

def select_cookies_for_sharing():
    refresh_screen()
    print(f" {style} \033[1;32mLOADING COOKIES FROM DATABASE...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/user/cookies")
    
    if status != 200 or not response.get('success'):
        print(f" {stylee} \033[1;31mFailed to load cookies")
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return None
    
    cookies = response.get('cookies', [])
    
    if not cookies:
        print(f" {stylee} \033[1;31mNo cookies stored in database")
        print(f" {style} \033[1;32mUse option to add cookies first")
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return None
    
    refresh_screen()
    print(f" {style} \033[1;32mSELECT COOKIES FOR AUTO SHARE")
    linex()
    print(f"\033[1;37m[\033[1;32mALL\033[1;37m]\033[1;32m USE ALL COOKIES")
    linex()
    
    for i, cookie_data in enumerate(cookies, 1):
        letter = chr(64 + i) if i <= 26 else str(i)
        status_indicator = '\033[1;31m[RESTRICTED]' if cookie_data.get('status') == 'restricted' else '\033[1;32m[ACTIVE]'
        uid_text = f"UID: {cookie_data['uid']}"
        print(f"\033[1;37m[{i:02d}/{letter}]\033[1;32m {cookie_data['name']} \033[1;37m({uid_text}) {status_indicator}\033[1;37m")
    
    linex()
    print(f" {style} \033[1;32mEnter numbers separated by commas (e.g., 1,2,3) or type ALL")
    linex()
    
    selection = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m SELECT \033[1;37m: \033[1;32m").strip().upper()
    
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
            print(f" {stylee} \033[1;31mInvalid selection")
            time.sleep(1)
            return None
    
    if not selected_cookies:
        print(f" {stylee} \033[1;31mNo valid cookies selected")
        time.sleep(1)
        return None
    
    refresh_screen()
    print(f" {style} \033[1;32mCONFIRM SELECTION")
    linex()
    print(f" {style} \033[1;32mSelected {len(selected_cookies)} cookie(s):")
    for cookie_data in selected_cookies:
        status_indicator = '\033[1;31m[RESTRICTED]' if cookie_data.get('status') == 'restricted' else '\033[1;32m[ACTIVE]'
        uid_text = f"UID: {cookie_data['uid']}"
        print(f"   \033[1;37m• \033[1;32m{cookie_data['name']} \033[1;37m({uid_text}) {status_indicator}\033[1;37m")
    linex()
    
    restricted_count = sum(1 for c in selected_cookies if c.get('status') == 'restricted')
    if restricted_count > 0:
        print(f" {stylee} \033[1;31mWARNING: {restricted_count} restricted account(s) detected!")
        print(f" {style} \033[1;32mRestricted accounts may not be able to share posts.")
        linex()
    
    confirm = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m Confirm? (Y/N) \033[1;37m: \033[1;32m").strip().upper()
    
    if confirm == 'Y':
        return selected_cookies
    else:
        return None

def start_auto_share():
    """Normal unlimited sharing"""
    global success_count, current_order
    
    if not user_data.get('isActive') and not user_data.get('isAdmin'):
        refresh_screen()
        print(f" {stylee} \033[1;31mACCESS DENIED")
        speak("Access denied, account not activated")
        linex()
        print(f" {stylee} \033[1;31mYour account is not activated.")
        print(f" {style} \033[1;32mPlease contact an administrator to activate your account.")
        linex()
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return
    
    refresh_screen()
    print(f" {style} \033[1;32mAUTO SHARE - NORMAL ACCOUNTS (UNLIMITED)")
    linex()
    speak("Auto share, normal accounts")
    print(f" {style} \033[1;32mINFORMATION:")
    print(f" {style} \033[1;32m• Make sure your post is set to PUBLIC")
    print(f" {style} \033[1;32m• Shares run at MAXIMUM SPEED (zero delays)")
    linex()
    
    link_or_id = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m POST LINK OR ID \033[1;37m: \033[1;32m").strip()
    
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
        print(f" {style} \033[1;32mAUTO SHARE COMPLETED")
        stop_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f" {style} \033[1;32mStop Time: {stop_time}")
        print(f" {style} \033[1;32mTotal Successful Shares: {success_count}")
        linex()
        
        if success_count > 0:
            api_request("POST", "/share/complete", {"totalShares": success_count})
            print(f" {style} \033[1;32mShares recorded to your account")
        
    except KeyboardInterrupt:
        end_time = datetime.datetime.now()
        
        refresh_screen()
        speak("Auto share stopped by user")
        print(f" {style} \033[1;37mAUTO SHARE STOPPED BY USER")
        stop_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f" {style} \033[1;32mStop Time: {stop_time}")
        print(f" {style} \033[1;32mTotal Successful Shares: {success_count}")
        linex()
        
        if success_count > 0:
            api_request("POST", "/share/complete", {"totalShares": success_count})
            print(f" {style} \033[1;32mShares recorded to your account")
    
    except Exception as e:
        refresh_screen()
        print(f" {stylee} \033[1;31mAn unexpected error occurred:")
        print(f" {stylee} \033[1;31m{str(e)}")
    
    linex()
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

def start_smm_panel_boost():
    """SMM Panel Boost with order system"""
    global success_count
    
    if not user_data.get('isActive') and not user_data.get('isAdmin'):
        refresh_screen()
        print(f" {stylee} \033[1;31mACCESS DENIED")
        speak("Access denied, account not activated")
        linex()
        print(f" {stylee} \033[1;31mYour account is not activated.")
        print(f" {style} \033[1;32mPlease contact an administrator to activate your account.")
        linex()
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return
    
    refresh_screen()
    print(f" {style} \033[1;32mSMM PANEL — MOST RECOMMENDED")
    linex()
    speak("SMM Panel, most recommended")
    print(f" {style} \033[1;32mINFORMATION:")
    print(f" {style} \033[1;32m• NO DELAYS - Instant sharing")
    print(f" {style} \033[1;32m• Creates order for tracking")
    print(f" {style} \033[1;32m• Supports multiple cookies")
    linex()
    print(f" {stylee} \033[1;31mNOT SUPPORTED POST LINK FORMATS")
    print(f" {stylee} \033[1;31m• https://www.facebook.com/share/p/XXXXX/")
    print(f" {stylee} \033[1;31m• https://www.facebook.com/share/XXXXX/")
    linex()
    print(f" {style} \033[1;32mAll other Facebook post link formats are supported")
    linex()
    
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
    
    refresh_screen()
    print(f" {style} \033[1;32mCREATE SMM BOOST ORDER")
    linex()
    speak("Create SMM boost order")
    
    customer_name = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m CUSTOMER NAME \033[1;37m: \033[1;32m").strip()
    if not customer_name:
        speak("Customer name is required")
        print(f" {stylee} \033[1;31mCustomer name is required")
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return
    
    post_link = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m POST LINK \033[1;37m: \033[1;32m").strip()
    if not post_link:
        speak("Post link is required")
        print(f" {stylee} \033[1;31mPost link is required")
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return
    
    if not validate_smm_post_link(post_link):
        refresh_screen()
        print(f" {stylee} \033[1;31mLINK FORMAT NOT SUPPORTED")
        speak("Link format not supported")
        linex()
        print(f" {stylee} \033[1;31mThis type of link format is NOT SUPPORTED!")
        linex()
        print(f" {stylee} \033[1;31mNOT SUPPORTED FORMATS")
        print(f" {stylee} \033[1;31m• https://www.facebook.com/share/p/XXXXX/")
        print(f" {stylee} \033[1;31m• https://www.facebook.com/share/XXXXX/")
        linex()
        print(f" {style} \033[1;32mSUPPORTED")
        print(f" {style} \033[1;32mAll other Facebook post link formats")
        linex()
        print(f" {style} \033[1;37mContact admin for guide on getting the correct link format.")
        linex()
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return
    
    share_count = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m SHARE COUNT \033[1;37m: \033[1;32m").strip()
    if not share_count or not share_count.isdigit():
        speak("Valid share count is required")
        print(f" {stylee} \033[1;31mValid share count is required")
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return
    
    share_count = int(share_count)
    
    amount = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m AMOUNT (₱) \033[1;37m: \033[1;32m").strip()
    if not amount:
        amount = '0'
    
    notes = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m NOTES (optional) \033[1;37m: \033[1;32m").strip()
    
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
                print(f" {style} \033[1;37mOrder ID already exists, generating new ID...")
                time.sleep(0.5)
                continue
            else:
                speak("Failed to create order after retries")
                print(f" {stylee} \033[1;31mFailed to create unique order ID after multiple attempts")
                input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
                return
        else:
            speak("Failed to create order")
            print(f" {stylee} \033[1;31m{response.get('message', 'Failed to create order') if isinstance(response, dict) else 'Failed to create order'}")
            input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
            return
    
    order_info = response.get('order', {})
    order_info['quantity'] = share_count
    order_info['postLink'] = post_link
    order_info['notes'] = notes
    
    speak("Order created successfully")
    print(f" {style} \033[1;32mOrder created!")
    print(f" {style} \033[1;32mOrder ID: \033[1;37m{order_info.get('orderId', 'N/A')}")
    linex()
    
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
            print(f" {style} \033[1;32mOrder status updated in database")
        
        if success_count > 0:
            api_request("POST", "/share/complete", {"totalShares": success_count})
            print(f" {style} \033[1;32mShares recorded to your account")
        
    except KeyboardInterrupt:
        end_time = datetime.datetime.now()
        
        generate_order_receipt(order_info, success_count, start_time, end_time)
        
        status, response = api_request("PUT", f"/admin/orders/{order_info.get('orderId')}", {
            "status": "processing",
            "currentCount": success_count
        })
        
        if status == 200:
            print(f" {style} \033[1;37mOrder marked as PROCESSING (partial completion)")
        
        if success_count > 0:
            api_request("POST", "/share/complete", {"totalShares": success_count})
            print(f" {style} \033[1;32mShares recorded to your account")
    
    except Exception as e:
        refresh_screen()
        print(f" {stylee} \033[1;31mAn unexpected error occurred:")
        print(f" {stylee} \033[1;31m{str(e)}")
    
    linex()
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

# ============ MAIN FUNCTION ============

def main():
    global user_token, user_data
    
    check_version()
    
    clear()
    print(f" {style} \033[1;32mWELCOME TO RPWTOOLS BY KENDRICK")
    speak("Welcome to RPW Tools by Kendrick")
    time.sleep(2)
    
    while True:
        refresh_screen()
        
        try:
            choice = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m CHOOSE \033[1;37m: \033[1;32m").upper()
        except KeyboardInterrupt:
            sys.exit()

        refresh_screen()

        if not user_token:
            if choice in ['1', '01', 'A']:
                login_user()
            elif choice in ['2', '02', 'B']:
                register_user()
            elif choice in ['0', '00', 'X']:
                print(f"\n {stylee} \033[1;31mEXITING TOOL...")
                sys.exit()
            else:
                print(f"\n {stylee} \033[1;31mINVALID SELECTION")
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
                print(f"\n {style} \033[1;32mLOGGING OUT...")
                user_token = None
                user_data = None
                time.sleep(1)
            else:
                print(f"\n {stylee} \033[1;31mINVALID SELECTION")
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
                print(f"\n {style} \033[1;32mLOGGING OUT...")
                user_token = None
                user_data = None
                time.sleep(1)
            else:
                print(f"\n {stylee} \033[1;31mINVALID SELECTION")
                time.sleep(0.8)
        
        else:
            if choice in ['1', '01', 'A']:
                manage_cookies()
            elif choice in ['2', '02', 'B']:
                show_user_stats()
            elif choice in ['0', '00', 'X']:
                print(f"\n {style} \033[1;32mLOGGING OUT...")
                user_token = None
                user_data = None
                time.sleep(1)
            else:
                print(f"\n {stylee} \033[1;31mINVALID SELECTION")
                time.sleep(0.8)

if __name__ == "__main__":
    main()

user_data = None

# --- ESPEAK CONFIGURATION ---
def speak(text):
    """Text-to-speech using espeak (non-blocking)"""
    try:
        threading.Thread(target=lambda: os.system(f'espeak -a 200 -s 150 "{text}" > /dev/null 2>&1'), daemon=True).start()
    except:
        pass

# --- GLOBAL VARIABLES ---
success_count = 0
lock = asyncio.Lock()
current_order = None

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def linex():
    print(f'\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

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
                linex()
                print(f" {stylee} \033[1;31mVERSION MISMATCH")
                linex()
                print(f" {style} \033[1;32mYour tool version \033[1;37m: \033[1;31m{CURRENT_VERSION}")
                print(f" {style} \033[1;32mServer version \033[1;37m: \033[1;32m{server_version}")
                linex()
                print(f" {stylee} \033[1;31mYour tool is outdated!")
                print(f" {style} \033[1;32mPlease update to the latest version to continue using this tool.")
                linex()
                input(f"\n {stylee} \033[1;31mPRESS ENTER TO EXIT")
                sys.exit(1)
    except:
        pass

def banner_header():
    banner_art = """
 ╦═╗╔═╗╦ ╦╔╦╗╔═╗╔═╗╦  ╔═╗
 ╠╦╝╠═╝║║║ ║ ║ ║║ ║║  ╚═╗
 ╩╚═╩  ╚╩╝ ╩ ╚═╝╚═╝╩═╝╚═╝"""
    
    print(f"\033[1;32m{banner_art}\033[1;37m")
    linex()
    print(f"{style} \033[1;32mDEVELOPER   \033[1;37m: \033[1;32mKEN DRICK")
    print(f"{style} \033[1;32mGITHUB      \033[1;37m: \033[1;32mRYO GRAHHH")
    print(f"{style} \033[1;32mVERSION     \033[1;37m: \033[1;32m{CURRENT_VERSION}")
    print(f"{style} \033[1;32mFACEBOOK    \033[1;37m: \033[1;32mfacebook.com/ryoevisu")
    print(f"{style} \033[1;32mTOOL NAME   \033[1;37m: \033[1;32m[ RPWTOOLS ]")
    
    if user_data:
        linex()
        print(f"{style} \033[1;32mUSERNAME       \033[1;37m: \033[1;32m{user_data['username'].upper()}")
        print(f"{style} \033[1;32mFACEBOOK       \033[1;37m: \033[1;32m{user_data.get('facebook', 'N/A')}")
        print(f"{style} \033[1;32mCOUNTRY        \033[1;37m: \033[1;32m{user_data.get('country', 'N/A').upper()}")
        
        is_active = user_data.get('isActive', False)
        
        if is_active:
            status_display = f"\033[1;32mACTIVE - FULL ACCESS"
        else:
            status_display = f"\033[1;31mINACTIVE - LIMITED"
        
        print(f"{style} \033[1;32mSTATUS         \033[1;37m: {status_display}\033[1;37m")
        
        cookie_count = user_data.get('cookieCount', 0)
        print(f"{style} \033[1;32mTOTAL COOKIES  \033[1;37m: \033[1;32m{cookie_count}")
    
    linex()

def show_menu():
    if not user_token:
        print(f"\033[1;37m[\033[1;32m01\033[1;37m]\033[1;32m LOGIN")
        print(f"\033[1;37m[\033[1;32m02\033[1;37m]\033[1;32m REGISTER")
        print(f"\033[1;37m[\033[1;31m00\033[1;37m]\033[1;31m EXIT")
    elif user_data and user_data.get('isAdmin'):
        print(f"\033[1;37m[\033[1;32m01\033[1;37m]\033[1;32m AUTO SHARE              — NORM ACCOUNTS")
        print(f"\033[1;37m[\033[1;32m02\033[1;37m]\033[1;32m SMM PANEL               — MOST RECOMMENDED")
        print(f"\033[1;37m[\033[1;32m03\033[1;37m]\033[1;32m MANAGE COOKIES          — DATABASE")
        print(f"\033[1;37m[\033[1;32m04\033[1;37m]\033[1;32m MY STATS                — STATISTICS")
        print(f"\033[1;37m[\033[1;32m05\033[1;37m]\033[1;32m ADMIN PANEL             — MANAGEMENT")
        print(f"\033[1;37m[\033[1;32m06\033[1;37m]\033[1;32m UPDATE TOOL             — LATEST VERSION")
        print(f"\033[1;37m[\033[1;31m00\033[1;37m]\033[1;31m LOGOUT")
    elif user_data and user_data.get('isActive'):
        print(f"\033[1;37m[\033[1;32m01\033[1;37m]\033[1;32m AUTO SHARE              — NORM ACCOUNTS")
        print(f"\033[1;37m[\033[1;32m02\033[1;37m]\033[1;32m SMM PANEL               — MOST RECOMMENDED")
        print(f"\033[1;37m[\033[1;32m03\033[1;37m]\033[1;32m MANAGE COOKIES          — DATABASE")
        print(f"\033[1;37m[\033[1;32m04\033[1;37m]\033[1;32m MY STATS                — STATISTICS")
        print(f"\033[1;37m[\033[1;32m05\033[1;37m]\033[1;32m UPDATE TOOL             — LATEST VERSION")
        print(f"\033[1;37m[\033[1;31m00\033[1;37m]\033[1;31m LOGOUT")
    else:
        print(f"\033[1;37m[\033[1;32m01\033[1;37m]\033[1;32m MANAGE COOKIES          — DATABASE")
        print(f"\033[1;37m[\033[1;32m02\033[1;37m]\033[1;32m MY STATS                — STATISTICS")
        print(f"\033[1;37m[\033[1;31m00\033[1;37m]\033[1;31m LOGOUT")
    linex()

def refresh_screen():
    clear()
    banner_header()
    show_menu()

def nice_loader(text="PROCESSING"):
    """Animated loader"""
    sys.stdout.write("\033[?25l")
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    
    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write(f"\r {style} \033[1;32m{text} \033[1;37m: " + animation[i % len(animation)])
        sys.stdout.flush()
    
    sys.stdout.write(f"\r{' ' * 80}\r")
    sys.stdout.flush()
    sys.stdout.write("\033[?25h")

def select_progress_display():
    refresh_screen()
    print(f" {style} \033[1;32mSHARING PROGRESS DISPLAY")
    linex()
    print(f" {style} \033[1;32mChoose how you want to see sharing progress:")
    linex()
    print(f"\033[1;37m[\033[1;32m1\033[1;37m]\033[1;32m SUCCESS COUNTER (1/100)")
    print(f"     \033[1;37m• \033[1;32mBest for smaller screens (mobile)")
    linex()
    print(f"\033[1;37m[\033[1;32m2\033[1;37m]\033[1;32m DETAILED LOGS")
    print(f"     \033[1;37m• \033[1;32mBest for larger screens (desktop)")
    linex()
    
    while True:
        choice = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m CHOICE (1 or 2) \033[1;37m: \033[1;32m").strip()
        if choice == '1':
            return 'minimal'
        elif choice == '2':
            return 'detailed'
        else:
            print(f" {stylee} \033[1;31mInvalid choice. Please enter 1 or 2")
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
    print(f" {style} \033[1;32mLOGIN TO RPWTOOLS")
    linex()
    speak("Login to RPW Tools")
    
    username = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m USERNAME \033[1;37m: \033[1;32m").strip()
    if not username:
        return
    
    password = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m PASSWORD \033[1;37m: \033[1;32m").strip()
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
        print(f" {style} \033[1;32mLogin successful!")
        linex()
        print(f" {style} \033[1;32mWelcome back, \033[1;37m{user_data['username'].upper()}")
        
        is_active = user_data.get('isActive', False)
        
        if is_active:
            status_text = 'ACTIVE - FULL ACCESS'
            print(f" {style} \033[1;32mStatus: {status_text}")
        else:
            status_text = 'INACTIVE - LIMITED ACCESS'
            print(f" {style} \033[1;31mStatus: {status_text}")
            print(f" {stylee} \033[1;31mYou can only manage cookies. Contact admin to activate.")
        
        print(f" {style} \033[1;32mTotal Cookies: \033[1;37m{user_data.get('cookieCount', 0)}")
        
        if user_data.get('isAdmin'):
            print(f" {style} \033[1;32mADMIN ACCESS GRANTED")
        
        linex()
    elif status == 403:
        if response.get('allowLimited'):
            user_token = response.get('token')
            user_data = response.get('user')
            print(f" {stylee} \033[1;31mLIMITED ACCESS")
            linex()
            print(f" {stylee} \033[1;31m{response.get('message', 'Account not activated')}")
            print(f" {style} \033[1;32mYou can still manage cookies.")
            linex()
        else:
            print(f" {stylee} \033[1;31mACCESS DENIED")
            linex()
            print(f" {stylee} \033[1;31m{response.get('message', 'Account not activated')}")
            linex()
    else:
        print(f" {stylee} \033[1;31m{response if isinstance(response, str) else response.get('message', 'Login failed')}")
        linex()
    
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

def register_user():
    global user_token, user_data
    
    refresh_screen()
    print(f" {style} \033[1;32mREGISTER NEW ACCOUNT")
    linex()
    speak("Register new account")
    
    username = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m USERNAME \033[1;37m: \033[1;32m").strip()
    if not username:
        return
    
    password = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m PASSWORD \033[1;37m: \033[1;32m").strip()
    if not password:
        return
    
    facebook = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m FACEBOOK LINK \033[1;37m: \033[1;32m").strip()
    if not facebook:
        return
    
    facebook = normalize_facebook_url(facebook)
    
    refresh_screen()
    print(f" {style} \033[1;32mNORMALIZED FACEBOOK URL: \033[1;37m{facebook}")
    linex()
    
    print(f" {style} \033[1;32mDETECTING YOUR COUNTRY...")
    speak("Detecting your country")
    nice_loader("DETECTING")
    
    country = get_country_from_ip()
    
    refresh_screen()
    print(f" {style} \033[1;32mDETECTED COUNTRY: \033[1;37m{country}")
    linex()
    confirm = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m Is this correct? (Y/N) \033[1;37m: \033[1;32m").strip().upper()
    
    if confirm == 'N':
        country = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m ENTER YOUR COUNTRY \033[1;37m: \033[1;32m").strip()
    
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
        print(f" {style} \033[1;32mRegistration successful!")
        linex()
        print(f" {style} \033[1;32m{user_data['username'].upper()}")
        print(f" {style} \033[1;32mYour account has been created!")
        linex()
        print(f" {stylee} \033[1;31mIMPORTANT NOTICE:")
        print(f" {style} \033[1;32mYour account is currently INACTIVE.")
        print(f" {style} \033[1;32mPlease contact an administrator to activate your account.")
        print(f" {style} \033[1;32mYou can still manage cookies while waiting for activation.")
        linex()
    else:
        print(f" {stylee} \033[1;31m{response if isinstance(response, str) else response.get('message', 'Registration failed')}")
        linex()
    
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

def show_user_stats():
    refresh_screen()
    print(f" {style} \033[1;32mLOADING STATS...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/user/stats")
    
    if status == 200 and response.get('success'):
        stats = response.get('stats')
        
        refresh_screen()
        print(f" {style} \033[1;32mUSER STATISTICS")
        linex()
        print(f" {style} \033[1;32mUsername: \033[1;37m{stats['username'].upper()}")
        
        is_active = stats.get('isActive', False)
        status_display = '\033[1;32mACTIVE - FULL ACCESS' if is_active else '\033[1;31mINACTIVE - LIMITED'
        print(f" {style} \033[1;32mAccount Status: {status_display}\033[1;37m")
        
        linex()
        print(f" {style} \033[1;32mSTATISTICS")
        print(f" {style} \033[1;32mTotal Shares: \033[1;37m{stats['totalShares']}")
        print(f" {style} \033[1;32mTotal Cookies: \033[1;37m{stats.get('cookieCount', 0)}")
        linex()
    else:
        print(f" {stylee} \033[1;31mFailed to get stats")
        linex()
    
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

def manage_cookies():
    while True:
        refresh_screen()
        print(f" {style} \033[1;32mMANAGE COOKIES")
        linex()
        print(f"\033[1;37m[\033[1;32m1\033[1;37m]\033[1;32m VIEW ALL COOKIES")
        print(f"\033[1;37m[\033[1;32m2\033[1;37m]\033[1;32m ADD COOKIE")
        print(f"\033[1;37m[\033[1;31m3\033[1;37m]\033[1;31m DELETE COOKIE")
        print(f"\033[1;37m[\033[1;31m4\033[1;37m]\033[1;31m DELETE ALL COOKIES")
        print(f"\033[1;37m[\033[1;31m0\033[1;37m]\033[1;31m BACK")
        linex()
        
        choice = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m CHOOSE \033[1;37m: \033[1;32m").strip()
        
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
            print(f"\n {stylee} \033[1;31mINVALID SELECTION")
            time.sleep(0.8)

def view_cookies():
    refresh_screen()
    print(f" {style} \033[1;32mLOADING COOKIES...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/user/cookies")
    
    if status == 200 and response.get('success'):
        cookies = response.get('cookies', [])
        
        refresh_screen()
        print(f" {style} \033[1;32mCOOKIES - Total: {len(cookies)}")
        linex()
        
        if not cookies:
            print(f" {style} \033[1;32mNo cookies stored yet.")
        else:
            for i, cookie_data in enumerate(cookies, 1):
                status_display = '\033[1;32m[ACTIVE]' if cookie_data['status'] == 'active' else '\033[1;31m[RESTRICTED]'
                
                uid_text = f"UID: {cookie_data['uid']}"
                print(f"\033[1;37m[{i:02d}]\033[1;32m {cookie_data['name']} \033[1;37m({uid_text}) {status_display}\033[1;37m")
                cookie_preview = cookie_data['cookie'][:50] + "..." if len(cookie_data['cookie']) > 50 else cookie_data['cookie']
                print(f"      Cookie: \033[1;37m{cookie_preview}")
                print(f"      Added: \033[1;32m{cookie_data['addedAt']}")
                
                if cookie_data['status'] == 'restricted':
                    print(f"      {stylee} \033[1;31mWARNING: This account is restricted!")
                
                linex()
        
    else:
        print(f" {stylee} \033[1;31mFailed to load cookies")
        linex()
    
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

def add_cookie():
    refresh_screen()
    print(f" {style} \033[1;32mADD COOKIE")
    linex()
    speak("Add cookie")
    
    cookie = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m COOKIE \033[1;37m: \033[1;32m").strip()
    if not cookie:
        return
    
    refresh_screen()
    print(f" {style} \033[1;32mVALIDATING COOKIE...")
    print(f" {style} \033[1;32mThis may take 10-15 seconds")
    linex()
    speak("Validating cookie, please wait")
    nice_loader("VALIDATING")
    
    status, response = api_request("POST", "/user/cookies", {"cookie": cookie})
    
    if status == 200 and isinstance(response, dict) and response.get('success'):
        speak("Cookie added successfully")
        print(f" {style} \033[1;32m{response.get('message')}")
        linex()
        print(f" {style} \033[1;32mName: \033[1;37m{response.get('name', 'Unknown')}")
        print(f" {style} \033[1;32mUID: \033[1;37m{response.get('uid', 'Unknown')}")
        status_display = f"\033[1;32m{response.get('status', 'unknown').upper()}" if response.get('status') == 'active' else f"\033[1;31m{response.get('status', 'unknown').upper()}"
        print(f" {style} \033[1;32mStatus: {status_display}\033[1;37m")
        
        if response.get('restricted'):
            linex()
            print(f" {stylee} \033[1;31mWARNING: This account is RESTRICTED!")
            print(f" {style} \033[1;32mRestricted accounts may not be able to share posts.")
        
        if user_data:
            user_data['cookieCount'] = response.get('totalCookies', 0)
        
        linex()
    else:
        error_msg = response if isinstance(response, str) else response.get('message', 'Failed to add cookie') if isinstance(response, dict) else 'Failed to add cookie'
        print(f" {stylee} \033[1;31m{error_msg}")
        linex()
    
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

def delete_cookie():
    refresh_screen()
    print(f" {style} \033[1;32mLOADING COOKIES...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/user/cookies")
    
    if status != 200 or not isinstance(response, dict) or not response.get('success'):
        error_msg = response if isinstance(response, str) else 'Failed to load cookies'
        print(f" {stylee} \033[1;31m{error_msg}")
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return
    
    cookies = response.get('cookies', [])
    
    if not cookies:
        refresh_screen()
        print(f" {style} \033[1;32mNo cookies to delete.")
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return
    
    refresh_screen()
    print(f" {stylee} \033[1;31mDELETE COOKIE")
    linex()
    
    for i, cookie_data in enumerate(cookies, 1):
        status_indicator = '\033[1;31m[RESTRICTED]' if cookie_data.get('status') == 'restricted' else '\033[1;32m[ACTIVE]'
        uid_text = f"UID: {cookie_data['uid']}"
        print(f"\033[1;37m[{i}]\033[1;32m {cookie_data['name']} \033[1;37m({uid_text}) {status_indicator}\033[1;37m")
    
    linex()
    
    choice = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m SELECT COOKIE NUMBER (0 to cancel) \033[1;37m: \033[1;32m").strip()
    
    if not choice or choice == '0':
        return
    
    try:
        cookie_index = int(choice) - 1
        if cookie_index < 0 or cookie_index >= len(cookies):
            print(f" {stylee} \033[1;31mInvalid cookie number")
            time.sleep(1)
            return
        
        selected_cookie = cookies[cookie_index]
    except:
        print(f" {stylee} \033[1;31mInvalid input")
        time.sleep(1)
        return
    
    refresh_screen()
    speak("Deleting cookie")
    nice_loader("DELETING")
    
    status, response = api_request("DELETE", f"/user/cookies/{selected_cookie['id']}")
    
    if status == 200 and isinstance(response, dict) and response.get('success'):
        speak("Cookie deleted successfully")
        print(f" {style} \033[1;32mCookie deleted!")
        if user_data:
            user_data['cookieCount'] = response.get('totalCookies', 0)
    else:
        error_msg = response if isinstance(response, str) else 'Failed to delete cookie'
        print(f" {stylee} \033[1;31m{error_msg}")
    
    linex()
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

def delete_all_cookies():
    refresh_screen()
    print(f" {stylee} \033[1;31mDELETE ALL COOKIES")
    linex()
    
    confirm = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;31m Delete ALL cookies? This cannot be undone! (YES/NO) \033[1;37m: \033[1;31m").strip().upper()
    
    if confirm != 'YES':
        return
    
    refresh_screen()
    speak("Deleting all cookies")
    nice_loader("DELETING")
    
    status, response = api_request("DELETE", "/user/cookies")
    
    if status == 200 and response.get('success'):
        speak("All cookies deleted")
        print(f" {style} \033[1;32m{response.get('message')}")
        if user_data:
            user_data['cookieCount'] = 0
    else:
        print(f" {stylee} \033[1;31mFailed to delete cookies")
    
    linex()
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

def update_tool_logic():
    print(f" {style} \033[1;32mCHECKING FOR UPDATES...")
    speak("Checking for updates")
    nice_loader("CHECKING")
    
    print(f" {style} \033[1;32mNEW VERSION FOUND! DOWNLOADING...")
    speak("Downloading update")
    nice_loader("UPDATING")
    
    print(f" {style} \033[1;32mUPDATE COMPLETE. RESTARTING...")
    speak("Update complete, restarting")
    time.sleep(1)
    
    os.execv(sys.executable, ['python'] + sys.argv)

# ============ ADMIN PANEL FUNCTIONS ============

def admin_panel():
    while True:
        refresh_screen()
        print(f" {style} \033[1;32mADMIN PANEL")
        linex()
        print(f"\033[1;37m[\033[1;32m1\033[1;37m]\033[1;32m VIEW ALL USERS")
        print(f"\033[1;37m[\033[1;32m2\033[1;37m]\033[1;32m ACTIVATE USER (Auto: Full Access)")
        print(f"\033[1;37m[\033[1;31m3\033[1;37m]\033[1;31m DEACTIVATE USER")
        print(f"\033[1;37m[\033[1;31m4\033[1;37m]\033[1;31m DELETE USER")
        print(f"\033[1;37m[\033[1;31m5\033[1;37m]\033[1;31m DELETE ALL USERS")
        print(f"\033[1;37m[\033[1;32m6\033[1;37m]\033[1;32m VIEW ACTIVITY LOGS")
        print(f"\033[1;37m[\033[1;32m7\033[1;37m]\033[1;32m DASHBOARD STATS")
        print(f"\033[1;37m[\033[1;32m8\033[1;37m]\033[1;32m VIEW ALL ORDERS")
        print(f"\033[1;37m[\033[1;31m0\033[1;37m]\033[1;31m BACK")
        linex()
        
        choice = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m CHOOSE \033[1;37m: \033[1;32m").strip()
        
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
            print(f"\n {stylee} \033[1;31mINVALID SELECTION")
            time.sleep(0.8)

def view_all_users():
    refresh_screen()
    print(f" {style} \033[1;32mLOADING USERS...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/admin/users")
    
    if status == 200 and response.get('success'):
        users = response.get('users', [])
        
        refresh_screen()
        print(f" {style} \033[1;32mALL USERS - Total: {len(users)}")
        linex()
        
        for i, user in enumerate(users, 1):
            admin_badge = f" \033[1;32m[ADMIN]" if user.get('isAdmin') else ""
            status_badge = '\033[1;32m[ACTIVE]' if user.get('isActive') else '\033[1;31m[INACTIVE]'
            
            print(f"\033[1;37m[{i:02d}]\033[1;32m {user['username'].upper()}{admin_badge} {status_badge}\033[1;37m")
            print(f"      Country: \033[1;32m{user['country']}")
            print(f"      Shares: \033[1;32m{user['totalShares']}")
            print(f"      Total Cookies: \033[1;37m{user.get('cookieCount', 0)}")
            linex()
        
    else:
        print(f" {stylee} \033[1;31mFailed to get users")
        linex()
    
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

def activate_user():
    refresh_screen()
    print(f" {style} \033[1;32mACTIVATE USER")
    print(f" {style} \033[1;32mNote: Activating will automatically grant FULL ACCESS")
    linex()
    
    status, response = api_request("GET", "/admin/users")
    
    if status != 200 or not response.get('success'):
        print(f" {stylee} \033[1;31mFailed to load users")
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return
    
    users = [u for u in response.get('users', []) if not u.get('isAdmin') and not u.get('isActive')]
    
    if not users:
        print(f" {style} \033[1;32mNo inactive users to activate.")
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return
    
    print(f" {style} \033[1;32mSELECT USER TO ACTIVATE")
    linex()
    for i, user in enumerate(users, 1):
        print(f"\033[1;37m[{i}]\033[1;32m {user['username'].upper()} - \033[1;31m[INACTIVE]\033[1;37m")
    linex()
    
    user_choice = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m SELECT USER NUMBER (0 to cancel) \033[1;37m: \033[1;32m").strip()
    
    if not user_choice or user_choice == '0':
        return
    
    try:
        user_index = int(user_choice) - 1
        if user_index < 0 or user_index >= len(users):
            print(f" {stylee} \033[1;31mInvalid user number")
            time.sleep(1)
            return
        
        selected_user = users[user_index]
    except:
        print(f" {stylee} \033[1;31mInvalid input")
        time.sleep(1)
        return
    
    refresh_screen()
    speak("Activating user")
    nice_loader("ACTIVATING")
    
    status, response = api_request("PUT", f"/admin/users/{selected_user['username']}/activate")
    
    if status == 200 and response.get('success'):
        speak("User activated successfully")
        print(f" {style} \033[1;32mUser activated successfully!")
        print(f" {style} \033[1;32m• Account Status: ACTIVE")
        print(f" {style} \033[1;32m• Access Level: FULL ACCESS")
    else:
        print(f" {stylee} \033[1;31m{response.get('message', 'Failed to activate user')}")
    
    linex()
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

def deactivate_user():
    refresh_screen()
    print(f" {stylee} \033[1;31mDEACTIVATE USER")
    print(f" {style} \033[1;32mNote: Deactivated users can still manage cookies but cannot share")
    linex()
    
    status, response = api_request("GET", "/admin/users")
    
    if status != 200 or not response.get('success'):
        print(f" {stylee} \033[1;31mFailed to load users")
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return
    
    users = [u for u in response.get('users', []) if not u.get('isAdmin') and u.get('isActive')]
    
    if not users:
        print(f" {style} \033[1;32mNo active users to deactivate.")
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return
    
    print(f" {style} \033[1;32mSELECT USER TO DEACTIVATE")
    linex()
    for i, user in enumerate(users, 1):
        print(f"\033[1;37m[{i}]\033[1;32m {user['username'].upper()} - \033[1;32m[ACTIVE]\033[1;37m")
    linex()
    
    user_choice = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m SELECT USER NUMBER (0 to cancel) \033[1;37m: \033[1;32m").strip()
    
    if not user_choice or user_choice == '0':
        return
    
    try:
        user_index = int(user_choice) - 1
        if user_index < 0 or user_index >= len(users):
            print(f" {stylee} \033[1;31mInvalid user number")
            time.sleep(1)
            return
        
        selected_user = users[user_index]
    except:
        print(f" {stylee} \033[1;31mInvalid input")
        time.sleep(1)
        return
    
    refresh_screen()
    speak("Deactivating user")
    nice_loader("DEACTIVATING")
    
    status, response = api_request("PUT", f"/admin/users/{selected_user['username']}/deactivate")
    
    if status == 200 and response.get('success'):
        speak("User deactivated")
        print(f" {style} \033[1;32mUser deactivated successfully!")
        print(f" {style} \033[1;32m• User can still manage cookies")
        print(f" {stylee} \033[1;31m• User cannot use sharing features")
    else:
        print(f" {stylee} \033[1;31m{response.get('message', 'Failed to deactivate user')}")
    
    linex()
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

def delete_user():
    refresh_screen()
    print(f" {stylee} \033[1;31mDELETE USER")
    linex()
    
    status, response = api_request("GET", "/admin/users")
    
    if status != 200 or not response.get('success'):
        print(f" {stylee} \033[1;31mFailed to load users")
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return
    
    users = [u for u in response.get('users', []) if not u.get('isAdmin')]
    
    if not users:
        print(f" {style} \033[1;32mNo users to delete.")
        input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")
        return
    
    print(f" {style} \033[1;32mSELECT USER TO DELETE")
    linex()
    
    for i, user in enumerate(users, 1):
        status_badge = '\033[1;32m[ACTIVE]' if user.get('isActive') else '\033[1;31m[INACTIVE]'
        print(f"\033[1;37m[{i:02d}]\033[1;32m {user['username'].upper()} - {status_badge}\033[1;37m")
    
    print(f"\033[1;37m[00]\033[1;31m CANCEL\033[1;37m")
    linex()
    
    choice = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;32m SELECT USER \033[1;37m: \033[1;32m").strip()
    
    if not choice or choice in ['0', '00']:
        return
    
    try:
        user_index = int(choice) - 1
        if user_index < 0 or user_index >= len(users):
            print(f" {stylee} \033[1;31mInvalid selection")
            time.sleep(1)
            return
        
        selected_user = users[user_index]
    except:
        print(f" {stylee} \033[1;31mInvalid input")
        time.sleep(1)
        return
    
    refresh_screen()
    print(f" {stylee} \033[1;31mCONFIRM DELETION")
    linex()
    print(f" User: \033[1;32m{selected_user['username'].upper()}")
    print(f" Country: \033[1;32m{selected_user['country']}")
    linex()
    
    confirm = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;31m Delete this user? This cannot be undone! (YES/NO) \033[1;37m: \033[1;31m").strip().upper()
    
    if confirm != 'YES':
        return
    
    speak("Deleting user")
    nice_loader("DELETING")
    
    status, response = api_request("DELETE", f"/admin/users/{selected_user['username']}")
    
    if status == 200 and response.get('success'):
        speak("User deleted")
        print(f" {style} \033[1;32mUser {selected_user['username']} deleted successfully!")
    else:
        print(f" {stylee} \033[1;31m{response.get('message', 'Failed to delete user')}")
    
    linex()
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

def delete_all_users():
    refresh_screen()
    print(f" {stylee} \033[1;31mDELETE ALL USERS")
    linex()
    print(f" {stylee} \033[1;31mWARNING: This will delete ALL non-admin users!")
    print(f" {stylee} \033[1;31mThis action CANNOT be undone!")
    linex()
    
    confirm = input(f"\033[1;37m[\033[1;32m?\033[1;37m]\033[1;31m Type CONFIRM to proceed \033[1;37m: \033[1;31m").strip()
    
    if confirm != 'CONFIRM':
        print(f" {style} \033[1;32mCANCELLED")
        time.sleep(1)
        return
    
    refresh_screen()
    speak("Deleting all users")
    nice_loader("DELETING ALL USERS")
    
    status, response = api_request("DELETE", "/admin/users")
    
    if status == 200 and response.get('success'):
        deleted_count = response.get('deletedCount', 0)
        speak(f"Deleted {deleted_count} users")
        print(f" {style} \033[1;32mDeleted {deleted_count} user(s) successfully!")
    else:
        print(f" {stylee} \033[1;31m{response.get('message', 'Failed to delete users')}")
    
    linex()
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

def view_activity_logs():
    refresh_screen()
    print(f" {style} \033[1;32mLOADING ACTIVITY LOGS...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/admin/logs?limit=20")
    
    if status == 200 and response.get('success'):
        logs = response.get('logs', [])
        
        refresh_screen()
        print(f" {style} \033[1;32mACTIVITY LOGS - Recent 20")
        linex()
        
        for log in logs:
            action_display = f"\033[1;32m{log['action'].upper()}" if log['action'] == 'login' else f"\033[1;37m{log['action'].upper()}"
            print(f"\033[1;37m[{log['timestamp']}]")
            print(f" User: \033[1;32m{log['username'].upper()} \033[1;37m| Action: {action_display}\033[1;37m")
            if log.get('details'):
                print(f" Details: \033[1;32m{log['details']}")
            linex()
    else:
        print(f" {stylee} \033[1;31mFailed to load logs")
        linex()
    
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

def dashboard_stats():
    refresh_screen()
    print(f" {style} \033[1;32mLOADING DASHBOARD...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/admin/dashboard")
    
    if status == 200 and response.get('success'):
        stats = response.get('stats', {})
        
        refresh_screen()
        print(f" {style} \033[1;32mADMIN DASHBOARD")
        linex()
        
        print(f" {style} \033[1;32mUSER STATISTICS")
        print(f" Total Users: \033[1;32m{stats['totalUsers']}")
        print(f" Active Users: \033[1;32m{stats['activeUsers']}")
        print(f" Inactive Users: \033[1;31m{stats['inactiveUsers']}")
        linex()
        
        print(f" {style} \033[1;32mORDER STATISTICS")
        print(f" Pending Orders: \033[1;37m{stats.get('pendingOrders', 0)}")
        print(f" Completed Orders: \033[1;32m{stats.get('completedOrders', 0)}")
        print(f" Total Revenue: \033[1;32m₱{stats.get('totalRevenue', 0)}")
        linex()
        
        print(f" {style} \033[1;32mACTIVITY STATISTICS")
        print(f" Total Shares: \033[1;32m{stats['totalShares']}")
        linex()
        
        print(f" {style} \033[1;32mRECENT USERS")
        for user in stats.get('recentUsers', []):
            status_badge = '\033[1;32m[ACTIVE]' if user.get('isActive') else '\033[1;31m[INACTIVE]'
            print(f" \033[1;32m{user['username'].upper()} - {status_badge} - {user['country']}\033[1;37m")
        linex()
    else:
        print(f" {stylee} \033[1;31mFailed to load dashboard")
        linex()
    
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

def view_all_orders():
    refresh_screen()
    print(f" {style} \033[1;32mLOADING ORDERS...")
    nice_loader("LOADING")
    
    status, response = api_request("GET", "/admin/orders")
    
    if status == 200 and response.get('success'):
        orders = response.get('orders', [])
        
        refresh_screen()
        print(f" {style} \033[1;32mALL BOOSTER ORDERS - Total: {len(orders)}")
        linex()
        
        if not orders:
            print(f" {style} \033[1;32mNo orders found.")
        else:
            for order in orders:
                status_colors = {
                    'pending': '\033[1;37m',
                    'processing': '\033[1;36m',
                    'completed': '\033[1;32m',
                    'cancelled': '\033[1;31m',
                    'refunded': '\033[1;35m'
                }
                status_color = status_colors.get(order['status'], '\033[1;37m')
                status_display = f"{status_color}[{order['status'].upper()}]\033[1;37m"
                
                print(f"\033[1;37m[{order['orderId']}] {status_display}")
                print(f"    Customer: \033[1;32m{order['customerName']}")
                print(f"    Post: \033[1;37m{order['postLink'][:50] + '...' if len(order['postLink']) > 50 else order['postLink']}")
                print(f"    Quantity: \033[1;37m{order['quantity']} \033[1;37m| Amount: \033[1;32m₱{order['amount']}")
                print(f"    Progress: \033[1;32m{order['currentCount']}\033[1;37m/\033[1;37m{order['quantity']} \033[1;37m({order['remainingCount']} remaining)")
                print(f"    Created: \033[1;37m{order['createdAt']}")
                if order.get('notes'):
                    print(f"    Notes: \033[1;37m{order['notes']}")
                linex()
    else:
        print(f" {stylee} \033[1;31mFailed to load orders")
        linex()
    
    input(f"\n {style} \033[1;32mPRESS ENTER TO CONTINUE")

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
                print(f" {stylee} \033[1;31mIncorrect post link!")
                return None
    except Exception as e:
        print(f" {stylee} \033[1;31mFailed to get post ID: {e}")
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
