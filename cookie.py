#!/usr/bin/env python3
"""
Facebook Cookie Extractor - Enhanced Version
Extracts cookies from Facebook accounts using UID and password
Supports both file input and manual UID entry with multiple login methods
"""

import os
import sys
import time
import requests
import random
from pathlib import Path

# ANSI color codes
W = '\033[97m'  # White
G = '\033[92m'  # Green
R = '\033[91m'  # Red
V = '\033[1;34m'  # Blue
RESET = '\033[0m'  # Reset

# Global counters
ok_count = 0
cp_count = 0
loop = 0
total_ids = 0


def clear_screen():
    """Clear terminal screen based on platform."""
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    """Display the script banner."""
    clear_screen()
    print(f"""{G}
    ╔═══════════════════════════════════════╗
    ║   Facebook Cookie Extractor Tool     ║
    ║   Extract Cookies from UID|Password   ║
    ╚═══════════════════════════════════════╝
{W}─────────────────────────────────────────────{W}""")


def linex():
    """Print a separator line."""
    print(f"{W}─────────────────────────────────────────────{W}")


def check_write_permissions(path):
    """Check if we have write permissions for a file."""
    try:
        with open(path, 'a'):
            pass
        return True
    except IOError:
        return False


def generate_user_agent():
    """Generate random user agent."""
    android_versions = ['10', '11', '12', '13']
    chrome_versions = ['110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120']
    devices = ['SM-G991B', 'SM-G998B', 'SM-A525F', 'SM-A326B', 'Pixel 6', 'Pixel 7']
    
    android = random.choice(android_versions)
    chrome = random.choice(chrome_versions)
    device = random.choice(devices)
    
    return f'Mozilla/5.0 (Linux; Android {android}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome}.0.0.0 Mobile Safari/537.36'


def extract_cookies_method_1(uid, password):
    """
    Method 1: Using Facebook iOS API endpoint
    """
    try:
        ses = requests.Session()
        ses.headers.update({
            'User-Agent': 'FBAN/Orca-Android;FBAV/327.0.1.48;FBPN/com.facebook.orca;FBLC/en_US;FBCR/Vodafone;FBBV/67467545;FBMF/samsung;FBBD/samsung;FBDV/SM-G991B;FBSV/11.0.0;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,width=1080,height=2400};FB_FW/1;'
        })
        
        url = (
            f"https://b-api.facebook.com/method/auth.login?"
            f"access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1"
            f"&format=json&sdk_version=2&email={uid}"
            f"&locale=en_US&password={password}&sdk=ios"
            f"&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
        )
        
        res = ses.get(url, timeout=20)
        data = res.json()
        
        if 'session_cookies' in data:
            cookies_raw = data['session_cookies']
            coki = ";".join(f"{i['name']}={i['value']}" for i in cookies_raw)
            return True, coki, "iOS API"
        elif 'error_msg' in data:
            return False, data['error_msg'], "iOS API"
        else:
            return False, "Unknown error", "iOS API"
    except Exception as e:
        return False, str(e), "iOS API"


def extract_cookies_method_2(uid, password):
    """
    Method 2: Using Facebook Android API endpoint
    """
    try:
        ses = requests.Session()
        
        user_agent = generate_user_agent()
        
        ses.headers.update({
            'User-Agent': user_agent,
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        })
        
        # Alternative API endpoint
        url = (
            f"https://b-api.facebook.com/method/auth.login?"
            f"access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
            f"&format=json&sdk_version=2&email={uid}"
            f"&locale=en_US&password={password}&sdk=android"
            f"&generate_session_cookies=1"
        )
        
        res = ses.get(url, timeout=20)
        data = res.json()
        
        if 'session_cookies' in data:
            cookies_raw = data['session_cookies']
            coki = ";".join(f"{i['name']}={i['value']}" for i in cookies_raw)
            return True, coki, "Android API"
        elif 'error_msg' in data:
            return False, data['error_msg'], "Android API"
        else:
            return False, "Unknown error", "Android API"
    except Exception as e:
        return False, str(e), "Android API"


