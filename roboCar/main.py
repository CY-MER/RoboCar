from Source import Simulation, Affichage, RoboCar
from Source import AdaptateurSimule
from Source import creer_strategie, Faire_Hexagone, Faire_Carre, Allez_retour
import time
import random

LARGEUR = 900
HAUTEUR = 600


def main():
    sim = Simulation(LARGEUR, HAUTEUR) #creation du monde
    robot1 = RoboCar("Flash1", (40, 270), 0, simulation=sim) #creation du robot
    robot2 = RoboCar("Flash2", (860, 270), 90, simulation=sim) #creation du robot
    adp1 = AdaptateurSimule(robot1) #adaptateur de pilotage
    adp2 = AdaptateurSimule(robot2)
    view = Affichage(LARGEUR, HAUTEUR) #affichage

    strat1 = Faire_Carre(adp1)
    strat1.start()
    strat2 = Allez_retour(adp2)
    strat2.start()

    running = True
    while running:
        if strat1.step(): #execution d'un pas de strategie (check si on passe a la suivante)
            robot1.change_couleur((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        #mise a jour physique du robot
        if not robot1.step():
            adp1.arreter()

        if strat2.step():
            robot2.change_couleur((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        if not robot2.step():
            adp2.arreter()

        #affichage
        running = view.update([robot1, robot2], sim.obstacles)

        time.sleep(0.01)

    view.stop()

if __name__ == "__main__":
    main()