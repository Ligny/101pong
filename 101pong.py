#!/usr/bin/python3
#
# Simple program to calculate vectors
# made in python 3, you can launch it with:
# ./101pong x0 y0 z0 x1 y1 z1 time
# (See subject for more details)

import sys
import math

class PongCalculator:
    def __init__(self, args):
        self.validate_input(args)
        self.x0, self.y0, self.z0, self.x1, self.y1, self.z1, self.n = map(float, args[1:])
        self.calculate_coordinates()

    def validate_input(self, args):
        if len(args) != 8:
            exit(84)

        if float(args[7]) < 0:
            exit(84)

        for arg in args[1:]:
            if not arg.replace('.', '', 1).isdigit():
                exit(84)

    def calculate_coordinates(self):
        x = self.x1 - self.x0
        y = self.y1 - self.y0
        z = self.z1 - self.z0

        coord_x = self.x1 + (x * self.n)
        coord_y = self.y1 + (y * self.n)
        coord_z = self.z1 + (z * self.n)

        power = y**2 + x**2 + z**2
        if power == 0:
            norm = 0
        else:
            norm = math.sqrt(power)
            radian = math.asin(math.sqrt(z**2) / norm)
            angle = math.degrees(radian)

        self.print_results(x, y, z, coord_x, coord_y, coord_z, angle)

    def print_results(self, x, y, z, coord_x, coord_y, coord_z, angle):
        print("The speed vector coordinates are:")
        print(f'({x:.2f}; {y:.2f}; {z:.2f})')
        print(f"At time t+{int(self.n)}, ball coordinates will be:")
        print(f'({coord_x:.2f}; {coord_y:.2f}; {coord_z:.2f})')

        if (self.z1 >= 0 and self.z1 < 0) or (self.z1 <= 0 and self.z1 > 0):
            print("The incidence angle is:")
            print(f"{angle:.2f} degrees")
        else:
            print("The ball won't reach the bat.")


if __name__ == "__main__":
    PongCalculator(sys.argv)
