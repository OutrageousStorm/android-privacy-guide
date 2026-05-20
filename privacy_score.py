#!/usr/bin/env python3
"""Calculate Android device privacy score"""
import subprocess

def adb(cmd):
    r = subprocess.run(['adb', 'shell'] + cmd.split(), capture_output=True, text=True)
    return r.stdout.strip()

score = 100
issues = []

# Checks
if adb("settings get secure location_mode") != "0":
    score -= 10
    issues.append("Location is enabled")

if adb("settings get global limit_ad_tracking") != "1":
    score -= 10
    issues.append("Ad tracking enabled")

if adb("dumpsys power | grep 'mScreenState'").endswith("1"):
    score -= 5
    issues.append("Screen on (battery drain)")

print(f"🔐 Privacy Score: {score}/100")
for issue in issues:
    print(f"  ⚠️  {issue}")
