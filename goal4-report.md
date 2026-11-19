# Goal 4: Port Scan Report

## Objective
Practise reconnaissance by building a small Python tool that automates port scanning, and use it on an authorised target.

## Method
- Tool: custom Python port scanner (portscan.py) using the socket library
- Target: scanme.nmap.org (a public host that permits scanning)
- Ports checked: 21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 3389, 8080

## Findings
| Port | Service | Status |
|------|---------|--------|
| 22 | SSH | Open |
| 80 | HTTP | Open |

## Impact
Open ports show an attacker which services are running. SSH could be targeted with password guessing or by exploiting an outdated version, and HTTP exposes a web server that may contain vulnerable software or pages.

## Remediation
- Close or filter any ports that are not needed.
- Keep SSH and web server software patched.
- Restrict SSH access with key-based login and firewall rules.
- Monitor for repeated connection attempts.

## Lessons Learned
I learned how a port scanner works at a basic level: it attempts a connection to each port and reports which ones accept it. Writing my own tool showed me what tools like Nmap automate. A limitation is that my scanner only checks a short list of ports and does not identify service versions, which I plan to improve.
