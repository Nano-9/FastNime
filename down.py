import os
import rich
import requests
from tqdm import tqdm
from rich.console import Console
from pathlib import Path

class iniciar_download:

	def __init__(self,iniciar,url,nome):
		self.iniciar = iniciar
		self.url_download2 = url
		self.nome = nome
		self.local_armazenamento = Path.home() / r"Downloads\FastNime"
		self.console = Console()

	def comecar_baixar(self):
		if self.iniciar == "On":

			self.lista_episodio_naruto_classico1 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35",
	"36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100","101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120","121","122","123","124","125","126","127","128","129","130","131","132","133","134","135","136","137","138","139","140","141","142","143","144","145","146","147","148","149","150","151","152","153","154","155","156","157",
	"158","159","160","161","162","163","164","165","166","167","168","169","170","171","172","173","174","175","176","177","178","179","180","181","182","183","184","185"
	,"186","187","188","189","190","191","192","193","194","195","196","197","198","199","200","201","202","203","204","205","206","207","208","209","210","211","212","213","214","215","216","217","218","219","220"]
			self.lista_episodio_nanatsu_no_taizai1 = ["01","02","03","04","05","06","007","8","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"]	
			self.lista_episodio_one_piece1 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35",
	"36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100","101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120","121","122","123","124","125","126","127","128","129","130","131","132","133","134","135","136","137","138","139","140","141","142","143","144","145","146","147","148","149","150","151","152","153","154","155","156","157",
	"158","159","160","161","162","163","164","165","166","167","168","169","170","171","172","173","174","175","176","177","178","179","180","181","182","183","184","185"
	,"186","187","188","189","190","191","192","193","194","195","196","197","198","199","200","201","202","203","204","205","206","207","208","209","210","211","212","213","214","215","216","217","218","219","220","221","222","223","224","225","226","227","228","229","230","231","232","233","234","235","236","237","238","239","240","241","242","243","244","245","246","247","248","249","250","251","252","253","254","255","256","257","258","259","260","261","262","263","264","265","266","267","268","269","270","271","272","273","274","275","276","277","278","279","280","281","282","283","284","285","286","287","288","289","290","291","292","293","294","295","296","297","298","299","300","301","302","303","304","305","306","307","308","309","310","311","312","313","314","315","316","317","318","319","320","321","322","323","324",
	"325","326","327","328","329","330","331","332","333","334","335","336","337","338","339","340","341","342","343","344","345","346","347","348","349","350","351","352"
	,"353","354","355","356","357","358","359","360","361","362","363","364","365","366","367","368","369","370","371","372","373","374","375","376","377","378","379","380","381","382","383","384","385","386","387","388","389","390","391","392","393","394","395","396","397","398","399","400","401","402","403","404","405","406","407","408","409","410","411","412","413","414","415","416","417","418","419","420","421","422","423","424","425","426","427","428","429","430","431","432","433","434","435","436","437","438","439","440","441","442","443","444","445","446","447","448","449","450","451","452","453","454","455","456","457","458","459","460","461","462","463","464","465","466","467","468","469","470","471","472","473","474","475","476","477","478","479","480","481","482","483","484","485","486","487","488","489","490","491",
	"492","493","494","495","496","497","498","499","500","501","502","503","504","505","506","507","508","509","510","511","512","513","514","515","516","517","518","519"
	,"520","521","522","523","524","525","526","527","528","529","530","531","532","533","534","535","536","537","538","539","540","541","542","543","544","545","546","547","548","549","550","551","552","553","554","555","556","557","558","559","560","561","562","563","564","565","566","567","568","569","570","571","572","573","574","575","576","577","578","579","580","581","582","583","584","585","586","587","588","589","590","591","592","593","594","595","596","597","598","599","600","601","602","603","604","605","606","607","608","609","610","611","612","613","614","615","616","617","618","619","620","621","622","623","624","625","626","627","628","629","630","631","632","633","634","635","636","637","638","639","640","641","642","643","644","645","646","647","648","649","650","651","652","653","654","655","656","657","658",
	"659","660","661","662","663","664","665","666","667","668","669","670","671","672","673","674","675","676","677","678","679","680","681","682","683","684","685","686"
	,"687","688","689","690","691","692","693","694","695","696","697","698","699","700","701","702","703","704","705","706","707","708","709","710","711","712","713","714","715","716","717","718","719","720","721","722","723","724","725","726","727","728","729","730","731","732","733","734","735","736","737","738","739","740","741","742","743","744","745","746","747","748","749","750","751","752","753","754","755","756","757","758","759","760","761","762","763","764","765","766","767","768","769","770","771","772","773","774","775","776","777","778","779","780","781","782","783","784","785","786","787","788","789","790","791","792","793","794","795","796","797","798","799","800","801","802","803","804","805","806","807","808","809","810","811","812","813","814","815","816","817","818","819","820","821","822","823","824","825",
	"826","827","828","829","830","831","832","833","834","835","836","837","838","839","840","841","842","843","844","845","846","847","848","849","850","851","852","853"
	,"854","855","856","857","858","859","860","861","862","863","864","865","866","867","868","869","870","871","872","873","874","875","876","877","878","879","880","881","882","883","884"]
			self.lista_episodio_no_game_no_life1 = ["01","02","03","04","05","06","07","08","09","10","11","12"]
			self.lista_episodio_dr_stone2 = ["01","02","03","04","05","06","07"]
			self.lista_episodio_one_punch_man1 = ["01","02","03","04","05","06","07","08","09","10","11","12"]
			self.lista_episodio_akame_ga_kill1 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"]
			self.lista_episodio_hellsing1 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14"]
			self.lista_episodio_black_clover1 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86"]
			self.lista_episodio_cavaleiros_do_zodiaco1 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100","101","102","103","104","105","106","107","108","109","110","111","112","113","114"]
			self.lista_episodio_pokemon2 = ["01","02","03"]
			self.lista_episodio_cowboy_bebop1 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]
			self.lista_episodio_hunter_x_hunter1 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92"]
			self.lista_episodio_bleach1 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35",
	"36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100","101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120","121","122","123","124","125","126","127","128","129","130","131","132","133","134","135","136","137","138","139","140","141","142","143","144","145","146","147","148","149","150","151","152","153","154","155","156","157",
	"158","159","160","161","162","163","164","165","166","167","168","169","170","171","172","173","174","175","176","177","178","179","180","181","182","183","184","185"
	,"186","187","188","189","190","191","192","193","194","195","196","197","198","199","200","201","202","203","204","205","206","207","208","209","210","211","212","213","214","215","216","217","218","219","220","221","222","223","224","225","226","227","228","229","230","231","232","233","234","235","236","237","238","239","240","241","242","243","244","245","246","247","248","249","250","251","252","253","254","255","256","257","258","259","260","261","262","263","264","265","266","267","268","269","270","271","272","273","274","275","276","277","278","279","280","281","282","283","284","285","286","287","288","289","290","291","292","293","294","295","296","297","298","299","300","301","302","303","304","305","306","307","308","309","310","311","312","313","314","315","316","317","318","319","320","321","322","323","324",
	"325","326","327","328","329","330","331","332","333","334","335","336","337","338","339","340","341","342","343","344","345","346","347","348","349","350","351","352"
	,"353","354","355","356","357","358","359","360","361","362","363","364","365","366"]
			self.lista_episodio_fairy_tail1 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35",
	"36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100","101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120","121","122","123","124","125","126","127","128","129","130","131","132","133","134","135","136","137","138","139","140","141","142","143","144","145","146","147","148","149","150","151","152","153","154","155","156","157",
	"158","159","160","161","162","163","164","165","166","167","168","169","170","171","172","173","174","175","176","177","178","179","180","181","182","183","184","185"
	,"186","187","188","189","190","191","192","193","194","195","196","197","198","199","200","201","202","203","204","205","206","207","208","209","210","211","212","213","214","215","216","217","218","219","220","221","222","223","224","225","226","227","228","229","230","231","232","233","234","235","236","237","238","239","240","241","242","243","244","245","246","247","248","249","250","251","252","253","254","255","256","257","258","259","260","261","262","263","264","265","266","267","268","269","270","271","272","273","274","275","276","277"]
			self.lista_episodio_kakegurui1 = ["01","02","03","04","05","06","07","08","09","10","11","12"]
			self.lista_episodio_kengan_ashura2 = ["01","02"]
			self.lista_episodio_eden2 = ["01","02","03","04"]
			self.lista_episodio_beastars1 = ["01","02","03","04","05","06","07","08","09","10","11","12"]
			self.lista_episodio_angel_beats1 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14"]
			self.lista_episodio_given1 = ["01","02","03","04","05","06","07","08","09","10","11"]
			self.lista_episodio_plastic_memories = ["01","02","03","04","05","06","07","08","09","10","11","12","13"]
			self.lista_episodio_kaichou_wa_maid_sama1 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]

	# checando se o nome está no link de download

			if "naruto-classico-legendado" in self.url_download2:
				os.makedirs("Anime_Naruto",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Anime_Naruto")
				for ep in self.lista_episodio_naruto_classico1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					
					self.http = 'https://servertv001.com/animes/n/naruto-classico-legendado'+"/{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")
					
					with open(self.nome+str(ep)+".mp4","wb") as video_naruto:
						for dados in self.progresso:
							os.path.join("Anime_Naruto"+"/"+str(video_naruto.write(dados)))
							self.progresso.update(len(dados))
						self.console.print("Status [COMPLETO]!\n",style="green bold")
						video_naruto.close()

			elif "nanatsu-no-taizai" in self.url_download2:
				os.makedirs("Nanatsu_No_Taizai",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Nanatsu_No_Taizai")

				for ep in self.lista_episodio_nanatsu_no_taizai1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = 'https://servertv001.com/animes/n/nanatsu-no-taizai'+"/{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")
					with open(self.nome+str(ep)+".mp4","wb") as video_nanatsu:
						for dados in self.progresso:
							os.path.join("Nanatsu_No_Taizai"+"/"+str(video_nanatsu.write(dados)))
							self.progresso.update(len(dados))
						video_nanatsu.close()

			elif "one-piece" in self.url_download2:
				os.makedirs("One_Piece",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("One_Piece")

				for ep in self.lista_episodio_one_piece1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = 'https://cdn.serverotaku01.co/010/animes/o/one-piece/'+"/{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")
					with open(self.nome+str(ep)+".mp4","wb") as video_one:
						for dados in self.progresso:
							os.path.join("One_Piece"+"/"+str(video_one.write(dados)))
							self.progresso.update(len(dados))
						video_one.close()

			elif "no-game-no-life" in self.url_download2:
				os.makedirs("No_Game_No_Life",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("No_Game_No_Life")

				for ep in self.lista_episodio_no_game_no_life1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://servertv001.com/animes/n/no-game-no-life/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")
					with open(self.nome+str(ep)+".mp4","wb") as video_nogame:
						for dados in self.progresso:
							os.path.join("No_Game_No_Life"+"/"+str(video_nogame.write(dados)))
							self.progresso.update(len(dados))
						video_nogame.close()

			elif "dr-stone" in self.url_download2:
				os.makedirs("Dr_Stone",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Dr_Stone")

				for ep in self.lista_episodio_dr_stone2:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://cdn.serverotaku01.co/010/animes/d/dr-stone/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")
					
					with open(self.nome+str(ep)+".mp4","wb") as video_dr:
						for dados in self.progresso:
							os.path.join("Dr_Stone"+"/"+str(video_dr.write(dados)))
							self.progresso.update(len(dados))
						video_dr.close()

			elif "one-punch-man" in self.url_download2:
				os.makedirs("One_Punch_Man",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("One_Punch_Man")

				for ep in self.lista_episodio_one_punch_man1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://servertv001.com/animes/o/one-punch-man/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")

					with open(self.nome+str(ep)+".mp4","wb") as video_onepunch:
						for dados in self.progresso:
							os.path.join("One_Punch_Man"+"/"+str(video_onepunch.write(dados)))
							self.progresso.update(len(dados))
						self.console.print("Status [COMPLETO]!",style="green bold")
						video_onepunch.close()
			

			elif "akame-ga-kill" in self.url_download2:
				os.makedirs("Akame_Ga_Kill",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Akame_Ga_Kill")

				for ep in self.lista_episodio_akame_ga_kill1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://servertv001.com/animes/a/akame-ga-kill/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")
			
					with open(self.nome+str(ep)+".mp4","wb") as video_akame:
						for dados in self.progresso:
							os.path.join("Akame_Ga_Kill"+"/"+str(video_akame.write(dados)))
							self.progresso.update(len(dados))
						self.console.print("Status [COMPLETO]!",style="green bold")
						video_akame.close()

			elif "black-clover" in self.url_download2:
				os.makedirs("Black_Clover",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Black_Clover")

				for ep in self.lista_episodio_black_clover1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://servertv001.com/animes/b/black-clover/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")

					with open(self.nome+ste(ep)+".mp4","wb") as video_black:
						for dados in self.progresso:
							os.path.join("Black_Clover"+"/"+str(video_black.write(dados)))
							self.progresso.update(len(dados))
						self.console.print("Status [COMPLETO]!",style="green bold")

			elif "cavaleiros-do-zodiaco" in self.url_download2:
				os.makedirs("Cavaleiros_Do_Zodiaco",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Cavaleiros_Do_Zodiaco")

				for ep in self.lista_episodio_cavaleiros_do_zodiaco1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://servertv001.com/animes/c/cavaleiros-do-zodiaco-dublado/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")

					with open(self.nome+str(ep)+".mp4","wb") as video_cavaleiro:
						for dados in self.progresso:
							os.path.join("Cavaleiros_Do_Zodiaco"+"/"+str(video_cavaleiro.write(dados)))
							self.progresso.update(len(dados))
						self.console.print("Status [COMPLETO]!",style="green bold")
						video_cavaleiro.close()

			elif "pokemon" in self.url_download2:
				os.makedirs("Pokemon",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Pokemon")

				for ep in self.lista_episodio_pokemon2:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://servertv001.com/animes/p/pokemon-dublado/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")

					with open(self.nome+str(ep)+".mp4","wb") as video_pokemon:
						for dados in self.progresso:
							os.path.join("Pokemon"+"/"+str(video_pokemon.write(dados)))
							self.progresso.update(len(dados))
						self.console.print("Status [COMPLETO]!",style="green bold")
						video_pokemon.close()

			elif "cowboy-bebop" in self.url_download2:
				os.makedirs("Cowboy_Bebop",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Cowboy_Bebop")

				for ep in self.lista_episodio_cowboy_bebop1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://servertv001.com/animes/c/cowboy-bebop/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")

					with open(self.nome+str(ep)+".mp4","wb") as video_cowboy:
						for dados in self.progresso:
							os.path.join("Cowboy_Bebop"+"/"+str(video_cowboy.write(dados)))
							self.progresso.update(len(dados))
						video_cowboy.close()

			elif "hunter-x-hunter" in self.url_download2:
				os.makedirs("Hunter_X_Hunter",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Hunter_X_Hunter")

				for ep in self.lista_episodio_hunter_x_hunter1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://servertv001.com/animes/h/hunter-x-hunter-legendado/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")

					with open(self.nome+str(ep)+".mp4","wb") as video_hunter:
						for dados in self.progresso:
							os.path.join("Hunter_X_Hunter"+"/"+str(video_hunter.write(dados)))
							self.progresso.update(len(dados))
						video_hunter.close()

			elif "bleach" in self.url_download2:
				os.makedirs("Bleach",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Bleach")

				for ep in self.lista_episodio_bleach1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://cdn.serverotaku01.co/010/animes/b/bleach/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")

					with open(self.nome+str(ep)+".mp4","wb") as video_bleach:
						for dados in self.progresso:
							os.path.join("Bleach"+"/"+str(video_bleach.write(dados)))
							self.progresso.update(len(dados))
						video_bleach.close()

			elif "fairy-tail" in self.url_download2:
				os.makedirs("Fairy_Tail",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Fairy_Tail")

				for ep in self.lista_episodio_fairy_tail1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://servertv001.com/animes/f/fairy-tail/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")

					with open(self.nome+str(ep)+".mp4","wb") as video_fairy:
						for dados in self.progresso:
							os.path.join("Fairy_Tail"+"/"+str(video_fairy.write(dados)))
							self.progresso.update(len(dados))
						video_fairy.close()


			elif "kakegurui" in self.url_download2:
				os.makedirs("Kakegurui",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Kakegurui")

				for ep in self.lista_episodio_kakegurui1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://servertv001.com/animes/k/kakegurui/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")

					with open(self.nome+str(ep)+".mp4","wb") as video_kake:
						for dados in self.progresso:
							os.path.join("Kakegurui"+"/"+str(video_kake.write(dados)))
							self.progresso.update(len(dados))
						video_kake.close()

			elif "kengan-ashura" in self.url_download2:
				os.makedirs("Kengan_Ashura",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Kengan_Ashura")

				for ep in self.lista_episodio_kengan_ashura2:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://cdn.serverotaku01.co/010/animes/k/kengan-ashura-dublado/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")

					with open(self.nome+str(ep)+".mp4","wb") as video_kengan:
						for dados in self.progresso:
							os.path.join("Kengan_Ashura"+"/"+str(video_kengan.write(dados)))
							self.progresso.update(len(dados))
						video_kengan.close()

			elif "eden" in self.url_download2:
				os.makedirs("Eden",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Eden")

				for ep in self.lista_episodio_eden2:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://cdn.serverotaku01.co/010/animes/e/eden-dublado/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")
			
					with open(self.nome+str(ep)+".mp4","wb") as video_eden:
						for dados in self.progresso:
							os.path.join("Eden"+"/"+str(video_eden.write(dados)))
							self.progresso.update(len(dados))
						video_eden.close()

			elif "beastars" in self.url_download2:
				os.makedirs("Beastars",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Beastars")

				for ep in self.lista_episodio_beastars1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://cdn.serverotaku01.co/010/animes/b/beastars/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")

					with open(self.nome+str(ep)+".mp4","wb") as video_beas:
						for dados in self.progresso:
							os.path.join("Beastars"+"/"+str(video_beas.write(dados)))
							self.progresso.update(len(dados))
						video_beas.close()

			elif "angel-beats" in self.url_download2:
				os.makedirs("Angel_Beats",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Angel_Beats")

				for ep in self.lista_episodio_angel_beats1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://servertv001.com/animes/a/angel-beats/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")

					with open(self.nome+str(ep)+".mp4","wb") as video_angel:
						for dados in self.progresso:
							os.path.join("Angel_Beats"+"/"+str(video_angel.write(dados)))
							self.progresso.update(len(dados))
						video_angel.close()

			elif "given" in self.url_download2:
				os.makedirs("Given",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Given")

				for ep in self.lista_episodio_given1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://cdn.serverotaku01.co/010/animes/g/given/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")

					with open(self.nome+str(ep)+".mp4","wb") as video_given:
						for dados in self.progresso:
							os.path.join("Given"+"/"+str(video_given.write(dados)))
							self.progresso.update(len(dados))
						video_given.close()
			
			elif "plastic-memories" in self.url_download2:
				os.makedirs("Plastic_Memories",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Plastic_Memories")

				for ep in self.lista_episodio_plastic_memories:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://servertv001.com/animes/p/plastic-memories/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")

					with open(self.nome+str(ep)+".mp4","wb") as video_plast:
						for dados in self.progresso:
							os.path.join("Plastic_Memories"+"/"+str(video_plast.write(dados)))
							self.progresso.update(len(dados))
						video_plast.close()

			elif "kaichou-wa-maid-sama" in self.url_download2:
				os.makedirs("Kaichou_Wa_Maid_Sama",exist_ok=True)
				os.chdir(self.local_armazenamento)
				os.chdir("Kaichou_Wa_Maid_Sama")

				for ep in self.lista_episodio_kaichou_wa_maid_sama1:
					print("Baixando {} episodio {}".format(self.nome,ep))
					self.http = "https://servertv001.com/animes/k/kaichou-wa-maid-sama/"+"{}.mp4".format(ep)
					self.r = requests.get(self.http,stream=True)
					self.total_arquivo = int(self.r.headers["Content-length"])
					self.progresso = tqdm(desc="Baixando...",iterable=self.r.iter_content(chunk_size=1024),total=self.total_arquivo,unit=" Kb",unit_scale=True,unit_divisor=1024,colour="blue")

					with open(self.nome+str(ep)+".mp4","wb") as video_kaich:
						for dados in self.progresso:
							os.path.join("Kaichou_Wa_Maid_Sama"+"/"+str(video_kaich.write(dados)))
							self.progresso.update(len(dados))
						video_kaich.close()
