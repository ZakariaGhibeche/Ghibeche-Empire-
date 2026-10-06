"""
Apex-Intel v1.0 (Direct Runner): Advanced URL Intelligence & Security Analyzer
Engineered by Commander Zakaria Ghibeche (Djelfa, Algeria)
"""

import urllib.request
import urllib.parse
import urllib.error
import ssl
import json

class ApexIntelEngine:
    def __init__(self, target_url: str):
        self.target_url = target_url
        if not self.target_url.startswith(('http://', 'https://')):
            self.target_url = 'https://' + self.target_url

    def analyze(self):
        print(f"[*] Starting Apex-Intel reconnaissance on: {self.target_url}")
        
        parsed_url = urllib.parse.urlparse(self.target_url)
        print(f"[+] Target Domain: {parsed_url.netloc}")

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        try:
            req = urllib.request.Request(
                self.target_url,
                headers={"User-Agent": "Apex-Intel-Security-Scanner/1.0"}
            )
            
            with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
                status_code = response.getcode()
                headers = dict(response.headers)
                print(f"[+] HTTP Status Code: {status_code}")
                print("[+] Security Headers Audited Successfully.")

            # Security Headers Audit
            sec_headers = ['Strict-Transport-Security', 'Content-Security-Policy', 'X-Frame-Options']
            for sh in sec_headers:
                found = any(k.lower() == sh.lower() for k in headers.keys())
                if found:
                    print(f"  [v] Present: {sh}")
                else:
                    print(f"  [x] Missing: {sh}")

            print("[+] Scan completed successfully!")

        except Exception as ex:
            print(f"[-] Error during analysis: {ex}")

if __name__ == "__main__":
    # ضع هنا أي رابط تريد فحصه مباشرة (مثال: موقعك أو موقع تجريبي)
    target = "https://github.com"
    engine = ApexIntelEngine(target)
    engine.analyze()
