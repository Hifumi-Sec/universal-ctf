import os, time, random
from subprocess import getoutput

VERSION = 'v1.1.11'

def color_scheme(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

banner = f'''\033[91m +
██╗   ██╗███╗   ██╗██╗██╗   ██╗███████╗██████╗ ███████╗ █████╗ ██╗          ██████╗████████╗███████╗
██║   ██║████╗  ██║██║██║   ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║         ██╔════╝╚══██╔══╝██╔════╝
██║   ██║██╔██╗ ██║██║██║   ██║█████╗  ██████╔╝███████╗███████║██║         ██║        ██║   █████╗  
██║   ██║██║╚██╗██║██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══██║██║         ██║        ██║   ██╔══╝  
╚██████╔╝██║ ╚████║██║ ╚████╔╝ ███████╗██║  ██║███████║██║  ██║███████╗    ╚██████╗   ██║   ██║     
 ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝     ╚═════╝   ╚═╝   ╚═╝ 
                                                {VERSION}
'''

print("-" * 100)
print(f'''
{banner}
{color_scheme(0, 140, 255, '[*]')}Universal CTF | {VERSION}
{color_scheme(0, 140, 255, '[$]')}Creator: Hifumi1337 (https://github.com/Hifumi1337)
{color_scheme(0, 140, 255, '[$]')}Open-Source: https://github.com/Hifumi1337/universal-ctf
''')
print("-" * 100)

whoami = getoutput("whoami")

while True:
    print("Available options:\n")
    print(f"[0] {color_scheme(0, 140, 255, '=>')} Recon")
    print(f"[1] {color_scheme(255, 0, 0, '=>')} Exploit\n")

    universal_ctf = input(f"{whoami}@CTF-Shell~$ ")

    # Handles the random messages appearing during each reboot
    random_recon_dict = ["Time to recon", "Recon time, it is", "Enumeration sensation", "R3c0n T1m3"]
    random_recon = random.choice(random_recon_dict)
    random_exploit_dict = ["Time to obliterate!", "Exploitation, more like destroy all humans", "Exploitation is my middle name!"]
    random_exploit = random.choice(random_exploit_dict)

    if universal_ctf == "0" or universal_ctf == "recon" or universal_ctf == "Recon":
        class Recon:

            # Available commands for recon
            available_commands = {
                "0": "Nmap",
                "1": "Gobuster",
                "2": "Nikto",
                "3": "Sublist3r",
                "4": "AutoRecon",
            }

            # IP address for recon
            ip_address = input("Enter the IP address (Target): ")

            print(f"\n{color_scheme(0, 140, 255, '[*]')} {random_recon}\n")

            # Nmap
            def nmap_scanner(self):
                # print("\nTool by: Coming Soon!\n")
                print(f"Default command: nmap -sC -sV {self.ip_address}")
                
                shall_we_continue = input("Do you want to continue (y/n): ")
                
                if shall_we_continue == "y" or shall_we_continue == "yes":
                    os.system(f'nmap -sC -sV {self.ip_address}')
                elif shall_we_continue == "n" or shall_we_continue == "no":
                    flags = input("Which flags would you like to use (ex: -sV -Pn): ")
                    print(f'New command: nmap {flags} {self.ip_address}')
                    
                    shall_we_continue_2 = input("Do you want to continue (y/n): ")

                    if shall_we_continue_2 == "y":
                        os.system(f'nmap {flags} {self.ip_address}')
                    else:
                        pass
                else:
                    pass
            
            # Gobuster
            def gobuster_scanner(self):
                # print("\nTool by: Coming Soon!\n")
                print(f"Default command: gobuster dir -u {self.ip_address} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")
                
                shall_we_continue = input("Do you want to continue (y/n): ")
                
                if shall_we_continue == "y" or shall_we_continue == "yes":
                    os.system(f'gobuster dir -u {self.ip_address} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt')
                elif shall_we_continue == "n" or shall_we_continue == "no":
                    flags = input("Which flags would you like to use (ex: -e): ")
                    wordlist = input("Which wordlist would you like to use (ex: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt): ")
                    
                    print(f'New command: gobuster dir -u {self.ip_address} {flags} -w {wordlist}')
                    
                    shall_we_continue_2 = input("Do you want to continue (y/n): ")
                    
                    if shall_we_continue_2 == "y" or shall_we_continue_2 == "yes":
                        os.system(f'gobuster dir -u {self.ip_address} {flags} -w {wordlist}')
                    else:
                        pass
            
            # Nikto
            def nikto_scanner(self):
                # print("\nTool by: Coming Soon!\n")
                print(f"Default command: nikto -h {self.ip_address}")
                
                shall_we_continue = input("Do you want to continue (y/n): ")
                
                if shall_we_continue == "y" or shall_we_continue == "yes":
                    os.system(f'nikto -h {self.ip_address}')
                elif shall_we_continue == "n":
                    flags = input("Which flags would you like to use (ex: -id): ")
                    print(f'New command: nikto -h {self.ip_address} {flags}')
                    
                    shall_we_continue_2 = input("Do you want to continue (y/n): ")
                    
                    if shall_we_continue_2 == "y" or shall_we_continue_2 == "yes":
                        os.system(f'nikto -h {self.ip_address} {flags}')
                    else:
                        print('Rebooting...')
                        os.system('python3 helper.py')
            
            # Sublist3r
            def sublist3r_enum(self):
                # print("\nTool by: Coming Soon!\n")
                print(f"Default command: python3 ../tools/Sublist3r/sublist3r.py -d {self.ip_address} -e google")
                
                shall_we_continue = input("Do you want to continue (y/n): ")
                
                if shall_we_continue == "y":
                    os.system(f'python3 ../tools/Sublist3r/sublist3r.py -d {self.ip_address} -e google')
                elif shall_we_continue == "n":
                    flags = input("Which flags would you like to use (ex: -d): ")
                    print(f'New command: python3 ../tools/Sublist3r/sublist3r.py -d {self.ip_address} {flags}')
                    
                    shall_we_continue_2 = input("Do you want to continue (y/n): ")
                    
                    if shall_we_continue_2 == "y":
                        os.system(f'python3 ../tools/Sublist3r/sublist3r.py -d {self.ip_address} {flags}')
                    else:
                        print('Rebooting...')
                        os.system('python3 ctf-helper.py')
            
            # AutoRecon by @Tib3rius
            def auto_recon_enum(self):
                print("\nTool by: @Tib3rius (https://github.com/Tib3rius)\n")
                print(f"Default command: python3 ../tools/AutoRecon/autorecon.py -o ../tools/AutoRecon/Results --single-target {self.ip_address}\n")
                
                shall_we_continue = input("Do you want to continue (y/n): ")
                
                if shall_we_continue == "y" or shall_we_continue == "yes":
                    os.system(f'python3 ../tools/AutoRecon/autorecon.py -o ../tools/AutoRecon/Results --single-target {self.ip_address}')
                elif shall_we_continue == "n" and shall_we_continue == "no":
                    flags = input("Which flags would you like to use (ex: --single-target): ")
                    print(f'New command: python3 ../tools/AutoRecon/autorecon.py -o ../tools/AutoRecon/Results {flags} {self.ip_address}')
                    
                    shall_we_continue_2 = input("Do you need to fix anything (y/n): ")
                    
                    if shall_we_continue_2 == "y":
                        flags = input("Which flags would you like to use (ex: --single-target): ")
                        print(f'New command: python3 ../tools/AutoRecon/autorecon.py -o ../tools/AutoRecon/Results {flags} {self.ip_address}')
                        
                        shall_we_continue_3 = input("Do you want to continue (y/n): ")
                        
                        if shall_we_continue_3 == "y":
                            os.system(f'python3 ../tools/AutoRecon/autorecon.py -o ../tools/AutoRecon/Results {flags} {self.ip_address}')
                        else:
                            pass
                    elif shall_we_continue_2 == "n":
                        os.system(f'python3 ../tools/AutoRecon/autorecon.py -o ../tools/AutoRecon/Results {flags} {self.ip_address}')
                    else:
                        pass

            for x in available_commands:
                print(f"{color_scheme(0, 140, 255, f'[{x}]')}{available_commands[x]}")
            
            options = input("\nPlease choose your command: ")

        r = Recon()

        if r.options == "0":
            r.nmap_scanner()
        elif r.options == "1":
            r.gobuster_scanner()
        elif r.options == "2":
            r.nikto_scanner()
        elif r.options == "3":
            r.sublist3r_enum()
        elif r.options == "4":
            r.auto_recon_enum()
        else:
            pass

    elif universal_ctf == "1" or universal_ctf == "exploit":

        class Exploit:

            # Available commands for exploit
            available_commands = ['Msfconsole', 'SQLMap']

            ip_address = input("Please enter the IP address (Target): ")
            
            print(f"\n{color_scheme(255, 0, 0, '[*]')} {random_exploit}\n")

            # msfconsole
            def metasploit_attack(self):
                print(f"Default command: msfconsole")
                
                shall_we_continue = input("Do you want to continue (y/n): ")
                
                if shall_we_continue == "y":
                    os.system(f'msfconsole')
                elif shall_we_continue == "n":
                    flags = input("Which flags would you like to use (ex: -q): ")
                    print(f'New command: msfconsole {flags}')
                    
                    shall_we_continue_2 = input("Do you want to continue (y/n): ")
                    
                    if shall_we_continue_2 == "y":
                        os.system(f'msfconsole {flags}')
                    else:
                        pass
            
            # SQLMap
            def sql_map_attack(self):
                print(f"Default command: sqlmap -u {self.ip_address}")
                
                shall_we_continue = input("Do you want to continue (y/n): ")
                
                if shall_we_continue == "y":
                    os.system(f'sqlmap -u {self.ip_address}')
                elif shall_we_continue == "n":
                    flags = input("Which flags would you like to use (ex: --forms): ")
                    print(f'New command: sqlmap -u {self.ip_address} {flags}')
                    
                    shall_we_continue_2 = input("Do you want to continue (y/n)? ")
                    
                    if shall_we_continue_2 == "y":
                        os.system(f'sqlmap -u {self.ip_address} {flags}')
                    else:
                        print("Closing...")

            print(f"{color_scheme(0, 140, 255, '[0]')}{available_commands[0]}")
            print(f"{color_scheme(0, 140, 255, '[1]')}{available_commands[1]}")
            
            options = input("\nPlease choose your command: ")

        e = Exploit()

        if e.options == "0":
            e.metasploit_attack()
        elif e.options == "1":
            e.sql_map_attack()
        else:
            print("Please choose a valid option (ex: 1)")

    elif universal_ctf == "quit" or universal_ctf == "exit":
        print("Universal CTF shutdown successfully")
        exit(0)
    
    else:
        print("Something went wrong")