#I don't recommend executing this python file. It might give your computer a stroke. These commands are just examples of how each method works.

from NordVPN import NordVPN

#Note: You only need to specify the nordvpn.exe if it is different from the path stated below
nordPath = '"C:\\Program Files\\NordVPN\\nordvpn.exe"'

#Quick Connects to the fastest server
NordVPN.quickConnect()


NordVPN.establishDedicatedConnection(nordPath=nordPath)
NordVPN.establishDoubleConnection()
NordVPN.establishObfuscatedConnection()
NordVPN.establishOnionConnection()
NordVPN.establishP2PConnection()
#include what countries to randomly select from. You can choose not to include your own list of countries and it will use a hard coded list
NordVPN.establishRandomConnection(countries=['Germany', 'Sweden', 'United Kingdom'])
NordVPN.customCountryConnection('Japan')
NordVPN.customServerConnection('example_server')