import os
import sys
from datetime import datetime

# ANSI colors - Classic mainframe green screen
GREEN = "\033[32m"
BLACK_BG = "\033[40m"
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"

# In-memory data
policies = {
    "POL001": {"client_name": "John Alexander Doe", "issue_date": "15/01/1985", "product_type": "Whole Life Assurance",
               "sum_assured": "100,000.00", "premium": "520.45", "status": "In Force"},
    "POL002": {"client_name": "Jane Mary Smith", "issue_date": "22/03/1990", "product_type": "Term Life",
               "sum_assured": "75,000.00", "premium": "185.60", "status": "Lapsed"},
    "POL003": {"client_name": "Robert Chen", "issue_date": "10/07/2001", "product_type": "Endowment",
               "sum_assured": "200,000.00", "premium": "1,250.00", "status": "In Force"}
}

pending_cases = {
    "NB001": {"name": "John Doe", "product": "Whole Life", "status": "Awaiting Medical", "sum": "150,000", "premium": "780.00"},
    "NB002": {"name": "Sarah Lee", "product": "Term Life", "status": "Referred", "sum": "80,000", "premium": "210.00"},
    "NB003": {"name": "Michael Brown", "product": "Endowment", "status": "Auto-approved", "sum": "300,000", "premium": "1,800.00"}
}

clients = {
    "CLI001": {"name": "John Alexander Doe", "address": "123 Legacy St, Sydney", "phone": "(02) 9876 5432", "email": "john.doe@example.com"},
    "CLI002": {"name": "Jane Mary Smith", "address": "456 Bondi Rd, Bondi", "phone": "(02) 9123 4567", "email": "jane.smith@example.com"},
    "CLI003": {"name": "Robert Chen", "address": "789 Collins St, Melbourne", "phone": "(03) 8765 4321", "email": "robert.chen@example.com"}
}

payments_log = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BLACK_BG + GREEN)

def print_header(title):
    print("=" * 80)
    print(f"{BOLD}{title.center(80)}{RESET}")
    print("-" * 80)
    print()

def print_footer():
    today = datetime.now().strftime("%d %b %Y")
    print("=" * 80)
    print(f"{CYAN}X = PF3(Exit)     B = PF7(Back)     M = PF12(Main Menu){RESET}".center(80))
    print(f"{'CLOAS v5.2 - ' + today:>80}")
    print(RESET)

def get_input(prompt=""):
    print(prompt, end="")
    return input().strip()

def check_pf_keys(user_input):
    inp = user_input.strip().lower()
    if inp == 'x':
        clear_screen()
        print(f"\n{BOLD}{'Session terminated (PF3). Goodbye.'.center(80)}{RESET}\n")
        sys.exit(0)
    elif inp == 'm':
        return 'menu'
    elif inp == 'b':
        return 'back'
    return None

def get_required_input(prompt):
    """Used for sequential data entry - blank Enter proceeds to next field, only X or M aborts"""
    while True:
        value = get_input(prompt)
        pf = check_pf_keys(value)
        if pf == 'menu':
            return 'menu'
        if pf == 'back':
            return 'back'
        return value  # blank or any value proceeds

# 6. Claims - FIXED: Blank Enter at Claim Number proceeds to new claim entry
def claims():
    clear_screen()
    print_header("CLAIMS PROCESSING")
    claim_num_input = get_input(" " * 10 + "Claim Number (blank for new): ")
    pf = check_pf_keys(claim_num_input)
    if pf == 'menu':
        return
    if pf == 'back':
        return

    # If user typed something and it's not blank, treat as existing claim inquiry (placeholder)
    if claim_num_input.strip():
        clear_screen()
        print_header("CLAIM INQUIRY")
        print(" " * 20 + f"Details for claim {claim_num_input.upper()} not yet implemented.")
        print(" " * 20 + "Press ENTER to return...")
        print_footer()
        final = get_input()
        check_pf_keys(final)
        return

    # NEW CLAIM - sequential entry
    clear_screen()
    print_header("NEW CLAIM ENTRY")

    policy_input = get_required_input(" " * 10 + "Policy Number : ")
    if policy_input == 'menu':
        return
    if policy_input == 'back':
        return
    policy = policy_input.upper()

    amount_input = get_required_input(" " * 10 + "Amount Claimed: ")
    if amount_input == 'menu':
        return
    if amount_input == 'back':
        return

    reason_input = get_required_input(" " * 10 + "Reason (Death/Maturity/Surrender): ")
    if reason_input == 'menu':
        return
    if reason_input == 'back':
        return

    # Confirmation
    clear_screen()
    print_header("CLAIM LODGED")
    print(" " * 15 + "Claim successfully lodged")
    ref = f"CLM{datetime.now().strftime('%y%m%d')}01"
    print(f" " * 15 + f"Reference: {ref}")
    print(f" " * 15 + f"Policy: {policy}  Amount: ${amount_input}  Reason: {reason_input.capitalize()}")
    print()
    print(" " * 20 + "Press ENTER to return, or X/B/M...")
    print_footer()
    final = get_input()
    check_pf_keys(final)

