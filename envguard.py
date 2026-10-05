"""
EnvGuard: Automated Environment Security & Secret Leakage Prevention Tool
Engineered by Commander Zakaria Ghibeche (Djelfa, Algeria)
Target: Global Open-Source Production Release
"""

import os
import json
import re
import sys

class EnvGuardScanner:
    """Scans project files for exposed API keys, passwords, and sensitive tokens."""
    
    PATTERNS = {
        "Generic API Key": r"(api[_-]?key|access[_-]?token|secret[_-]?key)\s*[:=]\s*['\"][a-zA-Z0-9_\-\.]{16,}['\"]",
        "JWT Token": r"eyJ[a-zA-Z0-9_\-]{10,}\.eyJ[a-zA-Z0-9_\-]{10,}\.[a-zA-Z0-9_\-]{10,}",
        "Private Key": r"-----BEGIN (RSA|PRIVATE) KEY-----",
        "Hardcoded Password": r"password\s*[:=]\s*['\"][^'\"\s]{6,}['\"]"
    }

    def __init__(self, target_dir="."):
        self.target_dir = target_dir

    def scan_codebase(self):
        print(f"[*] Starting EnvGuard security audit on: {os.path.abspath(self.target_dir)}")
        violations = 0

        for root, dirs, files in os.walk(self.target_dir):
            # Skip hidden directories like .git
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for file in files:
                if file.endswith(('.py', '.json', '.env', '.yml', '.yaml', '.sh')):
                    file_path = os.path.join(root, file)
                    violations += self._inspect_file(file_path)

        if violations > 0:
            print(f"[-] Audit Failed: Found {violations} potential security vulnerability/secret leak!")
            sys.exit(1)
        else:
            print("[+] Audit Passed: No hardcoded secrets or vulnerabilities detected.")

    def _inspect_file(self, file_path):
        file_violations = 0
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                
                for label, pattern in self.PATTERNS.items():
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    if matches:
                        print(f"  [!] WARNING: {label} detected in {file_path}")
                        file_violations += 1
        except Exception as e:
            pass
            
        return file_violations

if __name__ == "__main__":
    scanner = EnvGuardScanner()
    scanner.scan_codebase()
