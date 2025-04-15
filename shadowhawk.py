import requests
import json
import argparse
from colorama import Fore, Style

def load_sites(file='sites.json'):
    with open(file, 'r') as f:
        return json.load(f)

def check_username(username, sites):
    print(f"\n{Fore.CYAN}🔍 Searching for username: {username}{Style.RESET_ALL}\n")
    for site, url in sites.items():
        full_url = url.format(username)
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200:
                print(f"{Fore.GREEN}[+] {site}: Found at {full_url}")
            elif response.status_code == 404:
                print(f"{Fore.RED}[-] {site}: Not found")
            else:
                print(f"{Fore.YELLOW}[?] {site}: Status {response.status_code}")
        except requests.RequestException as e:
            print(f"{Fore.MAGENTA}[!] Error checking {site}: {e}")

def main():
    parser = argparse.ArgumentParser(description="🕵️ ShadowHawk: OSINT tool to find usernames across the web.")
    parser.add_argument("username", help="Username to search for")
    args = parser.parse_args()

    sites = load_sites()
    check_username(args.username, sites)

if __name__ == "__main__":
    main()
