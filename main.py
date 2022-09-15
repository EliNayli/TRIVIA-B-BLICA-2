#------------------------------------------------------------------Bienvenidos a mi TRIVIA de la BIBLIA, en esta oportunidad tendremos preguntas con 3 alternativas de las cuales solo uno es correcta. ¡ÉXITOS YOU CAN DO IT!
nombre = input("Ingresa tu nombre: ")
print("-------------Bienvenid@ a mi trivia", nombre.upper(), "---------")
print("--------- Pondremos a prueba cuanto conoces de la BIBLIA --------\n")
print(
    "Nota: Responde las preguntas seleccionando la letra de la alternativa y presionando 'ENTER' para enviar tu respuesta. Además obtendrás un puntaje final por cada acierto se te sumará 10 puntos y por cada desacierto se te descontará 5 puntos \n"
)
x=0
#PREGUNTA1
print("PREGUNTA 1) ¿A cuál tribu pertenecía Saúl?")
print("a) ¿Neftalí?")
print("b) ¿leví?")
print("c) ¿Benjamin?")

respuesta_1 = input("\nIngresa tu respuesta: ")

while respuesta_1 not in ("a","b","c","*"):
  respuesta_1 = input("Debes responder a, b, c o *.Ingresa nuevamente: ")
if respuesta_1 == "*":
  respuesta_1 = input("Mensaje secreto (Benjamin). Ingresa nuevamente: ")
  print(" \n¡Muy bien! :) ----------------")
  x+=10
elif respuesta_1 == "a":
  print("\n¡Fallaste! - La respuesta es: Benjamin\n")
  x-=5
elif respuesta_1 == "b":
  print("\n¡Fallaste! - La respuesta es: Benjamin\n")
  x-=5
else:
  print(" \n¡Muy bien! :) ----------------")
  x+=10
  
#PREGUNTA2
  
print("\nPREGUNTA 2) ¿Cuántos años tenía Caleb cuando le pidió Hebrón a Josué?")
print("a) 40 años")
print("b) 85 años")
print("c) 120 años")

respuesta_2 = input("\nIngresa tu respuesta: ")
while respuesta_2 not in ("a","b","c","*"):
  respuesta_2 = input("Debes responder a, b, c o *.Ingresa nuevamente: ")
if respuesta_2 == "*":
  respuesta_2 = input("Mensaje secreto (85 años). Ingresa nuevamente: ")
  print(" \n¡Muy bien! :) ----------------")
  x+=10
elif respuesta_2 =="a":
  print("\n¡Fallaste! - La respuesta es: 85 años\n")
  x-=5
elif respuesta_2 == "c":
  print("\n¡Fallaste! - La respuesta es: 85 años\n")
  x-=5
else:
  print(" \n¡Muy bien! :) ----------------")
  x+=10

#PREGUNTA3
  
print("\nPREGUNTA 3) ¿Quiénes fueron algunos de los que se unieron a Pablo luego de oír su discurso en Atenas?")
print("a) Nicodemo y su familia")
print("b) Dionisio y Dámaris")
print("c) Arquímides y Jacobo")

respuesta_3 = input("\nIngresa tu respuesta: ")
while respuesta_3 not in ("a","b","c","*"):
  respuesta_3 = input("Debes responder a, b, c o *.Ingresa nuevamente: ")
if respuesta_3 == "*":
  respuesta_3 = input("Mensaje secreto (Dionisio y Dámaris). Ingresa nuevamente: ")
  print(" \n¡Muy bien! :) ----------------")
  x+=10
elif respuesta_3 == "a":
  print("\n¡Fallaste! - La respuesta es: Dionisio y Dámaris\n")
  x-=5
elif respuesta_3 == "c":
  print("\n¡Fallaste! - La respuesta es: Dionisio y Dámaris\n")
  x-=5
else:
  print(" \n¡Muy bien! :) ----------------")
  x+=10

#PREGUNTA4
  
print("\nPREGUNTA 4) ¿Cuál libro de la Biblia termina con un signo de interrogación?")
print("a) Jonás")
print("b) Joel")
print("c) Judas")

respuesta_4 = input("\nIngresa tu respuesta: ")
while respuesta_4 not in ("a","b","c","*"):
  respuesta_4 = input("Debes responder a, b, c o *.Ingresa nuevamente: ")
if respuesta_4 == "*":
  respuesta_4 = input("Mensaje secreto (Jonás). Ingresa nuevamente: ")
  print(" \n¡Muy bien! :) ----------------")
  x+=10
elif respuesta_4 == "b":
  print("\n¡Fallaste! - La respuesta es: Jonás\n")
  x-=5
elif respuesta_4 == "c":
  print("\n¡Fallaste! - La respuesta es: Jonás\n")
  x-=5
else:
  print(" \n¡Muy bien! :) ----------------")
  x+=10

#PREGUNTA5
  
print("\nPREGUNTA 5) ¿Cuántos versículos tiene el Salmo 119?")
print("a) 176 vers.")
print("b) 200 vers.")
print("c) 100 vers.")

respuesta_5 = input("\nIngresa tu respuesta: ")
while respuesta_5 not in ("a","b","c","*"):
  respuesta_5 = input("Debes responder a, b, c o *.Ingresa nuevamente: ")
if respuesta_5 == "*":
  respuesta_5 = input("Mensaje secreto (176 vers.). Ingresa nuevamente: ")
  print(" \n¡Muy bien! :) ----------------")
  x+=10
