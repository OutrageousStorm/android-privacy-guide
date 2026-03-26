# Level 3 — Advanced Privacy (Half day, root optional)

Full de-Google, network isolation, and custom ROM setup.

---

## Option A: Stay on stock, maximally hardened

If you can't or won't flash a custom ROM:

### 1. Disable all Google telemetry
```bash
# Disable Google services that phone home
adb shell pm disable-user --user 0 com.google.android.partnersetup
adb shell pm disable-user --user 0 com.google.android.feedback
adb shell pm disable-user --user 0 com.google.android.onetimeinitializer
adb shell pm disable-user --user 0 com.google.android.setupwizard

# Block Firebase Analytics across the board
adb shell pm disable-user --user 0 com.google.firebase.analytics
```

### 2. Private DNS + Always-on VPN
Settings → Network → Private DNS → `dns.quad9.net`
Settings → Network → VPN → [your VPN] → Always-on VPN + Block without VPN

Recommended VPNs (open source, audited):
- [Mullvad](https://mullvad.net) — anonymous, accepts cash/Monero
- [ProtonVPN](https://protonvpn.com) — audited, free tier
- Self-hosted: [WireGuard](https://wireguard.com)

### 3. Hosts-based ad blocking
```bash
# Install NetGuard with filtering enabled
# Import block list from: https://energized.pro
# Or use AdAway (root) with Steven Black's hosts list
```

### 4. Work Profile isolation
Use Shelter (F-Droid) to create a work profile:
- Install all Google/untrusted apps in work profile
- Main profile stays Google-free
- One-tap freeze/unfreeze the work profile

---

## Option B: Flash a privacy ROM

**Best options:**
| ROM | Devices | Google support |
|-----|---------|---------------|
| GrapheneOS | Pixel only | Sandboxed Play |
| CalyxOS | Pixel + some others | microG built-in |
| DivestOS | 200+ devices | Optional microG |
| /e/OS | 250+ devices | microG + Murena cloud |

---

## Network traffic analysis

Before and after hardening, audit what your phone is actually sending:

```bash
# PCAPdroid — capture all traffic without root
# Install from F-Droid, enable VPN mode, analyze in Wireshark

# Or via ADB:
adb shell tcpdump -i any -w /sdcard/capture.pcap
adb pull /sdcard/capture.pcap
# Open in Wireshark on PC
```

---

## After this level

Your phone makes significantly fewer connections to ad networks and trackers. Test your privacy at:
- https://coveryourtracks.eff.org (browser)
- https://www.dnsleaktest.com (DNS)
- https://ipleak.net (VPN)
