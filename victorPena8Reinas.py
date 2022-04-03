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

    for x in rX: #Si las posiciones afectadas están en la lista de p1 (la cual guarda las reinas colocadas), devuelve false
        for y in p1:
            if x == y:
                return False
    continuar = True            
    if comprobar == True:
        if filaComprobada+1 != filaCorrespondiente(pR):#Donde pone la próxima reina, si la va a poner 2 filas después signfica que ha fallado y que tiene que comprobar la siguiente posicion en la fila anterior           
            continuar = False
            if filaCorrespondiente(pR)-1 == filaR1 and filaCorrespondiente(pR)-filaCorrespondiente(p1[-1]) <= 2:
                continuar = True
        if continuar == True: #Si no intenta poner dos filas después o la siguiente no es la fila de la reina, la pone  
            if len(f1) != 0:
                colocar = True              
                for x in f1: #Hay que comprobar que no sea igual a una posicion que ha provocado fallo ya en esa fila
                    if x == pR:
                        colocar = False
                if colocar == True:
                    p1.append(pR) #Añadimos la reina a la lista de reinas colocadas
                    return True #Si es verdadero se pone la posicion de la fila correspondiente en la posicion del ultimo elemento de la lista   
            else:
                p1.append(pR) #Añadimos la reina a la lista de reinas colocadas
                return True #Si es verdadero se pone la posicion de la fila correspondiente en la posicion del ultimo elemento de la lista              
        else:
            return False

def comprobarDisponibilidad():  #Comprueba si la posicion para colocar una reina esta afectada por otra reina, mediante la lista de reinas colocadas
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
        filaComprobada = filaCorrespondiente(posicionRemovida)-1 #Para retroceder y comprobar desde una fila anterior con la siguiente posicion disponible a la última del fallo, evitando esta, se iguala la filaComprobar a la de la posicion removida y se le resta 1
        if filaComprobada == filaR1: #Si la nueva fila es igual a la fila de la reina quiere decir que la ultima disponible se había saltado la fila de la reina, por lo tanto hay que restarle otra más para poder comprobar la que realmente corresponde y no comprobar miles de posibilidades innecesarias
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
        for y in range(8):
            if p == 8*y+x:
                return x               

def filaCorrespondiente(p):
    for x in range(8):
        for y in range(1, 9):
            if p == 8*x+y:
                return x + 1

#Variable con la ultima fila comprobada
filaComprobada = 0

#Lista con posiciones de las reinas colocadas pX
p1 = []

#Lista con posicion probadas en la fila, se borra cuando se ha comprobado la fila entera
f1 = []

#Primero colocamos la reina donde queramos, añadiendola la lista de posiciones colocadas.
#Pedir por input fila y columna para bloquear

datos = False                                               #Con el booleano gestionamos el fin del while si se cumplen las condiciones
while datos == False:  
    print('\nIntroduce una posicion en el tablero indicando fila y columna del 1 al 8\n')
    try:
        fila = int(input('Introduce la fila: '))
        columna = int(input('Introduce la columna: '))                                                                                                  
        datos = True       
    except ValueError:    
        datos = False            

    if datos != False:
        if fila < 1 or fila > 8:                                          
            datos = False                                                               

        if columna < 1 or columna > 8:                                          
            datos = False   

    if datos == False:    
        print('Formato de fila/columna incorrecto')

posicionR1 = ((fila-1) * 8) + columna 
p1.append(posicionR1)
filaR1 = filaCorrespondiente(posicionR1)
if filaR1 == 1: #Para evitar que checkee lineas innecesarias si la reina esta en la fila 1, la filaComprobada por defecto pasa a ser 1 en vez de 0. Ha de ser asi debido a la logica de mi algoritmo. De no ser así, no sabria correctamente si ya ha fallado y seguiria probando posiciones innecesarias, dandole trabajo extra al programa.
    filaComprobada = 1
#En este punto esta colocada la reina

while len(p1)!=8: #Mientras todas las reinas no esten colocadas, tratara de colocarlas
    comprobarDisponibilidad()#Comprobamos la primera posicion libre por columnas para colocar la siguiente reina y la coloca. Si retorna false, la propia función busca la forma correcta de colocar la siguiente reina, cuando falla retrocede hasta encontrar el camino correcto.
print('**************************************')
print(f"La reina que has colocado es -> {posicionR1}")
print(f"Posiciones de Reinas colocadas -> {p1}")
print('**************************************')

cadena = '+---- ---- ---- ---- ---- ---- ---- -----+\n|'
for x in range(1, 65):
    pintarX = False
    for y in p1:        
        if x == y:
            pintarX = True                  
    if pintarX == True:
        cadena += ' RE  '   #RE INDICA QUE SE COLOCA UNA REINA EN ESA POSICION
    else:
        if x < 10:
            cadena += f'  {x}  ' #Pinta la posición, los espacios son para dar formato
        else:
            cadena += f' {x}  '
    if x%8 == 0 and x != 0 and x != 64:
        cadena +='|\n|'
    elif x == 64:
        cadena += '|\n' 
cadena += '+---- ---- ---- ---- ---- ---- ---- -----+'      
print(cadena)        