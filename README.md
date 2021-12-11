# dos-atack-tor
script de python que permite usar conexiones cebollas para atacar paginas .onion o paginas convencionales via tor. tiene capacidad de ajustar la cantidad de informacion a enviar, el numero de hilos a usar, el tiempo de duracion del ataque, atacar a un directorio en especial y etc. Su ataque es sencillo, trata de saturar un recurso en base a peticiones GET en rutas del servidor excesivamente lentas.
 ![Alt text](https://raw.githubusercontent.com/desmonHak/dos-atack-tor/main/image/Screenshot_2021-12-11_02-55-33.png) 

se a de ejecutar con python 2, ejemplo:

-----------------------------------------------------------------------------------------
	python2 script-dos.py -ip 127.0.0.1 -t False -p 8000 -th 20 -c 10 -peticion POST -time 30
-----------------------------------------------------------------------------------------

