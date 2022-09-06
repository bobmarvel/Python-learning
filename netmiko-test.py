from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.234.3',
    'username': 'test',
    'password': 'Test123',
    'secret': 'Test123',
    'port': 22,
}

ssh = ConnectHandler(**cisco_router)

ssh.enable()

result = ssh.send_command('show ip int br')
print (result)

