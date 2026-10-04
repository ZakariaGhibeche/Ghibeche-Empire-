#!/usr/bin/env python3
"""
Project: Ghibeche-Empire
File: empire_main.py
Author: Commander Zakaria Ghibeche
Description: Centralized CLI Dashboard uniting Cryptography, Matrix effects,
             and Automated Infrastructure Intelligence into one master hub.
"""

import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("=" * 65)
    print("       🛡️  GHIBECHE-EMPIRE - CENTRAL COMMAND DASHBOARD  🛡️       ")
    print("       Commander: Zakaria Ghibeche | Elite Python Infrastructure ")
    print("=" * 65)

def main_menu():
    while True:
        clear_screen()
        banner()
        print("\n[!] SELECT OPERATIONAL MODULE:\n")
        print("  [1] 🔐 Ghibeche Crypt Engine (Encryption & Decryption)")
        print("  [2] 🌐 Empire Nexus Intelligence (Scan & Report Generator)")
        print("  [3] ⚡ Matrix Terminal Simulator")
        print("  [4] 📊 View Infrastructure Status")
        print("  [0] 🚪 Exit Empire Mainframe\n")
        
        choice = input("Empire-Core > Enter your choice (0-4): ").strip()
        
        if choice == '1':
            clear_screen()
            print("--- [ 1. GHIBECHE CRYPT ENGINE ] ---")
            msg = input("Enter text to process: ").strip()
            shift = int(input("Enter cryptographic shift key (e.g., 3): ") or 3)
            
            # Simple simulation of internal crypt engine logic
            encrypted = "".join([chr(ord(c) + shift) for c in msg])
            decrypted = "".join([chr(ord(c) - shift) for c in encrypted])
            
            print(f"\n[+] Raw Input: {msg}")
            print(f"[+] Encrypted: {encrypted}")
            print(f"[+] Decrypted: {decrypted}")
            input("\nPress Enter to return to main menu...")
            
        elif choice == '2':
            clear_screen()
            print("--- [ 2. EMPIRE NEXUS INTELLIGENCE SCANNER ] ---")
            os.system('python3 empire_nexus.py' if os.path.exists('empire_nexus.py') else 'python empire_nexus.py')
            input("\nPress Enter to return to main menu...")
            
        elif choice == '3':
            clear_screen()
            print("--- [ 3. MATRIX TERMINAL SIMULATOR ] ---")
            os.system('python3 ghibeche_matrix.py' if os.path.exists('ghibeche_matrix.py') else 'python ghibeche_matrix.py')
            input("\nPress Enter to return to main menu...")
            
        elif choice == '4':
            clear_screen()
            print("--- [ 4. INFRASTRUCTURE FILES STATUS ] ---")
            files = ["ghibeche_crypt.py", "ghibeche_matrix.py", "empire_nexus.py", "EMPIRE_REPORT.md", "README.md"]
            for f in files:
                status = "ONLINE [SECURE]" if os.path.exists(f) else "MISSING"
                print(f" * {f} ---> {status}")
            input("\nPress Enter to return to main menu...")
            
        elif choice == '0':
            print("\n[!] Shutting down Empire Mainframe. Stay secure, Commander.")
            sys.exit(0)
        else:
            print("\n[-] Invalid selection. Try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n[!] Force shutdown initiated by Commander.")
        sys.exit(0)
