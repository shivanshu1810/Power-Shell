# Python IT Utilities

Five small command-line tools for everyday IT support tasks. Python 3 standard library only, nothing to install.

| Script | What it does | Example |
|--------|--------------|---------|
| `subnet_calculator.py` | Shows network, broadcast, masks, and usable range for an IP/prefix | `python subnet_calculator.py 192.168.1.10/24` |
| `password_generator.py` | Generates strong temporary passwords for onboarding | `python password_generator.py 16 5` |
| `port_checker.py` | Checks whether common ports (HTTP, RDP, SSH, etc.) are open on a host | `python port_checker.py 192.168.1.20 3389 22` |
| `file_organizer.py` | Sorts a messy folder into folders by file type (preview first) | `python file_organizer.py ~/Downloads --apply` |
| `ping_sweep.py` | Finds live hosts on a small network (/24 or smaller) | `python ping_sweep.py 192.168.1.0/24` |

## Why I built these
Each one covers a task I'd run into on a service desk: planning a subnet, setting up a new user, troubleshooting "the app can't connect", cleaning up a user's files, and checking what's online.

## Notes
- `file_organizer.py` only previews unless you add `--apply`, and never overwrites existing files.
- `ping_sweep.py`: only scan networks you own or have permission to scan. Some devices block ping, so a silent host isn't always offline.
- `port_checker.py`: "closed/filtered" means no connection was made. It can't tell a closed port from a firewall block.

## Testing
Tested on Linux with Python 3.12. [Add: tested on Windows 11 with Python ___ once you've run them there.]
