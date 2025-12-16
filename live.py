#!/usr/bin/env python3
"""
Facebook Account Live Checker - m.facebook.com Method
Most reliable single method for checking if accounts are live
"""

import os
import sys
import time
import requests
import re

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


def extract_account_name(html_content):
    """
    Extract account name from HTML content using multiple patterns
    """
    try:
        # Pattern 1: From title tag
        if '<title>' in html_content:
            title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
            if title_match:
                title = title_match.group(1)
                # Clean the title
                if ' | Facebook' in title:
                    return title.split(' | Facebook')[0].strip()
                elif ' - Facebook' in title:
                    return title.split(' - Facebook')[0].strip()
                elif '|' in title:
                    return title.split('|')[0].strip()
                return title.strip()
        
        # Pattern 2: From meta tags
        meta_patterns = [
            r'<meta property="og:title" content="(.*?)"',
            r'<meta name="description" content="(.*?)"',
            r'<meta property="al:android:url" content=".*?u=(\d+)"'
        ]
        
        for pattern in meta_patterns:
            match = re.search(pattern, html_content, re.IGNORECASE)
            if match:
                name = match.group(1)
                if name and len(name) > 0 and 'facebook' not in name.lower():
                    return name.strip()
        
        # Pattern 3: From profile header
        header_patterns = [
            r'<h1[^>]*>(.*?)</h1>',
            r'<h3[^>]*class="[^"]*profpic[^"]*"[^>]*>(.*?)</h3>',
        ]
        
        for pattern in header_patterns:
            match = re.search(pattern, html_content, re.IGNORECASE | re.DOTALL)
            if match:
                name = match.group(1)
                # Clean HTML tags
                name = re.sub(r'<[^>]+>', '', name)
                name = name.strip()
                if name and len(name) > 0:
                    return name
        
        return "Unknown"
    except:
        return "Unknown"


def check_account_status(uid):
    """
    Check if Facebook account is live using m.facebook.com
    This is the most reliable single method
    
    Args:
        uid: Facebook User ID
        
    Returns:
        dict: Account status with detailed information
    """
    try:
        profile_url = f"https://m.facebook.com/{uid}"
        
        # Multiple user agents to try for better reliability
        user_agents = [
            'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Linux; Android 13; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
        ]
        
        for user_agent in user_agents:
            try:
                headers = {
                    'User-Agent': user_agent,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'none',
                    'Cache-Control': 'max-age=0',
                }
                
                # Make request with timeout
                response = requests.get(
                    profile_url, 
                    headers=headers, 
                    timeout=15, 
                    allow_redirects=True,
                    verify=True
                )
                
                # Check status code
                if response.status_code == 200:
                    content = response.text
                    content_lower = content.lower()
                    
                    # STRONG indicators that account is LIVE and ACTIVE
                    live_indicators = [
                        'timeline',
                        'timelineBody',
                        'profile_picture',
                        '<div id="objects_container"',
                        'about_section',
                        'Add Friend',
                        'Message',
                        'See Friendship',
                        'Friends',
                        'Photos',
                        'About',
                        'following',
                        'followers',
                        'Posts',
                        'profile_cover',
                        'cover photo',
                        'Intro',
                        'Lives in',
                        'Studied at',
                        'Works at',
                        'From',
                        'view_profile',
                        'profile/timeline',
                        'See More About',
                    ]
                    
                    # Count how many live indicators are present
                    live_count = sum(1 for indicator in live_indicators if indicator.lower() in content_lower)
                    
                    # DEAD/UNAVAILABLE indicators
                    dead_indicators = [
                        'content is currently unavailable',
                        'content isn\'t available',
                        'page you requested',
                        'this page isn\'t available',
                        'sorry, this page isn\'t available',
                        'this content isn\'t available right now',
                        'the link you followed may be broken',
                        'page not found',
                        'page isn\'t available',
                        'profile not available',
                        'account has been disabled',
                        'account has been deleted',
                        'user not found',
                    ]
                    
                    # Check for dead indicators
                    has_dead_indicator = any(indicator in content_lower for indicator in dead_indicators)
                    
                    # Check for redirect to error page
                    is_error_redirect = 'facebook.com/404' in response.url or '/unsupported' in response.url
                    
                    # Decision logic with confidence scoring
                    if has_dead_indicator or is_error_redirect:
                        return {
                            'status': 'not_live',
                            'confidence': 'high',
                            'reason': 'Profile page shows unavailable/deleted message',
                            'url': profile_url
                        }
                    
                    # If we have strong indicators of a live account
                    elif live_count >= 3:
                        account_name = extract_account_name(content)
                        
                        return {
                            'status': 'live',
                            'confidence': 'high' if live_count >= 5 else 'medium',
                            'name': account_name,
                            'indicators': live_count,
                            'url': profile_url,
                            'reason': f'Found {live_count} activity indicators on profile'
                        }
                    
                    # If we have some indicators but not many
                    elif live_count > 0:
                        account_name = extract_account_name(content)
                        
                        return {
                            'status': 'live',
                            'confidence': 'low',
                            'name': account_name,
                            'indicators': live_count,
                            'url': profile_url,
                            'reason': 'Profile exists but may be restricted or private'
                        }
                    
                    # Unclear - page loaded but no clear indicators
                    else:
                        return {
                            'status': 'unknown',
                            'confidence': 'low',
                            'reason': 'Profile page loaded but status unclear',
                            'url': profile_url
                        }
                
                # 404 means profile doesn't exist
                elif response.status_code == 404:
                    return {
                        'status': 'not_live',
                        'confidence': 'high',
                        'reason': 'Profile not found (HTTP 404)',
                        'url': profile_url
                    }
                
                # Other error codes
                elif response.status_code >= 400:
                    return {
                        'status': 'not_live',
                        'confidence': 'medium',
                        'reason': f'HTTP error {response.status_code}',
                        'url': profile_url
                    }
                
                # If this user agent worked, no need to try others
                if response.status_code == 200:
                    break
                    
            except requests.Timeout:
                # Try next user agent on timeout
                continue
            except requests.ConnectionError:
                # Try next user agent on connection error
                continue
        
        # If all user agents failed
        return {
            'status': 'error',
            'confidence': 'none',
            'reason': 'Could not connect to Facebook',
            'url': profile_url
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'confidence': 'none',
            'reason': f'Unexpected error: {str(e)}',
            'url': f'https://m.facebook.com/{uid}'
        }


