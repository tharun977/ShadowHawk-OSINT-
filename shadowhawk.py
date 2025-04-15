import json
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor

def load_sites():
    with open("sites.json", "r") as f:
        return json.load(f)

def check_username(site, url_template, username):
    url = url_template.format(username)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                return f"[+] Found on {site}: {url}"
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return f"[-] Not found on {site}"
    except Exception:
        return f"[!] Error checking {site}"
    return f"[-] Not found on {site}"

def search_all(username):
    results = []
    sites = load_sites()
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(check_username, site, url, username)
            for site, url in sites.items()
        ]
        for future in futures:
            results.append(future.result())
    return results

if __name__ == "__main__":
    username = input("Enter username to search: ").strip()
    print(f"\n🔍 Searching for '{username}'...\n")
    for result in search_all(username):
        print(result)
    print("\n🔍 Search completed.")
