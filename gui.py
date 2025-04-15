import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
from shadowhawk import search_all, save_results

def start_scan():
    username = username_entry.get().strip()
    proxy = proxy_entry.get().strip() or None

    result_display.delete(1.0, tk.END)
    result_display.insert(tk.END, f"Scanning '{username}'...\n")

    def threaded_scan():
        results = search_all(username, proxy)
        for site, url, status in results:
            result_display.insert(tk.END, f"{status}: {site} -> {url}\n")
        save_results(results)
        result_display.insert(tk.END, "\nScan complete. Results saved.")

    threading.Thread(target=threaded_scan).start()

root = tk.Tk()
root.title("ShadowHawk OSINT")
root.geometry("600x400")

ttk.Label(root, text="Username:").pack(pady=5)
username_entry = ttk.Entry(root, width=40)
username_entry.pack()

ttk.Label(root, text="Proxy (optional):").pack(pady=5)
proxy_entry = ttk.Entry(root, width=40)
proxy_entry.pack()

ttk.Button(root, text="Start Scan", command=start_scan).pack(pady=10)

result_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15)
result_display.pack(fill=tk.BOTH, expand=True)

root.mainloop()