# All other functions (unchanged from the last working version)
# 1. Policy Inquiry
def policy_inquiry():
    while True:
        clear_screen()
        print_header("CLOAS - POLICY INQUIRY")
        print("     Policy Number: ___________")
        print()
        print(" " * 10 + "Enter Policy Number (e.g., POL001) or use X/B/M")
        print_footer()

        policy_num = get_input("\n" + " " * 20 + "Policy Number: ")
        pf = check_pf_keys(policy_num)
        if pf == 'menu' or pf == 'back':
            return

        policy_num = policy_num.upper()
        if policy_num in policies:
            p = policies[policy_num]
            clear_screen()
            print_header("POLICY INQUIRY RESULTS")
            print(f"     Policy Number : {policy_num}")
            print(f"     Client Name   : {p['client_name']}")
            print(f"     Issue Date    : {p['issue_date']}")
            print(f"     Product Type  : {p['product_type']}")
            print(f"     Sum Assured   : {p['sum_assured']}")
            print(f"     Premium       : {p['premium']}")
            print(f"     Status        : {p['status']}")
            print()
            print(" " * 20 + "Press ENTER to continue, or X/B/M...")
            print_footer()
            get_input()
            return
        elif policy_num:
            clear_screen()
            print_header("ERROR - POLICY NOT FOUND")
            print(" " * 20 + f"No record for policy {policy_num}")
            print(" " * 20 + "Press ENTER to try again...")
            print_footer()
            get_input()

# 2. New Business
def new_business():
    global pending_cases
    clear_screen()
    print_header("NEW BUSINESS ENTRY")
    print("     Enter new application details:")
    print()

    client = get_required_input(" " * 10 + "Client Name   : ")
    if client == 'menu' or client == 'back': return

    product = get_required_input(" " * 10 + "Product Type  : ")
    if product == 'menu' or product == 'back': return

    sum_ass = get_required_input(" " * 10 + "Sum Assured   : ")
    if sum_ass == 'menu' or sum_ass == 'back': return

    new_id = f"NB{len(pending_cases) + 1:03d}"
    pending_cases[new_id] = {
        "name": client or "Unknown",
        "product": product or "Unknown",
        "status": "New Application",
        "sum": sum_ass or "0.00",
        "premium": "TBC"
    }

    clear_screen()
    print_header("NEW BUSINESS - CONFIRMATION")
    print(f"     New application for: {client or 'Unknown'}")
    print(f"     Product            : {product or 'Not specified'}")
    print(f"     Sum Assured        : {sum_ass or '0.00'}")
    print()
    print(" " * 15 + "Application successfully submitted!")
    print(" " * 15 + f"Reference: {new_id} - Queued for underwriting")
    print()
    print(" " * 20 + "Press ENTER to return, or X/B/M...")
    print_footer()
    get_input()

# 3. Policy Maintenance
def policy_maintenance():
    clear_screen()
    print_header("POLICY MAINTENANCE")
    policy_num = get_input(" " * 10 + "Enter Policy Number: ")
    pf = check_pf_keys(policy_num)
    if pf == 'menu' or pf == 'back': return
    policy_num = policy_num.upper()

    if policy_num not in policies:
        clear_screen()
        print_header("ERROR")
        print(" " * 20 + "Policy not found.")
        print_footer()
        get_input()
        return

    while True:
        clear_screen()
        print_header(f"MAINTENANCE - {policy_num}")
        print("     Select action:")
        print("         A - Address Change")
        print("         B - Beneficiary Update")
        print("         L - Loan Request")
        print("         R - Reinstatement")
        print()
        action = get_input(" " * 20 + "Action: ")
        pf = check_pf_keys(action)
        if pf == 'menu' or pf == 'back': return

        if action.upper() == 'A':
            new_address = get_required_input(" " * 10 + "New Address: ")
            if new_address == 'menu' or new_address == 'back': return
            msg = "Address updated"
        elif action.upper() == 'B':
            new_beneficiary = get_required_input(" " * 10 + "New Beneficiary: ")
            if new_beneficiary == 'menu' or new_beneficiary == 'back': return
            msg = "Beneficiary updated"
        elif action.upper() == 'L':
            loan_amount = get_required_input(" " * 10 + "Loan Amount: ")
            if loan_amount == 'menu' or loan_amount == 'back': return
            msg = f"Loan of ${loan_amount} approved"
        elif action.upper() == 'R':
            msg = "Policy reinstated"
        else:
            msg = "Action completed"

        clear_screen()
        print_header("UPDATE CONFIRMATION")
        print(" " * 20 + msg)
        print()
        print(" " * 20 + "Press ENTER to continue...")
        print_footer()
        get_input()
        break

