# 🛡️ Apex-Sentinel | Zero-Dependency Security Scanner

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Architecture](https://img.shields.io/badge/Architecture-Zero--Dependency-success.svg)](#)

**Apex-Sentinel** is a lightweight, zero-dependency Python security auditor designed to detect hardcoded secrets, sensitive credentials, private keys, and suspicious IP addresses/IoCs in source code repositories.

Built specifically for high-efficiency environments, CI/CD security pipelines, and mobile testing environments (Pydroid 3 / Termux).

---

## ✨ Features

- 🚀 **Zero Dependencies**: Runs instantly on standard Python 3.x without `pip install`.
- 🔐 **Secret Leak Detection**: Identifies leaked GitHub Tokens, AWS Keys, Private Keys, and API credentials.
- 🌐 **Network IoC Scanner**: Flags exposed IP addresses and internal configuration endpoints.
- 📱 **Cross-Platform**: Seamless execution on Linux, Android (Pydroid 3/Termux), macOS, and Windows.
- 📊 **Clean Audit Logs**: Outputs structured, clear security assessment reports.

---

## ⚡ Quick Start

### Run locally or in Termux / Pydroid 3:

```bash
# Scan current directory
python apex_sentinel.py

# Scan a specific project path
python apex_sentinel.py /path/to/target_project
==================================================
 🛡️ APEX-SENTINEL SECURITY AUDIT REPORT 🛡️ 
==================================================

📁 File: ./empire_main.py
   ⚠️  [Line 95] Found IP Address: `sample_logs = "INFO: Auth success from 192.168.1.100"`
📁 File: ./apex_sentinel.py
   ⚠️  [Line 16] Found Private Key: `"Private Key": r"-----BEGIN PRIVATE KEY-----"`
