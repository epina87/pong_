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

#Crear Texto Player
miFuente = pg.font.Font(None,20)
texto_jugador1 = miFuente.render("Player-1",0,(200,60,80)) 
texto_jugador2 = miFuente.render("Player-2",0,(200,60,80)) 


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
    punto  = bola.mover()
    
    #Control Rebote Raqueta
    if bola.derecha >= raqueta2.izquierda and bola.abajo>= raqueta2.arriba and bola.arriba<= raqueta2.abajo:
        bola.rebotar()

    elif bola.izquierda <= raqueta1.derecha and bola.abajo>= raqueta1.arriba and bola.arriba<= raqueta1.abajo:
        bola.rebotar() 
    
    #Guardar Puntos
    if punto == "r1":
        raqueta1.puntos += 1 
    elif punto == "r2":    
        raqueta2.puntos += 1 
    Puntos_raqueta2 = miFuente.render(str(raqueta2.puntos),0,(200,60,80))
    Puntos_raqueta1 = miFuente.render(str(raqueta1.puntos),0,(200,60,80))

    #Mostrar Objetos
    pantalla_principal.fill((0,0,0))
    bola.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    #Mostrar Player
    pantalla_principal.blit(texto_jugador1,(100,10))
    pantalla_principal.blit(texto_jugador2,(700,10))

    #Mostrar Puntos
    pantalla_principal.blit(Puntos_raqueta1,(100,500))
    pantalla_principal.blit(Puntos_raqueta2,(700,500))

    #Envió Tarjeta Gráfica
    pg.display.flip()