def extract_cookies_method_3(uid, password):
    """
    Method 3: Using mbasic.facebook.com login
    """
    try:
        ses = requests.Session()
        
        user_agent = generate_user_agent()
        
        ses.headers.update({
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Referer': 'https://mbasic.facebook.com/',
        })
        
        # Get login page
        login_page = ses.get('https://mbasic.facebook.com/login/', timeout=20)
        
        # Try to login
        login_data = {
            'email': uid,
            'pass': password,
            'login': 'Log In'
        }
        
        login_response = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100', 
                                 data=login_data, 
                                 allow_redirects=True,
                                 timeout=20)
        
        cookies = ses.cookies.get_dict()
        
        # Check if login successful
        if 'c_user' in cookies:
            coki = ";".join([f"{key}={value}" for key, value in cookies.items()])
            return True, coki, "mbasic"
        elif 'checkpoint' in cookies or 'checkpoint' in login_response.url:
            return False, "Account is in checkpoint", "mbasic"
        else:
            return False, "Invalid credentials", "mbasic"
    except Exception as e:
        return False, str(e), "mbasic"


def extract_cookies_from_credentials(uid, password, save_file='/sdcard/uid_pass_cookies.txt', cp_file='/sdcard/Cps_ex.txt'):
    """
    Extract cookies using multiple methods
    Tries different API endpoints until one works
    """
    methods = [
        ("Method 1 (iOS API)", extract_cookies_method_1),
        ("Method 2 (Android API)", extract_cookies_method_2),
        ("Method 3 (mbasic)", extract_cookies_method_3),
    ]
    
    print(f"{W}[{V}•{W}]{V} Trying multiple login methods...{W}")
    
    for method_name, method_func in methods:
        try:
            print(f"{W}[{V}•{W}]{V} Attempting {method_name}...{W}", end='', flush=True)
            
            success, result, api_used = method_func(uid, password)
            
            if success:
                print(f" {G}✓ Success!{W}")
                
                # Save to file
                try:
                    with open(save_file, 'a') as s:
                        s.write(f"{uid}|{password}|{result}\n")
                except:
                    pass
                
                return True, f"{G}[OK]{W} Cookies extracted successfully using {api_used}!", result
            else:
                print(f" {R}✗ Failed{W}")
                
                # If checkpoint, save to CP file
                if 'checkpoint' in result.lower():
                    try:
                        with open(cp_file, 'a') as c:
                            c.write(f"{uid}|{password}\n")
                    except:
                        pass
                    return False, f"{R}[CP]{W} Account is in checkpoint!", None
            
            time.sleep(1)  # Small delay between methods
            
        except Exception as e:
            print(f" {R}✗ Error{W}")
            continue
    
    return False, f"{R}[ERROR]{W} All login methods failed. Please verify credentials.", None


