#Variables
my_string_var= "Mi variable cadena"
print(my_string_var)

my_int_var = 10
print(my_int_var)

my_boole_var = False
print(my_boole_var)

#concatena cadenas
print(my_boole_var,my_string_var)

convertie_int_str = str(my_int_var)
print(type(convertie_int_str))

#Funciones Precargadas en el sistema
print("\n Mi caddena string tiene ", len(my_string_var))

#varioables en una sola linea
name, surneame, aplias, edad = "David","Cruz", "Dave", 25 
print("\n me llamo: ",name,"\n me apellido:",surneame, "\n mi alias:",aplias,"\n y tengo la edad de:",edad)

#intrducir valores desde teclado
first_nmame = input ('Cual es tu nombre? ')
print(first_nmame)

age = input("Cual es tu edad?")
print(age)

#Forzamas el tipo de dato
address: str ="Mi direccion"
address = 32
print(type(address))
