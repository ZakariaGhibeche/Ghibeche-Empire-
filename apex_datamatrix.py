"""
Apex-DataMatrix v1.0: Advanced Log Parsing & Statistical Data Analysis Engine
Engineered by Commander Zakaria Ghibeche (Djelfa, Algeria)
Brand: Apex-Empire (Global Open-Source Production Release)
"""

import re
import json
import time
from collections import Counter

class ApexDataMatrix:
    """Parses raw log data, extracts sensitive entities (IPs, Emails, URLs), and computes statistics."""
    
    def __init__(self, raw_logs: str):
        self.raw_logs = raw_logs

    def analyze_logs(self) -> dict:
        print("[*] Initializing Apex-DataMatrix pattern extraction & statistical analysis...")
        
        # Regex patterns for sensitive entity extraction
        ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        url_pattern = r'https?://[^\s<>"]+|www\.[^\s<>"]+'

        ips = re.findall(ip_pattern, self.raw_logs)
        emails = re.findall(email_pattern, self.raw_logs)
        urls = re.findall(url_pattern, self.raw_logs)

        # Statistical frequency counting
        ip_counts = Counter(ips)
        email_counts = Counter(emails)
        url_counts = Counter(urls)

        analysis_report = {
            "author": "Commander Zakaria Ghibeche",
            "brand": "Apex-Empire",
            "module": "Apex-DataMatrix v1.0",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_entities_found": len(ips) + len(emails) + len(urls),
            "statistics": {
                "unique_ips": len(ip_counts),
                "unique_emails": len(email_counts),
                "unique_urls": len(url_counts)
            },
            "extracted_data": {
                "ip_addresses": dict(ip_counts.most_common(5)),
                "emails": dict(email_counts.most_common(5)),
                "urls": dict(url_counts.most_common(5))
            },
            "status": "Analysis Complete & Verified"
        }

        return analysis_report

    def export_report(self, filename="apex_datamatrix_report.json"):
        report = self.analyze_logs()
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4, ensure_ascii=False)
        print(f"[+] Apex-DataMatrix statistical report successfully exported to: {filename}")

if __name__ == "__main__":
    sample_log_data = """
    [2026-10-06 10:00:15] INFO: User login from 192.168.1.50 using admin@apex-empire.dz
    [2026-10-06 10:02:30] WARN: Failed auth attempt from 10.0.0.15 against target https://api.apex-empire.dz/v1/auth
    [2026-10-06 10:05:12] INFO: Data sync initiated by security@apex-empire.dz via 192.168.1.50
    [2026-10-06 10:10:44] ALERT: Unauthorized scan detected from 203.0.113.42 targeting https://malicious-node.test/payload
    """
    
    matrix = ApexDataMatrix(sample_log_data)
    matrix.export_report()
