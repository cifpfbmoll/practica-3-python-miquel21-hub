#Pida un número que como máximo tenga tres cifras (por ejemplo serían válidos 1, 99 i 213 pero no 1001). Si el usuario introduce un número de más de tres cifras debe un informar con un mensaje de error como este “ERROR: El número 1005 tiene más de tres cifras”.
Numero=int(input("Numero de tres cifras:\n"))
if -999>Numero or Numero>999:
     print("error")
else :
     print("Correct number")

