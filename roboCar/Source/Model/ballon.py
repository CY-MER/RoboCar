import math

LARGEUR = 900 #dim ecran
HAUTEUR = 600

class Ballon:
    def __init__(self, position, angle=0):
        self.x, self.y = position
        self.rayon = 15

        self.vect_x = 0
        self.vect_y = 0

    def pousser(self, vit, angle):
        """ ajouter de la vitesse au ballon """
        self.vect_x += vit * math.cos(angle)
        self.vect_y += vit * math.sin(angle)

    def step(self):
        """ bouge le ballon selon son vecteur de vitesse """

        #si le robot touche un bord
        if self.x + self.rayon > LARGEUR or self.x - self.rayon < 0:
            self.vect_x = -self.vect_x
        if self.y + self.rayon > HAUTEUR or self.y - self.rayon < 0:
            self.vect_y = -self.vect_y

        self.x += self.vect_x
        self.y += self.vect_y