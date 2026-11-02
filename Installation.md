# Installation Guide

This document covers downloading, installing, and verifying Python, along with solutions to common installation problems.

---

## 1. Installation Steps

### Windows

1. Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click **Download Python 3.x.x** (the latest stable version is shown automatically).
3. Run the downloaded `.exe` installer.
4. **Important:** On the first installer screen, check the box **"Add python.exe to PATH"** before proceeding.
5. Click **Install Now** and wait for the installation to complete.
6. Click **Close** once you see the "Setup was successful" message.

<!-- After taking your screenshot, save it as Images/windows_installer.png and uncomment the next line -->
<!-- ![Windows installer with Add python.exe to PATH checked](Images/windows_installer.png) -->

### macOS

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/) and download the macOS installer (`.pkg` file).
2. Open the downloaded `.pkg` file.
3. Follow the on-screen instructions in the installation wizard.
4. Enter your macOS account password if prompted.
5. Click **Close** once installation finishes.

Alternatively, using [Homebrew](https://brew.sh/):
```bash
brew install python3
```

### Linux (Debian/Ubuntu-based)

Most Linux distributions come with Python pre-installed. To install or update it manually:
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

### Linux (Fedora/RHEL-based)
```bash
sudo dnf install python3 python3-pip -y
```

---

## 2. Verification Steps

After installation, confirm Python was installed correctly.

### Step 1: Check the Python Version

Open a terminal (Command Prompt, PowerShell, or Terminal app) and run:
```bash
python --version
```
or, on some systems:
```bash
python3 --version
```
Expected output:
```
Python 3.x.x
```

### Step 2: Check pip (Python's Package Manager)
```bash
pip --version
```
Expected output should show the pip version along with the Python version it's linked to.

### Step 3: Run a Test Script

Create a file named `hello.py` with the following content:
```python
print("Python installation verified successfully!")
```
Run it:
```bash
python hello.py
```
If the message prints without errors, Python is correctly installed.

<!-- After taking your screenshot, save it as Images/verify_version.png and uncomment the next line -->
<!-- ![Terminal showing python --version and hello.py output](Images/verify_version.png) -->

---

## 3. Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| `'python' is not recognized as an internal or external command` (Windows) | Python was not added to PATH | Reinstall Python and check "Add python.exe to PATH", or manually add the Python install directory to the system PATH |
| `command not found: python` (macOS/Linux) | System uses `python3` instead of `python` | Use `python3` and `pip3` instead, or create an alias |
| Installation freezes or fails midway | Antivirus/firewall interference or insufficient permissions | Temporarily disable antivirus, run the installer as Administrator/root, or free up disk space |
| `pip` not recognized | pip was not installed with Python | Run `python -m ensurepip --upgrade` |
| Permission denied errors on Linux/macOS | Installing without proper privileges | Use `sudo` for system-wide installation, or install in a virtual environment instead |
| Multiple Python versions conflict | Old versions still present on the system | Use `py -0` (Windows) or `which -a python3` (macOS/Linux) to identify versions, and update PATH priority accordingly |

### General Tips
- Always download installers only from the official site: [python.org](https://www.python.org)
- Restart your terminal (or computer) after installation if commands aren't recognized
- Consider using a virtual environment (`python -m venv myenv`) to avoid conflicts between projects

---

Continue to **FAQ.md** for frequently asked questions about Python installation.
