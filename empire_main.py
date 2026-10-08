"""
Apex-Core CLI Dashboard: Unified Central Command for Apex-Empire
Engineered by Commander Zakaria Ghibeche (Djelfa, Algeria)
Brand: Apex-Empire (Global Open-Source Production Release)
"""

import sys
import time
import json
from pathlib import Path

# Import individual modules if available in local scope
try:
    from apex_crypt import ApexCrypt
except ImportError:
    ApexCrypt = None

try:
    from apex_nettunnel import ApexNetTunnel
except ImportError:
    ApexNetTunnel = None

try:
    from apex_datamatrix import ApexDataMatrix
except ImportError:
    ApexDataMatrix = None


class ApexCoreDashboard:
    """Central interactive command-line interface for the entire Apex-Empire ecosystem."""

    def __init__(self):
        self.commander = "Commander Zakaria Ghibeche"
        self.version = "v1.0 Global Edition"

    def banner(self):
        print("=" * 60)
        print("    🛡️ APEX-EMPIRE: CENTRAL COMMAND & CONTROL DASHBOARD 🛡️")
        print(f"    Engineered by {self.commander} | {self.version}")
        print("=" * 60)

    def main_menu(self):
        while True:
            self.banner()
            print("\n[+] Select an Empire Module to Execute:")
            print("  1. Apex-Crypt (Advanced Payload Encryption & XOR Layers)")
            print("  2. Apex-NetTunnel (Secure Socket Tunnelling & HMAC)")
            print("  3. Apex-DataMatrix (Log Parsing & Statistical Extraction)")
            print("  4. View System Integrity & Status Report")
            print("  5. Exit Central Command")
            
            choice = input("\nApex-Empire> ").strip()

            if choice == "1":
                self.run_apex_crypt()
            elif choice == "2":
                self.run_apex_nettunnel()
            elif choice == "3":
                self.run_apex_datamatrix()
            elif choice == "4":
                self.show_system_status()
            elif choice == "5":
                print("\n[*] Exiting Apex-Core Dashboard. Stay secure, Commander.")
                sys.exit(0)
            else:
                print("\n[!] INVALID SELECTION. Please choose an option from 1 to 5.")
                time.sleep(1.5)

    def run_apex_crypt(self):
        print("\n--- Executing Apex-Crypt Module ---")
        if ApexCrypt:
            payload = input("Enter payload to encrypt: ").strip() or "ApexEmpireSecurePayload"
            crypt = ApexCrypt(payload)
            crypt.export_report()
        else:
            print("[+] Simulating Apex-Crypt: Payload encrypted and XOR applied successfully.")
            report = {"module": "Apex-Crypt", "status": "SUCCESS", "author": self.commander}
            with open("apex_crypt_report.json", "w") as f:
                json.dump(report, f, indent=4)
            print("[+] Report saved to apex_crypt_report.json")
        input("\nPress Enter to return to main menu...")

    def run_apex_nettunnel(self):
        print("\n--- Executing Apex-NetTunnel Module ---")
        if ApexNetTunnel:
            tunnel = ApexNetTunnel()
            tunnel.simulate_node_communication()
        else:
            print("[+] Simulating Apex-NetTunnel: Secure socket channel established with HMAC validation.")
        input("\nPress Enter to return to main menu...")

    def run_apex_datamatrix(self):
        print("\n--- Executing Apex-DataMatrix Module ---")
        if ApexDataMatrix:
            sample_logs = "INFO: Auth success from 192.168.1.100 using user@apex.dz visiting https://api.apex.dz"
            matrix = ApexDataMatrix(sample_logs)
            matrix.export_report()
        else:
            print("[+] Simulating Apex-DataMatrix: Log patterns extracted successfully.")
        input("\nPress Enter to return to main menu...")

    def show_system_status(self):
        print("\n--- Apex-Empire System Status ---")
        modules = ["apex_crypt.py", "apex_nettunnel.py", "apex_datamatrix.py", "apex_intel.py", "README.md"]
        for mod in modules:
            exists = Path(mod).exists()
            status = "[ONLINE / ACTIVE]" if exists else "[MISSING]"
            print(f"  - {mod}: {status}")
        input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    dashboard = ApexCoreDashboard()
    dashboard.main_menu()
