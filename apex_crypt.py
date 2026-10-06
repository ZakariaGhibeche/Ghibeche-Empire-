"""
Apex-Crypt v1.0: Advanced Payload Encasement & Custom Cryptographic Obfuscation Engine
Engineered by Commander Zakaria Ghibeche (Djelfa, Algeria)
Brand: Apex-Empire (Global Open-Source Production Release)
"""

import base64
import hashlib
import json
import zlib
import time

class ApexCryptEngine:
    """Provides high-security payload compression, obfuscation, and encryption-grade transformations."""
    
    def __init__(self, payload_data: str, secret_pass: str = "ApexEmpire2026"):
        self.payload_data = payload_data
        self.secret_pass = secret_pass

    def obfuscate_payload(self) -> str:
        print("[*] Initializing Apex-Crypt advanced payload encasement...")
        
        # Step 1: Compression to minimize payload footprint
        compressed = zlib.compress(self.payload_data.encode('utf-8'))
        
        # Step 2: Custom XOR Layer with Secret Hash Key
        key_hash = hashlib.sha256(self.secret_pass.encode('utf-8')).digest()
        obfuscated_bytes = bytearray()
        for i, b in enumerate(compressed):
            obfuscated_bytes.append(b ^ key_hash[i % len(key_hash)])
            
        # Step 3: Base64 Encoding for transport safety
        encoded_token = base64.b64encode(obfuscated_bytes).decode('utf-8')
        return encoded_token

    def generate_report(self):
        token = self.obfuscate_payload()
        checksum = hashlib.sha256(token.encode('utf-8')).hexdigest()
        
        print(f"[+] Payload successfully encased and obfuscated.")
        print(f"[+] Cryptographic Checksum (SHA-256): {checksum[:32]}...")

        report = {
            "author": "Commander Zakaria Ghibeche",
            "brand": "Apex-Empire",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "checksum_sha256": checksum,
            "obfuscated_payload": token,
            "status": "Ready for Secure Deployment"
        }

        filename = "apex_crypt_report.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        print(f"[+] Apex-Crypt report securely exported to: {filename}")

if __name__ == "__main__":
    sample_payload = "EXEC_SYS_RECON_MODULE:TARGET_SECURE_NODE_ALPHA"
    engine = ApexCryptEngine(sample_payload)
    engine.generate_report()
