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
        cls.windowsExecute(f'{nordPath} -c -g "Dedicated IP"')

    #Double VPN
    @classmethod
    def establishDoubleConnection(cls, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        cls.windowsExecute(f'{nordPath} -c -g "Double VPN"')

    #Obfuscated Server
    @classmethod
    def establishObfuscatedConnection(cls, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        cls.windowsExecute(f'{nordPath} -c -g "Obfuscated Servers"')

    #Onion Over VPN
    @classmethod
    def establishOnionConnection(cls, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        cls.windowsExecute(f'{nordPath} -c -g "Onion Over VPN"')
    
    #P2P Connection
    @classmethod
    def establishP2PConnection(cls, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        cls.windowsExecute(f'{nordPath} -c -g "P2P"')

    #Quick Connect to the fastest server
    @classmethod
    def quickConnect(cls, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        cls.windowsExecute(f'{nordPath} -c')

    #Chooses a random country's vpn server
    @classmethod
    def establishRandomConnection(cls, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        country = random.choice(cls.servers)
        cls.windowsExecute(f'{nordPath} -c -g {country}')

    #Connects to a custom country
    @classmethod
    def customCountryConnection(cls, customCountry, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        country = random.choice(cls.servers)
        cls.windowsExecute(f'{nordPath} -c -g {customCountry}')

    #Connects to a custom country
    @classmethod
    def customServerConnection(cls, customServer, nordPath='"C:\\Program Files\\NordVPN\\nordvpn.exe"'):
        country = random.choice(cls.servers)
        cls.windowsExecute(f'{nordPath} -c -g {customServer}')


