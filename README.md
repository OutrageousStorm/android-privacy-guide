# 🔏 Android Privacy Guide

A practical, no-BS guide to hardening Android privacy — with and without root.

---

## Levels

| Level | Effort | Root needed | Result |
|-------|--------|-------------|--------|
| [Baseline](guides/01-baseline.md) | 30 min | No | Removes obvious trackers, locks down permissions |
| [Intermediate](guides/02-intermediate.md) | 2 hrs | No | ADB hardening, DNS, firewall |
| [Advanced](guides/03-advanced.md) | Half day | Optional | Custom ROM, full de-Google |
| [Maximum](guides/04-maximum.md) | Weekend | Recommended | GrapheneOS, network isolation |

---

## Quick wins (do these now)

```bash
# Revoke dangerous permissions from apps that don't need them
adb shell pm revoke com.facebook.katana android.permission.ACCESS_FINE_LOCATION
adb shell pm revoke com.facebook.katana android.permission.READ_CONTACTS

# Disable advertising ID entirely
adb shell settings put global limit_ad_tracking 1

# Disable cross-app tracking (Android 12+)
adb shell settings put global restricted_networking_mode 0

# Block background app activity
adb shell cmd appops set <package> RUN_IN_BACKGROUND deny
```

---

## FOSS replacements

| Google app | FOSS alternative | Notes |
|-----------|-----------------|-------|
| Chrome | [Brave](https://brave.com) / [Firefox](https://firefox.com) | Brave has built-in ad block |
| Google Search | [SearXNG](https://searx.space) / DuckDuckGo | Self-hostable |
| Gmail | [FairEmail](https://email.faircode.eu) / [K-9 Mail](https://k9mail.app) | Open source |
| Google Maps | [OsmAnd](https://osmand.net) / [Organic Maps](https://organicmaps.app) | Offline capable |
| Google Photos | [Ente](https://ente.io) / [Immich](https://immich.app) | E2E encrypted |
| Google Drive | [Nextcloud](https://nextcloud.com) / [Proton Drive](https://proton.me/drive) | Self-hostable |
| Google Calendar | [Proton Calendar](https://proton.me/calendar) / [Simple Calendar](https://github.com/SimpleMobileTools/Simple-Calendar) | |
| Gboard | [FUTO Keyboard](https://keyboard.futo.org) / [OpenBoard](https://github.com/openboard-team/openboard) | No network access |
| YouTube | [NewPipe](https://newpipe.net) / [ReVanced](https://revanced.app) | No Google account |

---

## Recommended apps

| App | Purpose |
|-----|---------|
| [Netguard](https://netguard.me) | No-root firewall — block per-app internet |
| [TrackerControl](https://trackercontrol.org) | Block trackers without root |
| [PCAPdroid](https://emanuele-f.github.io/PCAPdroid/) | Network traffic monitor |
| [Shizuku](https://shizuku.rikka.app) | Run ADB commands without PC |
| [App Manager](https://muntashirakon.github.io/AppManager/) | Full app control — permissions, ops, components |

---

*See also: [android-privacy-hardener](https://github.com/OutrageousStorm/android-privacy-hardener)*  
*Maintained by [OutrageousStorm](https://github.com/OutrageousStorm)*
