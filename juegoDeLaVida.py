import numpy as np
import pygame
import time

pygame.init() # iniciamos el pygame

ancho, alto = 600, 600
pantalla = pygame.display.set_mode((ancho,alto)) # creamos la pantalla
fondoPantalla = 35,35,35 # de color casi negro

pantalla.fill(fondoPantalla) # se pinta el fondo de la pantalla

# numero de celdas en cada eje
celdasX, celdasY = 50,50

anchoCeldas = ancho / celdasX # ancho de la celda
altoCeldas = alto / celdasY # alto de la celda

pauseExecution = False # control de la ejecución del juego

# celda a 1 --> viva || celda a 0 --> muerta
estadoTablero = np.zeros((celdasX,celdasY)) # matriz de tamaño del tablero

# inicialización del tablero
# palo
estadoTablero[5,3] = 1
estadoTablero[5,4] = 1
estadoTablero[5,5] = 1

# automata que se mueve por pantalla
estadoTablero[21,21] = 1
estadoTablero[22,22] = 1
estadoTablero[22,23] = 1
estadoTablero[21,23] = 1
estadoTablero[20,23] = 1

while True:
    # para no sobreescribir el tablero puesto que las comparaciones se hacen con el estado inicial y no con el actualizado en el momento
    copiaTablero = np.copy(estadoTablero)

    # limpiamos la pantalla
    pantalla.fill(fondoPantalla) # se pinta el fondo de la pantalla

    # delay
    time.sleep(0.2)

    ev = pygame.event.get() 

    for event in ev:
        if event.type == pygame.KEYDOWN: # al pulsar el teclado
            pauseExecution = not pauseExecution
        
        mouseClick = pygame.mouse.get_pressed() # nos da el boton izq, rueda o boton derecho pulsado

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos() # lo devuelve en pixeles
            celX, celY = int(np.floor(posX / anchoCeldas)), int(np.floor(posY / altoCeldas)) # pos celda
            copiaTablero[celX,celY] = not mouseClick[2] # si pulso el izq pon 0, si pulso otro pon 1

    # recorremos el tablero
    for y in range (0,celdasY):
        for x in range (0,celdasX):

            if not pauseExecution:
                # vecinos cercanos a cada x,y
                # con el modulo conseguimos que el vecino del tablero de un borde actue como un toroide [de la izquierda se pasa a la derecha y de arriba a abajo]
                vecinos = estadoTablero[(x-1) % celdasX,(y-1) % celdasY] + \
                        estadoTablero[(x-1) % celdasX,(y) % celdasY] + \
                        estadoTablero[(x-1) % celdasX,(y+1) % celdasY] + \
                        estadoTablero[(x) % celdasX,(y-1) % celdasY] + \
                        estadoTablero[(x) % celdasX,(y) % celdasY] + \
                        estadoTablero[(x+1) % celdasX,(y-1) % celdasY] + \
                        estadoTablero[(x+1) % celdasX,(y) % celdasY] + \
                        estadoTablero[(x+1) % celdasX,(y+1) % celdasY] 

                # regla 1 del juego de la vida: si muerto y tres vecinos vivos, entonces revive
                if estadoTablero[x,y] == 0 and vecinos == 3:
                    copiaTablero[x,y] = 1
                
                # regla 2 del juego de la vida: si vivo y vecinos menor que 2 o mayor que 3, entonces muere
                elif estadoTablero[x,y] == 1 and (vecinos < 2 or vecinos > 3):
                    copiaTablero[x,y] = 0

            # polígono
            poligono = [((x)*anchoCeldas, (y)*altoCeldas),
                        ((x+1)*anchoCeldas, (y)*altoCeldas),
                        ((x+1)*anchoCeldas, (y+1)*altoCeldas),
                        ((x)*anchoCeldas, (y+1)*altoCeldas)]

            # el ultimo término es el grosor del poligono
            if copiaTablero[x,y] == 0: # muerto en negro
                pygame.draw.polygon(pantalla, (128,128,128), poligono, 1) 
            else: # vivo en blanco
                pygame.draw.polygon(pantalla, (255,255,255), poligono, 0)

    estadoTablero = np.copy(copiaTablero)

    pygame.display.flip() # actualizo los fotogramas