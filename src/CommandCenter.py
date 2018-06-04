class CommandCenter():
    hatch_open = False
    shells_count = 0
    target_locked = False
    cannon_angles = []
    cannon_tilts = []

    def __init__(self, shell_count, cannon_count):
        self.shells_count = shell_count
        for x in range(0, cannon_count):
            self.cannon_angles.append(0)
            self.cannon_tilts.append(10)

    def fire_canon(self, cannon_nb, angle, distance):
        if (not self.hatch_open and self.shells_count >= 1):
            if (self.target_locked):
                self.turn_cannon(cannon_nb, angle)
                tilt_angle = self.calculate_angle(cannon_nb, distance)
                self.tilt_cannon(cannon_nb, tilt_angle)
                self.fire_shell(cannon_nb)
                return 0
            else:
                return 1
        else:
            return 2


    def turn_cannon(self, cannon_nb, angle):
        print("turning cannon " + str(cannon_nb) + " from " +
              str(self.cannon_angles[cannon_nb]) + "° to " + str(angle) + "°")
        self.cannon_angles[cannon_nb] = angle


    def tilt_cannon(self, cannon_nb, angle):
        print("tilting cannon " + str(cannon_nb) + " from " +
              str(self.cannon_tilts[cannon_nb]) + "° to " + str(angle) + "°")
        self.cannon_tilts[cannon_nb] = angle


    # Average cannon ball speed: 438m/s
    def calculate_angle(self, cannon_nb, distance):
        return distance / 10


    def fire_shell(self, cannon_nb):
        self.shells_count += -1
        print("cannon " + str(cannon_nb) + " does 'Phew'!")
        print("there are now " + str(self.shells_count) + " shells left")

    def lock_target(self):
        print("Locking on Target")
        self.target_locked = True

    def unlock_target(self):
        print("Target unlocked")
        self.target_locked = False