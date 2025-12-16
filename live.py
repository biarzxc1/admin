#!/usr/bin/env python3
"""
Facebook Account Live Checker - Enhanced Version
Checks if a Facebook account is truly live and active
Uses multiple reliable verification methods
"""

import os
import sys
import time
import requests
import json

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


def check_via_graph_api_v1(uid):
    """
    Method 1: Check via Facebook Graph API with public access token
    This checks if the account exists and is accessible
    """
    try:
        # Multiple access tokens to try
        access_tokens = [
            "6628568379|c1e620fa708a1d5696fb991c1bde5662",
            "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            "2429830407|84bf0e08f3c83728e91f13c708178f8e"
        ]
        
        for token in access_tokens:
            try:
                api_url = f"https://graph.facebook.com/{uid}?fields=id,name,link&access_token={token}"
                response = requests.get(api_url, timeout=10)
                data = response.json()
                
                if 'id' in data and 'name' in data:
                    return {
                        'status': 'live',
                        'id': data['id'],
                        'name': data['name'],
                        'link': data.get('link', f'https://facebook.com/{uid}'),
                        'method': 'Graph API v1'
                    }
                elif 'error' in data:
                    error_code = data['error'].get('code')
                    error_msg = data['error'].get('message', '')
                    
                    # Check specific error codes
                    if error_code == 803:  # Account doesn't exist
                        return {
                            'status': 'not_live',
                            'error': 'Account does not exist',
                            'method': 'Graph API v1'
                        }
                    elif 'Unsupported get request' in error_msg:
                        return {
                            'status': 'not_live',
                            'error': 'Account not found or deleted',
                            'method': 'Graph API v1'
                        }
                    elif error_code == 100:  # Invalid parameter
                        return {
                            'status': 'not_live',
                            'error': 'Invalid UID',
                            'method': 'Graph API v1'
                        }
                    # Try next token
                    continue
            except:
                continue
        
        return {
            'status': 'unknown',
            'error': 'Could not verify with available tokens',
            'method': 'Graph API v1'
        }
    except Exception as e:
        return {
            'status': 'error',
            'error': str(e),
            'method': 'Graph API v1'
        }


def check_via_profile_url(uid):
    """
    Method 2: Check by accessing the profile URL directly
    This verifies if the profile page loads successfully
    """
    try:
        profile_url = f"https://mbasic.facebook.com/{uid}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }
        
        response = requests.get(profile_url, headers=headers, timeout=10, allow_redirects=True)
        
        # Check response
        if response.status_code == 200:
            content = response.text.lower()
            
            # Check for indicators that account exists
            if 'timeline' in content or 'about' in content or 'photos' in content:
                # Extract name if possible
                name = "Unknown"
                if '<title>' in response.text:
                    try:
                        title = response.text.split('<title>')[1].split('</title>')[0]
                        if '|' in title:
                            name = title.split('|')[0].strip()
                        else:
                            name = title.strip()
                    except:
                        pass
                
                return {
                    'status': 'live',
                    'name': name,
                    'method': 'Profile URL'
                }
            
            # Check for indicators that account doesn't exist or is unavailable
            elif 'content not found' in content or 'page not found' in content or 'this page isn' in content:
                return {
                    'status': 'not_live',
                    'error': 'Profile not found',
                    'method': 'Profile URL'
                }
            else:
                return {
                    'status': 'unknown',
                    'error': 'Could not determine status',
                    'method': 'Profile URL'
                }
        elif response.status_code == 404:
            return {
                'status': 'not_live',
                'error': 'Profile not found (404)',
                'method': 'Profile URL'
            }
        else:
            return {
                'status': 'unknown',
                'error': f'Unexpected status code: {response.status_code}',
                'method': 'Profile URL'
            }
    except Exception as e:
        return {
            'status': 'error',
            'error': str(e),
            'method': 'Profile URL'
        }


