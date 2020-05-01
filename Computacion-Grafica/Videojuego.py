import pygame
import random

#aaaa

ANCHO=600
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
        self.Vida=3

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely

    def PositionPlayer(self):
        x = self.rect.x
        y = self.rect.y
        coord = [x,y]
        return coord

class Rival(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("Enemy Airplane.png")
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=5
        self.vely=0
        self.tiempoDisparo = random.randrange(40,60)

    def update(self):
        self.tiempoDisparo -= 1
        self.rect.x+=self.velx
        self.rect.y+=self.vely

    def PositionRival(self):
        x = self.rect.x - (self.rect.width / 2)
        y = self.rect.bottom
        coord = [x,y]
        return coord


class Bala(pygame.sprite.Sprite):
    def __init__(self, pos, cl = BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("Cohete.png")
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0] - self.rect.width / 2 + j.rect.width/2
        self.rect.y=pos[1] - self.rect.height/ 2
        self.vely=0

    def update(self):
        self.rect.y += self.vely

if __name__ == '__main__':
    pygame.init()
    #Definicion de variables
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    jugadores=pygame.sprite.Group()
    rivales=pygame.sprite.Group()
    balas = pygame.sprite.Group()
    balasRivales = pygame.sprite.Group()

    j=Jugador([300,200])
    jugadores.add(j)

    n=10
    for i in range(n):
        x=random.randrange(ANCHO)
        y=random.randrange(ALTO - 150)
        #vx=random.randrange(2,5)
        r=Rival([x,y])
        #r.velx=vx
        rivales.add(r)


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

            if event.type == pygame.MOUSEBUTTONDOWN:
                positionbullet = j.PositionPlayer()
                b = Bala(positionbullet)
                b.vely = -10
                balas.add(b)

            if event.type == pygame.KEYUP:
                j.vely=0
                j.velx=0

    #Controles Generales----------------------------------------------------------------------
        #Control de jugador
        if j.rect.x > ANCHO:
            j.rect.x=0-j.rect.width

        if j.rect.x < 0 - j.rect.width:
            j.rect.x=ANCHO

        #control de rivales
        for r in rivales:
            if r.rect.x > ANCHO - r.rect.width:
                r.rect.x=ANCHO - r.rect.width
                r.rect.y += 10
                r.velx = -5


            if r.rect.x < 0:
                r.rect.x=0
                r.rect.y += 10
                r.velx = 5

        #control disparo enemigo
        for r in rivales:
            if r.tiempoDisparo < 0:
                print("disparo")
                posRival = r.PositionRival()
                balaRival = Bala(posRival, ROJO)
                balaRival.vely = 5
                balasRivales.add(balaRival)
                r.tiempoDisparo = random.randrange(40,60)


    #Colisiones----------------------------------------------------------------------
        lista_Colisiones = pygame.sprite.spritecollide(j,rivales, False)

        for b in balasRivales:
            colisionBalaJugador = pygame.sprite.spritecollide(b,jugadores, False)
            for j in colisionBalaJugador:
                j.Vida -= 1

        for j in jugadores:
            if j.Vida < 0:
                finDeJuego = True

        for b in balas:
            colisionBalaEnemigo = pygame.sprite.spritecollide(b,rivales, True)

            for colision in colisionBalaEnemigo:
                balas.remove(b)



#limpieza de memoria----------------------------------------------------------------------
    #balas aliadas
        for b in balas:
            if b.rect.y < -40:
                balas.remove(b)


        #balas enemigas
        for b in balasRivales:
            if b.rect.y > ALTO:
                balas.remove(b)

        #Refresco
        if not finDeJuego:
            jugadores.update()
            rivales.update()
            balas.update()
            balasRivales.update()
            ventana.fill(AZUL)
            jugadores.draw(ventana)
            rivales.draw(ventana)
            balas.draw(ventana)
            balasRivales.draw(ventana)
            pygame.display.flip()
            reloj.tick(40)
        else:
            fuente = pygame.font.Font(None,60)
            mensaje = fuente.render('Fin de Juego',True,BLANCO)
            ventana.fill(NEGRO)
            ventana.blit(mensaje,[100,100])
            pygame.display.flip()
