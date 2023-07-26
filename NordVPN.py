import subprocess
import random

class NordVPN:

    # List of Countries with Servers
    servers = ['Australia', 'Austria', 'Brazil', 'Canada', 'Costa Rica', 'Denmark', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hong Kong', 'Iceland', 'Ireland', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Poland', 'Romania', 'Serbia', 'Singapore', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Turkey', 'Ukraine', 'United Kingdom', 'Vietnam']

    @staticmethod
    def windowsExecute(command, debug=False):
        # Prints the attempted command for debugging purposes
        if debug:
            print(command)
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            if debug:
                print(f"Error: {e}")

    #Dedicated IP Address
    @classmethod
    def establishDedicatedConnection(cls, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        command = f'{nordPath} -c -g "Dedicated IP"'
        cls.windowsExecute(command)
        return command

    #Double VPN
    @classmethod
    def establishDoubleConnection(cls, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        command = f'{nordPath} -c -g "Double VPN"'
        cls.windowsExecute(command)
        return command

    #Obfuscated Server
    @classmethod
    def establishObfuscatedConnection(cls, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        command = f'{nordPath} -c -g "Obfuscated Servers"'
        cls.windowsExecute(command)
        return command

    #Onion Over VPN
    @classmethod
    def establishOnionConnection(cls, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        command = f'{nordPath} -c -g "Onion Over VPN"'
        cls.windowsExecute(command)
        return command
    
    #P2P Connection
    @classmethod
    def establishP2PConnection(cls, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        command = f'{nordPath} -c -g "P2P"'
        cls.windowsExecute(command)
        return command

    #Quick Connect to the fastest server
    @classmethod
    def quickConnect(cls, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        command = f'{nordPath} -c'
        cls.windowsExecute(command)
        return command

    #Chooses a random country's vpn server
    @classmethod
    def establishRandomConnection(cls, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"', countries=[]):
        servers = cls.servers if countries == [] else countries
        country = random.choice(cls.servers)
        command = f'{nordPath} -c -g {country}'
        cls.windowsExecute(command)
        return command

    #Connects to a custom country
    @classmethod
    def customCountryConnection(cls, customCountry, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        country = random.choice(cls.servers)
        command = f'{nordPath} -c -g {customCountry}'
        cls.windowsExecute(command)
        return command

    #Connects to a custom country
    @classmethod
    def customServerConnection(cls, customServer, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        country = random.choice(cls.servers)
        command = f'{nordPath} -c -g {customServer}'
        cls.windowsExecute(command)
        return command


