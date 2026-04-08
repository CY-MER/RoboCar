from Source import Simulation, Affichage, RoboCar
from Source import AdaptateurSimule
from Source import creer_strategie
import time

LARGEUR = 800
HAUTEUR = 600

def q1_1():
    sim = Simulation(LARGEUR, HAUTEUR)
    robot = RoboCar("Flash", (770, 570), 180, simulation=sim)
    view = Affichage(LARGEUR, HAUTEUR)
    running = True
    while running:
        running = view.update(robot, sim.obstacles)
        time.sleep(0.01)
    view.stop()

if __name__ == "__main__":
    q1_1()