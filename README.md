# CLOAS Simulator - Legacy Life Insurance Policy Administration System

A Python-based terminal simulation of **CLOAS** (Computations Life Office Administration System), a fictional but realistic legacy COBOL/CICS mainframe policy administration system from the 1970s–1980s era.

This program recreates the classic "green screen" experience with authentic layout, PF-key navigation, and end-to-end workflow for life insurance operations.

## Features

- Classic IBM 3270-style green-on-black terminal interface
- Full PF-key simulation:
  - **X** → Exit program (PF3)
  - **B** → Back one level (PF7)
  - **M** → Return to Main Menu (PF12)
  - **Enter** (blank) → Proceed / continue
- Complete workflow:
  - New Business → Underwriting → Policy Issuance → Inquiry
  - Policy maintenance, client updates, payments, claims
- Dynamic data updates (in-memory)

## Project Structure

cloas_simulator.py
│
├── Main Program
│   └── main_menu() - Central navigation loop
│
├── Core Functions
│   ├── clear_screen()          - Terminal clearing & color setup
│   ├── print_header()          - Top banner with title
│   ├── print_footer()          - PF keys + version/date
│   ├── get_input()             - Standard input
│   ├── check_pf_keys()         - Handles X/M/B (but treats blank as back)
│   └── get_required_input()    - For data entry sequences (blank proceeds)
│
├── Menu Modules (1–8)
│   ├── 1. policy_inquiry()          - Search and display policy details
│   ├── 2. new_business()            - Create new application → adds to underwriting queue
│   ├── 3. policy_maintenance()      - Address, beneficiary, loan, reinstatement updates
│   ├── 4. client_details()          - Search client → view & update phone/email
│   ├── 5. payments_billing()        - View history → record new payment
│   ├── 6. claims()                  - Lodge new claim with policy, amount, reason
│   ├── 7. underwriting()            - Review cases → Accept (creates policy), Load, Decline, Require Info
│   └── 8. reports()                 - In-force listing, premium summary, lapsed policies
│
└── Data (in-memory dictionaries)
├── policies        - Issued policies (POLxxx)
├── pending_cases   - New business awaiting underwriting (NBxxx)
├── clients         - Client master records
└── payments_log    - Payment history per policy


## How to Run

### Requirements
- Python 3.6+
- Run in a terminal that supports ANSI colors:
  - **Recommended**: Windows Terminal, PowerShell, Command Prompt, or any Linux/macOS terminal

### Execution
```bash
python cloas_simulator.py

Navigation Guide

Type menu numbers 1–8 to select options
Use these keys on any screen:
X or x → Exit program immediately
M or m → Return to Main Menu
B or b → Go back one screen
Enter (blank) → Continue / proceed to next field

All inputs are case-insensitive

Sample Workflow

2 → New Business
Enter client name, product, sum assured → Confirmation + NBxxx reference
7 → Underwriting
See new case → Select it → Type A → Policy issued (POLxxx created)
1 → Policy Inquiry
Enter new POL number → Full policy details displayed
6 → Claims
Leave claim number blank → Enter → Provide policy, amount, reason → Claim lodged with reference
5 → Payments & Billing
Record payments → History updated and viewable

Notes

All data is stored in memory — resets on program exit
Designed for educational/demonstration purposes to show legacy mainframe UX
No external dependencies — pure Python standard library + ANSI colors

Future Enhancements (Ideas)

Save/load data to JSON file
Add claim history and status tracking
Implement existing claim inquiry
Add valuation and commission reports
Simulate batch processing / overnight runs


Enjoy your journey back to the golden age of mainframe insurance systems! 🖥️💚
Built with ❤️ for legacy system enthusiasts
