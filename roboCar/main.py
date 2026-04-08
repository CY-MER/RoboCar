from Source import Simulation, Affichage, RoboCar
from Source import AdaptateurSimule
from Source import creer_strategie, Faire_Hexagone
import time
import random

LARGEUR = 900
HAUTEUR = 600


def main():
    sim = Simulation(LARGEUR, HAUTEUR) #creation du monde
    robot = RoboCar("Flash", (770, 570), 180, simulation=sim) #creation du robot
    adp = AdaptateurSimule(robot) #adaptateur de pilotage
    view = Affichage(LARGEUR, HAUTEUR) #affichage

    strat = Faire_Hexagone(adp) #comportement hexagonal
    strat.start()

    robot.dessine(True)

    running = True
    while running:
        if strat.step(): #execution d'un pas de strategie (check si on passe a la suivante)
            robot.change_couleur((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        #mise a jour physique du robot
        if not robot.step():
            adp.arreter()

        #affichage
        running = view.update(robot, sim.obstacles)

        time.sleep(0.01)

    view.stop()

if __name__ == "__main__":
    main()