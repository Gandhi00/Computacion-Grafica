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

class Bloque(pygame.sprite.Sprite):
    def __init__(self, pos, anchura, altura, color=VERDE):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([anchura, altura])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= pos[1]
        self.VelocidadFondo = 0

    def update(self):
        pass
        #self.rect.x += self.VelocidadFondo


if __name__ == '__main__':

    pygame.init()
    #Definicion de variables
    ventana=pygame.display.set_mode([ANCHO,ALTO])

    animal = pygame.image.load('animales.png')

    #recortar columnas
    filas=[]
    for j in range(8):
        columnas=[]
        for i in range(12):
            recorte = animal.subsurface(32*i,32*j,32,32)
            columnas.append(recorte)
        filas.append(columnas)

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
    cont = 0

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
        if cont >= 2:
            cont = 0
        else:
            cont += 1

        if not finDeJuego:
            jugadores.update()
            ventana.fill(VERDE)
            ventana.blit(filas[1][cont],[0,0])
            jugadores.draw(ventana)
            bloques.draw(ventana)
            pygame.display.flip()
            reloj.tick(40)
