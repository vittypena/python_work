def posicionesAfectadas( fila, columna ):
    rX = []    
    pR = ((fila-1) * 8) + columna #Posicion donde colocamos la reina      
    comprobar = True
    for x in range(1, columna): #Diagonales hacia la izquierda
        if x<fila: #Controlar los numeros negativos fuera del tablero
            rX.append(pR-x*8-x)
        resultado = pR+x*8-x
        if resultado<=64: #Controlar numeros positivos fuera del rango maximo
            rX.append(resultado)

    for x in range(1, 8-columna+1): #Diagonales hacia la derecha    
        if x<fila:
            rX.append(pR-x*8+x)
        resultado = pR+x*8+x
        if resultado<=64:
            rX.append(resultado)            

    numero = ((fila-1)*8)+1 #Recto izquierda/derecha
    for x in range(1, 9):
        rX.append(numero)
        numero+=1

    for x in range(1, fila): #Recto hacia arriba
        rX.append(pR-8*x)

    for x in range(1, 8 - fila + 1): #Recto hacia abajo
        rX.append(pR+8*x)  


    for x in rX: #Si las posiciones afectadas estan en la lista de p1 (la cual guarda las reinas colocadas), devuelve false
    	for y in p1:
    		if x == y:
    			return False
    continuar = True			
    if comprobar == True:
        if filaComprobada+1 != filaCorrespondiente(pR):#Donde pone la proxima reina, si la va a poner 2 filas despues signfica que ha fallado y que tiene que comprobar la siguiente posicion en la fila anterior        	
        	continuar = False
        	if filaCorrespondiente(pR)-1 == filaR1 and filaCorrespondiente(pR)-filaCorrespondiente(p1[-1]) <= 2:
        	    continuar = True
        if continuar == True: #Si no lo intenta poner dos filas despues o la siguiente no es la fila de la reina, la pone	
        	if len(f1) != 0:
        		colocar = True        		
	        	for x in f1: #Hay que comprobar que no sea igual a una posicion que ha provocado fallo ya en esa fila
	        		if x == pR:
	        			colocar = False
	        	if colocar == True:
	        		p1.append(pR) #Añadimos la reina a la lista de reinas colocadas
	        		return True #si es verdadero se pone la posicion de la fila correspondiente en la posicion del ultimo elemento de la lista   
	        else:
	        	p1.append(pR) #Añadimos la reina a la lista de reinas colocadas
	        	return True #si es verdadero se pone la posicion de la fila correspondiente en la posicion del ultimo elemento de la lista   	    	
        else:
        	return False
def comprobarDisponibilidad():  #Comprueba si la posicion para colocar una reina esta afectada por otra reina
	comprobar = False	
	for x in range(1, 65):
		if comprobar == True:
			break
		fila = filaCorrespondiente(x)
		columna = columnaCorrespondiente(x)
		if posicionesAfectadas(fila, columna) == True:
			global filaComprobada
			filaComprobada =  filaCorrespondiente(p1[-1]) 
			comprobar = True						
			break
	if comprobar == False:				
		posicionRemovida = p1.pop(-1) #Elimina la ultima reina colocada y la guarda en una variable de forma temporal
		filaComprobada = filaCorrespondiente(posicionRemovida)-1 #Para retroceder y comprobar desde una fila anterior con la siguiente posicion disponible a la ultima de fallo, evitando esta, se iguala la filaComprobar a la de la posicion removida y se le resta 1
		if filaComprobada == filaR1: #Si la nueva fila es igual a la fila de la reina quiere decir que la ultima disponible se habia saltado la fila de la reina, por lo tanto hay que restarle otra más para poder comprobar la que realmente corresponde
			filaComprobada += -1
		f1.append(posicionRemovida) #Añadimos a la lista de posiciones ya comprobadas de esa fila, la posicion que dio el fallo, para que la evite
		remover = []
		for x in f1:
			if x > posicionRemovida: #Si en la lista de fallos hay posiciones por delante de la que se esta comprobando, hay que eliminar todas para que no de por malas, posiciones que al retroceder son buenas en el punto actual, esto ha de ser asi para poder ir retrocediendo y avanzando de forma correcta
				remover.append(x)
		for x in remover:			
			f1.remove(x)
def columnaCorrespondiente(p):   #Devuelve la columna correspondiente a la posicion
    for x in range(1, 9):
        if p == 8*0+x or p == 8*1+x or p == 8*2+x or p == 8*3+x or p == 8*4+x or p == 8*5+x or p == 8*6+x or p == 8*7+x: 
            return x

def filaCorrespondiente(p):
    for x in range(8):
        if p == 8*x+1 or p == 8*x+2 or p == 8*x+3 or p == 8*x+4 or p == 8*x+5 or p == 8*x+6 or p == 8*x+7 or p == 8*x+8:
            return x + 1

#Variable con la ultima fila comprobada correctamente
filaComprobada = 0

#Lista con posiciones de las reinas colocadas pX
p1 = []

#Lista con posicion probadas en la fila, se borra cuando se ha comprobado la fila entera, aqui 
f1 = []
#Primero colocamos la reina donde queramos y bloqueamos esas posiciones (Esta reina 'r1' sera inalterable, por tanto su lista también).
#TODO pedir por input fila y columna para bloquear
fila = 2
columna = 8
posicionR1 = ((fila-1) * 8) + columna 
p1.append(posicionR1)
filaR1 = filaCorrespondiente(posicionR1)
if filaR1 == 1:
	filaComprobada = 1
	
#En este punto esta colocada la reina

#Comprobamos la primera posicion libre por columnas para colocar la siguiente reina
while len(p1)!=8: #Mientras todas las reinas no esten colocadas, tratara de colocarlas
	comprobarDisponibilidad()

print(f"La reina principal es {posicionR1}")
print(f"Posiciones de Reinas colocadas -> {p1}")


#if buscarDisponibilidad() == None: #Si no encuentra ninguno
#    ultBorrado = p1.pop() #Borra la ultima reina colocada y guarda su posicion  
#    desbloquearColumna(ultBorrado) 
#    print(f'La columna del ultimo borrado es {columnaCorrespondiente(ultBorrado)}')
#    del r6[:] #Borra la lista de ultima reina colocada    
#    bloquear()

    	
