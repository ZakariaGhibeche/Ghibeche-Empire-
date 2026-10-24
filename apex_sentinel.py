#!/usr/bin/env python3
"""
Project: Apex-Sentinel
Author: Commander Zakaria Ghibeche (Apex-Empire)
Description: Zero-dependency security scanner for secrets and vulnerabilities in source code.
"""

import os
import re
import sys

# أنماط البحث عن البيانات الحساسة والمفاتيح المسربة (Regex Patterns)
SENSITIVE_PATTERNS = {
    "GitHub Token": r"ghp_[a-zA-Z0-9]{36}",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Private Key": r"-----BEGIN PRIVATE KEY-----",
    "Generic API Key": r"api[_-]?key['\"]?\s*[:=]\s*['\"'][a-zA-Z0-9_\-]{16,45}['\"]",
    "IP Address": r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
}

def scan_file(file_path):
    findings = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_no, line in enumerate(f, 1):
                for vuln_name, pattern in SENSITIVE_PATTERNS.items():
                    if re.search(pattern, line):
                        findings.append({
                            "line": line_no,
                            "type": vuln_name,
                            "content": line.strip()[:60] # اقتطاع النص لحماية الخصوصية
                        })
    except Exception as e:
        pass
    return findings

def scan_directory(root_dir):
    report = {}
    ignored_dirs = {'.git', '__pycache__', 'venv', 'env', 'node_modules'}
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in ignored_dirs]
        for file in filenames:
            # فحص ملفات بايثون والنصوص والكونفجريشن
            if file.endswith(('.py', '.env', '.json', '.sh', '.yml', '.yaml', '.md')):
                full_path = os.path.join(dirpath, file)
                file_findings = scan_file(full_path)
                if file_findings:
                    report[full_path] = file_findings
    return report

def generate_markdown_report(report):
    print("\n" + "="*50)
    print(" 🛡️ APEX-SENTINEL SECURITY AUDIT REPORT 🛡️ ")
    print("="*50 + "\n")
    
    if not report:
        print("✅ [SECURE] No sensitive leaks or vulnerabilities detected. System clean!")
        return

    for filepath, issues in report.items():
        print(f"📁 File: {filepath}")
        for issue in issues:
            print(f"   ⚠️  [Line {issue['line']}] Found {issue['type']}: `{issue['content']}`")
        print("-" * 40)

if __name__ == "__main__":
    target_path = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f"[*] Starting Apex-Sentinel scan on target: {target_path} ...")
    audit_results = scan_directory(target_path)
    generate_markdown_report(audit_results)