# 4. Client Details
def client_details():
    clear_screen()
    print_header("CLIENT DETAILS INQUIRY")
    search = get_input(" " * 10 + "Name or ID search: ")
    pf = check_pf_keys(search)
    if pf == 'menu' or pf == 'back': return

    matches = [cid for cid, data in clients.items() if search.upper() in data["name"].upper() or search.upper() in cid]
    if matches:
        cid = matches[0]
        clear_screen()
        print_header("CLIENT PROFILE")
        print(f"     Client ID   : {cid}")
        print(f"     Name        : {clients[cid]['name']}")
        print(f"     Address     : {clients[cid]['address']}")
        print(f"     Phone       : {clients[cid]['phone']}")
        print(f"     Email       : {clients[cid]['email']}")
        print()
        print(" " * 10 + "Update phone/email? (Y/N)")
        update = get_input(" " * 20 + "Choice: ")
        pf = check_pf_keys(update)
        if pf == 'menu' or pf == 'back': return
        if update.lower() == 'y':
            new_phone = get_required_input(" " * 10 + "New Phone: ")
            if new_phone == 'menu' or new_phone == 'back': return
            clients[cid]['phone'] = new_phone
            new_email = get_required_input(" " * 10 + "New Email: ")
            if new_email == 'menu' or new_email == 'back': return
            clients[cid]['email'] = new_email
            clear_screen()
            print_header("CLIENT UPDATED")
            print(" " * 20 + "Contact details updated.")
        print()
        print(" " * 20 + "Press ENTER to continue...")
        print_footer()
        get_input()
    else:
        clear_screen()
        print_header("NO RESULTS")
        print(" " * 20 + "No client found")
        print_footer()
        get_input()

# 5. Payments & Billing
def payments_billing():
    global payments_log
    clear_screen()
    print_header("PAYMENTS & BILLING")
    policy_num = get_input(" " * 10 + "Policy Number: ")
    pf = check_pf_keys(policy_num)
    if pf == 'menu' or pf == 'back': return
    policy_num = policy_num.upper()

    if policy_num not in policies:
        clear_screen()
        print_header("ERROR")
        print(" " * 20 + "Policy not found.")
        print_footer()
        get_input()
        return

    if policy_num not in payments_log:
        payments_log[policy_num] = []

    clear_screen()
    print_header("PAYMENT HISTORY")
    print(f"     Policy: {policy_num}")
    if payments_log[policy_num]:
        for pay in payments_log[policy_num]:
            print(f"     {pay['date']}  Premium Paid  ${pay['amount']}  {pay['method']}")
    else:
        print("     No payments recorded yet.")
    print()
    print(" " * 10 + "Record new payment? (Y/N)")
    choice = get_input(" " * 20 + "Choice: ")
    pf = check_pf_keys(choice)
    if pf == 'menu' or pf == 'back': return
    if choice.lower() == 'y':
        amount = get_required_input(" " * 10 + "Amount: ")
        if amount == 'menu' or amount == 'back': return
        method = get_required_input(" " * 10 + "Method (Direct Debit/Credit/BPAY): ")
        if method == 'menu' or method == 'back': return
        payments_log[policy_num].append({
            "date": datetime.now().strftime("%d/%m/%Y"),
            "amount": amount,
            "method": method
        })
        clear_screen()
        print_header("PAYMENT RECORDED")
        print(" " * 20 + f"${amount} recorded via {method}")
        print_footer()
        get_input()

