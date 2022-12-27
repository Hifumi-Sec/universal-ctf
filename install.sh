#!/bin/bash

##############################################################
# Universal CTF                                              #
# Creator: azazelm3dj3d (https://github.com/azazelm3dj3d)    #
# Open-Source: https://github.com/azazelm3dj3d/universal-ctf #
##############################################################

# These are all of the current commands in this tool. If you run this install script, it will check to make sure they're installed.

# Updates your current packages, so no matter which option is chosen, this makes sure it's a clean install
sudo apt update

# Installs any required modules for the main script
pip install -r requirements.txt

# Nmap installer
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

# Metasploit installer
if ! which msfconsole > /dev/null; then
    echo -e "Command is not present. Would you like to install it? (y/n) \c"
    read user_reply
    if "$user_reply" = "y"; then
        # Depending on how your system is set up (and user permissions), you may have to add sudo in appropiate places (If you get a connection error, then you need PostgreSQL installed)
        metasploit_install = "cd tools && curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && sudo chmod 755 msfinstall && ./msfinstall && msfconsole --version"
        echo $metasploit_install
    fi
else
    echo "Metasploit is already installed."
fi

# Sublist3r installer
git clone https://github.com/aboul3la/Sublist3r.git
mv Sublist3r tools/
cd tools/Sublist3r
pip install -r requirements.txt
echo "Successfully installed Sublist3r"

# AutoRecon installer
git clone https://github.com/Tib3rius/AutoRecon.git
mv AutoRecon tools/
cd tools/AutoRecon
pip install -r requirements.txt
echo "Successfully installed AutoRecon"