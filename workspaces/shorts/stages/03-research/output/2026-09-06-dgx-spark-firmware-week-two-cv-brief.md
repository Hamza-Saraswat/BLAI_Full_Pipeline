---
slug: 2026-09-06-dgx-spark-firmware-week-two-cv
stage: 03-research
topic: "Two DGX Spark firmware CVEs fixed in the August 2026 drop: what broke, what is fixed, patch tonight"
depth: standard
generated_at: 2026-09-06T11:35:29Z
sources: 9
hub: "[[videos/2026-09-06-dgx-spark-firmware-week-two-cv]]"
---

# Research brief: DGX Spark firmware week -- two CVEs fixed, patch now

## Summary
NVIDIA's August 2026 DGX Spark bulletin (number 5867, dated 2026-08-25) patches five UEFI-layer flaws, every one of them in DGX Spark firmware versions 0 to 1.110.12, with UEFI 1.110.13 as the fixed version -- the release-notes page already lists UEFI 1.110.13 as current. The most arresting number is 8.2: the CVSS 3.1 score NVIDIA assigns to both CVE-2026-24262 and the other two HIGH-rated system-firmware flaws, where a privileged attacker's out-of-bounds write or NULL pointer dereference may lead to code execution, escalation of privileges, denial of service, information disclosure and data tampering. The strongest concrete case for the patch-tonight angle: NVIDIA's own fix path is five terminal commands in the OS and Component Update Guide, so the entire remediation is one sitting. Could not be verified: whether any of these flaws is exploited in the wild, and whether the Dell Pro Max with GB10 partner hardware receives 1.110.13 at the same time as the Founders Edition (release notes warn GB10 partner systems "may not receive updates at the same time"). One conflict the writer must respect: the confirmed angle calls both CVEs out-of-bounds writes, but NVIDIA's bulletin classifies CVE-2026-24263 as a NULL pointer dereference (CWE-476) and reserves out-of-bounds write (CWE-787) for CVE-2026-24262 and CVE-2026-47626.

## Thesis
NVIDIA just fixed five UEFI firmware vulnerabilities in the DGX Spark, three of them rated 8.2 HIGH including an out-of-bounds write an already-privileged attacker can turn into code execution, and the entire fix lands tonight through one firmware update to UEFI 1.110.13.

## Explanation path
Start with what the machine is: the DGX Spark boots through UEFI firmware, the layer underneath DGX OS, so a flaw there sits below the operating system the viewer manages. Then land the event: on 2026-08-25 NVIDIA published security bulletin 5867 covering five CVEs in that firmware layer, all of them fixed in the same version, 1.110.13. Before the impact can land, the viewer needs what "privileged attacker" means here -- the vector is AV:L, local, with PR:H, privileges required high, which bounds the scare honestly: this is not a remote hole, it is a foothold an attacker who is already inside uses to get bigger. With that understood, the impacts of the 8.2 HIGH flaws follow: code execution, escalation of privileges, denial of service, information disclosure, data tampering. Close on the action, which is the reason the video exists: the DGX Dashboard or five terminal commands -- apt update, apt dist-upgrade, fwupdmgr refresh, fwupdmgr upgrade, reboot -- carry the machine to UEFI 1.110.13, and the viewer can check the version and run it tonight.

## Claims
1. **NVIDIA's August 2026 DGX Spark security bulletin addresses five CVEs dated 2026-08-25, and every one of them is fixed by updating the firmware to version 1.110.13.**
   - Source: Security Bulletin: NVIDIA DGX Spark - August 2026, https://nvidia.custhelp.com/app/answers/detail/a_id/5867/~/security-bulletin%3A-nvidia-dgx-spark---august-2026
   - Tier: primary | Confidence: high | Accessed: 2026-09-06 | Via: web_extract
   - Quote: "| CVE-2026-47626 | DGX Spark | UEFI | 0 to 1.110.12 | 1.110.13 |" (the Security Updates table lists this row identically for CVE-2026-47624, CVE-2026-24263, CVE-2026-24262 and CVE-2026-24225; Revision History: "1.0 | 2026-08-25 | Initial Release")
