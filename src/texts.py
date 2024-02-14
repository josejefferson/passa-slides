import socket
from ip import getIPs
from qrcode import qrCode
from clear import clearConsole
from colorama import init as coloramaInit, Back as B, Fore as F, Style as S

PORT = 14859
coloramaInit(autoreset=True)

# Mostra instruções para um determinado IP
def printIPInstructions(ip, i):
	text = ' '
	if ip == '192.168.137.1': text += 'Conecte ao Wi-Fi do seu PC e acesse no navegador'
	elif i >= 1: text += 'Caso não funcione, tente acessar'
	else: text += 'Entre no navegador e acesse'

	BRIGHT = S.BRIGHT if i == 0 else ''
	
	text += f'\n {BRIGHT}{F.GREEN}http://{ip}:{PORT}{S.RESET_ALL}\n\n'
	text += BRIGHT + qrCode(f'http://{ip}:{PORT}')

	print(text)

# Mostra instruções para todos os IPs
def printInstructions():
	ips = getIPs()

	if len(ips) <= 0:
		print(f'{S.BRIGHT}{F.RED} ERRO: O seu computador não está conectado a nenhuma rede')

	if len(ips) >= 1:
		printIPInstructions(ips[0], 0)

	if len(ips) >= 2:
		printIPInstructions(ips[1], 1)

	if len(ips) >= 3:
		printIPInstructions(ips[2], 2)

# Mostra o cabeçalho da aplicação
def print_texts():
	clearConsole()
	print(f'{S.BRIGHT}{F.YELLOW} ╔═╗╔═╗╔═╗╔═╗╔═╗  ╔═╗╦  ╦╔╦╗╔═╗╔═╗')
	print(f'{S.BRIGHT}{F.YELLOW} ╠═╝╠═╣╚═╗╚═╗╠═╣  ╚═╗║  ║ ║║║╣ ╚═╗')
	print(f'{S.BRIGHT}{F.YELLOW} ╩  ╩ ╩╚═╝╚═╝╩ ╩  ╚═╝╩═╝╩═╩╝╚═╝╚═╝')
	print(f' Desenvolvido por: {S.BRIGHT}Jefferson Dantas')
	print(f' {S.BRIGHT}{F.BLUE}https://github.com/josejefferson\n')
	printInstructions()
