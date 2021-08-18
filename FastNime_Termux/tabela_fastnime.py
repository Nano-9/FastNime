# modulo do fastnime, está separado para não ficar um código gigante
from tabulate import tabulate

def mostar_catalogo_fastnime():
		cabecalho = ["Animes","Episodios disp","Servidores","Leg/Dub"]
		dados = [

		["Naruto Clássico",220,"Server-TV","Os dois"],
		["Nanatsu No Taizai",25,"Server-TV","Legendado"],
		["One Piece", 884,"Super Animes-TV","Legendado"],
		["No Game, No Life",12,"Server-TV","Legendado"],
		["Dr. Stone","07","Server Otaku01","Legendado"],
		["One Punch Man",12,"Super Animes-TV","Legendado"],
		["Akame Ga Kill",24,"Server-TV","Legendado"],
		["Hellsing",14,"Server-TV","Legendado"],
		["Black Clover",86,"Server Otaku01","Legendado"],
		["Cavaleiros Do Zodíaco",114,"Server-TV","Dublado"],
		["Pokémon","03","Server-TV","Dublado"],
		["Cowboy Bebop",26,"Server-TV","Legendado"],
		["Hunter X Hunter",96,"Server-TV","Legendado"],
		["Bleach",366,"Server Otaku01","Legendado"],
		["Fairy Tail",277,"Server-TV","Legendado"],
		["Kakegurui",12,"Server-TV","Legendado"],
		["Kengan Ashura","02","Server Otaku01","Dublado"],
		["Eden","04","Server Otaku01","Dublado"],
		["Beastars",12,"Server Otaku01","Legendado"],
		["Angel Beats",14,"Server-TV","Legendado"],
		["Given",11,"Server Otaku01","Legendado"],
		["Plastic Memories",13,"Server-TV","Legendado"],
		["Kaichou wa Maid-sama",26,"Server-TV","Legendado"]


		]

		tabela = tabulate(dados,headers=cabecalho,tablefmt="fancy_grid")
		print(tabela)
