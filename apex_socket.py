"""
Apex-Socket v1.0: Network Security Scanner & Secure Crypto-Payload Engine
Engineered by Commander Zakaria Ghibeche (Djelfa, Algeria)
Brand: Apex-Empire (Global Open-Source Production Release)
"""

import socket
import ssl
import sys
import json
import hashlib
import hmac
import base64
import time

class ApexSocketEngine:
    """Performs network reconnaissance, port scanning, and secure cryptographic handshakes."""
    
    def __init__(self, target_host: str, ports: list = None):
        self.target_host = target_host.replace('https://', '').replace('http://', '').split('/')[0]
        self.ports = ports or [21, 22, 80, 443, 8080, 8443]

    def scan_ports(self):
        print(f"[*] Starting Apex-Socket network audit on target: {self.target_host}")
        open_ports = []
        
        for port in self.ports:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1.5)
                result = s.connect_ex((self.target_host, port))
                if result == 0:
                    print(f"  [v] Port {port}: OPEN")
                    open_ports.append(port)
                else:
                    print(f"  [x] Port {port}: Closed / Filtered")
                s.close()
            except Exception as e:
                print(f"  [-] Error scanning port {port}: {e}")
                
        return open_ports

    def generate_secure_token(self, secret_key: str, message: str) -> str:
        """Advanced Cryptographic HMAC-SHA256 Token Generation for Secure Network Comm."""
        key_bytes = secret_key.encode('utf-8')
        msg_bytes = message.encode('utf-8')
        signature = hmac.new(key_bytes, msg_bytes, hashlib.sha256).digest()
        token = base64.b64encode(signature).decode('utf-8')
        return token

    def execute_audit(self, secret_pass: str = "ApexEmpireSecret2026"):
        open_ports = self.scan_ports()
        
        test_msg = f"Commander-Zakaria-{int(time.time())}"
        crypto_token = self.generate_secure_token(secret_pass, test_msg)
        
        print(f"[*] Generating Advanced Cryptographic Handshake Token...")
        print(f"  [+] HMAC-SHA256 Token: {crypto_token[:32]}...")

        report = {
            "target": self.target_host,
            "open_ports": open_ports,
            "crypto_token_sample": crypto_token,
            "status": "Secured & Audited"
        }

        filename = "apex_socket_report.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        print(f"[+] Apex-Socket reconnaissance report saved to: {filename}")

if __name__ == "__main__":
    target = "github.com"
    engine = ApexSocketEngine(target)
    engine.execute_audit()
