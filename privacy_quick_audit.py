#!/usr/bin/env python3
"""Quick privacy audit for Android — scans dangerous perms and suggests fixes"""
import subprocess, json

def adb(cmd):
    r = subprocess.run(['adb', 'shell'] + cmd.split(), capture_output=True, text=True)
    return r.stdout.strip()

RISKY = [
    'android.permission.ACCESS_FINE_LOCATION',
    'android.permission.READ_CONTACTS',
    'android.permission.RECORD_AUDIO',
    'android.permission.CAMERA',
]

apps = {}
for line in adb('pm list packages').splitlines():
    pkg = line.replace('package:', '').strip()
    for perm in RISKY:
        out = adb(f'dumpsys package {pkg} | grep {perm}')
        if 'granted=true' in out:
            if pkg not in apps: apps[pkg] = []
            apps[pkg].append(perm.split('.')[-1])

print(f"Found {len(apps)} apps with risky permissions:")
for pkg, perms in sorted(apps.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"  {pkg}: {', '.join(perms)}")
