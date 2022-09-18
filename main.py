
import time #IMPORT LIBRERIA TIME
#------------------------------------------------------------------Bienvenidos a mi TRIVIA de la BIBLIA, en esta oportunidad tendremos preguntas con 3 alternativas de las cuales solo uno es correcta. ¡ÉXITOS YOU CAN DO IT!
RED = '\033[31m'    #Color Rojo
BLUE = '\033[34m'  #Color Azul
MAGENTA = '\033[35m' #Color Fucsia
GREEN = '\033[32m'  #Color Verde
WHITE = '\033[37m' #Color blanco
RESET = '\033[39m'  #Finaliza el color

nombre = input(MAGENTA+"INGRESA TU NOMBRE: "+RESET)
print(GREEN+"-------------Bienvenid@ a mi TRIVIA BIBLICA ",WHITE+ nombre.upper()+RESET, "---------"+RESET)
print(GREEN+"--------- Pondremos a prueba cuanto conoces de la BIBLIA --------\n"+RESET)

time.sleep(1)
print(MAGENTA+"Nota: "+RESET, GREEN+"Responde las preguntas seleccionando la letra de la alternativa y presionando 'ENTER' para enviar tu respuesta. Además obtendrás un puntaje final por cada acierto se te sumará 10 puntos y por cada desacierto se te descontará 5 puntos \n"+RESET)

intentos=0
iniciar_juego = True 
time.sleep(1)

