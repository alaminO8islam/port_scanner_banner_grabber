# 🔍 Port Scanner & Banner Grabber

A command-line network security tool that scans for open ports and extracts service banners from remote hosts. Built with Python, this utility helps identify running services, potential vulnerabilities, and provides insights for ethical hacking and penetration testing tasks.

---

## 🛠️ Tech Stack

| Language | Libraries | Network | IDE |
|----------|-----------|---------|-----|
| <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" height="28"> | <img src="https://img.shields.io/badge/socket-internal-lightgrey?style=for-the-badge" height="28"> | <img src="https://img.shields.io/badge/TCP%20Sockets-005f73?style=for-the-badge" height="28"> | <img src="https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" height="28"> |

---

## 📂 Project Structure

```
port_scanner_banner_grabber/
├── scanner/
│   ├── __init__.py
│   ├── port_scanner.py         # Core logic for port scanning
│   ├── banner_grabber.py       # Grabs service banners after scan
│   └── utils.py                # IP/Port validation, formatting, helpers
│
├── main.py                     # Entry point for CLI execution
├── README.md
├── LICENSE
├── .gitignore
└── requirements.txt
```

---

## 🚀 Features

- ✅ Scan a range of ports on a target IP/host
- ✅ Extract service banners from open ports
- ✅ Clean terminal-based interface
- ✅ Modular code for future extension
- ✅ Zero external dependencies (built-in `socket`)

---

## 📦 Installation

Make sure you have Python 3.6+ installed.

```bash
git clone https://github.com/alaminO8islam/port_scanner_banner_grabber.git
cd port_scanner_banner_grabber
python main.py
```

--- 

## 🧪 Usage

python main.py 

Then input:

🔹 Target IP or Hostname

🔹 Starting Port

🔹 Ending Port

You’ll receive:

✅ List of open ports

✅ Detected service banners

---

## 🔐 Disclaimer

This tool is intended for educational and authorized penetration testing only. Never use it on networks you don’t own or don’t have explicit permission to scan.

---

## 📜 License

This project is licensed under the MIT License.


