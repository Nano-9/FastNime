# esse script está sendo desenvolvido por lucas walker
# script para baixar animes ou assistir online pelo navegador
# [ATENÇÃO] leia o Readme.md para saber sobre!

try:
	import os
	import sys
	import requests
	import json
	import datetime
	import rich
	from entrada import inicio
	from tabela_fastnime import mostrar_catalogo_fastnime
	from down import iniciar_download
	from tqdm import tqdm
	from time import sleep
	from pathlib import Path
	from rich.console import Console
except:
	print("\n[ATENÇÃO]: Parece que você não tem as bibliotecas necessárias para rodar o programa!\n")
	print("Digite: pip install -r requirements.txt e tente novamente!")
	sys.exit()
else:
	pass

class AnimeDownload:

	def __init__(self,episodio,nome,preferencia,tudo,hora,minuto,segundo):
		if sys.platform == "win32":
			os.system("cls")
		elif sys.platform == "linux":
			os.system("clear")

		self.episodio = str(episodio)
		self.nome = nome
		self.nome2 = nome.lower()
		self.preferencia = preferencia.capitalize()
		self.diahora = hora
		self.diaminuto = minuto
		self.diasegundo = segundo
		self.url_download = ""
		self.url_anime = ""
		self.nome_download = ""
		self.url_download2 = ""
		self.tudo = tudo.upper()
		self.trocar_nome = ""
		self.console = Console()


		if " " in self.nome:
			self.trocar_nome = nome.replace(" ","-")
			self.url_anime = "https://sugoi-api.herokuapp.com/episode/{}/{}".format(episodio,self.trocar_nome)
		else:
			self.url_anime = "https://sugoi-api.herokuapp.com/episode/{}/{}".format(episodio,self.url_anime)

	def pegar_dados(self):
		print("Aguardando conexão...")
		self.r = requests.get(self.url_anime)
		self.dados = json.loads(self.r.text)
		
		for key,value in self.dados.items():
			if key == "info":
				for key2,value2 in value.items():
					if key2 == "name":
						self.nome_download = value2

			elif key == "cdn":
				if self.preferencia == "Dublado":
					for link in value:
						lista_episodios = link["links"]
						for links in lista_episodios:
							if links != None:
								self.link_an = links.split("/")[-2]
								self.juntar = self.link_an.replace("-", " ")
								if "dublado" in self.juntar:
									self.url_download = links
									self.url_download2 = links
								else:
									self.url_download = links
									self.url_download2 = links

				elif self.preferencia == "Legendado":
					for link in value:
						lista_episodios = link["links"]
						for links in lista_episodios:
							if links != None:
								self.link_an = links.split("/")[-2]
								self.juntar = self.link_an.replace("-", " ")
								if "legendado" in self.juntar:
									self.url_download = links
									self.url_download2 = links
								else:
									self.url_download = links
									self.url_download2 = links

	def download_episodio_anime(self):
		self.local_armazenamento = Path.home() / r"Downloads\FastNime"
		os.makedirs("Animes",exist_ok=True)
		self.x = requests.get(self.url_download,stream=True)
		if self.x.status_code == 200:
			print("Conexão aceita!\n")
			sleep(2)
			os.system("clear")
			self.console.print("============== ÁREA DE DOWNLOAD DO EPISÓDIO ==============\n",style="red bold")
			print("Baixando o episódio {} de {}\n".format(self.episodio,self.nome_download))
			self.tamanho_episodio = int(self.x.headers["Content-length"])
			self.barra_progresso = tqdm(desc=f"[{self.diahora}:{self.diaminuto}:{self.diasegundo}] [\033[1;32mINFO\033[m]: Baixando",iterable=self.x.iter_content(chunk_size=1024),total=self.tamanho_episodio,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")
			
			os.chdir(self.local_armazenamento)
			try:
				os.chdir("Animes")
			except:
				with open(self.nome_download+self.episodio+".mp4","wb") as ep:
					for byte_episodio in self.barra_progresso:
						os.path.join("Animes" + "/" + str(ep.write(byte_episodio)))
						self.barra_progresso.update(len(byte_episodio))
					ep.close()
			else:
				with open(self.nome_download+self.episodio+".mp4","wb") as ep:
					for byte_episodio in self.barra_progresso:
						os.path.join("Animes" + "/" + str(ep.write(byte_episodio)))
						self.barra_progresso.update(len(byte_episodio))
					ep.close()

			print("Episódio {} de {} baixado!".format(self.episodio,self.nome_download))
			sleep(3)
		else:
			print("[ATENÇÃO]: A conexão não foi estabelecida com o host!")
			print("voltando...")
			sleep(3)

	def download_todos_os_episodios(self):
		limpar()
		self.console.print("============== ÁREA DE DOWNLOADS DOS EPISÓDIOS ==============\n",style="red bold")
		baix = iniciar_download(iniciar="On",url=self.url_download2,nome=self.nome,hora=self.diahora,minuto=self.diaminuto,segundo=self.diasegundo)
		baix.comecar_baixar()
		
# função de fora que é para limpar o terminal
def limpar():
	if sys.platform == "win32":
		os.system("cls")
	elif sys.platform == "linux":
		os.system("clear")



# classe da apresentação do FastNime

class FastNime:

	def __init__(self):
		self.data = str(datetime.datetime.now())
		self.hora = self.data[11:13]
		self.minuto = self.data[14:16]
		self.segundo = self.data[17:19]
		self.ano = self.data[0:4]
		self.mes = self.data[5:7]
		self.dia = self.data[8:10]

	def pegar_escolha_usuario(self):
		while True:
			limpar()
			print("Programa rodando em {}/{}/{} as {}:{}:{}".format(self.dia,self.mes,self.ano,self.hora,self.minuto,self.segundo))
			self.escolha = inicio()

			if self.escolha == 1:

				limpar()
				mostrar_catalogo_fastnime()
				print("\nEnter para voltar ao menu: ")
				input()

			elif self.escolha == 2:
				limpar()
				self.lista_valida = ["01","02","03","04","05","06","07","08","09"]
				try:
					self.nome = str(input("Informe o nome completo do anime que deseja baixar: ")).strip().capitalize()
					self.episodio = str(input("Informe o número do episódio que deseja baixar: ")).strip()
				except KeyboardInterrupt:
					print("\nO usuário resolveu fechar o programa!")
					sleep(1)
					sys.exit()
				if self.nome != "Cavaleiros do zodiaco":
					try:
						self.preferencia = str(input("Você quer legendado ou dublado: ")).strip()
					except KeyboardInterrupt:
						print("\nO usuário resolveu fechar o programa!")
						sleep(1)
						sys.exit()
				try:
					self.download_tudo_ou_nao = str(input("Deseja baixar todos os episódios do anime escolhido [S/N]: ")).strip().upper()
				except KeyboardInterrupt:
					print("\nO usuário resolveu fechar o programa!")
					sleep(1)
					sys.exit()
				if int(self.episodio) > 0 and int(self.episodio) < 10:
					if self.episodio in self.lista_valida:
						if self.nome == "Cavaleiros do zodiaco":
							self.search_anime = AnimeDownload(episodio=self.episodio,nome=self.nome,preferencia="dublado",tudo=self.download_tudo_ou_nao,hora=self.hora,minuto=self.minuto,segundo=self.segundo)
							self.search_anime.pegar_dados()
							if self.download_tudo_ou_nao in "S":
								self.search_anime.download_todos_os_episodios()
							elif self.download_tudo_ou_nao == "N" or self.download_tudo_ou_nao == "n":
								self.search_anime.pegar_dados()
								self.search_anime.download_episodio_anime()
						else:
							self.search_anime = AnimeDownload(episodio=self.episodio,nome=self.nome,preferencia=self.preferencia,tudo=self.download_tudo_ou_nao,hora=self.hora,minuto=self.minuto,segundo=self.segundo)
							if self.download_tudo_ou_nao in "S":
								self.search_anime.pegar_dados()
								self.search_anime.download_todos_os_episodios()
							elif self.download_tudo_ou_nao == "N" or self.download_tudo_ou_nao == "n":
								self.search_anime.pegar_dados()
								self.search_anime.download_episodio_anime()
					else:
						limpar()
						print("Número de episódio inválido! Coloque o 0 primeiro. Exemplo: 01, 02...")
						sleep(4)

				else:
					self.search_anime = AnimeDownload(episodio=self.episodio,nome=self.nome,preferencia=self.preferencia,tudo=self.download_tudo_ou_nao,hora=self.hora,minuto=self.minuto,segundo=self.segundo)
					if self.download_tudo_ou_nao in "S":
						self.search_anime.pegar_dados()
						self.search_anime.download_todos_os_episodios()
					elif self.download_tudo_ou_nao == "N" or self.download_tudo_ou_nao == "n":
						self.search_anime.pegar_dados()
						self.search_anime.download_episodio_anime()

			elif self.escolha == 3:
				print("Saindo...")
				sleep(1)
				sys.exit()

entrar = FastNime()
entrar.pegar_escolha_usuario()
