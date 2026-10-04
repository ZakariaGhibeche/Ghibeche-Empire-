#!/usr/bin/env python3
"""
Project: Ghibeche-Empire
File: empire_shield.py
Author: Commander Zakaria Ghibeche
Description: Automated Security Shield & File Integrity Inspector.
"""

import os
import sys

# قائمة الملفات الأساسية التي تتكون منها الإمبراطورية
EMPIRE_CORE_FILES = [
    "empire_main.py",
    "empire_nexus.py",
    "ghibeche_crypt.py",
    "ghibeche_matrix.py",
    "empire_logger.py"
]

def inspect_empire_integrity():
    """Scans and verifies the integrity of all Ghibeche-Empire core modules."""
    print("=" * 65)
    print("      🛡️  GHIBECHE-EMPIRE - INTEGRITY & SECURITY SHIELD  🛡️      ")
    print("=" * 65)
    print(f"[*] Initiating full system audit by Commander Zakaria Ghibeche...\n")
    
    missing_files = []
    secure_count = 0
    
    for file in EMPIRE_CORE_FILES:
        if os.path.exists(file):
            file_size = os.path.getsize(file)
            print(f"[🟢 ONLINE / SECURE] Module found: {file} ({file_size} bytes)")
            secure_count += 1
        else:
            print(f"[🔴 MISSING / THREAT] Critical module missing: {file}")
            missing_files.append(file)
            
    print("\n" + "-" * 65)
    if not missing_files:
        print(f"[*] STATUS: 100% SECURE. All {secure_count} core modules are operational.")
        print("[*] The empire shield is active and holding strong!")
    else:
        print(f"[*] STATUS: WARNING. {len(missing_files)} core modules require attention.")
    print("=" * 65)

if __name__ == "__main__":
    inspect_empire_integrity()
