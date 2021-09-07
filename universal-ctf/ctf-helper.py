import os
import time
import sys
# Importing version number so I only have to update it once
sys.path.insert(0, '../')
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

Universal CTF | {VERSION}
Creator: Hifumi Sec (https://github.com/Hifumi-Sec)
Open-Source: https://github.com/Hifumi-Sec/universal-ctf
''')

print("Available options: \n[1] => Recon \n[2] => Exploit\n")
universal_ctf = input("What type of commands are you looking for: ")

if universal_ctf == "1":

    # Ip address for recon - may eventually add ports
    ip_address = input("Please enter the IP address (Target): ")
    # port = input("Please enter the port: ")

    print(color_scheme(0,140,255,'[*]'), f'Time to recon {ip_address}')
    time.sleep(1)

    # Handles the Nmap command for scanning ports
    def nmapScanner():
        print(f"Default command: nmap -sC -sV {ip_address}")
        shall_we_continue = input("Do You Want To Continue? [y/n] ")
        if shall_we_continue == "y":
            os.system(f'nmap -sC -sV {ip_address}')
        elif shall_we_continue == "n":
            flags = input("Which flags would you like to use (ex: -sV): ")
            print(f'New command: nmap {flags} {ip_address}')

            shall_we_continue_2 = input("Do You Want To Continue? [y/n] ")
            if shall_we_continue_2 == "y":
                os.system(f'nmap {flags} {ip_address}')
            else:
                print("Closing...")

    print("1: Nmap")
    options = input("Please choose your command: ")

    if options == "1":
        nmapScanner()
    else:
        print("Doesn't exist yet! ⊙﹏⊙")

elif universal_ctf == "2":
    
    # ip_address = input("Please enter the IP address for the VM/box: ")
    # port = input("Please enter the port: ")

    print(color_scheme(0,140,255,'[*]'), f'Time to obliterate this machine!')
    time.sleep(1)

    # msfconsole command - all this does for now is boot it up, options for flags are available
    def metasploitAttack():
        print(f"Default command: msfconsole")
        shall_we_continue = input("Do You Want To Continue? [y/n] ")
        if shall_we_continue == "y":
            os.system(f'msfconsole')
        elif shall_we_continue == "n":
            flags = input("Which flags would you like to use (ex: -q): ")
            print(f'New command: msfconsole {flags}')
            
            shall_we_continue_2 = input("Do You Want To Continue? [y/n] ")
            if shall_we_continue_2 == "y":
                os.system(f'msfconsole {flags}')
            else:
                print("Closing...")

    print("1: Msfconsole")
    options = input("Please choose your command: ")

    if options == "1":
        metasploitAttack()
    else:
        print("Doesn't exist yet! ⊙﹏⊙")

else:
    print("Something went wrong")