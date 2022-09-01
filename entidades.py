from random import randint
import pygame as pg
class Bola:
    def __init__(self, center_x, center_y,radio=10, color=(255,255,0)):
        self.center_x = center_x
        self.center_y = center_y 
        self.color = color
        self.radio  = radio

        self.vx = 0
        self.vy = 0

    def dibujar(self,pantalla):
        pg.draw.circle(pantalla,self.color,(self.center_x,self.center_y), self.radio)
   
    def mover(self,raqueta1,raqueta2,x_max= 800 , y_max =600):
        self.center_x += self.vx
        self.center_y += self.vy

        if self.center_y  >= y_max - self.radio or self.center_y < self.radio :
            self.vy = self.vy * -1

        if self.center_x >=x_max or self.center_x<0:
             #Guardar Puntos
            if self.center_x >=x_max:
                raqueta1.puntos += 1               
            elif self.center_x<0:
                raqueta2.puntos += 1 
                
            self.center_x = x_max // 2
            self.center_y = y_max // 2 
            
            self.rebotar()

    def comprobar_choque(self,*raquetas):
        for raqueta_activa in raquetas:
            if self.derecha >= raqueta_activa.izquierda and \
                self.izquierda<= raqueta_activa.derecha and \
                self.abajo>= raqueta_activa.arriba and \
                self.arriba<= raqueta_activa.abajo:
                self.rebotar()

                return



    def rebotar(self):
 
            self.vy  = -5
            self.vy *= randint(-1,1)  
            self.vx *=  -1  

    @property
    def izquierda(self):
        return self.center_x - self.radio

    @property
    def derecha(self):
        return self.center_x + self.radio

    @property
    def arriba(self):
        return self.center_y - self.radio

    @property
    def abajo(self):
        return self.center_y + self.radio

class Raqueta:
    def __init__(self, center_x, center_y , w=120,h =20, color=(255,255,0)) -> None:
        self.center_x = center_x
        self.center_y = center_y 
        self.color = color
        self.w = w
        self.h  = h

        self.vx = 0
        self.vt = 0    

        self.puntos = 0

    def dibujar(self,pantalla):
        pg.draw.rect(pantalla,self.color,(self.center_x - self.w//2, self.center_y - self.h // 2, self.w, self.h))

    def mover(self,tecla_arriba,tecla_abajo,y_max=600 ):
        estado_teclas = pg.key.get_pressed()
        if estado_teclas[tecla_arriba]:   
            self.center_y -= self.vy
        if self.center_y < 0 + self.h //2:
            self.center_y = self.h //2

        if estado_teclas[tecla_abajo]:
            self.center_y += self.vy        
        if self.center_y > y_max - self.h //2:
            self.center_y = y_max - self.h //2

    @property
    def izquierda(self):
        return self.center_x - self.w //2

    @property
    def derecha(self):
        return self.center_x + self.w //2

    @property
    def arriba(self):
        return self.center_y - self.h //2

    @property
    def abajo(self):
        return self.center_y + self.h //2

