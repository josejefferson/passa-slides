import os

# Limpa o console
def clearConsole():
	command = 'clear'
	if os.name in ('nt', 'dos'):
		command = 'cls'
	os.system(command)
