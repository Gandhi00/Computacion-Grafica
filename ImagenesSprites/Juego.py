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
    def __init__(self, pos, img):
        pygame.sprite.Sprite.__init__(self)
        self.img=img
        self.contador=0
        self.accion=1
        self.LimitesAnimaciones=[3,3,2,4,1,3,4,4,6,0]
        self.image=self.img[self.accion][self.contador]
        self.rect=self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= pos[1]
        self.velx=0
        self.vely=0
        self.Bloques = None


    def update(self):
        if self.contador < self.LimitesAnimaciones[self.accion]:
            self.contador += 1
        else:
            self.contador = 0
            self.accion=1
        self.image=self.img[self.accion][self.contador]

        self.rect.x+=self.velx
        self.rect.y+=self.vely

if __name__ == '__main__':

    pygame.init()
    #Definicion de variables
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    ken = pygame.image.load('ken.png')

    #recorte de imagen
    Columna = []
    for f in range(10):
        fila = []
        for c in range(7):
            cuadro = ken.subsurface(70*c,80*f,70,80)
            fila.append(cuadro)
        Columna.append(fila)

    jugadores=pygame.sprite.Group()
    j=Jugador([300,200], Columna)
    jugadores.add(j)

    contador = 0
    reloj = pygame.time.Clock()
    fin = False

    cadena = ''

    while not fin:
        #Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    j.accion=2
                    j.contador=0
                    cadena += 'c'
                if event.key == pygame.K_z:
                    cadena += 'z'
                if event.key == pygame.K_x:
                    cadena += 'x'
                if event.key == pygame.K_RIGHT:
                    j.velx=5
                    j.vely=0
                    j.direccion=1
                if event.key == pygame.K_LEFT:
                    j.velx=-5
                    j.vely=0
                    j.direccion=1
                if event.key == pygame.K_UP:
                    j.vely= -5
                    j.velx=0
                    j.direccion=3
                if event.key == pygame.K_DOWN:
                    j.vely= 5
                    j.velx=0
                    j.direccion=0

            if event.type == pygame.KEYUP:
                j.vely=0
                j.velx=0
                j.contador=0


        if len(cadena) >= 3:
            if cadena == 'zxc':
                print ("hado ken")
                cadena = ''
            else:
                cadena = ''

        jugadores.update()
        ventana.fill(NEGRO)
        #ventana.blit(Columna[5][contador],[0,0])
        jugadores.draw(ventana)
        pygame.display.flip()
        reloj.tick(40)