elif respuesta_5 == "b":
  print("\n¡Fallaste! - La respuesta es: 176 vers.\n")
  x-=5
elif respuesta_5 == "c":
  print("\n¡Fallaste! - La respuesta es: 176 vers.\n")
  x-=5
else:
  print(" \n¡Muy bien! :) ----------------")
  x+=10

#PREGUNTA6
  
print("\nPREGUNTA 6) ¿Quién gobernó siendo rey y sacerdote al mismo tiempo?")
print("a) Joacaz")
print("b) Melquisedec")
print("c) Manasés")

respuesta_6 = input("\nIngresa tu respuesta: ")
while respuesta_6 not in ("a","b","c","*"):
  respuesta_6 = input("Debes responder a, b, c o *.Ingresa nuevamente: ")
if respuesta_6 == "*":
  respuesta_6 = input("Mensaje secreto (Melquisedec). Ingresa nuevamente: ")
  print(" \n¡Muy bien! :) ----------------")
  x+=10
elif respuesta_6 == "a":
  print("\n¡Fallaste! - La respuesta es: Melquisedec\n")
  x-=5
elif respuesta_6 == "c":
  print("\n¡Fallaste! - La respuesta es: Melquisedec\n")
  x-=5
else:
  print(" \n¡Muy bien! :) ----------------")
  x+=10

#PREGUNTA7
  
print("\nPREGUNTA 7) ¿Cuál fue la mujer que primero acogió a su enemigo y después lo mató?")
print("a) Raquel")
print("b) Débora")
print("c) Jael")

respuesta_7 = input("\nIngresa tu respuesta: ")
while respuesta_7 not in ("a","b","c","*"):
  respuesta_7 = input("Debes responder a, b, c o *.Ingresa nuevamente: ")
if respuesta_7 == "*":
  respuesta_7 = input("Mensaje secreto (Jael). Ingresa nuevamente: ")
  print(" \n¡Muy bien! :) ----------------")
  x+=10
if respuesta_7 == "a":
  print("\n¡Fallaste! - La respuesta es: Jael\n")
  x-=5
elif respuesta_7 == "b":
  print("\n¡Fallaste! - La respuesta es: Jael\n")
  x-=5
else:
  print(" \n¡Muy bien! :) ----------------")
  x+=10

#PREGUNTA8
  
print("\nPREGUNTA 8) ¿Qué animal mordió a Pablo en la mano?")
print("a) Víbora")
print("b) Escorpión")
print("c) Lagarto")

respuesta_8 = input("\nIngresa tu respuesta: ")
while respuesta_8 not in ("a","b","c","*"):
  respuesta_8 = input("Debes responder a, b, c o *.Ingresa nuevamente: ")
if respuesta_8 == "*":
  respuesta_8 = input("Mensaje secreto (Víbora). Ingresa nuevamente: ")
  print(" \n¡Muy bien! :) ----------------")
  x+=10
elif respuesta_8 == "b":
  print("\n¡Fallaste! - La respuesta es: Víbora\n")
  x-=5
elif respuesta_8 == "c":
  print("\n¡Fallaste! - La respuesta es: Víbora\n")
  x-=5
else:
  print(" \n¡Muy bien! :) ----------------")
  x+=10

#PREGUNTA9
  
print("\nPREGUNTA 9) ¿Cómo se llamaba la mujer de Job?")
print("a) Abigail")
print("b) Amaráis")
print("c) La Biblia no dice")

respuesta_9 = input("\nIngresa tu respuesta: ")
while respuesta_9 not in ("a","b","c","*"):
  respuesta_9 = input("Debes responder a, b, c o *.Ingresa nuevamente: ")
if respuesta_9 == "*":
  respuesta_9 = input("Mensaje secreto (La Biblia no dice). Ingresa nuevamente: ")
  print(" \n¡Muy bien! :) ----------------")
  x+=10
elif respuesta_9 == "a":
  print("\n¡Fallaste! - La respuesta es: La Biblia no dice\n")
  x-=5
elif respuesta_9 == "b":
  print("\n¡Fallaste! - La respuesta es: La Biblia no dice\n")
  x-=5
else:
  print(" \n¡Muy bien! :) ----------------")
  x+=10

#PREGUNTA10
  
print("\nPREGUNTA 10) ¿Quién ideó y dirigió el proyecto para la construcción del arca?")
print("a) Noé")
print("b) Dios")
print("c) Obed-Edom")

respuesta_10 = input("\nIngresa tu respuesta: ")
while respuesta_10 not in ("a","b","c","*"):
  respuesta_10 = input("Debes responder a, b, c o *.Ingresa nuevamente: ")
if respuesta_10 == "*":
  respuesta_10 = input("Mensaje secreto (Dios). Ingresa nuevamente: ")
  print(" \n¡Muy bien! :) ----------------")
  x+=10
elif respuesta_10 == "a":
  print("\n¡Fallaste! - La respuesta es: Dios\n")
  x-=5
elif respuesta_10 == "c":
  print("\n¡Fallaste! - La respuesta es: Dios\n")
  x-=5
else:
  print(" \n¡Muy bien! :) ----------------")
  x+=10


if x >= 80: 
  print("\n", nombre.upper(), "ERES UN GENIO TIENES: ", x , "PUNTOS")
  
else:
  print("\n", nombre.upper()," VAS BIEN TIENES: ", x , "PUNTOS")