comprobar = False																#Con el booleano gestionamos el fin del while si se cumplen las condiciones
while comprobar == False:    
    cadena = input("Escribe el CCC: ")

    try:    
        int(cadena)																#Pasarlo a int para comprobar que son numeros
        comprobar = True
    except ValueError:
        comprobar = False    

    if len(cadena)<20 or len(cadena)>20:										
	    comprobar = False														

    if comprobar == False:
    	print('Formato de CCC incorrecto')

#En este punto el CCC es correcto, solo queda realizar los calculos:
#He creado otra cadena aparte para poder conservar el numero de cuenta intacto y de esa manera concatenarlo al final en el resultado.

cadenaIBAN = cadena																#Paso a str para poder concatenar los numeros 14-E 28-S y los dos digitos de control
cadenaIBAN += '142800'															#Los dos digitos de control son 00, como en el ejemplo
cadenaNumIBAN = int(cadenaIBAN)													#Paso a int para poder realizar los calculos para sacar los dos digitos
resultadoIBAN = 98-(cadenaNumIBAN%97)
if resultadoIBAN<10:
    resultadoFinal = 'ES' + '0' + str(resultadoIBAN) + cadena					#Si es menor que 10 le concateno un 0 para que se quede como 0X y no X
else:
    resultadoFinal = 'ES' + str(resultadoIBAN) + cadena   

print(f"El código IBAN para la CCC introducida es: {resultadoFinal}")			#VictorPena


	