def extract_cookies_from_file(file_path, save_file='/sdcard/uid_pass_cookies.txt', cp_file='/sdcard/Cps_ex.txt'):
    """
    Extract cookies from a file containing UID|PASSWORD per line
    """
    global ok_count, cp_count, loop, total_ids
    
    # Reset counters
    ok_count = 0
    cp_count = 0
    loop = 0
    
    # Check write permissions
    if not check_write_permissions(save_file):
        print(f"{R}[ERROR] No write permissions for: {save_file}{W}")
        print(f"{R}Please check storage access permissions.{W}")
        return False
        
    if not check_write_permissions(cp_file):
        print(f"{R}[ERROR] No write permissions for: {cp_file}{W}")
        print(f"{R}Please check storage access permissions.{W}")
        return False
    
    # Check if input file exists
    if not os.path.exists(file_path):
        print(f"{R}[ERROR] File not found: {file_path}{W}")
        return False
    
    # Read and validate file
    try:
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"{R}[ERROR] Could not read file: {e}{W}")
        return False
    
    total_ids = len(lines)
    if total_ids == 0:
        print(f"{R}[ERROR] File is empty: {file_path}{W}")
        return False
    
    # Display info
    banner()
    print(f'{W}[{G}•{W}]{G} Total IDs    {W}: {R}{total_ids}{W}')
    print(f'{W}[{G}•{W}]{G} Input File   {W}: {R}{os.path.basename(file_path)}{W}')
    print(f'{W}[{G}•{W}]{G} Output File  {W}: {R}{os.path.basename(save_file)}{W}')
    print(f'{W}[{G}•{W}]{G} CP File      {W}: {R}{os.path.basename(cp_file)}{W}')
    linex()
    print(f'{W}[{G}•{W}]{G} Starting extraction...{W}')
    linex()
    
    # Process each line
    for line in lines:
        loop += 1
        
        try:
            # Validate format
            if '|' not in line:
                print(f"{R}[SKIP] Invalid format: {line[:50]}...{W}")
                continue
            
            # Parse UID and password
            parts = line.split('|', 1)
            uid = parts[0].strip()
            pw = parts[1].strip()
            
            if not uid or not pw:
                print(f"{R}[SKIP] Empty UID or password{W}")
                continue
            
            print(f"\n{W}[{V}•{W}]{V} Processing {loop}/{total_ids}: {uid}{W}")
            
            # Try multiple methods
            success, message, cookies = extract_cookies_from_credentials(uid, pw, save_file, cp_file)
            
            if success:
                print(f"{G}[OK] {uid}|{pw[:3]}{'*' * (len(pw)-3)}{W}")
                ok_count += 1
            else:
                if 'checkpoint' in message.lower():
                    print(f"{R}[CP] {uid}|{pw[:3]}{'*' * (len(pw)-3)}{W}")
                    cp_count += 1
                else:
                    print(f"{R}[FAIL] {uid}{W}")
            
            time.sleep(2)  # Delay between accounts
                
        except KeyboardInterrupt:
            print(f"\n\n{R}[!] Process interrupted by user{W}")
            break
            
        except Exception as e:
            print(f"\r{R}[ERROR] {str(e)[:50]}{W}")
            time.sleep(2)
            continue
    
    # Final summary
    print('\n')
    linex()
    print(f'{W}[{G}✓{W}]{G} Extraction completed!{W}')
    linex()
    print(f'{W}[{G}•{W}]{G} Total Processed {W}: {V}{loop}{W}')
    print(f'{W}[{G}•{W}]{G} Successful (OK) {W}: {G}{ok_count}{W}')
    print(f'{W}[{R}•{W}]{G} Checkpoint (CP) {W}: {R}{cp_count}{W}')
    linex()
    
    if ok_count > 0:
        print(f'{W}[{G}•{W}]{G} Results saved to: {save_file}{W}')
    if cp_count > 0:
        print(f'{W}[{R}•{W}]{G} Checkpoints saved to: {cp_file}{W}')
    
    return True


def manual_uid_entry():
    """Manual UID and password entry mode."""
    banner()
    print(f"{W}[{G}•{W}]{G} Manual UID Entry Mode{W}")
    print(f"{W}[{G}•{W}]{G} Enter UID and password to extract cookies{W}")
    linex()
    
    # Get UID
    uid = input(f'{W}[{G}•{W}]{G} Enter UID {W}: {G}').strip()
    if not uid:
        print(f"{R}[ERROR] UID cannot be empty!{W}")
        input(f"{W}[{G}•{W}]{G} Press Enter to continue... ")
        return
    
    # Get Password
    password = input(f'{W}[{G}•{W}]{G} Enter Password {W}: {G}').strip()
    if not password:
        print(f"{R}[ERROR] Password cannot be empty!{W}")
        input(f"{W}[{G}•{W}]{G} Press Enter to continue... ")
        return
    
    # Check write permissions
    save_file = '/sdcard/uid_pass_cookies.txt'
    cp_file = '/sdcard/Cps_ex.txt'
    
    if not check_write_permissions(save_file) or not check_write_permissions(cp_file):
        print(f"{R}[ERROR] No write permissions for /sdcard/{W}")
        print(f"{R}Please check storage access permissions.{W}")
        input(f"{W}[{G}•{W}]{G} Press Enter to continue... ")
        return
    
    # Extract cookies
    linex()
    print(f'{W}[{G}•{W}]{G} Extracting cookies...{W}')
    linex()
    
    success, message, cookies = extract_cookies_from_credentials(uid, password, save_file, cp_file)
    
    print(f"\n{message}")
    
    if success and cookies:
        print(f'\n{W}[{G}•{W}]{G} Cookies saved to: {save_file}{W}')
        print(f'\n{W}[{G}•{W}]{G} Extracted Cookies:{W}')
        linex()
        print(f'{G}{cookies}{W}')
        linex()
    else:
        print(f'\n{W}[{R}•{W}]{R} Failed to extract cookies{W}')
        print(f'{W}[{V}•{W}]{V} Tip: Make sure your UID and password are correct{W}')
        print(f'{W}[{V}•{W}]{V} Tip: Try logging in to Facebook manually first{W}')
    
    input(f"\n{W}[{G}•{W}]{G} Press Enter to continue... ")


