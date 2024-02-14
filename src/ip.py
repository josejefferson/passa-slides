import socket

# Retorna os endereços IP do computador
def getIPs():
	ips = []

	if 'netifaces' in globals():
		for interface in netifaces.interfaces():
			for address in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
				ips.append(address['addr'])
	else:
		ips = socket.gethostbyname_ex(socket.gethostname())[-1]

	if '192.168.137.1' in ips: ips.insert(0, ips.pop(ips.index('192.168.137.1')))
	if '192.168.56.1' in ips: ips.remove('192.168.56.1')
	if '127.0.0.1' in ips: ips.remove('127.0.0.1')
	if '127.0.1.1' in ips: ips.remove('127.0.1.1')

	return ips
