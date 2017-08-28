from random import *

def generarmazo():
    return sample( [(x,y) for x in ['A','J','Q','K',2,3,4,5,6,7,8,9,10] for y in ['♥','♦','♣','♥'] ], 52)
def valor_carta(carta):
    if carta[0]=='J' or carta[0]=='Q' or carta[0]=='K':
        return 10;
    if carta[0]=='A':
        return 11;
    return int(carta[0]);


def valor_mano(mano):
    if mano==[]:
        return 0;
    return valor_carta(mano[0])+valor_mano(mano[1:])

def jugar(mazo, casa, jugador):
    if casa!=[] and jugador!=[]:
        print ("La casa tiene las cartas: ",casa[0], " <_,_> ")
        print()
        print ("Tienes las cartas: ",jugador ,"Con un puntaje de ", valor_mano(jugador))
        print()
        if mazo!=[]:
            if valor_mano(jugador)<21:
                if (input("¿Desea tomar otra carta?(s/n)")==('s' or 'S')):
                    jugar(mazo[1:],casa,jugador+mazo[:1])
                else:juegopc(mazo,casa,jugador)
            elif valor_mano(jugador)==21:
                print("Tienes 21, es turno de la casa")
                juegopc(mazo,casa,jugador)
            else: print("Te has pasado :'c pierdes :c")
    else:
        jugar(mazo[4:],mazo[:2], mazo[2:4])
        
def juegopc(mazo, casa, jugador):
    print("La casa tiene ", casa, " con un total de ", valor_mano(casa))
   
    if valor_mano(casa)==21:
        print("la casa gana")
    elif valor_mano(casa)<21 and valor_mano(casa)<valor_mano(jugador):
        juegopc(mazo[1:], casa+mazo[:1], jugador)
    elif valor_mano(casa)>=valor_mano(jugador) and valor_mano(casa)<21:
            print("La casa gana")
    else:
        print("Has ganado con : ", jugador )
    
print("Iniciando:")
jugar(generarmazo(),[],[])
