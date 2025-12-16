#!/usr/bin/env python3
"""
Facebook Account Live Checker
Checks if a Facebook account is live or not using UID
Verifies by checking profile picture status
"""

import os
import sys
import time
import requests

# ANSI color codes
W = '\033[97m'  # White
G = '\033[92m'  # Green
R = '\033[91m'  # Red
V = '\033[1;34m'  # Blue
Y = '\033[93m'  # Yellow
RESET = '\033[0m'  # Reset


def clear_screen():
    """Clear terminal screen based on platform."""
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    """Display the script banner."""
    clear_screen()
    print(f"""{G}
    ╔═══════════════════════════════════════╗
    ║  Facebook Account Live Checker Tool  ║
    ║      Check Account Status by UID     ║
    ╚═══════════════════════════════════════╝
{W}─────────────────────────────────────────────{W}""")


def linex():
    """Print a separator line."""
    print(f"{W}─────────────────────────────────────────────{W}")


def check_facebook_profile_picture(uid):
    """
    Check if a UID has a real profile picture using Facebook Graph API
    
    Args:
        uid: Facebook User ID
        
    Returns:
        str: "live" if account has real profile picture, "not_live" otherwise
    """
    pic_url = f"https://graph.facebook.com/{uid}/picture?type=normal"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36"
    }
    
    try:
        response = requests.get(pic_url, headers=headers, allow_redirects=False, timeout=10)
        
        if response.status_code == 302:
            redirect_url = response.headers.get("Location", "")
            
            # If redirect URL contains "scontent", it's a real profile picture
            if "scontent" in redirect_url:
                return "live"
            else:
                return "not_live"
        else:
            return "unknown"
            
    except requests.RequestException as e:
        return "error"


def check_account_via_api(uid):
    """
    Check account status via Facebook Graph API
    
    Args:
        uid: Facebook User ID
        
    Returns:
        dict: Account status information
    """
    try:
        # Try to get basic profile info
        api_url = f"https://graph.facebook.com/{uid}?fields=id,name&access_token=6628568379|c1e620fa708a1d5696fb991c1bde5662"
        
        response = requests.get(api_url, timeout=10)
        data = response.json()
        
        if 'id' in data:
            return {
                'status': 'live',
                'id': data.get('id'),
                'name': data.get('name', 'Unknown'),
                'method': 'API'
            }
        elif 'error' in data:
            error_msg = data['error'].get('message', 'Unknown error')
            if 'Unsupported get request' in error_msg or 'does not exist' in error_msg:
                return {
                    'status': 'not_live',
                    'error': error_msg,
                    'method': 'API'
                }
            else:
                return {
                    'status': 'unknown',
                    'error': error_msg,
                    'method': 'API'
                }
        else:
            return {
                'status': 'unknown',
                'method': 'API'
            }
    except Exception as e:
        return {
            'status': 'error',
            'error': str(e),
            'method': 'API'
        }


