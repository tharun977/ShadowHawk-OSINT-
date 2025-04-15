
# 🦅 ShadowHawk - OSINT Username Recon Tool

ShadowHawk is a fast, lightweight, and privacy-focused Open Source Intelligence (OSINT) tool that searches for usernames across multiple platforms. Designed for ethical hackers, security researchers, and digital investigators, ShadowHawk helps you discover an individual's digital footprint in seconds — all while keeping you anonymous via proxy/Tor support.

> 💡 No external Python libraries required to run the basic version.

---

## ⚡ Features

| Feature                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| 🔍 Multi-platform search       | Searches usernames on major social platforms like GitHub, Twitter, Reddit, etc. |
| 💾 Offline mode                | Uses `sites.json` to operate fully offline.                                 |
| 🔐 Tor proxy support           | Route requests via Tor for anonymity (optional).                            |
| 🔄 Identity rotation           | Automatically rotate Tor identities to avoid rate limits.                   |
| 📊 Export support              | Outputs results as plain text, with support for JSON/CSV planned.           |
| ⚙️ No dependencies             | Works with just the Python standard library.                                |
| 💻 Planned UI                  | Minimal GUI planned using native Python (Tkinter).                          |
| 📱 Telegram Bot (planned)     | Chatbot-style OSINT interface on your mobile.                               |
| 📧 Email/Phone Recon (planned)| Extract info from emails/phone numbers using regex/APIs.                    |

---

## 📂 Project Structure

```
ShadowHawk-OSINT/
├── core/
│   ├── engine.py           # Core logic for username checks
│   ├── sites.py            # Site dictionary loader
│   ├── tor_rotation.py     # Optional Tor identity changer
├── shadowhawk.py           # Main CLI tool
├── sites.json              # List of platforms to scan
└── README.md
```

---

## 🚀 How to Use

### 🔧 1. Clone the Repo
```bash
git clone https://github.com/tharun977/ShadowHawk-OSINT-.git
cd ShadowHawk-OSINT-
```

---

### ▶️ 2. Run the Tool
```bash
python3 shadowhawk.py
```

You’ll be prompted to enter the username you want to scan.

---

## 🌐 Optional: Enable Tor Mode

> Requires [Tor](https://www.torproject.org/) and `stem` module.

### 🛠 Tor Setup Steps:
1. Install Tor and enable ControlPort in `torrc`:
    ```bash
    ControlPort 9051
    HashedControlPassword <your_password_hash>
    ```
2. Install the Python module:
    ```bash
    pip install stem
    ```

3. Use the `new_tor_identity()` function from `tor_rotation.py` to rotate IP.

4. Configure `proxy = "socks5h://127.0.0.1:9050"` in your requests (already integrated into tool).

---

## 🗂 Add More Platforms

To add or remove platforms, simply edit `sites.json`:

```json
{
  "GitHub": "https://github.com/{}",
  "Reddit": "https://www.reddit.com/user/{}",
  "Instagram": "https://www.instagram.com/{}"
}
```

> `{}` will be dynamically replaced with the username you're scanning.

---

## 🎯 Roadmap

- [x] Tor Identity Rotation
- [x] Proxy support via `socks5h`
- [x] Modular site loader
- [ ] Basic GUI with Tkinter
- [ ] Export results as CSV/JSON
- [ ] Email/phone OSINT
- [ ] Telegram bot support
- [ ] Dark Web user search (future research)

---

## ❗ Disclaimer

> This tool is intended for **ethical and educational purposes only**. Use responsibly and in accordance with your local laws and regulations.

---

## 📜 License

MIT License — feel free to use, modify, and contribute!