def get_file_path():
    """Get file path from user with validation."""
    banner()
    print(f"{W}[{G}•{W}]{G} File Input Mode{W}")
    print(f"{W}[{G}•{W}]{G} Enter the path to your UID|PASSWORD file{W}")
    print(f"{W}[{G}•{W}]{G} Format: Each line should be UID|PASSWORD{W}")
    print(f"{W}[{G}•{W}]{G} Example: 100012345678|MyPassword123{W}")
    linex()
    
    file_path = input(f'{W}[{G}•{W}]{G} File path {W}: {G}').strip()
    
    # Remove quotes if present
    file_path = file_path.strip('"').strip("'")
    
    if not file_path:
        print(f"{R}[ERROR] File path cannot be empty!{W}")
        input(f"{W}[{G}•{W}]{G} Press Enter to continue... ")
        return None
    
    # Expand user path
    file_path = os.path.expanduser(file_path)
    
    if os.path.exists(file_path):
        return file_path
    else:
        print(f"{R}[ERROR] File not found: {file_path}{W}")
        input(f"{W}[{G}•{W}]{G} Press Enter to continue... ")
        return None


def main_menu():
    """Display main menu for cookie extraction."""
    while True:
        banner()
        print(f"{W}[{G}1{W}]{G} Extract from File (UID|PASSWORD per line){W}")
        print(f"{W}[{G}2{W}]{G} Manual UID Entry (Single extraction){W}")
        print(f"{W}[{R}0{W}]{R} Exit{W}")
        linex()
        
        choice = input(f'{W}[{G}•{W}]{G} Select option {W}: {G}').strip()
        
        if choice == '1':
            # File input mode
            file_path = get_file_path()
            if file_path:
                # Ask for custom output paths (optional)
                banner()
                print(f"{W}[{G}•{W}]{G} Use default output paths?{W}")
                print(f"{W}[{G}•{W}]{G} OK File: /sdcard/uid_pass_cookies.txt{W}")
                print(f"{W}[{G}•{W}]{G} CP File: /sdcard/Cps_ex.txt{W}")
                linex()
                
                use_default = input(f'{W}[{G}•{W}]{G} Use defaults? (y/n) {W}: {G}').strip().lower()
                
                if use_default == 'y':
                    save_file = '/sdcard/uid_pass_cookies.txt'
                    cp_file = '/sdcard/Cps_ex.txt'
                else:
                    save_file = input(f'{W}[{G}•{W}]{G} OK output file {W}: {G}').strip() or '/sdcard/uid_pass_cookies.txt'
                    cp_file = input(f'{W}[{G}•{W}]{G} CP output file {W}: {G}').strip() or '/sdcard/Cps_ex.txt'
                
                # Extract cookies
                success = extract_cookies_from_file(file_path, save_file, cp_file)
                
                if success:
                    print(f'{W}[{G}✓{W}]{G} Process completed successfully!{W}')
                else:
                    print(f'{W}[{R}✗{W}]{R} Process failed!{W}')
                
                linex()
                input(f'{W}[{G}•{W}]{G} Press Enter to continue... ')
        
        elif choice == '2':
            # Manual UID entry mode
            manual_uid_entry()
        
        elif choice == '0':
            print(f"\n{G}Thanks for using Cookie Extractor!{W}")
            sys.exit(0)
        
        else:
            print(f"{R}[ERROR] Invalid choice! Please select 1, 2, or 0.{W}")
            input(f"{W}[{G}•{W}]{G} Press Enter to continue... ")


def main():
    """Main function."""
    try:
        # Set terminal title
        sys.stdout.write('\x1b]2;Facebook Cookie Extractor\x07')
        
        # Show main menu
        main_menu()
        
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] Process interrupted by user{W}")
        sys.exit(0)
        
    except Exception as e:
        print(f"\n{R}[FATAL ERROR] {e}{W}")
        input(f"{W}[{G}•{W}]{G} Press Enter to exit... ")
        sys.exit(1)


if __name__ == "__main__":
    main()