def check_single_account(uid):
    """
    Check a single Facebook account status using multiple methods
    
    Args:
        uid: Facebook User ID
    """
    banner()
    print(f"{W}[{G}•{W}]{G} Checking UID: {V}{uid}{W}")
    linex()
    
    # Method 1: Check profile picture
    print(f"{W}[{V}•{W}]{V} Method 1: Checking profile picture...{W}", end='', flush=True)
    pic_status = check_facebook_profile_picture(uid)
    
    if pic_status == "live":
        print(f" {G}✓ LIVE{W}")
        print(f"{W}[{G}•{W}]{G} Status: {G}Account is LIVE (has profile picture){W}")
    elif pic_status == "not_live":
        print(f" {R}✗ NOT LIVE{W}")
        print(f"{W}[{R}•{W}]{R} Status: Account may be inactive or default picture{W}")
    else:
        print(f" {Y}? UNKNOWN{W}")
    
    time.sleep(1)
    
    # Method 2: Check via API
    print(f"{W}[{V}•{W}]{V} Method 2: Checking via Graph API...{W}", end='', flush=True)
    api_result = check_account_via_api(uid)
    
    if api_result['status'] == 'live':
        print(f" {G}✓ LIVE{W}")
        print(f"{W}[{G}•{W}]{G} Name: {G}{api_result.get('name', 'Unknown')}{W}")
        print(f"{W}[{G}•{W}]{G} ID: {G}{api_result.get('id', uid)}{W}")
    elif api_result['status'] == 'not_live':
        print(f" {R}✗ NOT LIVE{W}")
        print(f"{W}[{R}•{W}]{R} Error: {api_result.get('error', 'Unknown')}{W}")
    else:
        print(f" {Y}? UNKNOWN{W}")
    
    linex()
    
    # Final verdict
    if pic_status == "live" or api_result['status'] == 'live':
        print(f"\n{W}[{G}✓{W}]{G} FINAL VERDICT: Account is LIVE!{W}")
        return "live"
    elif pic_status == "not_live" and api_result['status'] == 'not_live':
        print(f"\n{W}[{R}✗{W}]{R} FINAL VERDICT: Account is NOT LIVE!{W}")
        return "not_live"
    else:
        print(f"\n{W}[{Y}?{W}]{Y} FINAL VERDICT: Status UNKNOWN{W}")
        return "unknown"


def check_from_file(file_path, output_file='/sdcard/live_accounts.txt', dead_file='/sdcard/dead_accounts.txt'):
    """
    Check multiple accounts from a file
    
    Args:
        file_path: Path to file containing UIDs (one per line)
        output_file: Path to save live accounts
        dead_file: Path to save dead accounts
    """
    if not os.path.exists(file_path):
        print(f"{R}[ERROR] File not found: {file_path}{W}")
        return
    
    try:
        with open(file_path, 'r') as f:
            uids = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"{R}[ERROR] Could not read file: {e}{W}")
        return
    
    if not uids:
        print(f"{R}[ERROR] File is empty{W}")
        return
    
    total = len(uids)
    live_count = 0
    dead_count = 0
    unknown_count = 0
    
    banner()
    print(f'{W}[{G}•{W}]{G} Total UIDs: {R}{total}{W}')
    print(f'{W}[{G}•{W}]{G} Input File: {R}{os.path.basename(file_path)}{W}')
    linex()
    print(f'{W}[{G}•{W}]{G} Starting check...{W}')
    linex()
    
    for i, uid in enumerate(uids, 1):
        try:
            print(f"\n{W}[{V}•{W}]{V} Checking {i}/{total}: {uid}{W}")
            
            # Check profile picture
            pic_status = check_facebook_profile_picture(uid)
            
            # Check via API
            api_result = check_account_via_api(uid)
            
            # Determine final status
            if pic_status == "live" or api_result['status'] == 'live':
                status = "live"
                live_count += 1
                print(f"{G}[LIVE] {uid}{W}")
                
                # Save to live file
                try:
                    with open(output_file, 'a') as f:
                        name = api_result.get('name', 'Unknown')
                        f.write(f"{uid}|{name}\n")
                except:
                    pass
                    
            elif pic_status == "not_live" or api_result['status'] == 'not_live':
                status = "not_live"
                dead_count += 1
                print(f"{R}[DEAD] {uid}{W}")
                
                # Save to dead file
                try:
                    with open(dead_file, 'a') as f:
                        f.write(f"{uid}\n")
                except:
                    pass
            else:
                status = "unknown"
                unknown_count += 1
                print(f"{Y}[UNKNOWN] {uid}{W}")
            
            # Show progress
            sys.stdout.write(
                f"\r{W}Progress: {i}/{total} | "
                f"{G}LIVE: {live_count}{W} | "
                f"{R}DEAD: {dead_count}{W} | "
                f"{Y}UNKNOWN: {unknown_count}{W}  "
            )
            sys.stdout.flush()
            
            time.sleep(1)  # Delay to avoid rate limiting
            
        except KeyboardInterrupt:
            print(f"\n\n{R}[!] Process interrupted by user{W}")
            break
        except Exception as e:
            print(f"{R}[ERROR] {str(e)[:50]}{W}")
            continue
    
    # Final summary
    print('\n')
    linex()
    print(f'{W}[{G}✓{W}]{G} Check completed!{W}')
    linex()
    print(f'{W}[{G}•{W}]{G} Total Checked {W}: {V}{i}{W}')
    print(f'{W}[{G}•{W}]{G} Live Accounts {W}: {G}{live_count}{W}')
    print(f'{W}[{R}•{W}]{G} Dead Accounts {W}: {R}{dead_count}{W}')
    print(f'{W}[{Y}•{W}]{G} Unknown Status {W}: {Y}{unknown_count}{W}')
    linex()
    
    if live_count > 0:
        print(f'{W}[{G}•{W}]{G} Live accounts saved to: {output_file}{W}')
    if dead_count > 0:
        print(f'{W}[{R}•{W}]{G} Dead accounts saved to: {dead_file}{W}')


