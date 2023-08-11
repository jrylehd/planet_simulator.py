'''
This module creates the class Earth and runs a program that finds the x and y coordinates
of earth at any given day in a year.
'''

from math import cos, sin, pi

'''
Creates a class Earth for an object.
'''
class Earth:
    
    def __init__(self, r, e): # given attributes of earth
        self.distance = r
        self.eccentricity = e

    def coordinates(self, d):
        alpha = (d * 2 * pi) / 365
        (x, y) = (self.distance*cos(alpha), self.distance*sin(alpha)*self.eccentricity) # location of earth on 2D grid
        return (x, y)

'''
This is the main program that runs the coordinates of the earth for every day of the year.
'''
def main():
    r = 10
    e = 0.85
    earth = Earth(r, e)
    
    for d in range(0, 366):
        (x, y) = earth.coordinates(d)
        print(f'( {x} , {y} ) at day {d}')

if __name__ == '__main__':
    main()