2. **CVE-2026-24262 is an out-of-bounds write in the DGX Spark system firmware, scored 8.2 HIGH, where a successful exploit may lead to code execution, escalation of privileges, denial of service, information disclosure, and data tampering.**
   - Source: Security Bulletin: NVIDIA DGX Spark - August 2026, https://nvidia.custhelp.com/app/answers/detail/a_id/5867/~/security-bulletin%3A-nvidia-dgx-spark---august-2026
   - Tier: primary | Confidence: high | Accessed: 2026-09-06 | Via: web_extract
   - Quote: "CVE-2026-24262 | NVIDIA DGX Spark contains a vulnerability in the system firmware, where a privileged attacker could be able to cause an out-of-bounds write. A successful exploit of this vulnerability may lead to code execution, escalation of privileges, denial of service, information disclosure, and data tampering."
3. **CVE-2026-24263 is a NULL pointer dereference in the DGX Spark system firmware, scored 8.2 HIGH, fixed in the same UEFI 1.110.13 update.**
   - Source: NVD-CVE-2026-24263, https://nvd.nist.gov/vuln/detail/CVE-2026-24263
   - Tier: primary | Confidence: high | Accessed: 2026-09-06 | Via: web_extract
   - Quote: "NVIDIA DGX Spark contains a vulnerability in the system firmware, where a privileged attacker could be able to cause a NULL pointer dereference. A successful exploit of this vulnerability may lead to code execution, escalation of privileges, denial of service, information disclosure, and data tampering."
4. **Both CVEs affect every DGX Spark firmware version from 0 to 1.110.12, and NVD published them on Aug 25, 2026.**
   - Source: NVD-CVE-2026-24262, https://nvd.nist.gov/vuln/detail/CVE-2026-24262
   - Tier: primary | Confidence: high | Accessed: 2026-09-06 | Via: web_extract
   - Quote: "Affected 0 to 1.110.12" and "NVD Published Date: Aug 25, 2026" (the CVE-2026-24263 page shows the identical version range and publish date)
5. **NVIDIA's documented manual update path is five terminal commands, and the DGX Dashboard is the recommended alternative.**
   - Source: OS and Component Update Guide -- DGX Spark User Guide, https://docs.nvidia.com/dgx/dgx-spark/os-and-component-update.html
   - Tier: primary | Confidence: high | Accessed: 2026-09-06 | Via: web_extract
   - Quote: "sudo apt update / sudo apt dist-upgrade / sudo fwupdmgr refresh / sudo fwupdmgr upgrade / sudo reboot" and "The DGX Dashboard is the **primary and recommended** way to perform system updates on your DGX Spark."
6. **The current DGX Spark software stack ships UEFI 1.110.13, the fixed version, alongside DGX OS 7.5.0 and GPU driver 580.159.03.**
   - Source: DGX Spark Release Notes, https://docs.nvidia.com/dgx/dgx-spark/release-notes.html
   - Tier: primary | Confidence: high | Accessed: 2026-09-06 | Via: web_extract
   - Quote: "| NVIDIA DGX OS | 7.5.0 | ... | UEFI | 1.110.13 | NVIDIA GPU Driver | 580.159.03 |"
7. **The attacker in both CVEs must already be a privileged local user: the CVSS 3.1 vector is AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H.**
   - Source: NVD-CVE-2026-24262, https://nvd.nist.gov/vuln/detail/CVE-2026-24262
   - Tier: primary | Confidence: high | Accessed: 2026-09-06 | Via: web_extract
   - Quote: "CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H"
8. **NVIDIA thanks one researcher, Alex Matrosov, for reporting four of the five flaws including both CVEs in this video.**
   - Source: Security Bulletin: NVIDIA DGX Spark - August 2026, https://nvidia.custhelp.com/app/answers/detail/a_id/5867/~/security-bulletin%3A-nvidia-dgx-spark---august-2026
   - Tier: primary | Confidence: high | Accessed: 2026-09-06 | Via: web_extract
   - Quote: "CVE-2026-47626, CVE-2026-24263, CVE-2026-24262, CVE-2026-24225: Alex Matrosov"
9. **The Canadian Centre for Cyber Security republished the advisory as AV26-849, confirming DGX Spark versions prior to 1.110.13 are the affected population.**
   - Source: NVIDIA security advisory (AV26-849), https://www.cyber.gc.ca/en/alerts-advisories/nvidia-security-advisory-av26-849
   - Tier: docs | Confidence: high | Accessed: 2026-09-06 | Via: web_extract
   - Quote: "NVIDIA DGX Spark - Versions prior to 1.110.13"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | CVSS 3.1 base score of CVE-2026-24262 and CVE-2026-24263 (NVIDIA CNA) | 8.2 HIGH | https://nvidia.custhelp.com/app/answers/detail/a_id/5867/~/security-bulletin%3A-nvidia-dgx-spark---august-2026 | "Base Score: 8.2 HIGH" |
