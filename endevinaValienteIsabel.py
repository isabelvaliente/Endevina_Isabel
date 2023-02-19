# Isabel Valiente Pardo.

# El import serveix per a traure el número atzar.
import random


# Una xicoteta explicació del joc.
print("------------------------------------------------------------------------------------------------------------")
print("Aquest programa crea un número aleatori entre l'1 i el 100, creus que eres capaç d'endevinar-lo? \nIntenta-ho.")
print("------------------------------------------------------------------------------------------------------------")
    
# Inicialitzem les variables necessàries.
altraPartida = True
comptadorPartides = 0
partidesGuanyades = 0
minimIntents = 10000000
maximintents = 0
acumulaorIntents = 0
partidaGuanyada = False

# Posem el while que serveix per a poder fer diverses partides.
while altraPartida :
    # Fem la variable que ens creara la clau aleatòria.
    atzar = random.randint(1, 100)
    
    # Inicialitzem altres variables.
    valorMinim = 1
    valorMaxim = 100
    
    # Demanem per teclat quants intents necessitaria per a encertar la clau.
    cuantitatIntents = int(input("Quants intents creus que et faran falta per a endevinar la clave? "))
    
    # Utilitzem el for perquè demane per teclat tants intents com hagen introduït abans.
    for intents in range(1, cuantitatIntents+1):
        # Demanem per teclat els intents.
        resposta = int(input(f"Intent {intents}: "))
        
        # Posem if,elif i else. Per si enccerta, per al rang i per a que done error si posa un número fora del rang.
        if resposta == atzar:
            print("------------------------------------------------------------------------------------------------------------")
            print(f"Molt bé! Ho has encertat en {intents} intents.")
            print("------------------------------------------------------------------------------------------------------------\n")
            partidesGuanyades +=1
            acumulaorIntents = acumulaorIntents + intents
            partidaGuanyada = True              
            break
        
        elif resposta > atzar and resposta <= valorMaxim:
            valorMaxim = resposta-1
            print(f"No. És menor. Està entre {valorMinim} i {valorMaxim}") 
                  
        elif resposta < atzar and resposta >= valorMinim:
                valorMinim = resposta+1
                print(f"No. És major. Està entre {valorMinim} i {valorMaxim}" )
        else: 
            print(f"No està en eixe rang. Està entre {valorMinim} i {valorMaxim}")
    # El else aquest serveix per si ix del bucle perquè s'ha quedat sense intents.    
    else:
        print("------------------------------------------------------------------------------------------------------------")
        print(f"Has perdut, la clau era {atzar}")
        print("------------------------------------------------------------------------------------------------------------")
    
    # Serveix per a traure els intents màxims i mínims de les partides guanyades.
    if partidaGuanyada:
        if intents < minimIntents:
            minimIntents = intents
            
        if intents > maximintents:
            maximintents = intents
    # Compta les partides que s'han jugat.  
    comptadorPartides += 1    
    # Es pregunta si es vol fer una altra partida.
    resposta2 = input("Vols fer una altra partida?\n\nPosa S o s per a continuar i cualsevol altra cosa per a finalitzar: ")
    
    # Aquest if fa que depenent de la resposta torne ha repetir-se el while o no.
    if resposta2 == "s" or resposta2 == "S":
        altraPartida = True
    else:
        altraPartida = False
    
        
    print("------------------------------------------------------------------------------------------------------------")

# Depenent de si s'ha jugat una partida o moltes mostra el missatge en plural o singular.
if comptadorPartides == 1: 
    # Tant en aquest print com en el de baix es mostren les partides guanyades respecte a les que s'han jugat.  
    print(f"Has guanyat {partidesGuanyades} de {comptadorPartides} partida.\n")
else:
    print(f"Has guanyat {partidesGuanyades} de {comptadorPartides} partides.\n")


""" Si no s'ha guanyat cap partida es mostrara el missatge de que no has encertat cap partida,
si no es mostrara els premis, la mitjana d'intents i els intents màxims y mínims de les 
partides guanyades"""  
if partidesGuanyades == 0:
    print("No has encertat cap partida")
else:
    
    print("PREMI\n"*partidesGuanyades)
    print("La mitja d'intents es: ", acumulaorIntents/partidesGuanyades)
    print("El mínim d'intents per partida es ", minimIntents, " i el màxim de ", maximintents, "\n")