def main_menu():
    """Display main menu."""
    while True:
        banner()
        print(f"{W}[{G}1{W}]{G} Check Single Account (Manual UID Entry){W}")
        print(f"{W}[{G}2{W}]{G} Check Multiple Accounts (From File){W}")
        print(f"{W}[{R}0{W}]{R} Exit{W}")
        linex()
        
        choice = input(f'{W}[{G}•{W}]{G} Select option {W}: {G}').strip()
        
        if choice == '1':
            # Single account check
            banner()
            print(f"{W}[{G}•{W}]{G} Single Account Check{W}")
            linex()
            
            uid = input(f'{W}[{G}•{W}]{G} Enter UID {W}: {G}').strip()
            
            if not uid:
                print(f"{R}[ERROR] UID cannot be empty!{W}")
                input(f"{W}[{G}•{W}]{G} Press Enter to continue... ")
                continue
            
            status = check_single_account(uid)
            
            input(f"\n{W}[{G}•{W}]{G} Press Enter to continue... ")
        
        elif choice == '2':
            # Multiple accounts check
            banner()
            print(f"{W}[{G}•{W}]{G} Multiple Accounts Check{W}")
            print(f"{W}[{G}•{W}]{G} File should contain one UID per line{W}")
            linex()
            
            file_path = input(f'{W}[{G}•{W}]{G} Enter file path {W}: {G}').strip()
            
            # Remove quotes if present
            file_path = file_path.strip('"').strip("'")
            
            if not file_path:
                print(f"{R}[ERROR] File path cannot be empty!{W}")
                input(f"{W}[{G}•{W}]{G} Press Enter to continue... ")
                continue
            
            # Expand user path
            file_path = os.path.expanduser(file_path)
            
            # Ask for custom output paths
            linex()
            use_default = input(f'{W}[{G}•{W}]{G} Use default output paths? (y/n) {W}: {G}').strip().lower()
            
            if use_default == 'y':
                output_file = '/sdcard/live_accounts.txt'
                dead_file = '/sdcard/dead_accounts.txt'
            else:
                output_file = input(f'{W}[{G}•{W}]{G} Live accounts file {W}: {G}').strip() or '/sdcard/live_accounts.txt'
                dead_file = input(f'{W}[{G}•{W}]{G} Dead accounts file {W}: {G}').strip() or '/sdcard/dead_accounts.txt'
            
            check_from_file(file_path, output_file, dead_file)
            
            input(f"\n{W}[{G}•{W}]{G} Press Enter to continue... ")
        
        elif choice == '0':
            print(f"\n{G}Thanks for using Account Checker!{W}")
            sys.exit(0)
        
        else:
            print(f"{R}[ERROR] Invalid choice! Please select 1, 2, or 0.{W}")
            input(f"{W}[{G}•{W}]{G} Press Enter to continue... ")


def main():
    """Main function."""
    try:
        # Set terminal title
        sys.stdout.write('\x1b]2;Facebook Account Checker\x07')
        
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