def check_single_account(uid):
    """
    Check a single Facebook account
    """
    banner()
    print(f"{W}[{G}•{W}]{G} Checking UID: {V}{uid}{W}")
    linex()
    print(f"{W}[{V}•{W}]{V} Connecting to m.facebook.com...{W}")
    
    # Check account status
    result = check_account_status(uid)
    
    linex()
    
    # Display results based on status
    if result['status'] == 'live':
        print(f"\n{W}[{G}✓{W}]{G} ACCOUNT IS LIVE!{W}")
        print(f"{W}[{G}•{W}]{G} Confidence: {result['confidence'].upper()}{W}")
        print(f"{W}[{G}•{W}]{G} Account Name: {G}{result.get('name', 'Unknown')}{W}")
        print(f"{W}[{G}•{W}]{G} Profile URL: {G}{result['url']}{W}")
        print(f"{W}[{G}•{W}]{G} Indicators Found: {result.get('indicators', 0)}{W}")
        print(f"{W}[{G}•{W}]{G} Reason: {result.get('reason', '')}{W}")
        return 'live', result.get('name', 'Unknown')
        
    elif result['status'] == 'not_live':
        print(f"\n{W}[{R}✗{W}]{R} ACCOUNT IS NOT LIVE / DELETED!{W}")
        print(f"{W}[{R}•{W}]{R} Confidence: {result['confidence'].upper()}{W}")
        print(f"{W}[{R}•{W}]{R} Reason: {result.get('reason', 'Unknown')}{W}")
        return 'not_live', None
        
    elif result['status'] == 'unknown':
        print(f"\n{W}[{Y}?{W}]{Y} STATUS UNCLEAR{W}")
        print(f"{W}[{Y}•{W}]{Y} Confidence: {result['confidence'].upper()}{W}")
        print(f"{W}[{Y}•{W}]{Y} Reason: {result.get('reason', 'Unknown')}{W}")
        print(f"{W}[{Y}•{W}]{Y} Note: Account may be heavily restricted or private{W}")
        return 'unknown', None
        
    else:  # error
        print(f"\n{W}[{R}✗{W}]{R} ERROR CHECKING ACCOUNT{W}")
        print(f"{W}[{R}•{W}]{R} Reason: {result.get('reason', 'Unknown error')}{W}")
        return 'error', None


def check_from_file(file_path, output_file='/sdcard/live_accounts.txt', dead_file='/sdcard/dead_accounts.txt'):
    """
    Check multiple accounts from a file
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
    error_count = 0
    
    banner()
    print(f'{W}[{G}•{W}]{G} Total UIDs: {R}{total}{W}')
    print(f'{W}[{G}•{W}]{G} Input File: {R}{os.path.basename(file_path)}{W}')
    linex()
    print(f'{W}[{G}•{W}]{G} Starting check...{W}')
    linex()
    
    for i, uid in enumerate(uids, 1):
        try:
            print(f"\n{W}[{V}#{i}{W}]{V} Checking: {uid}{W}", end=' ')
            
            # Check account
            result = check_account_status(uid)
            
            # Process result
            if result['status'] == 'live':
                live_count += 1
                name = result.get('name', 'Unknown')
                confidence = result.get('confidence', 'unknown')
                
                print(f"{G}✓ LIVE ({confidence}){W}")
                
                # Save to live file
                try:
                    with open(output_file, 'a') as f:
                        f.write(f"{uid}|{name}|{confidence}\n")
                except:
                    pass
                    
            elif result['status'] == 'not_live':
                dead_count += 1
                print(f"{R}✗ DEAD{W}")
                
                # Save to dead file
                try:
                    with open(dead_file, 'a') as f:
                        f.write(f"{uid}\n")
                except:
                    pass
                    
            elif result['status'] == 'unknown':
                unknown_count += 1
                print(f"{Y}? UNKNOWN{W}")
                
            else:  # error
                error_count += 1
                print(f"{R}✗ ERROR{W}")
            
            # Show progress
            sys.stdout.write(
                f"\r{W}Progress: {i}/{total} | "
                f"{G}LIVE: {live_count}{W} | "
                f"{R}DEAD: {dead_count}{W} | "
                f"{Y}UNKNOWN: {unknown_count}{W} | "
                f"{R}ERROR: {error_count}{W}     "
            )
            sys.stdout.flush()
            
            # Delay to avoid rate limiting
            time.sleep(2)
            
        except KeyboardInterrupt:
            print(f"\n\n{R}[!] Process interrupted by user{W}")
            break
        except Exception as e:
            print(f"\n{R}[ERROR] {str(e)[:50]}{W}")
            error_count += 1
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
    print(f'{W}[{R}•{W}]{G} Errors {W}: {R}{error_count}{W}')
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
            
            status, name = check_single_account(uid)
            
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


if __name__ == "__main__"
