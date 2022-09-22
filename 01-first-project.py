import random

print("----------------------------------------")
print("Creador de nombre random para tu cerveza")
print("---------------------------------------- \n")

name = input("Cual es tu nombre?: ")
beer_type = input(f"Perfecto {name}, Cual es el color de tu cerveza?: ").lower()
beer = input("Por ultimo. Con quue identificarías tu cerveza en una palabra: ").lower().capitalize()
default_prepositions = ['de', 'en', 'entre', 'tras']


print(f"Listo, el nombre con mejor coincidencía es:\n"
      f" '{beer} { random.choice( default_prepositions ) } { beer_type }'")


num1 = round( 13/2, 0 )

print( num1)