| 2 | Affected firmware versions | 0 to 1.110.12 | https://nvd.nist.gov/vuln/detail/CVE-2026-24262 | "Affected 0 to 1.110.12" |
| 3 | Fixed UEFI version | 1.110.13 | https://nvidia.custhelp.com/app/answers/detail/a_id/5867/~/security-bulletin%3A-nvidia-dgx-spark---august-2026 | "Updated Version: 1.110.13" |
| 4 | CVEs addressed in the August 2026 bulletin | 5 | https://nvidia.custhelp.com/app/answers/detail/a_id/5867/~/security-bulletin%3A-nvidia-dgx-spark---august-2026 | bulletin Details table lists CVE-2026-24262, CVE-2026-47626, CVE-2026-24263, CVE-2026-24225, CVE-2026-47624 |
| 5 | Bulletin initial release date | 2026-08-25 | https://nvidia.custhelp.com/app/answers/detail/a_id/5867/~/security-bulletin%3A-nvidia-dgx-spark---august-2026 | "1.0 | 2026-08-25 | Initial Release" |
| 6 | Terminal commands in NVIDIA's documented manual update path | 5 | https://docs.nvidia.com/dgx/dgx-spark/os-and-component-update.html | "sudo apt update / sudo apt dist-upgrade / sudo fwupdmgr refresh / sudo fwupdmgr upgrade / sudo reboot" |
| 7 | Ubuntu Pro OS support term included with DGX Spark | 10-year | https://docs.nvidia.com/dgx/dgx-spark/os-and-component-update.html | "The Ubuntu Pro OS license in DGX Spark includes 10-year OS support from Canonical." |

## Analogy candidates
- **Locked display case inside an already-locked shop**: the DGX Spark is a shop with a locked front door (your OS login), and the UEFI firmware is a display case inside holding the most valuable goods; the CVEs are a flaw in the case's lock that only matters once someone is already inside the shop, but once they are, it hands them the goods, the alarm code and the keys to the till. Breaks when: the shop analogy implies goods stay inside one room, while a UEFI compromise is S:C, scope changed, meaning the escape reaches beyond the firmware component into the whole system -- the case does not just open, it dissolves into the shop.

## Misconceptions
- Myth: "A firmware CVE scoring 8.2 HIGH means strangers on the internet can walk into my DGX Spark tonight." Reality: the CVSS 3.1 vector is AV:L/AC:L/PR:H, attack vector local and privileges required high, so the attacker must already hold privileged local access; the flaw is how a foothold escalates, not how one begins (claims 2, 3, 7).
- Myth: "Ubuntu keeps my DGX Spark firmware patched automatically, same as any apt package." Reality: the fixed UEFI version arrives through a firmware update -- NVIDIA's documented path runs fwupdmgr refresh then fwupdmgr upgrade after the apt steps, or the DGX Dashboard, and versions prior to 1.110.13 remain vulnerable until that update lands (claims 1, 5, 9).

## Glossary
- **UEFI**: the firmware layer that boots the DGX Spark and sits underneath the operating system, which is where all five CVEs live.
- **CVE**: a public catalog entry giving a reported security flaw a standard ID so vendors and users refer to the same bug.
- **CVSS 3.1 base score**: a 0.0 to 10.0 severity rating for a vulnerability; 8.2 falls in the HIGH band.
- **out-of-bounds write**: a bug where a program writes past the end of its allotted memory, letting an attacker corrupt adjacent data or code.
- **NULL pointer dereference**: a bug where the firmware follows a pointer that points at nothing, which can crash the system or, in some cases, be steered into executing attacker code.
- **fwupdmgr**: the Linux command-line tool that downloads and installs firmware updates on the DGX Spark, including the UEFI 1.110.13 fix.
- **DGX Dashboard**: the recommended graphical interface on the DGX Spark for installing system, driver and firmware updates.
- **privileged attacker**: an attacker who already holds elevated, local access to the machine, the prerequisite for all five CVEs in this bulletin.

## Unverified
- No source fetched this run states whether any of the five CVEs is exploited in the wild.
- No source fetched this run gives the date the 1.110.13 UEFI image itself shipped or the bulletin's "Updated 08/21/2026" header relates to the 2026-08-25 revision date; treat the release date as 2026-08-25.
- Community reports suggest the update completes in under fifteen minutes, but no source fetched this run states a firmware update duration; frame it as "one sitting," not a number.
- No source fetched this run states whether GB10 partner systems such as the Dell Pro Max with GB10 receive the 1.110.13 fix at the same time as the Founders Edition.
- No source fetched this run confirms the exact UEFI version shipping on a brand-new DGX Spark delivered this week.

