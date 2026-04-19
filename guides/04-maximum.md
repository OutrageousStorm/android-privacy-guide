# Level 4 — Maximum Privacy (GrapheneOS Only)

The absolute highest privacy — using GrapheneOS with extensive hardening.

## Prerequisites

- Pixel device (GrapheneOS support required)
- Fresh GrapheneOS install with locked bootloader

## Setup

### 1. Isolate Google services completely

Use a **secondary user profile** for Google Play apps:

```
Settings → System → Multiple users → Add user
→ In new user, install Sandboxed Google Play
→ Only log into Google in that user account
```

Main profile: Google-free.  
Work profile: Sandboxed Play isolated.

### 2. Network isolation via firewall + Tor

Install **Orbot** (F-Droid) for system-wide Tor:

```
Settings → Network & internet → VPN → Orbot (always on)
Block without VPN: enabled
Restrict Background: all apps
```

Result: All traffic routes through Tor automatically.

### 3. Disable all background activity

```bash
adb shell cmd appops set --all RUN_IN_BACKGROUND deny
adb shell cmd appops set --all MONITOR_LOCATION deny
adb shell cmd appops set --all READ_CLIPBOARD deny
```

### 4. Block entire domains via system DNS

GrapheneOS + private DNS:

```
Settings → Network & internet → Private DNS
Custom: max.rethinkdns.com  (malware + tracking blocker)
```

Alternative: **NextDNS** with family/malware/adult content filters.

### 5. Time-based location spoofing

Install **Organic Maps** (offline) with fake GPS enabled:

```
F-Droid → Organic Maps
Settings → Location → Enable location spoofing
Set fake location to a random place
```

Now all location requests return a spoofed location 50+ miles away.

### 6. Microphone & camera isolation

```bash
adb shell settings put global audio_recording_disable 1
adb shell settings put global camera_use_restrict 1
```

Revoke via AppOps every app except Signal, Jami, XMPP client.

### 7. One-time use Telegram

If you must use Telegram:

```
Secondary user profile ONLY
Delete account immediately after use
Run Telegram inside Orbot VPN
Disable: auto-download, auto-play video, cloud sync, auto-delete
```

Actually: Switch to **Jami** (decentralized, peer-to-peer, zero tracking).

### 8. Zero telemetry OS-level

```bash
adb shell settings put secure ota_disable_automatic_update 1
adb shell settings put global debugging_allow_bug_reports 0
adb shell settings put global crash_to_log_policy 0
```

### 9. Encrypted messaging only

- **Signal**: encrypted messaging + calls (verified)
- **Jami**: decentralized, no servers
- **Matrix/Element**: federated, encrypted with Megolm
- **Briar**: mesh network, works over Tor

Do NOT use: Telegram, WhatsApp (end-to-end encryption doesn't prevent metadata).

### 10. Secure mail setup

```
ProtonMail + Bridge (CLI POP3/SMTP)
  or
Tutanota (full E2E encryption)
```

Both clients: FairEmail (F-Droid)

## Privacy checklist

```
□ GrapheneOS installed & locked
□ Secondary user for Google apps
□ Tor/Orbot system-wide
□ Private DNS enabled (max.rethinkdns.com)
□ Background activity blocked
□ Location spoofing active
□ Mic/camera disabled except for Signal
□ Messaging: Signal + Jami + Matrix
□ Email: ProtonMail or Tutanota
□ No Google account on main profile
□ USB debugging disabled
□ Developer options hidden
□ Auto-reboot: 12 hours
□ Duress PIN configured
```

## Result

A device that:
- Cannot be passively tracked (Tor forces exit node rotation)
- Cannot be actively geolocated (spoofed location + offline maps)
- Shares no data with Google/Meta/Apple
- Survives border crossing (Duress PIN auto-wipe)
- Uses only peer-to-peer or E2E encrypted apps
- Has zero telemetry

## Still vulnerable to

- Fingerprinting via system fonts/DPI (rare attack)
- Physical surveillance (camera/microphone)
- Quantum computing breaking encryption (decades away)
- Zero-day kernel exploit (GrapheneOS hardens against this, but not immune)
