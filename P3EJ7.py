#Pida al usuario tres número que serán el día, mes y año. Comprueba que la fecha introducida es válida.
print("Hola, para recuperar la contraseña introduce los siguientes datos")
dia=int(input("Introduce el dia de nacimiento de tu hermana"))
mes=int(input("Introduce el mes de nacimiento de tu hermana"))
año=int(input("Introduce el año de nacimiento de tu hermana"))
if dia==15 and mes==2 and año==2005:
    print("Datos correctos ",dia,"/",mes,"/",año,)
else:
    print("Datos incorrectos")
    
    

