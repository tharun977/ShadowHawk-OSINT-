import json
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor
import csv
import os
from datetime import datetime
import logging
import re

# === Config ===
OUTPUT_DIR = "output"
LOG_FILE = "shadowhawk.log"

# === Logger Setup ===
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

# === ANSI Colors ===
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def load_sites():
    with open("sites.json", "r") as f:
        return json.load(f)

def check_username(site, url_template, username, proxy=None):
    url = url_template.format(username)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        if proxy:
            proxy_handler = urllib.request.ProxyHandler({'http': proxy, 'https': proxy})
            opener = urllib.request.build_opener(proxy_handler)
            urllib.request.install_opener(opener)

        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                msg = f"[+] Found on {site}: {url}"
                print(GREEN + msg + RESET)
                logging.info(msg)
                return (site, url, "Found")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            msg = f"[-] Not found on {site}"
            print(RED + msg + RESET)
            return (site, url, "Not Found")
    except Exception as e:
        msg = f"[!] Error checking {site}"
        print(YELLOW + msg + RESET)
        logging.warning(f"{msg}: {e}")
        return (site, url, "Error")
    
    return (site, url, "Not Found")

def search_all(username, proxy=None):
    results = []
    sites = load_sites()
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(check_username, site, url, username, proxy)
            for site, url in sites.items()
        ]
        for future in futures:
            results.append(future.result())
    return results

def extract_emails_and_phones(text):
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    phones = re.findall(r"\+?\d[\d\s\-\(\)]{7,}\d", text)
    return emails, phones

def save_results(results):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    txt_file = os.path.join(OUTPUT_DIR, f"results_{timestamp}.txt")
    csv_file = os.path.join(OUTPUT_DIR, f"results_{timestamp}.csv")

    with open(txt_file, "w") as f:
        for site, url, status in results:
            f.write(f"{site}: {url} - {status}\n")

    with open(csv_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Site", "URL", "Status"])
        writer.writerows(results)

    print(CYAN + f"\n[✓] Results saved to {txt_file} and {csv_file}" + RESET)

if __name__ == "__main__":
    mode = input("1. Username Scan\n2. Email/Phone Extract\nChoose option (1/2): ").strip()
    if mode == "1":
        # old username flow
        username = input("Enter username: ").strip()
        proxy = input("Use proxy? (leave blank if none): ").strip() or None
        results = search_all(username, proxy)
        save_results(results)
    elif mode == "2":
        sample = input("Paste text to scan:\n")
        emails, phones = extract_emails_and_phones(sample)
        print("\n📧 Emails found:", emails)
        print("📱 Phone numbers found:", phones)

# === Main Runner ===
if __name__ == "__main__":
    print(CYAN + "\n🕵️  ShadowHawk OSINT Scanner" + RESET)
    username = input("🔎 Enter username to search: ").strip()
    proxy_input = input("🌐 Use proxy? (e.g. http://127.0.0.1:9050 or leave blank): ").strip()
    proxy = proxy_input if proxy_input else None

    print(f"\nSearching for '{username}'...\n")
    results = search_all(username, proxy)
    save_results(results)
    print(GREEN + "\n[✓] Search completed!" + RESET)
    print(CYAN + "🦅 ShadowHawk - Stay Safe!" + RESET)

