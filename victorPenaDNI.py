diccAbc = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]			
comprobar = False												#Con el booleano gestionamos el fin del while si se cumplen las condiciones
while comprobar == False:  
	cadena = input("Escribe el DNI: ")
	try:
		cadenaNum = int(cadena)									#Pasarlo a int para comprobar que son numeros        															
		comprobar = True       
	except ValueError:    
		comprobar = False            

	if len(cadena)<8 or len(cadena)>8:										    
		comprobar = False        														

	if comprobar == False:    
		print('Formato de DNI incorrecto')
            
resultadoLetra = diccAbc[cadenaNum%23]							#Comprobamos la letra correspondiente en el diccionario de letras con el resultado
print(f"La letra que corresponde al DNI introducido es: {resultadoLetra} y el NIF completo es {cadena}{resultadoLetra}")	#Victor Pena