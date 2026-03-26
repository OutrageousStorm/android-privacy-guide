# Level 2 — Intermediate Privacy (2 hours, no root)

Deeper hardening using ADB and network-level blocking.

---

## 1. ADB permission hardening

Connect via USB with USB debugging enabled:

```bash
# Revoke location from social/advertising apps
for pkg in com.facebook.katana com.instagram.android com.twitter.android com.tiktok.android; do
  adb shell pm revoke $pkg android.permission.ACCESS_FINE_LOCATION 2>/dev/null
  adb shell pm revoke $pkg android.permission.ACCESS_COARSE_LOCATION 2>/dev/null
  adb shell pm revoke $pkg android.permission.READ_CONTACTS 2>/dev/null
done

# Disable background location for all apps
adb shell appops set --all MONITOR_LOCATION deny

# Disable clipboard reading
adb shell appops set --all READ_CLIPBOARD deny
```

## 2. Wireless ADB (no cable needed after setup)

Android 11+:
1. Settings → Developer Options → Wireless debugging → enable
2. `adb pair <ip>:<port>` then `adb connect <ip>:<port>`
3. Now use Shizuku app for ongoing ADB access without a PC

## 3. NetGuard firewall

Install [NetGuard](https://netguard.me) (F-Droid) and:
- Block all apps by default
- Whitelist only apps that need internet
- Enable filtering for detailed host blocking
- Import a blocklist (e.g. energized.pro or Steven Black's hosts)

## 4. TrackerControl

Install [TrackerControl](https://trackercontrol.org) to identify and block trackers in every app:
- Shows which trackers each app contacts
- Block specific companies (Google Analytics, Facebook, Crashlytics)
- Works without root via VPN interface

## 5. Disable hidden data collection

```bash
# Disable MIUI/Samsung telemetry components (device-specific — use with care)
adb shell pm disable-user --user 0 com.miui.analytics
adb shell pm disable-user --user 0 com.samsung.android.app.telephonyui

# Restrict background data for all apps
adb shell cmd netpolicy restrict-background enable

# Disable app suggestions / personalization
adb shell settings put secure package_verifier_user_consent -1
```

## 6. Lock down Chrome (if you can't replace it)

```bash
# Disable Chrome sync, Safe Browsing calls, and telemetry
# In Chrome: Settings → Sync → turn off
# Settings → Privacy → turn off all diagnostic sharing
# Use a content blocker extension (Brave's built-in is better)
```

---

**After this level: most trackers blocked, background data locked down, permissions tightened.**