# 7. Underwriting
def underwriting():
    global pending_cases, policies
    while True:
        clear_screen()
        print_header("UNDERWRITING WORKBENCH")
        print("     Pending New Business Cases:")
        print()
        if not pending_cases:
            print(" " * 10 + "No pending cases.")
        else:
            for case, data in pending_cases.items():
                print(f"     {case} - {data['name']:<20} {data['product']:<15} {data['status']}")
        print()
        print(" " * 10 + "Select case number for review or use X/B/M")
        print_footer()

        user_input = get_input("\n" + " " * 20 + "Case: ")
        pf = check_pf_keys(user_input)
        if pf == 'menu' or pf == 'back':
            return

        case_id = user_input.strip().upper()
        if case_id not in pending_cases:
            if case_id:
                clear_screen()
                print_header("ERROR")
                print(" " * 20 + f"Invalid case: {case_id}")
                print(" " * 20 + "Press ENTER to continue...")
                print_footer()
                get_input()
            continue

        case = pending_cases[case_id]
        while True:
            clear_screen()
            print_header(f"UNDERWRITING REVIEW - {case_id}")
            print(f"     Applicant   : {case['name']}")
            print(f"     Product     : {case['product']}")
            print(f"     Sum Assured : ${case['sum']}")
            print(f"     Premium     : ${case['premium']}")
            print(f"     Current     : {case['status']}")
            print()
            print("     Decision:")
            print("         A - Accept Standard")
            print("         L - Load/Exclude")
            print("         D - Decline")
            print("         R - Require More Info")
            print_footer()

            decision = get_input(" " * 20 + "Decision: ")
            pf = check_pf_keys(decision)
            if pf == 'menu':
                return
            if pf == 'back':
                break

            decision = decision.upper()
            if decision == "A":
                new_pol = f"POL{len(policies) + 1:03d}"
                policies[new_pol] = {
                    "client_name": case["name"],
                    "issue_date": datetime.now().strftime("%d/%m/%Y"),
                    "product_type": case["product"],
                    "sum_assured": case["sum"],
                    "premium": case["premium"] if case["premium"] != "TBC" else "Calculated",
                    "status": "In Force"
                }
                del pending_cases[case_id]
                clear_screen()
                print_header("POLICY ISSUED")
                print(" " * 20 + f"Case {case_id} accepted standard.")
                print(" " * 20 + f"New Policy Number: {new_pol}")
                print(" " * 20 + "Policy is now In Force.")
            elif decision == "L":
                case["status"] = "Loaded"
                case["premium"] = str(float(case["sum"].replace(",", "")) * 0.012)
                clear_screen()
                print_header("DECISION RECORDED")
                print(" " * 20 + f"Case {case_id} - Loaded with extra premium")
            elif decision == "D":
                case["status"] = "Declined"
                clear_screen()
                print_header("DECISION RECORDED")
                print(" " * 20 + f"Case {case_id} - Declined")
            elif decision == "R":
                case["status"] = "Further Info Required"
                clear_screen()
                print_header("DECISION RECORDED")
                print(" " * 20 + f"Case {case_id} - Further information required")
            else:
                clear_screen()
                print_header("ERROR")
                print(" " * 20 + "Invalid decision")
                print_footer()
                get_input()
                continue

            print()
            print(" " * 20 + "Press ENTER to continue...")
            print_footer()
            get_input()
            break

# 8. Reports
def reports():
    clear_screen()
    print_header("REPORTS MENU")
    print("     1. In-Force Policy Listing")
    print("     2. Premium Income Summary")
    print("     3. Lapsed Policies")
    print("     4. Claims Paid Report")
    print_footer()

    rep = get_input(" " * 20 + "Report number: ")
    pf = check_pf_keys(rep)
    if pf == 'menu' or pf == 'back': return

    clear_screen()
    print_header(f"REPORT {rep or 'CANCELLED'} - OUTPUT")
    if rep == "1":
        print(YELLOW + "POLICY     CLIENT NAME             STATUS    SUM ASSURED" + RESET)
        for pol, data in policies.items():
            if data["status"] == "In Force":
                print(f"{pol}     {data['client_name']:<23} {data['status']:<10} {data['sum_assured']}")
    elif rep == "2":
        total = sum(float(p["premium"].replace(",", "")) for p in policies.values() if p["status"] == "In Force")
        print(f"Total Annual Premium Income: ${total:,.2f}")
    elif rep == "3":
        for pol, data in policies.items():
            if data["status"] == "Lapsed":
                print(f"{pol}     {data['client_name']}")
    print()
    print(" " * 20 + "Press ENTER to return...")
    print_footer()
    get_input()

# Main Menu
def main_menu():
    while True:
        clear_screen()
        print_header("CLOAS MAIN MENU")
        print("     1. Policy Inquiry             5. Payments & Billing")
        print("     2. New Business               6. Claims")
        print("     3. Policy Maintenance         7. Underwriting")
        print("     4. Client Details             8. Reports")
        print()
        print(" " * 10 + "Select 1-8 or type X=Exit, B=Back, M=Menu")
        print_footer()

        choice = get_input(" " * 25).lower()

        if choice == 'x':
            clear_screen()
            print(f"\n{BOLD}{'Thank you for using CLOAS. Session ended.'.center(80)}{RESET}\n")
            sys.exit(0)
        elif choice == '1': policy_inquiry()
        elif choice == '2': new_business()
        elif choice == '3': policy_maintenance()
        elif choice == '4': client_details()
        elif choice == '5': payments_billing()
        elif choice == '6': claims()
        elif choice == '7': underwriting()
        elif choice == '8': reports()

if __name__ == "__main__":
    main_menu()