# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:18:53 2021

@author: Seren
"""

import sys, pygame
from sys import exit

def main():
    pygame.init()

    #Definiamo i colori e dimensione dello sfondo
    size = (800, 600)
    black = (0, 0, 0)
    
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Snake')
    
    clock = pygame.time.Clock() #verrà usato per controllare quanto velocemente si aggiorna lo screen
    carryOn = True
    
    while carryOn:
        for event in pygame.event.get():
            
            #Se l'utente vuole chiudere il gioco, preme sulla (x)
            if event.type == pygame.QUIT:
                carryOn = False
                pygame.quit()
                exit()
    
        
    
        screen.fill(black)
       # screen.blit(ball, ballrect)
       # pygame.display.flip()
        clock.tick(90)
    
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
