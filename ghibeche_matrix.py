# =========================================
# GHIBECHE-EMPIRE: DATA ANALYZER MATRIX
# Author: Zakaria Ghibeche
# Description: Professional text & data analysis tool
# =========================================

import sys
from datetime import datetime

class GhibecheMatrix:
    def __init__(self):
        self.version = "1.0.0"
        self.empire_tag = "Ghibeche-Empire"
        print(f"[{self.empire_tag}] Initializing Matrix Analyzer v{self.version}...")

    def analyze(self, text):
        if not text:
            return {"error": "Input text is empty."}
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        words = text.split()
        chars_with_spaces = len(text)
        chars_no_spaces = len(text.replace(" ", ""))
        word_count = len(words)
        lines = text.count('\n') + 1

        report = f"""
=========================================
   GHIBECHE-EMPIRE ANALYSIS REPORT
=========================================
[+] Timestamp: {timestamp}
[+] Total Characters (with spaces): {chars_with_spaces}
[+] Total Characters (no spaces): {chars_no_spaces}
[+] Total Words: {word_count}
[+] Total Lines: {lines}
[+] Status: SECURED & PROCESSED BY EMPIRE
=========================================
"""
        return report

if __name__ == "__main__":
    matrix = GhibecheMatrix()
    
    # Sample text analysis for the global portfolio
    sample_data = "Building the global technical empire through precision and Python."
    print(f"\nTarget Data: {sample_data}\n")
    
    result = matrix.analyze(sample_data)
    print(result)
