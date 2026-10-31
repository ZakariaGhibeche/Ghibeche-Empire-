#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
====================================================================
 APEX-EMPIRE INTELLIGENCE SYSTEM - CORE ENGINE
 Developed by: Zakaria Ghibeche (Apex-Empire)
 Architecture: Native Python 3.x | Zero-Dependency Framework
====================================================================
"""

import os
import sys

# استدعاء أداة Apex-Sentinel إذا كانت موجودة في نفس المجلد
try:
    from apex_sentinel import scan_directory
except ImportError:
    scan_directory = None


def print_banner():
    banner = """
  █████╗ ██████╗ ███████╗██╗  ██╗    ███████╗███╗   ███╗██████╗ ██╗██████╗ ███╗   ██╗
 ██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝    ██╔════╝████╗ ████║██╔══██╗██║██╔══██╗████╗  ██║
 ███████║██████╔╝█████╗   ╚███╔╝     █████╗  ██╔████╔██║██████╔╝██║██████╔╝██╔██╗ ██║
 ██╔══██║██╔═══╝ ██╔══╝   ██╔██╗     ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║██╔══██╗██║╚██╗██║
 ██║  ██║██║     ███████╗██╔╝ ██╗    ███████╗██║ ╚═╝ ██║██║     ██║██║  ██║██║ ╚████║
 ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
 ------------------------------------------------------------------------------------
  Apex-Empire System Core v1.0 | Developer: Zakaria Ghibeche
  Zero-Dependency Ecosystem for Security Auditing & Code Intelligence
 ------------------------------------------------------------------------------------
"""
    print(banner)


def run_sentinel_module():
    print("\n[+] Launching Module: Apex-Sentinel (Security Auditor)...")
    target = input("[?] Enter target directory to scan (default: '.'): ").strip()
    if not target:
        target = "."

    if scan_directory:
        scan_directory(target)
    else:
        print("[!] Error: 'apex_sentinel.py' module not found in working directory.")


def show_system_status():
    print("\n[⚙️] Apex-Empire System Status:")
    print(f" - Operating System : {os.name} ({sys.platform})")
    print(f" - Python Version    : {sys.version.split()[0]}")
    print(f" - Working Directory : {os.getcwd()}")
    print(" - Loaded Modules    : Apex-Sentinel [Active]")


def main():
    while True:
        print_banner()
        print("Select an option from the Control Panel:")
        print(" [1] Run Apex-Sentinel (Code Security Audit)")
        print(" [2] Display System Information & Status")
        print(" [0] Exit Apex-Empire Engine")
        
        choice = input("\n[Apex-Empire] Select > ").strip()
        
        if choice == "1":
            run_sentinel_module()
            input("\nPress Enter to return to main menu...")
        elif choice == "2":
            show_system_status()
            input("\nPress Enter to return to main menu...")
        elif choice == "0":
            print("\n[+] Shutting down Apex-Empire System. Standby for next instruction, Commander!")
            sys.exit(0)
        else:
            print("\n[!] Invalid selection. Please try again.")


if __name__ == "__main__":
    main()