## Suggested outline
1. Hook: NVIDIA just rated two flaws in your DGX Spark's boot firmware 8.2 out of 10 -- and the fix is five commands you can run tonight.
2. What the machine is: UEFI is the firmware underneath DGX OS, so these bugs live below the Linux you administrate.
3. The event: security bulletin 5867, dated 2026-08-25, five CVEs, every version from 0 to 1.110.12 affected, all fixed in one update.
4. What broke, honestly: CVE-2026-24262 is an out-of-bounds write and CVE-2026-24263 a NULL pointer dereference, both 8.2 HIGH, both turning an already-privileged local attacker into code execution and full tampering.
5. The honest catch: the vector says privileged local attacker, so this is not a remote hole -- it is why the box under your desk still needs the patch.
6. The action tonight: DGX Dashboard, or apt update, apt dist-upgrade, fwupdmgr refresh, fwupdmgr upgrade, reboot -- land on UEFI 1.110.13.

## Viewer situation
You have a DGX Spark on your desk running AI workloads, and you have never touched its firmware.

## Has process
true
- Open the DGX Dashboard and install available updates, or open a terminal on the Spark.
- Run sudo apt update, then sudo apt dist-upgrade.
- Run sudo fwupdmgr refresh, then sudo fwupdmgr upgrade, and approve the UEFI 1.110.13 update when prompted.
- Reboot the machine to apply the firmware update.
- Confirm the UEFI version now reads 1.110.13.

## Objection
The CVSS vector requires a privileged local attacker, so if nobody hostile already has root on my Spark there is nothing to exploit and the patch can wait for the next maintenance window.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://nvidia.custhelp.com/app/answers/detail/a_id/5867/~/security-bulletin%3A-nvidia-dgx-spark---august-2026 | Security Bulletin: NVIDIA DGX Spark - August 2026 | primary | web_extract | 2026-09-06 |
| 2 | https://nvd.nist.gov/vuln/detail/CVE-2026-24262 | NVD-CVE-2026-24262 | primary | web_extract | 2026-09-06 |
| 3 | https://nvd.nist.gov/vuln/detail/CVE-2026-24263 | NVD-CVE-2026-24263 | primary | web_extract | 2026-09-06 |
| 4 | https://docs.nvidia.com/dgx/dgx-spark/os-and-component-update.html | OS and Component Update Guide -- DGX Spark User Guide | primary | web_extract | 2026-09-06 |
| 5 | https://docs.nvidia.com/dgx/dgx-spark/release-notes.html | DGX Spark Release Notes | primary | web_extract | 2026-09-06 |
| 6 | https://www.cyber.gc.ca/en/alerts-advisories/nvidia-security-advisory-av26-849 | NVIDIA security advisory (AV26-849) | docs | web_extract | 2026-09-06 |
| 7 | https://github.com/NVIDIA/product-security/tree/main/2026/5867 | NVIDIA/product-security: 2026/5867 | primary | web_extract | 2026-09-06 |
| 8 | https://www.nvidia.com/en-us/product-security/ | NVIDIA Product Security | primary | web_extract | 2026-09-06 |
| 9 | https://www.servethehome.com/nvidia-dgx-spark-and-dell-partner-gb10-firmware/ | NVIDIA DGX Spark and Partner GB10 Firmware | benchmark | web_extract | 2026-09-06 |

## Notes
Conflict: the confirmed angle describes both CVEs as out-of-bounds writes, but NVIDIA's bulletin classifies CVE-2026-24263 as a NULL pointer dereference (CWE-476); out-of-bounds write (CWE-787) applies to CVE-2026-24262 and CVE-2026-47626. The brief follows the primary source; the script should say "an out-of-bounds write and a NULL pointer dereference" or "two system-firmware flaws." The angle is otherwise intact: both are system-firmware flaws, both 8.2 HIGH, both fixed in 1.110.13. Tooling: web_search plus web_extract only; FireCrawl not available in this environment. 4 searches, 9 page fetches, 0 failures. ServeTheHome fetched as the independent walk-through of the same firmware-update procedure. NVD is NVD enrichment pending but mirrors NVIDIA's CNA data verbatim, including the 8.2 score.