while iniciar_juego == True: 
  intentos += 1
  puntaje=0
  correctas=0

 #---------------------------------------------    
  #PREGUNTA1
  print(MAGENTA+"\nPREGUNTA 1) ¿A cuál tribu pertenecía Saúl?"+RESET)
  print(BLUE+"a) ¿Neftalí?"+RESET)
  print(BLUE+"b) ¿leví?"+RESET)
  print(BLUE+"c) ¿Benjamin?"+RESET)
  
  respuesta_1 = input("\nIngresa tu respuesta: ")
  while respuesta_1 not in ("a","b","c","*"):
    respuesta_1 = input("Debes responder a, b, c o *. Ingresa nuevamente: ")
  while respuesta_1 == "*":
      respuesta_1 = input("Comodín (Benjamin). Ingresa nuevamente: ")
  if respuesta_1 == "a":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  elif respuesta_1 == "b":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  else:
      puntaje+=10
      correctas+=1
      print(GREEN+" \n¡Muy bien! :) ----------------"+RESET)
      print(GREEN+" \n¡TIENES +10 PUNTOS!"+RESET)
      time.sleep(1)

  
  #PREGUNTA2
  print(MAGENTA+"\nPREGUNTA 2) ¿Cuántos años tenía Caleb cuando le pidió Hebrón a Josué?"+RESET)
  print(BLUE+"a) 40 años"+RESET)
  print(BLUE+"b) 85 años"+RESET)
  print(BLUE+"c) 120 años"+RESET)
  
  respuesta_2 = input("\nIngresa tu respuesta: ")
  while respuesta_2 not in ("a","b","c","*"):
    respuesta_2  = input("Debes responder a, b, c o *. Ingresa nuevamente: ")
  while respuesta_2 == "*":
    respuesta_2 = input("Comodín (85 años). Ingresa nuevamente: ")
  if respuesta_2 == "a":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  elif respuesta_2 == "c":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  else:
    puntaje+=10
    correctas+=1
    print(GREEN+" \n¡Muy bien! :) ----------------"+RESET)
    print(GREEN+" \n¡TIENES +10 PUNTOS!"+RESET)
    time.sleep(1) 

  #PREGUNTA3
  print(MAGENTA+"\nPREGUNTA 3) ¿Quiénes fueron algunos de los que se unieron a Pablo luego de oír su discurso en Atenas?"+RESET)
  print(BLUE+"a) Nicodemo y su familia"+RESET)
  print(BLUE+"b) Dionisio y Dámaris"+RESET)
  print(BLUE+"c) Arquímides y Jacobo"+RESET)
  
  respuesta_3 = input("\nIngresa tu respuesta: ")
  while respuesta_3 not in ("a","b","c","*"):
    respuesta_3  = input("Debes responder a, b, c o *. Ingresa nuevamente: ")
  while respuesta_3 == "*":
    respuesta_3 = input("Comodín (85 años). Ingresa nuevamente: ")
  if respuesta_3 == "a":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  elif respuesta_3 == "c":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  else:
    puntaje+=10
    correctas+=1
    print(GREEN+" \n¡Muy bien! :) ----------------"+RESET)
    print(GREEN+" \n¡TIENES +10 PUNTOS!"+RESET)
    time.sleep(1) 

      #PREGUNTA4
  print(MAGENTA+"\nPREGUNTA 4) ¿Cuál libro de la Biblia termina con un signo de interrogación?"+RESET)
  print(BLUE+"a) Jonás"+RESET)
  print(BLUE+"b) Joel"+RESET)
  print(BLUE+"c) Judas"+RESET)
  
  respuesta_4 = input("\nIngresa tu respuesta: ")
  while respuesta_4 not in ("a","b","c","*"):
    respuesta_4  = input("Debes responder a, b, c o *. Ingresa nuevamente: ")
  while respuesta_4 == "*":
    respuesta_4 = input("Comodín (Jonás). Ingresa nuevamente: ")
  if respuesta_4 == "b":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  elif respuesta_4 == "c":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  else:
    puntaje+=10
    correctas+=1
    print(GREEN+" \n¡Muy bien! :) ----------------"+RESET)
    print(GREEN+" \n¡TIENES +10 PUNTOS!"+RESET)
    time.sleep(1) 

     #PREGUNTA5
  print(MAGENTA+"\nPREGUNTA 5) ¿Cuántos versículos tiene el Salmo 119?"+RESET)
  print(BLUE+"a) 176 vers."+RESET)
  print(BLUE+"b) 200 vers."+RESET)
  print(BLUE+"c) 100 vers."+RESET)
  
  respuesta_5 = input("\nIngresa tu respuesta: ")
  while respuesta_5 not in ("a","b","c","*"):
    respuesta_5  = input("Debes responder a, b, c o *. Ingresa nuevamente: ")
  while respuesta_5 == "*":
    respuesta_5 = input("Comodín (176 vers.). Ingresa nuevamente: ")
  if respuesta_5 == "b":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  elif respuesta_5 == "c":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  else:
    puntaje+=10
    correctas+=1
    print(GREEN+" \n¡Muy bien! :) ----------------"+RESET)
    print(GREEN+" \n¡TIENES +10 PUNTOS!"+RESET)
    time.sleep(1) 

    #PREGUNTA6
  print(MAGENTA+"\nPREGUNTA 6) ¿Quién gobernó siendo rey y sacerdote al mismo tiempo?"+RESET)
  print(BLUE+"a) Joacaz"+RESET)
  print(BLUE+"b) Melquisedec"+RESET)
  print(BLUE+"c) Manasés"+RESET)
  
  respuesta_6 = input("\nIngresa tu respuesta: ")
  while respuesta_6 not in ("a","b","c","*"):
    respuesta_6  = input("Debes responder a, b, c o *. Ingresa nuevamente: ")
  while respuesta_6 == "*":
    respuesta_6 = input("Comodín (Melquisedec). Ingresa nuevamente: ")
  if respuesta_6 == "a":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  elif respuesta_6 == "c":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  else:
    puntaje+=10
    correctas+=1
    print(GREEN+" \n¡Muy bien! :) ----------------"+RESET)
    print(GREEN+" \n¡TIENES +10 PUNTOS!"+RESET)
    time.sleep(1) 

     #PREGUNTA7
  print(MAGENTA+"\nPREGUNTA 7) ¿Cuál fue la mujer que primero acogió a su enemigo y después lo mató?"+RESET)
  print(BLUE+"a) Raquel"+RESET)
  print(BLUE+"b) Débora"+RESET)
  print(BLUE+"c) Jael"+RESET)
  
  respuesta_7 = input("\nIngresa tu respuesta: ")
  while respuesta_7 not in ("a","b","c","*"):
    respuesta_7  = input("Debes responder a, b, c o *. Ingresa nuevamente: ")
  while respuesta_7 == "*":
    respuesta_7 = input("Comodín (Jael). Ingresa nuevamente: ")
  if respuesta_7 == "a":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  elif respuesta_7 == "b":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  else:
    puntaje+=10
    correctas+=1
    print(GREEN+" \n¡Muy bien! :) ----------------"+RESET)
    print(GREEN+" \n¡TIENES +10 PUNTOS!"+RESET)
    time.sleep(1) 

     #PREGUNTA8
  print(MAGENTA+"\nPREGUNTA 8) ¿Qué animal mordió a Pablo en la mano?"+RESET)
  print(BLUE+"a) Víbora"+RESET)
  print(BLUE+"b) Escorpión"+RESET)
  print(BLUE+"c) Lagarto"+RESET)
  
  respuesta_8 = input("\nIngresa tu respuesta: ")
  while respuesta_8 not in ("a","b","c","*"):
    respuesta_8  = input("Debes responder a, b, c o *. Ingresa nuevamente: ")
  while respuesta_8 == "*":
    respuesta_8 = input("Comodín (Víbora). Ingresa nuevamente: ")
  if respuesta_8 == "b":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  elif respuesta_8 == "c":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  else:
    puntaje+=10
    correctas+=1
    print(GREEN+" \n¡Muy bien! :) ----------------"+RESET)
    print(GREEN+" \n¡TIENES +10 PUNTOS!"+RESET)
    time.sleep(1) 


     #PREGUNTA9
  print(MAGENTA+"\nPREGUNTA 9) ¿Cómo se llamaba la mujer de Job?"+RESET)
  print(BLUE+"a) Abigail"+RESET)
  print(BLUE+"b) Amaráis"+RESET)
  print(BLUE+"c) La Biblia no dice"+RESET)
  
  respuesta_9 = input("\nIngresa tu respuesta: ")
  while respuesta_9 not in ("a","b","c","*"):
    respuesta_9  = input("Debes responder a, b, c o *. Ingresa nuevamente: ")
  while respuesta_9 == "*":
    respuesta_9 = input("Comodín (La Biblia no dice). Ingresa nuevamente: ")
  if respuesta_9 == "a":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  elif respuesta_9 == "b":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  else:
    puntaje+=10
    correctas+=1
    print(GREEN+" \n¡Muy bien! :) ----------------"+RESET)
    print(GREEN+" \n¡TIENES +10 PUNTOS!"+RESET)
    time.sleep(1) 


     #PREGUNTA10
  print(MAGENTA+"\nPREGUNTA 10) ¿Quién ideó y dirigió el proyecto para la construcción del arca?"+RESET)
  print(BLUE+"a) Noé"+RESET)
  print(BLUE+"b) Dios"+RESET)
  print(BLUE+"c) Obed-Edom"+RESET)
  
  respuesta_10 = input("\nIngresa tu respuesta: ")
  while respuesta_10 not in ("a","b","c","*"):
    respuesta_10  = input("Debes responder a, b, c o *. Ingresa nuevamente: ")
  while respuesta_10 == "*":
    respuesta_10 = input("Comodín (Dios). Ingresa nuevamente: ")
  if respuesta_10 == "a":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  elif respuesta_10 == "c":
    print(RED+"\n¡Fallaste!"+RESET)
    puntaje-=5
    print(RED+" \n¡TIENES -05 PUNTOS!"+RESET)
    time.sleep(1)
  else:
    puntaje+=10
    correctas+=1
    print(GREEN+" \n¡Muy bien! :) ----------------"+RESET)
    print(GREEN+" \n¡TIENES +10 PUNTOS!"+RESET)
    time.sleep(1) 


    
  #---------------------------------------------
  #MUESTRA EL PUNTAJE OBTENIDO
  if puntaje >= 80 and correctas >=80:
    print("\n",nombre.upper(),MAGENTA+"ERES UN GENIO \nTIENES: ", correctas, "respuesta(s) correcta(s)", "y un puntaje total de: "+RESET, puntaje)
  else:
      print(GREEN+"\n---------------> "+RESET,nombre.upper(),GREEN+"SIGUE INTENTANDO  <---------------  \nTIENES: ", correctas, "respuesta(s) correcta(s)", "y un puntaje total de: "+RESET, puntaje)
    
    #VOLVER A ITERAR EL JUEGO
  print("\nRealizaste",intentos,"intento(s)"," ¿Deseas jugar nuevamente?")
  repetir_juego = input(MAGENTA+"Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+RESET).lower()
  if repetir_juego != "si":
    print(MAGENTA+"Espero que lo hayas pasado bien, vuelve pronto"+RESET)
    iniciar_juego = False 