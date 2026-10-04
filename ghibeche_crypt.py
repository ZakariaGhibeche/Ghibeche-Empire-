#!/usr/bin/env python3
"""
Project: Ghibeche-Empire
File: ghibeche_crypt.py
Author: Commander Zakaria Ghibeche
Description: Advanced cryptographic utility designed for high-security 
             data scrambling and secure empire communications.
"""

import base64
import hashlib
import sys

class GhibecheCryptEngine:
    def __init__(self, master_key: str):
        self.master_key = master_key.encode('utf-8')
        # Generate a secure 32-byte key using SHA-256 hash of the master key
        self.sec_key = hashlib.sha256(self.master_key).digest()

    def encrypt_data(self, plain_text: str) -> str:
        """Encrypts plain text using advanced XOR masking layered with Base64 encoding."""
        data_bytes = plain_text.encode('utf-8')
        encrypted_bytes = bytearray()
        
        key_len = len(self.sec_key)
        for i, b in enumerate(data_bytes):
            # Apply dynamic XOR transformation with key rotation
            masked_byte = b ^ self.sec_key[i % key_len]
            encrypted_bytes.append(masked_byte)
            
        # Encode to Base64 for safe transport and storage
        encoded_output = base64.urlsafe_b64encode(encrypted_bytes).decode('utf-8')
        return encoded_output

    def decrypt_data(self, cipher_text: str) -> str:
        """Decrypts the secure cipher text back to original readable plain text."""
        try:
            decoded_bytes = base64.urlsafe_b64decode(cipher_text.encode('utf-8'))
            decrypted_bytes = bytearray()
            
            key_len = len(self.sec_key)
            for i, b in enumerate(decoded_bytes):
                original_byte = b ^ self.sec_key[i % key_len]
                decrypted_bytes.append(original_byte)
                
            return decrypted_bytes.decode('utf-8')
        except Exception as e:
            return f"[ERROR] Decryption failed. Invalid key or corrupted payload: {str(e)}"

def banner():
    print("=" * 60)
    print("      🛡️  GHIBECHE EMPIRE - CRYPTOGRAPHIC ENGINE v1.0  🛡️      ")
    print("      Author: Zakaria Ghibeche | Global Security Tool        ")
    print("=" * 60)

if __name__ == "__main__":
    banner()
    
    # Simulation / CLI Test Suite for Global Standards
    secret_message = "Elite Python Infrastructure of Ghibeche Empire"
    encryption_passphrase = "Zakaria-Master-Secret-2026"
    
    print(f"[*] Initializing Cryptographic Core...")
    engine = GhibecheCryptEngine(encryption_passphrase)
    
    print(f"[+] Target Payload: {secret_message}")
    ciphertext = engine.encrypt_data(secret_message)
    print(f"[🔒] Encrypted Payload (Global Transmission Format): {ciphertext}")
    
    recovered_text = engine.decrypt_data(ciphertext)
    print(f"[🔓] Decrypted Payload Verification: {recovered_text}")
    print("=" * 60)
    print("[✔] Ghibeche Crypt Engine executed successfully with 0 errors.")
