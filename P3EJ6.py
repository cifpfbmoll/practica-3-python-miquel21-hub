#Pida al usuario el precio de un producto y el nombre del producto y muestre\
# el mensaje con el precio del IVA (21%). 
print("Hola, bienvenido a nuestra tienda Orbea")
name=input("¿Cual es el modelo de su bicicleta?")
if name=="red" :
     print("Su bicicleta cuesta 123,97 y con el 21 % de iva seran 150€")
elif name=="black":
     print("Su bicicleta cuesta 223,14 y con el 21 % de iva se quedará en 270€")
else :
     print("Su bicicleta vale 100 y con el iva se queda en 120")
