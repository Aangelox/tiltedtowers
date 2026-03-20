import turtle

turtle.speed(10000000)

class Casa:

    def __init__(self, toit, porte, nbetage, couleur):
        self.toit = toit
        self.porte = porte
        self.nbetage = nbetage
        self.couleur = couleur
        self.coord = turtle.pos()

    def pos(self):
        turtle.pos()

    def fenetre(self):
        pass

    def dessinporte(self):
        turtle.color('black', 'black')
        turtle.seth(0)
        turtle.penup()
        turtle.sety(self.coord[1])
        turtle.setx(self.coord[0] + 55)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(50)
        turtle.end_fill()

    def rdc(self):
        turtle.seth(0)
        turtle.color('black', self.couleur)
        turtle.begin_fill()
        turtle.forward(140)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(140)
        turtle.left(90)
        turtle.forward(60)
        turtle.end_fill()
        self.dessinporte()
        self.fenetre('gauche', 0)
        self.fenetre('droite', 0)

    def etage(self, nb):
        turtle.seth(0)
        turtle.color('black', self.couleur)
        turtle.penup()
        turtle.sety(self.coord[1] + 60 * nb)
        turtle.setx(self.coord[0])
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(140)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(140)
        turtle.left(90)
        turtle.forward(60)
        turtle.end_fill()
        self.fenetre('gauche', nb)
        self.fenetre('mid', nb)
        self.fenetre('droite', nb)
    
    def fenetre(self,side, etage):
        if side == 'gauche':
            x = 15
        if side == 'mid':
            x = 55
        if side == 'droite':
            x = 95
        turtle.seth(0)
        turtle.penup()
        turtle.setx(self.coord[0] + x)
        turtle.sety(self.coord[1] + etage * 60)
        turtle.left(90)
        turtle.forward(20)
        turtle.pendown()
        turtle.color('black', 'light blue')
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(30)
            turtle.right(90)
        turtle.end_fill()

    def dessintoit(self, etage, styletoit):
        if styletoit == 'triangle':
            turtle.color('black', self.couleur)
            turtle.penup()
            turtle.setx(self.coord[0])
            turtle.sety(self.coord[1] + (etage+1) * 60)
            turtle.pendown()
            turtle.seth(0)
            turtle.begin_fill()
            turtle.seth(0)
            turtle.forward(140)         # base du toit
            turtle.left(150)
            turtle.forward(80)          # pente gauche du toit
            turtle.left(60)
            turtle.forward(80)          # pente droite du toit
            turtle.left(150)
            turtle.end_fill()

        if styletoit == 'plat':
            turtle.color('black', 'black')
            turtle.penup()
            turtle.setx(self.coord[0])
            turtle.sety(self.coord[1] + (etage+1) * 60)
            turtle.pendown()
            turtle.seth(0)
            turtle.begin_fill()
            turtle.seth(0)
            turtle.forward(140)
            turtle.left(90)
            turtle.forward(10)
            turtle.left(90)
            turtle.forward(140)
            turtle.left(90)
            turtle.forward(10)
            turtle.end_fill()



    
    def dessincasa(self):
        self.rdc()
        for i in range(self.nbetage):
            self.etage(i+1)
        self.dessintoit(self.nbetage, 'plat')
        turtle.done()
        
        
        
    
    


gg = Casa(0,0,3,'pink')
gg.dessincasa()
