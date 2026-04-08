from Source import Simulation, Affichage, RoboCar, Ballon
from Source import AdaptateurSimule
from Source import creer_strategie, Faire_Hexagone, Faire_Carre, Allez_retour
import time
import random

LARGEUR = 900
HAUTEUR = 600


def main():
    sim = Simulation(LARGEUR, HAUTEUR) #creation du monde

    robot1 = RoboCar("Flash1", (40, 270), 0, simulation=sim) #creation du robot
    robot2 = RoboCar("Flash2", (860, 270), 180, simulation=sim) #creation du robot
    adp1 = AdaptateurSimule(robot1) #adaptateur de pilotage
    adp2 = AdaptateurSimule(robot2)

    ballon = Ballon((450, 290))
    ballon.pousser(5, 0) #vitesse initiale du ballon

    view = Affichage(LARGEUR, HAUTEUR) #affichage

    strat1 = creer_strategie(adp1)
    strat2 = creer_strategie(adp2)

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
        ballon.step() #physique du ballon
        ballon.robot_pousse(robot1)
        ballon.robot_pousse(robot2)

        #affichage
        running = view.update([robot1, robot2], sim.obstacles, ballon)

        time.sleep(0.01)

    view.stop()

if __name__ == "__main__":
    main()