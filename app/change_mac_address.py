from random import randint
from subprocess import call


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
    mac_address = ':'.join([get_hex_pair() for _ in range(6)])
    return mac_address

def get_mac():
    pass

def set_mac(address):
    pass

if __name__ == '__main__':
    set_wifi('wlan0', 'down')

    set_wifi('wlan0', 'up')
