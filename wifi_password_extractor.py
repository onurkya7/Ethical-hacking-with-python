import subprocess
import re

command1 = "netsh wlan show profiles"
networks = subprocess.check_output(command1, shell=True, text=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)', networks)
final_output = ""

for network in network_list:
    command2 = f"netsh wlan show profile name=\"{network}\" key=clear"
    one_network_result = subprocess.check_output(command2, shell=True, text=True)
    final_output += one_network_result

print(final_output)

with open("wifipasswords.txt", 'w', encoding='utf-8') as file:
    file.write(final_output)
