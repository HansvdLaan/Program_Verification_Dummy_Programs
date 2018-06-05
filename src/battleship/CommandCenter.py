class CommandCenter():
    hatch_open = False
    shells_count = 0
    target_locked = False
    cannon_angle = 0
    cannon_tilt = 0

    def __init__(self, shell_count):
        self.shells_count = shell_count

    def fire_canon(self, angle, distance):
        if (not self.hatch_open and self.shells_count >= 1):
            if (self.target_locked):
                self.turn_cannon(angle)
                tilt_angle = self.calculate_angle(distance)
                self.tilt_cannon(tilt_angle)
                self.fire_shell()
                return 0
            else:
                return 1
        else:
            return 2

    def turn_cannon(self, angle):
        print("turning cannon from " +
              str(self.cannon_angle) + "° to " + str(angle) + "°")
        self.cannon_angle = angle


    def tilt_cannon(self, tilt):
        print("tilting cannon from " +
              str(self.cannon_tilt) + "° to " + str(tilt) + "°")
        self.cannon_angle = tilt

    def calculate_angle(self, distance):
        return distance / 10


    def fire_shell(self):
        self.shells_count += -1
        print("the cannon does 'Phew'!")
        print("there are now " + str(self.shells_count) + " shells left")

    def lock_target(self):
        print("Locking on Target")
        self.target_locked = True

    def unlock_target(self):
        print("Target unlocked")
        self.target_locked = False