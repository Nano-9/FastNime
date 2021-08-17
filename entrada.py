import rich
from rich.console import Console
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

	escolha1 = int(input("O que deseja: "))
	return escolha1
