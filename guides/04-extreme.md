# Level 4 — Extreme Privacy (Full Weekend, Root Required)

Maximum privacy at the cost of convenience. For people who treat their phone like a security appliance.

---

## 1. Reflash with GrapheneOS

GrapheneOS is the most hardened Android. No Google by default, Sandboxed Play optional.

```bash
# Requirements: Pixel 6–9 only
# Visit: https://grapheneos.org/install/web
# Follow the web installer (easiest)
```

After install, you're at 90% privacy baseline. Everything below is hardening *GrapheneOS itself*.

---

## 2. Aggressive AppOps denial

Deny everything by default, allow only per-app as needed:

```bash
# Deny clipboard reading globally (huge privacy win)
adb shell appops set --all READ_CLIPBOARD deny

# Deny location monitoring
adb shell appops set --all MONITOR_LOCATION deny

# Deny body sensor access
adb shell appops set --all BODY_SENSORS deny

# Deny activity recognition
adb shell appops set --all ACTIVITY_RECOGNITION deny

# Deny call log access
adb shell appops set --all READ_CALL_LOG deny
```

---

## 3. Network isolation with Orbot (Tor)

Route all traffic through Tor:

```bash
# Install Orbot from F-Droid
# Enable: Orbot → Start VPN
# Then every app uses Tor (or can't connect)
```

**Caveat:** Slow. But maximum anonymity.

---

## 4. Hardware keystroke injection detection

Some devices support checking USB/Bluetooth keystroke injection:

```bash
# Check if available
adb shell dumpsys input_method | grep keyboard

# Can install Bluetooth keystroke detector apps
# (minimal protection, mostly theater)
```

---

## 5. Disable all wireless radios by default

Keep everything off, enable only when needed:

```bash
# Disable WiFi until explicitly enabled
adb shell settings put global wifi_on 0
adb shell settings put global bluetooth_on 0
adb shell settings put global location_mode 0
adb shell settings put global mobile_data 0  # sim card only

# NFC completely off
adb shell settings put secure nfc_enabled 0
```

---

## 6. Use a privacy DNS (Quad9, NextDNS)

```bash
# Settings → Network → Private DNS → set to:
dns.quad9.net     # malware + ad blocking
privacy.nextdns.io # advanced filtering (custom account)
```

---

## 7. IMSI catcher & stingray detection

Some phones can partially detect fake cell towers:

```bash
# Android 12+ has some protections
adb shell settings get secure strict_phone_number_formatting

# Install: NetMonitor (F-Droid) to see cell tower changes
```

**Reality check:** Phone companies could enable IMSI catcher logs, but most don't expose them.

---

## 8. Physical security measures

- Use a strong PIN (8+ digits, not repeating)
- Enable Duress PIN (wipes device if entered)
- Use encrypted backups (E2E cloud storage like Proton Drive)
- Consider a Faraday bag for high-sensitivity situations

---

## 9. Review every single permission

```bash
# Go through every app with fine-tooth comb:
for pkg in $(adb shell pm list packages -3 | cut -d: -f2); do
  perms=$(adb shell dumpsys package $pkg | grep -i "granted=true" | grep -i "LOCATION\|CALL\|SMS\|CONTACT\|CAMERA\|MICROPHONE")
  if [ -n "$perms" ]; then
    echo "⚠️  $pkg: $perms"
  fi
done
```

---

## 10. Sandboxing with Shelter (advanced)

Create a completely isolated second user:

```bash
# Install Shelter (F-Droid)
# Create: Work Profile
# Use: for all Google apps + any untrusted apps
# Main profile: completely Google-free + verified FOSS only
```

---

## Reality check

**You still cannot:**
- Prevent your carrier from knowing your location (they own the network)
- Prevent SMS reading (if SIM is compromised)
- Protect against evil maid attacks (physical device access)
- Hide metadata from VPN provider (if not Tor)
- Protect against 0-day vulnerabilities (by definition)

**What you CAN do:**
- Make bulk data harvesting impractical (no Google, no trackers, VPN/Tor)
- Prevent app-level tracking (permissions, AppOps, sandboxing)
- Reduce advertising network data collection (DNS, network-level blocking)
- Survive casual physical access (strong PIN, wipe on duress)

**Bottom line:** Extreme privacy is possible. But it requires:
1. Rare hardware (Pixel)
2. Specialized OS (GrapheneOS)
3. Constant vigilance (check perms, update regularly, review logs)
4. Significant inconvenience (no cloud sync, slower network via Tor, many apps don't work)

For most people, **Level 2–3 is the sweet spot:** private enough to avoid mass tracking, practical enough for daily life.

For journalists, dissidents, or people with real threats: **Level 4 is the minimum.**
