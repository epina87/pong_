import pygame as pg
from entidades import Bola,Raqueta

#Inicio
pg.init()
#Crear Pantalla
pantalla_principal = pg.display.set_mode((800,600))
#Titulo Juego
pg.display.set_caption("Pong ")

#Guardar clase tiempo
cronometro = pg.time.Clock()

#Crear Var. Control Salida Juego
game_over = False

#Crear Bola
bola = Bola(400,300,color=(255,255,255))
#Asignar Velocidad Bola
bola.vx = 5
bola.vy = -5

#Crear Raqueta
raqueta1 = Raqueta(20,300,w=20,h=120,color=(255,255,255))
raqueta2 = Raqueta(780,300,w=20,h=120,color=(255,255,255))
#Asignar Velocidad Raqueta
raqueta2.vy = 5
raqueta1.vy = 5

#Crear Línea Centro
lin_Centro = Raqueta(400,300,w=5,h=600,color=(0,255,255))

#Crear Texto Player
miFuente = pg.font.Font(None,30)
texto_jugador1 = miFuente.render("Player-1",0,(0,255,255)) 
texto_jugador2 = miFuente.render("Player-2",0,(0,255,255)) 


#Bucle Juego
while not game_over:
    # Control de tiempo 
    dt = cronometro.tick(60)
    #Gestión Eventos
    for evento in pg.event.get():
        #Salir Juego
        if evento.type == pg.QUIT:
            game_over = True

    #Mover Raqueta
    raqueta2.mover(pg.K_UP,pg.K_DOWN)
    raqueta1.mover(pg.K_w,pg.K_s)

    #Mover Bola y retorna punto
    bola.mover(raqueta1,raqueta2)

    #Control Rebote Raqueta
    bola.comprobar_choque(raqueta1,raqueta2)
        
    #Guardar Puntos
    Puntos_raqueta2 = miFuente.render(str(raqueta2.puntos),0,(0,255,255))
    Puntos_raqueta1 = miFuente.render(str(raqueta1.puntos),0,(0,255,255))

    #Mostrar Objetos
    pantalla_principal.fill((0,0,0))
    bola.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    lin_Centro.dibujar(pantalla_principal)

    #Mostrar Player
    pantalla_principal.blit(texto_jugador1,(150,10))
    pantalla_principal.blit(texto_jugador2,(550,10))

    #Mostrar Puntos
    pantalla_principal.blit(Puntos_raqueta1,(150,500))
    pantalla_principal.blit(Puntos_raqueta2,(550,500))

    #Envió Tarjeta Gráfica
    pg.display.flip()

