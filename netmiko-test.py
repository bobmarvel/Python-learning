from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.234.99',
    'username': 'python',
    'password': 'Cisco123',
    'port': 22,
}

#CREATE ssh connect handler for the router
ssh = ConnectHandler(**cisco_router)
#enter enable 
ssh.enable()
#use send command function to send command, print to recieve it
result = ssh.send_command('show ip route')
print (result)

