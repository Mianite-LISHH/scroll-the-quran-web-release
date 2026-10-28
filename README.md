# Scroll the Qur’an — public browser release

Public distribution of the tested guest-reader web application. This repository contains only compiled public browser files, licensed scripture, fonts, attribution, and deployment verification. Private source, credentials, personal records, and live payment integrations are not included.

Application source checkpoint: 5e30747cdfabf26e88ce88f647e4c1ae50331d27.

Build command: `python3 verify.py`. Publish directory: `public`. Directory entries support direct public-information URLs without a server-side rewrite. `render.yaml` also records the intended security headers and SPA rewrite for hosts that apply Blueprint settings.

This is a development release, not a completed production or app-store release. Accounts/cloud sync, advanced licensed study, approved audio and billing are not configured in this guest build. Essential reading remains free.

Arabic: Tanzil Uthmani v1.1; 114 surahs and 6,236 source records. Translation: Talal Itani, ClearQuran naming editions. Font: Amiri Quran, SIL OFL. The original redistribution and attribution terms are included under `public/licenses` and in the reader’s Sources view. No blanket license supersedes those terms.
