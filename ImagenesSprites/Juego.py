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
    def __init__(self, pos, img, limiteY):
        pygame.sprite.Sprite.__init__(self)
        self.img=img
        self.contador=0
        self.accion=1
        self.limiteY=limiteY
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
        if self.rect.bottom < self.limiteY:
            self.rect.bottom=self.limiteY
            self.vely=0
        if self.rect.bottom > ALTO:
            self.rect.bottom=ALTO
        self.rect.y+=self.vely

class bloque(pygame.sprite.Sprite):
    def __init__(self, pos, dim,cl=VERDE):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dim)
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= pos[1]
        self.velx=0

    def update(self):
        self.rect.x+=self.velx

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
    bloques=pygame.sprite.Group()
    limiteY = 370

    j=Jugador([300,400], Columna,limiteY)
    jugadores.add(j)

    b=bloque([370,370],[70,70],AZUL)
    bloques.add(b)


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

        #Identificacion de Combos
        if len(cadena) >= 3:
            if cadena == 'zxc':
                print ("hado ken")
                cadena = ''
            else:
                cadena = ''

        #Identificacion de colisiones
        listaColision = pygame.sprite.spritecollide(j,bloques,False)
        for b in listaColision:
            if j.accion==2:
                if ((j.rect.bottom) > b.rect.bottom - 20) and ((j.rect.bottom) < b.rect.bottom + 20):
                    b.velx=5

        #friccion de bloques
        for b in bloques:
            if b.velx > 0:
                b.velx -= 1

        #update de elementos
        jugadores.update()
        bloques.update()
        ventana.fill(NEGRO)

        #linea de horizonte
        pygame.draw.line(ventana,BLANCO,[0,limiteY],[ANCHO,limiteY])

        #base del jugador
        pygame.draw.line(ventana,BLANCO,[j.rect.left - 20,j.rect.bottom],[j.rect.right + 20,j.rect.bottom])

        #base de los bloques
        for b in bloques:
            pygame.draw.line(ventana,BLANCO,[b.rect.left - 20,b.rect.bottom],[b.rect.right + 20,b.rect.bottom])
            #rango de ataque
            pygame.draw.line(ventana,AMARILLO,[b.rect.left - 20,b.rect.bottom + 15],[b.rect.right + 20,b.rect.bottom + 15])
            pygame.draw.line(ventana,AMARILLO,[b.rect.left - 20,b.rect.bottom - 15],[b.rect.right + 20,b.rect.bottom - 15])

        #ventana.blit(Columna[5][contador],[0,0])

        #dibujo de elementos
        bloques.draw(ventana)
        jugadores.draw(ventana)

        #actualizacion y reloj
        pygame.display.flip()
        reloj.tick(40)

        '''
                listaColision = pygame.sprite.spritecollide(j,bloques,False)
                for b in listaColision:
                    if j.rect.y >= b.rect.y - 10 and j.rect.y <= b.rect.y + 10:
                        if j.accion==2:
                            if j.rect.x < b.rect.x:
                                b.velx=5
                            if j.rect.x > b.rect.x:
                                b.velx=-5

                for b in bloques:
                    if b.velx > 0:
                        b.velx -= 1
                    if b.velx < 0:
                        b.velx += 1


                jugadores.update()
                bloques.update()
                ventana.fill(NEGRO)
                #ventana.blit(Columna[5][contador],[0,0])
                for b in bloques:
                    if j.rect.y >= b.rect.y:
                        bloques.draw(ventana)
                        jugadores.draw(ventana)

                    if j.rect.y < b.rect.y:
                        jugadores.draw(ventana)
                        bloques.draw(ventana)
                pygame.display.flip()
                reloj.tick(40)
        '''
