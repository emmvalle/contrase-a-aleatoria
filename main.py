import random
characteres= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
contrasena = int(input("pon la longitud de tu cotraseña"))
x= ""
for i in range(contrasena):
    x+= random.choice(characteres)

print("esta es tu contraseña",x)
