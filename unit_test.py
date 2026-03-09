import unittest
import math

from robocar import RoboCar
from simulation import Simulation
from strategies import Deplacement


class TestRoboCar(unittest.TestCase):

    def setUp(self):
        self.robot = RoboCar("Flash", (100, 200), 0)

    def test_initialisation(self):
        self.assertEqual(self.robot.x, 100)
        self.assertEqual(self.robot.y, 200)
        self.assertEqual(self.robot.vG, 0)
        self.assertEqual(self.robot.vR, 0)

    def test_calculer_vitesse(self):
        self.robot.set_vitesse_gauche(50)
        self.robot.set_vitesse_droite(50)
        v, w = self.robot.calculer_vitesse()
        self.assertEqual(v, 50)
        self.assertEqual(w, 0)

    def test_update(self):
        self.robot.set_vitesse_gauche(10)
        self.robot.set_vitesse_droite(10)
        self.robot.update(1)
        self.assertAlmostEqual(self.robot.x, 110)
class TestSimulation(unittest.TestCase):

    def setUp(self):
        self.sim = Simulation(800, 600)

    def test_avancer(self):
        self.sim.avancer(80)
        self.assertEqual(self.sim.robot.vG, 80)
        self.assertEqual(self.sim.robot.vR, 80)

    def test_arreter(self):
        self.sim.avancer(80)
        self.sim.arreter()
        self.assertEqual(self.sim.robot.vG, 0)
        self.assertEqual(self.sim.robot.vR, 0)
class TestStrategie(unittest.TestCase):

    def setUp(self):
        self.sim = Simulation(800, 600)
        self.strat = Deplacement(self.sim, self.sim.robot)

    def test_avancer_x_metres(self):
        fini = self.strat.avancer_x_metres(1, 80)
        self.assertFalse(fini)



if __name__ == "__main__":
    unittest.main()