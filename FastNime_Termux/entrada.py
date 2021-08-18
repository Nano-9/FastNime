import os
import sys
import rich
from rich.console import Console
from time import sleep
console = Console()
def inicio():
	console.print("""
,------.               ,--.         ,--.  ,--.,--.                  
|  .---',--,--. ,---.,-'  '-.,-----.|  ,'.|  |`--',--,--,--. ,---.  
|  `--,' ,-.  |(  .-''-.  .-''-----'|  |' '  |,--.|        || .-. : 
|  |`  \ '-'  |.-'  `) |  |         |  | `   ||  ||  |  |  |\   --. 
`--'    `--`--'`----'  `--'         `--'  `--'`--'`--`--`--' `----'
			  
			  Versão 1.0
""",style="blue bold")

	print("Opções:\n")
	print("""
[ 1 ] - Mostrar catalogo de animes
[ 2 ] - Fazer download dos episódios
[ 3 ] - Sair
		""")
	try:
		escolha1 = int(input("O que deseja: "))
	except ValueError:
		print("\nO valor inserido não é suportado! Por favor, informe um número inteiro!")
	except KeyboardInterrupt:
		print("\nO usuário resolveu fechar o programa!")
		sleep(1)
		sys.exit()
	else:
		while escolha1 <= 0 or escolha1 > 3:
			print("Opção inválida!")
			sleep(1)
			try:
				escolha1 = int(input("O que deseja: "))
			except ValueError:
				print("\nO valor inserido não é suportado! Por favor, informe um número inteiro!")
			except KeyboardInterrupt:
				print("\nO usuário resolveu fechar o programa!")
				sleep(1)
				sys.exit()
		return escolha1
