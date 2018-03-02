#!/usr/bin/env python
#created by jonathan sciott james the great
# this is justr pygame it required the gui to be running and focused to detect keys
# why cant it do this without it?
import  pygame, sys
from pygame.locals import*
print("esc key to exit the game window must be focused for this to work")
while True:
    DISPLAYSURF = pygame.display.set_mode((50,10)) # calls the gui before reading the keys
    while True:                          # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:       #quit if x on the game gui is clicked 
                pygame.quit()            #close the game window
                sys.exit()               #exit to the system
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:#quit if "esc" key pressed 
                    pygame.quit()        #close the game window
                    sys.exit()           #exit to the system
                print(event.key, end=" ") #test jsj pm , it works!!*************
#               print(event.key)          #altranate syntax works too*************



    
