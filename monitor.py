#! /usr/bin/env python3


#Coder: akrecH
#Github: https://github.com/akr3ch


import os,sys
from time import sleep
from termcolor import cprint

user = os.getuid()

if user != 0:
    cprint('[!]run ','red',attrs=['bold'],end='')
    cprint('sudo '+sys.argv[0],'yellow',attrs=['bold'])
else:
    cprint('Permforming apt update & apt upgrade...','green',attrs=['bold'])
    try:
       os.system('sudo apt-get update -y && sudo apt-get full-upgrade -y 2>/dev/null')
       cprint('Installing required packages...','green',attrs=['bold'])

       #install dkms and bc
       os.system('sudo apt install dkms bc -y 2>/dev/null')
        
       #install the required linux header
       cprint('Installing the letest linux header...','green',attrs=['bold'])
       os.system('sudo apt install linux-headers-$(uname -r) -y 2>/dev/null')

       #clone the required driver
       cprint('Cloning the required driver for the adapter...','green',attrs=['bold'])
       os.system('git clone https://github.com/Munazirul/rtl8188eus')
       
       #removes the current driver
       cprint('Removing the current installed driver...','green',attrs=['bold'])
       os.system('sudo rmmod r8188eu.ko 2>/dev/null')
    
       cprint('Adding r8188eu to blacklist...','green',attrs=['bold'])
       sleep(1)
       os.system('sudo echo "blacklist r8188eu" > /etc/modprobe.d/realtek.conf')
       sleep(1)
    
       #no idea :)
       cprint('Making all files...','green',attrs=['bold'])
       os.system('cd rtl8188eus;make;sudo make install;sudo modprobe 8188eu')

       #ask user for reboot
       cprint('[+]Process complete...\n[*]Reboot to apply all changes? [y/n]','green',attrs=['bold'])
       i=input('>>')
       if i == 'y':
           os.system('reboot')
       else:
           pass

    except(KeyboardInterrupt):
          cprint('[!]Process cancelled by user','red',attrs=['bold'])
          sys.exit(0)
