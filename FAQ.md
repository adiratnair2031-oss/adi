# Frequently Asked Questions (FAQ)

**Q1: Which version of Python should I install — Python 2 or Python 3?**
A: Always install Python 3. Python 2 was officially discontinued (end-of-life) in January 2020 and no longer receives updates or security patches.

**Q2: Do I need to install pip separately?**
A: No. Since Python 3.4+, pip is bundled with the official installer by default. If it's missing, run `python -m ensurepip --upgrade`.

**Q3: What is the difference between `python` and `python3` commands?**
A: On Windows, `python` usually points to the installed version. On macOS and many Linux distributions, `python` may not exist or may point to an older system version, so `python3` is used to explicitly call Python 3.

**Q4: How do I install multiple versions of Python on the same machine?**
A: You can install multiple versions side by side. Use tools like `pyenv` (macOS/Linux) or the Python Launcher `py` (Windows) to switch between versions easily.

**Q5: Why should I use a virtual environment?**
A: A virtual environment (`venv`) isolates project dependencies, preventing version conflicts between different projects. Create one with:
```bash
python -m venv myenv
```

**Q6: How do I uninstall Python?**
A:
- **Windows:** Go to Settings → Apps → find Python → Uninstall
- **macOS:** Remove the Python framework from `/Library/Frameworks/Python.framework` (if installed via the official installer) or run `brew uninstall python3` (if installed via Homebrew)
- **Linux:** Use `sudo apt remove python3` or the equivalent for your package manager

**Q7: How do I update Python to the latest version?**
A: Download the latest installer from python.org and run it — it will typically upgrade the existing installation. On Linux, use your package manager's update commands.

**Q8: Is an internet connection required after installation?**
A: No, once installed, Python runs offline. An internet connection is only needed to download the installer and to install additional packages via pip.

**Q9: I installed Python, but my IDE (VS Code/PyCharm) doesn't detect it. What do I do?**
A: Restart the IDE, and manually set the Python interpreter path in the IDE settings to point to the installed Python executable.

---

# Conclusion

Installing Python is a straightforward process once you understand the requirements and steps involved. This documentation covered:

- The software and hardware prerequisites for installing Python
- Step-by-step installation instructions for Windows, macOS, and Linux
- How to verify that the installation completed successfully
- Common troubleshooting scenarios and their solutions
- Answers to frequently asked questions

With Python correctly installed and verified, you are now ready to start writing and running Python programs, installing additional libraries with pip, and exploring the wide ecosystem of tools built around the language.

For further learning, refer to the official Python documentation at [https://docs.python.org](https://docs.python.org).
