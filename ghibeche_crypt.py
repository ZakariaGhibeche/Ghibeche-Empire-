# Ghibeche-Empire Security System - Ultimate Edition v2
# Author: Zakaria Ghibeche

def ghibeche_encrypt(text, shift=3):
    return "".join([chr(ord(char) + shift) for char in text])

def ghibeche_decrypt(encrypted_text, shift=3):
    return "".join([chr(ord(char) - shift) for char in encrypted_text])

if __name__ == "__main__":
    print("=== GHIBECHE EMPIRE SECURITY SYSTEM ===")
    
    try:
        raw_message = input("Enter operational message to secure: ")
        
        # تنظيف مستمر لأي رموز تحكم تظهر في البداية
        message = raw_message
        while message.startswith("^@") or message.startswith("^"):
            message = message.lstrip("^@").strip()
            
        # تنظيف عام لأي حروف غير مطبوعة أو مسافات زائدة
        message = message.strip()
        
        if message:
            encrypted = ghibeche_encrypt(message)
            decrypted = ghibeche_decrypt(encrypted)
            
            print("\n[+] Status: SECURED SUCCESSFULLY")
            print(f"[+] Original: {message}")
            print(f"[+] Encrypted (Empire Code): {encrypted}")
            print(f"[+] Decrypted (Verified): {decrypted}")
        else:
            print("[-] Error: Message is empty after cleaning.")
    except Exception as e:
        print(f"[-] Error: {e}")
        
    print("========================================")
