import os
import time
import sys
import random
from tabulate import tabulate
# Importing version number so I only have to update it once
sys.path.insert(0, '../config/')
from __version__ import VERSION

def color_scheme(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

# uwu
print(f'''
⣱⣿⣿⡟⡐⣰⣧⡷⣿⣴⣧⣤⣼⣯⢸⡿⠁⣰⠟⢀⣼⠏⣲⠏⢸⣿⡟⣿⣿⣿⣿⣿⣿
⣿⣿⡟⠁⠄⠟⣁⠄⢡⣿⣿⣿⣿⣿⣿⣦⣼⢟⢀⡼⠃⡹⠃⡀⢸⡿⢸⣿⣿⣿⣿⣿⡟
⣿⣿⠃⠄⢀⣾⠋⠓⢰⣿⣿⣿⣿⣿⣿⠿⣿⣿⣾⣅⢔⣕⡇⡇⡼⢁⣿⣿⣿⣿⣿⣿⢣
⣿⡟⠄⠄⣾⣇⠷⣢⣿⣿⣿⣿⣿⣿⣿⣭⣀⡈⠙⢿⣿⣿⡇⡧⢁⣾⣿⣿⣿⣿⣿⢏⣾
⣿⡇⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢻⠇⠄⠄⢿⣿⡇⢡⣾⣿⣿⣿⣿⣿⣏⣼⣿
⣿⣷⢰⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢰⣧⣀⡄⢀⠘⡿⣰⣿⣿⣿⣿⣿⣿⠟⣼⣿⣿
⢹⣿⢸⣿⣿⠟⠻⢿⣿⣿⣿⣿⣿⣿⣿⣶⣭⣉⣤⣿⢈⣼⣿⣿⣿⣿⣿⣿⠏⣾⣹⣿⣿
⢸⠇⡜⣿⡟⠄⠄⠄⠈⠙⣿⣿⣿⣿⣿⣿⣿⣿⠟⣱⣻⣿⣿⣿⣿⣿⠟⠁⢳⠃⣿⣿⣿
⠄⣰⡗⠹⣿⣄⠄⠄⠄⢀⣿⣿⣿⣿⣿⣿⠟⣅⣥⣿⣿⣿⣿⠿⠋⠄⠄⣾⡌⢠⣿⡿⠃
⠜⠋⢠⣷⢻⣿⣿⣶⣾⣿⣿⣿⣿⠿⣛⣥⣾⣿⠿⠟⠛⠉⠄⠄⠄⠄⣾⡌⢠⣿⡿⠃

██╗   ██╗███╗   ██╗██╗██╗   ██╗███████╗██████╗ ███████╗ █████╗ ██╗          ██████╗████████╗███████╗
██║   ██║████╗  ██║██║██║   ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║         ██╔════╝╚══██╔══╝██╔════╝
██║   ██║██╔██╗ ██║██║██║   ██║█████╗  ██████╔╝███████╗███████║██║         ██║        ██║   █████╗  
██║   ██║██║╚██╗██║██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══██║██║         ██║        ██║   ██╔══╝  
╚██████╔╝██║ ╚████║██║ ╚████╔╝ ███████╗██║  ██║███████║██║  ██║███████╗    ╚██████╗   ██║   ██║     
 ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝     ╚═════╝   ╚═╝   ╚═╝     

Universal CTF | {VERSION}
Creator: Hifumi Sec (https://github.com/Hifumi-Sec)
Open-Source: https://github.com/Hifumi-Sec/universal-ctf
Support The Dev: https://github.com/sponsors/Hifumi-Sec
''')
print("-" * 100)

print("Available options:\n")
print('[1]', color_scheme(0,140,255,'=>'),'Recon')
print('[2]', color_scheme(255,0,0,'=>'),'Exploit\n')
universal_ctf = input("What type of commands are you looking for: ")

# Handles the random messages appearing during each iteration
randomReconDict = ["Time to recon", "Recon time, it is", "Enumeration sensation"]
randomRecon = random.choice(randomReconDict)
randomExploitDict = ["Time to obliterate!"]
randomExploit = random.choice(randomExploitDict)


if universal_ctf == "1":

    # available commands for recon
    available_commands = [
        [1, 'Nmap', 'nmap -h'], 
        [2, 'Gobuster', 'gobuster -h'],
        [3, 'Nikto', 'nikto -H'],
        [4, 'Sublist3r', 'python3 ../tools/Sublist3r/sublist3r.py -h']
    ]

    # Ip address for recon - may eventually add ports
    ip_address = input("Please enter the IP address (Target): ")

    print('\n' + color_scheme(0,140,255,'[*]'), randomRecon + '\n')
    time.sleep(1)

    # Handles the Nmap command for scanning ports
    def nmapScanner():
        print(f"Default command: nmap -sC -sV {ip_address}")
        shall_we_continue = input("Do You Want To Continue (y/n): ")
        if shall_we_continue == "y":
            os.system(f'nmap -sC -sV {ip_address}')
        elif shall_we_continue == "n":
            flags = input("Which flags would you like to use (ex: -sV): ")
            print(f'New command: nmap {flags} {ip_address}')
        else:
            print("Closing...")

            shall_we_continue_2 = input("Do You Want To Continue (y/n): ")
            if shall_we_continue_2 == "y":
                os.system(f'nmap {flags} {ip_address}')
            else:
                print("Closing...")
    
    # Handles uri enumeration using Gobuster
    def gobusterScanner():
        print(f"Default command: gobuster dir -u {ip_address} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")
        shall_we_continue = input("Do You Want To Continue (y/n): ")
        if shall_we_continue == "y":
            os.system(f'gobuster dir -u {ip_address} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt')
        elif shall_we_continue == "n":
            flags = input("Which flags would you like to use (ex: -e): ")
            # command_sec = input("What type of enumeration would you like to run (ex: dir): ")
            wordlist = input("Which wordlist would you like to use (ex: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt): ")
            print(f'New command: gobuster dir -u {ip_address} {flags} -w {wordlist}')
            shall_we_continue_2 = input("Do You Want To Continue (y/n): ")
            if shall_we_continue_2 == "y":
                os.system(f'gobuster dir -u {ip_address} {flags} -w {wordlist}')
            else:
                print("Closing...")
    
    # Nikto scanner for web servers
    def niktoScanner():
        print(f"Default command: nikto -h {ip_address}")
        shall_we_continue = input("Do You Want To Continue (y/n): ")
        if shall_we_continue == "y":
            os.system(f'nikto -h {ip_address}')
        elif shall_we_continue == "n":
            flags = input("Which flags would you like to use (ex: -id): ")
            print(f'New command: nikto -h {ip_address} {flags}')
            shall_we_continue_2 = input("Do You Want To Continue (y/n): ")
            if shall_we_continue_2 == "y":
                os.system(f'nikto -h {ip_address} {flags}')
            else:
                print("Closing...")
    
    # Sublist3r command - handles subdomain enumeration
    def sublist3rEnum():
        print(f"Default command: python3 ../tools/Sublist3r/sublist3r.py -d {ip_address} -e google")
        shall_we_continue = input("Do You Want To Continue (y/n): ")
        if shall_we_continue == "y":
            os.system(f'python3 ../tools/Sublist3r/sublist3r.py -d {ip_address} -e google')
        elif shall_we_continue == "n":
            flags = input("Which flags would you like to use (ex: -d): ")
            print(f'New command: python3 ../tools/Sublist3r/sublist3r.py -d {ip_address} {flags}')
            shall_we_continue_2 = input("Do You Want To Continue (y/n): ")
            if shall_we_continue_2 == "y":
                os.system(f'python3 ../tools/Sublist3r/sublist3r.py -d {ip_address} {flags}')
            else:
                print("Closing...")

    print (tabulate(available_commands, headers=["ID", "Command", "Learn More"]))
    options = input("\nPlease choose your command: ")

    if options == "1":
        nmapScanner()
    elif options == "2":
        gobusterScanner()
    elif options == "3":
        niktoScanner()
    elif options == "4":
        sublist3rEnum()
    else:
        print("Please choose a valid option (ex: 1)")

elif universal_ctf == "2":

    # available commands for exploit
    available_commands = [
        [1, 'Msfconsole', 'The Metasploit Framework is a Ruby-based, modular penetration testing platform that enables you to execute exploits.'],
        [2, 'SQLMap', 'SQLMap is penetration testing tool that automates the process of detecting and exploiting SQL injection flaws.']
    ]
    
    # port = input("Please enter the port: ")

    ip_address = input("Please enter the IP address for the VM/box: ")
    print('\n' + color_scheme(255,0,0,'[*]'), randomExploit + '\n')
    time.sleep(1)

    # msfconsole command - all this does for now is boot it up, options for flags are available
    def metasploitAttack():
        print(f"Default command: msfconsole")
        shall_we_continue = input("Do You Want To Continue (y/n): ")
        if shall_we_continue == "y":
            os.system(f'msfconsole')
        elif shall_we_continue == "n":
            flags = input("Which flags would you like to use (ex: -q): ")
            print(f'New command: msfconsole {flags}')
            
            shall_we_continue_2 = input("Do You Want To Continue (y/n): ")
            if shall_we_continue_2 == "y":
                os.system(f'msfconsole {flags}')
            else:
                print("Closing...")
        
    def sqlMapAttack():
        print(f"Default command: sqlmap -u {ip_address}")
        shall_we_continue = input("Do You Want To Continue (y/n): ")
        if shall_we_continue == "y":
            os.system(f'sqlmap -u {ip_address}')
        elif shall_we_continue == "n":
            flags = input("Which flags would you like to use (ex: --forms): ")
            print(f'New command: sqlmap -u {ip_address} {flags}')
            
            shall_we_continue_2 = input("Do You Want To Continue (y/n)? ")
            if shall_we_continue_2 == "y":
                os.system(f'sqlmap -u {ip_address} {flags}')
            else:
                print("Closing...")

    print (tabulate(available_commands, headers=["ID", "Command", "Description"]))
    options = input("\nPlease choose your command: ")

    if options == "1":
        metasploitAttack()
    elif options == "2":
        sqlMapAttack()
    else:
        print("Please choose a valid option (ex: 1)")

else:
    print("Something went wrong")