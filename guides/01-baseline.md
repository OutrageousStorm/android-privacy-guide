# Level 1 — Baseline Privacy (30 minutes, no root)

The minimum everyone should do. Works on any Android device.

---

## 1. Permissions audit

Go through every app and revoke permissions it doesn't need:
- **Location** → Only grant to maps/weather. Revoke from social media, games, browsers.
- **Contacts** → Only grant to phone, SMS, email apps.
- **Microphone** → Only grant to camera, voice recorder, calls. Not social media.
- **Camera** → Only grant to camera app and video call apps.

```bash
# Via ADB — list all apps with a permission
adb shell pm list packages | while read pkg; do
  pkg=${pkg#package:}
  perm=$(adb shell dumpsys package $pkg 2>/dev/null | grep "android.permission.ACCESS_FINE_LOCATION")
  [ -n "$perm" ] && echo "$pkg"
done
```

## 2. Disable advertising ID

Settings → Privacy → Ads → Delete advertising ID (Android 12+)
Or on older Android: set Opt out of Ads Personalization.

```bash
adb shell settings put global limit_ad_tracking 1
```

## 3. Disable Google Activity tracking

- Google Account → Data & Privacy → turn off Web & App Activity, YouTube History, Location History
- Or just don't use a Google account

## 4. Block unnecessary background activity

Settings → Battery → Background usage limits → restrict apps you don't use actively.

## 5. Use a privacy-respecting browser

Install [Brave](https://brave.com) or [Firefox](https://firefox.com) with uBlock Origin.
Remove Chrome from home screen (can't fully uninstall on stock Android).

## 6. Use encrypted DNS

Settings → Network → Private DNS → set to:
- `dns.quad9.net` (no tracking, malware blocking)
- `1dot1dot1dot1.cloudflare-dns.com` (fast, privacy-respecting)
- Or self-host with AdGuard Home

## 7. Review app installs

Uninstall anything you haven't used in 30 days. Every app is a potential data collection point.

---

**Time: ~30 minutes. No root needed. Significant baseline improvement.**
