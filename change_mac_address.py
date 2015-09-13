from random import randint
from subprocess import call


def wifi_down():
    call(['sudo', 'ip', 'link', 'set', 'dev', 'wlan0', 'down'])

def wifi_up():
    call(['sudo', 'ip', 'link', 'set', 'dev', 'wlan0', 'up'])

def generate_mac():
    mac_address = ':'.join([get_hex_pair() for _ in range(6)])
    return mac_address

def decimal_to_hex(n):
    """Takes a number from 0 to 15 and returns the hex digit."""
    return(hex(n)[2:])

def get_hex_pair():
    x = str(decimal_to_hex(randint(0, 15)))
    y = str(decimal_to_hex(randint(0, 15)))
    return x + y

