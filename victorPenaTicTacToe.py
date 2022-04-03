from random import randrange

def pintarTablero():
	cadena = '+-------+\n| '
	contador = 0
	for x in tablero:
		for y in x:			
			contador += 1
			cadena += f'{y} '
			if contador % 3 == 0 and contador != 9:
				cadena += '|\n| '
			if contador == 9:
				cadena += '|\n+-------+'			
	return cadena

def comprobarEstado(jugador):
	#Horizontales
	if(tablero[0][0] == jugador and tablero[0][1] == jugador and tablero[0][2] == jugador):
		return True
	if(tablero[1][0] == jugador and tablero[1][1] == jugador and tablero[1][2] == jugador):
		return True
	if(tablero[2][0] == jugador and tablero[2][1] == jugador and tablero[2][2] == jugador):
		return True
	#Verticales
	if(tablero[0][0] == jugador and tablero[1][0] == jugador and tablero[2][0] == jugador):
		return True
	if(tablero[0][1] == jugador and tablero[1][1] == jugador and tablero[2][1] == jugador):
		return True
	if(tablero[0][2] == jugador and tablero[1][2] == jugador and tablero[2][2] == jugador):
		return True
	#Diagonales
	if(tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador):
		return True
	if(tablero[2][0] == jugador and tablero[1][1] == jugador and tablero[0][2] == jugador):
		return True
	return False

def añadirJugada(numero, jugador):
	fila = posiciones[numero][0]
	columna = posiciones[numero][1]
	if tablero[fila][columna] == 'X' or tablero[fila][columna] == 'O':
		if jugador == 'X':
			añadirJugada(str(randrange(1, 9)), jugador)
		if jugador == 'O':
			datos = False  
			while datos == False: #Comprobar que los datos introducidos son correctos
				try:
					jugada = int(input('Introduce la posición de tu jugada (1 al 9), esa esta ocupada: '))
					datos = True 
				except ValueError:
					datos = False 

				if datos != False:
				    if jugada < 1 or jugada > 9:                                          
	          			datos = False

				if datos == False:
					print('Formato de posición introducido incorrecto')

			añadirJugada(str(jugada), jugador)
	else:
		tablero[fila][columna] = jugador
		global ultColocada
		ultColocada = numero		

#Declaracion de tablero
tablero = [
	['1','2','3'],
	['4','5','6'],
	['7','8','9']
]
#Declaracion de diccionario, para equiparar un numero a la posicion de fila/columna que pide el ejercicio. Clave (numero), Valor (posiciones correspondientes)
posiciones = {
	'1': [0,0], '2': [0,1], '3': [0,2], '4': [1,0], '5': [1,1], '6': [1,2], '7': [2,0], '8': [2,1], '9': [2,2]
}

print(pintarTablero())

#Turno inicial de la IA
tablero[1][1] = 'X'
print(pintarTablero())
print('La IA ha colocado en la posición 5')
print('Turno del jugador')
fin = False
contador = 0
ultColocada = ''
#Partida
while fin == False:	
	if contador == 8:
		print('Hay un empate')
		fin = True
		break
	fin = False
	if contador % 2 != 0:
		jugador = 'X'
	else:
		jugador = 'O'
	contador += 1
	if jugador == 'O':
		datos = False  
		while datos == False: #Comprobar que los datos introducidos son correctos
			try:
				jugada = int(input('Introduce la posición de tu jugada (1 al 9): '))
				datos = True 
			except ValueError:
				datos = False 
			if datos != False:
				if jugada < 1 or jugada > 9:                                          
					datos = False
			if datos == False:    
				print('Formato de posición introducido incorrecto')

		añadirJugada(str(jugada), jugador)		
		print(pintarTablero())		
		print('El jugador ha colocado')
		print('*********************************************')
		if(comprobarEstado(jugador)) == True:
			print(f'Has ganado!!')
			fin = True
	else:
		añadirJugada(str(randrange(1, 9)), jugador)		
		print(pintarTablero())	
		print(f'La IA ha colocado en la posición {ultColocada}')
		print('Turno del jugador')		
		if(comprobarEstado(jugador)) == True:				
			print(f'La IA ha ganado, has perdido!!')
			fin = True		 

    			