import os
import time
import sys
import random
# Importing version number so I only have to update it once
sys.path.insert(0, '../config/')
from __version__ import VERSION

def color_scheme(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

banner = '''\033[91m +
██╗   ██╗███╗   ██╗██╗██╗   ██╗███████╗██████╗ ███████╗ █████╗ ██╗          ██████╗████████╗███████╗
██║   ██║████╗  ██║██║██║   ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║         ██╔════╝╚══██╔══╝██╔════╝
██║   ██║██╔██╗ ██║██║██║   ██║█████╗  ██████╔╝███████╗███████║██║         ██║        ██║   █████╗  
██║   ██║██║╚██╗██║██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══██║██║         ██║        ██║   ██╔══╝  
╚██████╔╝██║ ╚████║██║ ╚████╔╝ ███████╗██║  ██║███████║██║  ██║███████╗    ╚██████╗   ██║   ██║     
 ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝     ╚═════╝   ╚═╝   ╚═╝ 
'''
# uwu
print(f'''
{banner}
{color_scheme(0,140,255,'[*]')}Universal CTF | {VERSION} {color_scheme(0,140,255,'[*]')}
{color_scheme(0,140,255,'[$]')}Creator: Hifumi Sec (https://github.com/Hifumi-Sec)
{color_scheme(0,140,255,'[$]')}Open-Source: https://github.com/Hifumi-Sec/universal-ctf
{color_scheme(0,140,255,'[$]')}Support The Dev: https://github.com/sponsors/Hifumi-Sec
''')
print("-" * 100)

print("Available options:\n")
print('[1]', color_scheme(0,140,255,'=>'),'Recon')
print('[2]', color_scheme(255,0,0,'=>'),'Exploit\n')
universal_ctf = input("What type of commands are you looking for: ")

# Handles the random messages appearing during each reboot
randomReconDict = ["Time to recon", "Recon time, it is", "Enumeration sensation", "R3c0n T1m3"]
randomRecon = random.choice(randomReconDict)
randomExploitDict = ["Time to obliterate!", "Exploitation, more like destroy all humans", "Exploitation is my middle name or is it man?"]
randomExploit = random.choice(randomExploitDict)


if universal_ctf == "1":

    # available commands for recon
    available_commands = ['Nmap', 'Gobuster', 'Nikto', 'Sublist3r', 'AutoRecon']

    # Ip address for recon - may eventually add ports
    ip_address = input("Please enter the IP address (Target): ")

    print('\n' + color_scheme(0,140,255,'[*]'), randomRecon + '\n')
    time.sleep(0.5)

    # Handles the Nmap command for scanning ports
    def nmapScanner():
        print(f"Default command: nmap -sC -sV {ip_address}")
        shall_we_continue = input("Do You Want To Continue (y/n): ")
        if shall_we_continue == "y":
            os.system(f'nmap -sC -sV {ip_address}')
        elif shall_we_continue == "n":
            flags = input("Which flags would you like to use (ex: -sV): ")
            print(f'New command: nmap {flags} {ip_address}')
            shall_we_continue_2 = input("Do You Want To Continue (y/n): ")
            if shall_we_continue_2 == "y":
                os.system(f'nmap {flags} {ip_address}')
            else:
                print('Rebooting...')
                os.system('python3 ctf-helper.py')
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
                print('Rebooting...')
                os.system('python3 ctf-helper.py')
    
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
                print('Rebooting...')
                os.system('python3 ctf-helper.py')
    
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
                print('Rebooting...')
                os.system('python3 ctf-helper.py')
    
    # AutoRecon by @Tib3rius
    def AutoReconEnum():
        print("\nAmazing tool by: @Tib3rius (https://github.com/Tib3rius)\n")
        print(f"Default command: python3 ../tools/AutoRecon/autorecon.py -o ../tools/AutoRecon/Results --single-target {ip_address}\n")
        shall_we_continue = input("Do You Want To Continue (y/n): ")
        if shall_we_continue == "y":
            os.system(f'python3 ../tools/AutoRecon/autorecon.py -o ../tools/AutoRecon/Results --single-target {ip_address}')
        elif shall_we_continue == "n":
            flags = input("Which flags would you like to use (ex: --single-target): ")
            print(f'New command: python3 ../tools/AutoRecon/autorecon.py -o ../tools/AutoRecon/Results {flags} {ip_address}')
            shall_we_continue_2 = input("Do you need to fix anything (y/n): ")
            if shall_we_continue_2 == "y":
                flags = input("Which flags would you like to use (ex: --single-target): ")
                print(f'New command: python3 ../tools/AutoRecon/autorecon.py -o ../tools/AutoRecon/Results {flags} {ip_address}')
                shall_we_continue_3 = input("Do You Want To Continue (y/n): ")
                if shall_we_continue_3 == "y":
                    os.system(f'python3 ../tools/AutoRecon/autorecon.py -o ../tools/AutoRecon/Results {flags} {ip_address}')
                else:
                    print("Rebooting...")
                    os.system('python3 ctf-helper.py')
            elif shall_we_continue_2 == "n":
                os.system(f'python3 ../tools/AutoRecon/autorecon.py -o ../tools/AutoRecon/Results {flags} {ip_address}')
            else:
                print('Rebooting...')
                os.system('python3 ctf-helper.py')

    print(f"""
    {color_scheme(0,140,255,'[1]')}{available_commands[0]}
    {color_scheme(0,140,255,'[2]')}{available_commands[1]}
    {color_scheme(0,140,255,'[3]')}{available_commands[2]}
    {color_scheme(0,140,255,'[4]')}{available_commands[3]}
    {color_scheme(0,140,255,'[5]')}{available_commands[4]}
    """)
    options = input("\nPlease choose your command: ")

    if options == "1":
        nmapScanner()
    elif options == "2":
        gobusterScanner()
    elif options == "3":
        niktoScanner()
    elif options == "4":
        sublist3rEnum()
    elif options == "5":
        AutoReconEnum()
    else:
        print("Please choose a valid option (ex: 1)")

elif universal_ctf == "2":

    # available commands for exploit
    available_commands = ['Msfconsole', 'SQLMap']

    ip_address = input("Please enter the IP address (Target): ")
    print('\n' + color_scheme(255,0,0,'[*]'), randomExploit + '\n')
    time.sleep(0.5)

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
    
    # Some sick SQL Injections using SQLMap
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

    print(f"""
    {color_scheme(0,140,255,'[1]')}{available_commands[0]}
    {color_scheme(0,140,255,'[2]')}{available_commands[1]}
    """)
    
    options = input("\nPlease choose your command: ")

    if options == "1":
        metasploitAttack()
    elif options == "2":
        sqlMapAttack()
    else:
        print("Please choose a valid option (ex: 1)")

else:
    print("Something went wrong")