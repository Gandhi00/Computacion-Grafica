import pygame
import random

#movimiento

ANCHO=700
ALTO=600
NEGRO=[0,0,0]
AZUL=[100,100,255]
ROJO=[255,0,0]
VERDE=[0,255,0]
AMARILLO=[255,255,0]
BLANCO=[255,255,255]

class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("Airplane.png")
        self.rect=self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= (ALTO - self.rect.height) - 10
        self.velx=0
        self.vely=0
        self.Bloques = None

    def PositionPlayer(self):
        x = self.rect.x
        y = self.rect.y
        coord = [x,y]
        return coord

    def update(self):
        #colision x
        self.rect.x+=self.velx

        #colision y
        self.rect.y+=self.vely


if __name__ == '__main__':
    pygame.init()
    #Definicion de variables
    ventana=pygame.display.set_mode([ANCHO,ALTO])

    texturas = pygame.image.load('TileA1.png')

    listaImagenes=[]
    for i in range(16):
        cuadro = texturas.subsurface(0,0,32,32)
        listaImagenes.append(cuadro)

    jugadores=pygame.sprite.Group()
    bloques=pygame.sprite.Group()

    j=Jugador([300,200])
    jugadores.add(j)

    #bloque=Bloque([200,300],200,120)
    #bloques.add(bloque)

    #bloque2=Bloque([50,50],50,50)
    #bloques.add(bloque2)

    #j.Bloques = bloques


    finDeJuego = False

    reloj=pygame.time.Clock()
    fin=False


    while not fin:
        #Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx=5
                    j.vely=0
                if event.key == pygame.K_LEFT:
                    j.velx=-5
                    j.vely=0
                if event.key == pygame.K_UP:
                    j.vely= -5
                    j.velx=0
                if event.key == pygame.K_DOWN:
                    j.vely= 5
                    j.velx=0


            if event.type == pygame.KEYUP:
                j.vely=0
                j.velx=0

        #Controles Generales----------------------------------------------------------------------
        #Control de jugador
        if j.rect.x > ANCHO:
            j.rect.x=0-j.rect.width

        if j.rect.x < 0 - j.rect.width:
            j.rect.x=ANCHO




    #limpieza de memoria----------------------------------------------------------------------
        #Refresco
        if not finDeJuego:
            jugadores.update()
            ventana.fill(AZUL)
            ventana.blit(listaImagenes[7],[0,0])
            jugadores.draw(ventana)
            bloques.draw(ventana)
            pygame.display.flip()
            reloj.tick(40)
