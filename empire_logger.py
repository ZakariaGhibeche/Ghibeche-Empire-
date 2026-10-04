#!/usr/bin/env python3
"""
Project: Ghibeche-Empire
File: empire_logger.py
Author: Commander Zakaria Ghibeche
Description: Advanced Audit & Event Logging Engine for Infrastructure Security.
"""

import os
import datetime

LOG_FILE = "empire_audit.log"

def log_event(event_type, description):
    """Logs an empire security or operational event with exact timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{event_type.upper()}] {description}\n"
    
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry)
        print(f"[+] [LOGGER] Event recorded successfully: {event_type}")
    except Exception as e:
        print(f"[-] [LOGGER ERROR] Failed to write log: {e}")

def view_logs():
    """Displays recent audit logs from the empire core."""
    if not os.path.exists(LOG_FILE):
        print("\n[-] No audit logs found. The empire is currently clean.")
        return
        
    print("\n" + "=" * 60)
    print("       🛡️  GHIBECHE-EMPIRE - AUDIT LOGS & SECURITY TRAIL  🛡️       ")
    print("=" * 60)
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[-15:]:  # Show last 15 security events
                print(line.strip())
    except Exception as e:
        print(f"[-] Error reading logs: {e}")
    print("=" * 60)

if __name__ == "__main__":
    # Test execution when run directly
    print("--- [ GHIBECHE-EMPIRE AUDT LOGGER INITIALIZED ] ---")
    log_event("SYSTEM", "Empire logger module executed directly by Commander.")
    view_logs()
