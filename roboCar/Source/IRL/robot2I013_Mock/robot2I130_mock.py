import math

class Robot2INO13Mock:
    """Classe de la simulation du robot réel pour les testes de syntaxe
    """
    
    WHEEL_BASE_WIDTH         = 117  # distance (mm) de la roue gauche a la roue droite.
    WHEEL_DIAMETER           = 66.5 #  diametre de la roue (mm)
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
    WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi # perimetre de la roue (mm)
    
    def __init__(self):
        self.MOTOR_LEFT = 0
        self.MOTOR_RIGHT = 0
        
    def stop(self):
        """Arreter le robot"""
        self.set_motor_dps(0)
        
    def set_motor_dps(self, dps):
        """Fixe la vitesse des moteur en nombre de degres par seconde"""
        self.MOTOR_LEFT = dps
        self.MOTOR_RIGHT = dps
        
    def get_motor_position(self):
        """Lit les etats des moteurs en degre."""
        return self.MOTOR_LEFT, self.MOTOR_RIGHT
        
        