def check_via_search(uid):
    """
    Method 3: Check if account appears in Facebook search results
    """
    try:
        search_url = f"https://mbasic.facebook.com/search/people/?q={uid}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }
        
        response = requests.get(search_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            content = response.text
            
            # Check if UID appears in search results
            if uid in content and ('profile' in content.lower() or 'timeline' in content.lower()):
                return {
                    'status': 'live',
                    'method': 'Search'
                }
            else:
                return {
                    'status': 'not_live',
                    'error': 'Not found in search',
                    'method': 'Search'
                }
        else:
            return {
                'status': 'unknown',
                'method': 'Search'
            }
    except Exception as e:
        return {
            'status': 'error',
            'error': str(e),
            'method': 'Search'
        }


def check_via_mobile_profile(uid):
    """
    Method 4: Check via mobile Facebook URL (m.facebook.com)
    Most reliable method for checking if account exists
    """
    try:
        profile_url = f"https://m.facebook.com/{uid}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://m.facebook.com/',
        }
        
        response = requests.get(profile_url, headers=headers, timeout=10, allow_redirects=True)
        
        if response.status_code == 200:
            content = response.text.lower()
            
            # Strong indicators that account exists and is live
            if any(indicator in content for indicator in ['timeline', 'profile', 'about', 'photos', 'friends', 'add friend', 'message']):
                # Try to extract name
                name = "Unknown"
                try:
                    if '<title>' in response.text:
                        title = response.text.split('<title>')[1].split('</title>')[0]
                        # Clean up the name
                        if ' | Facebook' in title:
                            name = title.split(' | Facebook')[0].strip()
                        elif '|' in title:
                            name = title.split('|')[0].strip()
                        else:
                            name = title.strip()
                except:
                    pass
                
                return {
                    'status': 'live',
                    'name': name,
                    'url': profile_url,
                    'method': 'Mobile Profile'
                }
            
            # Indicators that account doesn't exist
            elif any(indicator in content for indicator in ['content is currently unavailable', 'page you requested', 'this content isn', 'sorry, this page']):
                return {
                    'status': 'not_live',
                    'error': 'Profile not available',
                    'method': 'Mobile Profile'
                }
        elif response.status_code == 404:
            return {
                'status': 'not_live',
                'error': 'Profile not found (404)',
                'method': 'Mobile Profile'
            }
        
        return {
            'status': 'unknown',
            'method': 'Mobile Profile'
        }
    except Exception as e:
        return {
            'status': 'error',
            'error': str(e),
            'method': 'Mobile Profile'
        }


