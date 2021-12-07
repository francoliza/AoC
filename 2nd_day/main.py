#!/usr/bin/python3

class Coordinates:
    def __init__(self):
        self.x = 0
        self.y = 0

    def forward(self, distance):
        distance = int(distance)
        self.x += distance

    def up(self, distance):
        distance = int(distance)
        self.y -= distance

    def down(self, distance):
        distance = int(distance)
        self.y += distance

    def current_x(self):
        return self.x

    def current_y(self):
        return self.y


def day_2_part_1():
    file1 = open('input_1.txt', 'r')
    lines = file1.readlines()

    coord = Coordinates()

    for line in lines:
        move, value = line.split()

        if move == 'forward':
            coord.forward(value)

        if move == 'up':
            coord.up(value)

        if move == 'down':
            coord.down(value)

    return coord.current_x() * coord.current_y()

def main():
    #coord = Coordinates()
    #print("initial values: X = {0:d}, Y = {1:d}".format(coord.current_x(), coord.current_y()))
    #print("up 2")
    #coord.up(2);
    #print("up(2): X = {0:d}, Y = {1:d}".format(coord.current_x(), coord.current_y()))

    result = day_2_part_1()
    print("result: ", result)

if __name__ == '__main__':
    main()

