from netmiko import ConnectHandler
cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   '10.10.20.48',
    'username': 'developer',
    'password': 'C1sco12345',
    'port' : 22,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}
loopback = {"int_name": "Loopback103",
            "description": " loopback 103",
            "ip": "1.1.1.1",
            "netmask": "255.255.255.0"}

# Create a CLI configuration
interface_config = [
    "interface {}".format(loopback["int_name"]),
    "description {}".format(loopback["description"]),
    "ip address {} {}".format(loopback["ip"], loopback["netmask"]),
    "no shut"
]
delete_loopback = [
    "no interface {}".format(loopback["int_name"])
]
net_connect = ConnectHandler(**cisco_881)
showarp = net_connect.send_command( 'show ip arp')
print(showarp)
output = net_connect.send_command('show ip int brief')
print(output)
createloopback = net_connect.send_config_set(interface_config)
output = net_connect.send_command('show ip int brief')
print(output)
output = net_connect.send_config_set(delete_loopback)
print(output)
output = net_connect.send_command('show ip int brief')
print(output)


