#!/bin/bash

############################################################
# Universal CTF | v1.0.2                                   #
# Creator: Hifumi Sec (https://github.com/Hifumi-Sec)      #
# Open-Source: https://github.com/Hifumi-Sec/universal-ctf #
############################################################

# These are all of the current commands in this tool. If you run this install script, it will check to make sure they're installed.

# Updates your current packages, so no matter which option is chosen, this makes sure it's a clean install
sudo apt update

# Installs any required modules for the ctf-helper.py script
pip install -r requirements.txt

# Nmap install
if ! which nmap > /dev/null; then
    echo -e "Command is not present. Would you like to install it? (y/n) \c"
    read user_reply
    if "$user_reply" = "y"; then
        nmap_install = "sudo apt install nmap && nmap --version"
        echo $nmap_install
    fi
else
    echo "Nmap is already installed."
fi

# Metasploit install
if ! which msfconsole > /dev/null; then
    echo -e "Command is not present. Would you like to install it? (y/n) \c"
    read user_reply
    if "$user_reply" = "y"; then
        # Depending on how your system is set up (and user permissions), you may have to add sudo in appropiate places (If you get a connection error, then you need PostgreSQL installed)
        metasploit_install = "mkdir msf_framework && cd msf_framework && curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && sudo chmod 755 msfinstall && ./msfinstall && msfconsole --version"
        echo $metasploit_install
    fi
else
    echo "Metasploit is already installed."
fi
