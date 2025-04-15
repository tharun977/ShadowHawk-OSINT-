from concurrent.futures import ThreadPoolExecutor
import requests

def check_username_on_site(url_template, username):
    url = url_template.format(username=username)
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return url
    except:
        pass
    return None

def scan_all_sites(sites, username):
    found = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_username_on_site, url, username) for url in sites]
        for future in futures:
            result = future.result()
            if result:
                found.append(result)
    return found
