from random import randint
from subprocess import call

import os
import errno

def set_wifi(network_interface, status):
    """Turns the wifi on or off.
    
    Takes a string like 'wlan0' and a status like 'up' or 'down'.
    """
    if status in ['up', 'down']:
  
        call(['sudo', 'ip', 'link', 'set', 'dev', network_interface, status])

def dec_to_hex(n):
    """Takes a decimal number from 0 to 15 and returns the corresponding hex digit."""
    return hex(n)[2:]


def get_hex_pair():
    """Returns a pair of hex digits as a string like: '5f'."""
    x = str(dec_to_hex(randint(0, 15)))
    y = str(dec_to_hex(randint(0, 15)))
    return x + y


def generate_mac():
    """Returns a randomly generated MAC address.
    
    Example format: '4a:bb:19:9f:3c:cf'.
    """ 
    half_mac_address = ':'.join([get_hex_pair() for _ in range(3)])
    mac_address = "52:54:00:"+half_mac_address
    print(mac_address) 
    return mac_address

def get_interface():
    """Gets your computer's network interfaces, return an array"""
    call(['sudo', 'ip', 'link', 'show'])
    pass

def get_mac():
    """Gets the current MAC address."""
    #ip addr show wlp1s0 | grep "link/ether\b" | awk '{print $2}' | cut -d/ -f1
    call(['sudo', 'ip', 'link', network_interface, 'show'])
    pass


def set_mac(network_interface, address):
    """Sets the MAC address."""
    call(['sudo', 'ip', 'link', 'set', 'dev', network_interface, "address", address])
    pass


def main():
    """Runs the procedures to change the MAC address."""
    """list the user's interfaces"""
    network_interface = input("Which interface would you like to change: ")
    print('Turning off the wireless interface: '+ network_interface)
    set_wifi(network_interface, 'down')
    print('Finished turning off the wireless interface: '+ network_interface)
    
    address = input("Enter the MAC address you would like(press enter for to be assigned a random MAC): ")
    if address == "":
        address = generate_mac()

    print('Setting MAC address to '+ address)
    set_mac(network_interface, address) 

    print('Turning on the wireless interface: '+ network_interface)
    set_wifi(network_interface, 'up')
    print('Finished turning on the wireless interface: '+ network_interface)


if __name__ == '__main__':
    main()