def check_single_account(uid):
    """
    Check a single Facebook account using all available methods
    """
    banner()
    print(f"{W}[{G}•{W}]{G} Checking UID: {V}{uid}{W}")
    linex()
    
    results = []
    live_count = 0
    dead_count = 0
    account_name = "Unknown"
    
    # Method 1: Mobile Profile (Most reliable)
    print(f"{W}[{V}•{W}]{V} Method 1: Checking mobile profile...{W}", end='', flush=True)
    result1 = check_via_mobile_profile(uid)
    results.append(result1)
    
    if result1['status'] == 'live':
        print(f" {G}✓ LIVE{W}")
        live_count += 1
        account_name = result1.get('name', 'Unknown')
        print(f"{W}[{G}•{W}]{G} Name: {G}{account_name}{W}")
    elif result1['status'] == 'not_live':
        print(f" {R}✗ NOT LIVE{W}")
        dead_count += 1
        print(f"{W}[{R}•{W}]{R} Error: {result1.get('error', 'Unknown')}{W}")
    else:
        print(f" {Y}? UNKNOWN{W}")
    
    time.sleep(1)
    
    # Method 2: Profile URL Check
    print(f"{W}[{V}•{W}]{V} Method 2: Checking profile URL...{W}", end='', flush=True)
    result2 = check_via_profile_url(uid)
    results.append(result2)
    
    if result2['status'] == 'live':
        print(f" {G}✓ LIVE{W}")
        live_count += 1
        if account_name == "Unknown":
            account_name = result2.get('name', 'Unknown')
    elif result2['status'] == 'not_live':
        print(f" {R}✗ NOT LIVE{W}")
        dead_count += 1
    else:
        print(f" {Y}? UNKNOWN{W}")
    
    time.sleep(1)
    
    # Method 3: Graph API
    print(f"{W}[{V}•{W}]{V} Method 3: Checking via Graph API...{W}", end='', flush=True)
    result3 = check_via_graph_api_v1(uid)
    results.append(result3)
    
    if result3['status'] == 'live':
        print(f" {G}✓ LIVE{W}")
        live_count += 1
        account_name = result3.get('name', account_name)
        print(f"{W}[{G}•{W}]{G} Name: {G}{result3.get('name', 'Unknown')}{W}")
        print(f"{W}[{G}•{W}]{G} Link: {G}{result3.get('link', '')}{W}")
    elif result3['status'] == 'not_live':
        print(f" {R}✗ NOT LIVE{W}")
        dead_count += 1
    else:
        print(f" {Y}? UNKNOWN{W}")
    
    linex()
    
    # Final verdict based on majority
    if live_count >= 2:
        print(f"\n{W}[{G}✓{W}]{G} FINAL VERDICT: Account is LIVE!{W}")
        print(f"{W}[{G}•{W}]{G} Account Name: {G}{account_name}{W}")
        print(f"{W}[{G}•{W}]{G} Profile URL: {G}https://facebook.com/{uid}{W}")
        return "live", account_name
    elif dead_count >= 2:
        print(f"\n{W}[{R}✗{W}]{R} FINAL VERDICT: Account is NOT LIVE or DELETED!{W}")
        return "not_live", None
    else:
        print(f"\n{W}[{Y}?{W}]{Y} FINAL VERDICT: Status UNCLEAR{W}")
        print(f"{W}[{Y}•{W}]{Y} Results are mixed. Account might be restricted or private.{W}")
        return "unknown", None


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
    
    banner()
    print(f'{W}[{G}•{W}]{G} Total UIDs: {R}{total}{W}')
    print(f'{W}[{G}•{W}]{G} Input File: {R}{os.path.basename(file_path)}{W}')
    linex()
    print(f'{W}[{G}•{W}]{G} Starting check...{W}')
    linex()
    
    for i, uid in enumerate(uids, 1):
        try:
            print(f"\n{W}[{V}•{W}]{V} Checking {i}/{total}: {uid}{W}")
            
            # Use all methods for accurate results
            results = []
            
            # Mobile profile check
            result1 = check_via_mobile_profile(uid)
            results.append(result1)
            
            time.sleep(0.5)
            
            # Profile URL check
            result2 = check_via_profile_url(uid)
            results.append(result2)
            
            time.sleep(0.5)
            
            # Graph API check
            result3 = check_via_graph_api_v1(uid)
            results.append(result3)
            
            # Count votes
            live_votes = sum(1 for r in results if r['status'] == 'live')
            dead_votes = sum(1 for r in results if r['status'] == 'not_live')
            
            # Get account name if available
            account_name = "Unknown"
            for r in results:
                if r['status'] == 'live' and 'name' in r and r['name'] != "Unknown":
                    account_name = r['name']
                    break
            
            # Determine final status (majority vote)
            if live_votes >= 2:
                status = "live"
                live_count += 1
                print(f"{G}[LIVE] {uid} - {account_name}{W}")
                
                # Save to live file
                try:
                    with open(output_file, 'a') as f:
                        f.write(f"{uid}|{account_name}\n")
                except:
                    pass
                    
            elif dead_votes >= 2:
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
            
            time.sleep(2)  # Delay to avoid rate limiting
            
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


if __name__ == "__main__":
    main()
