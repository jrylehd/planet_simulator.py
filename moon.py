'''
This module creates the class Moon and runs a program that finds the x and y coordinates
of moon based off of the earth at any given day in a year.
'''

from math import sin, cos, pi
from earth import Earth

'''
Creates a class Moon for an object.
'''
class Moon: 
    
    def __init__(self, r, e, R): # given attributes for earth and moon
        self.earthdistance = r
        self.eartheccentricity = e
        self.distance = R
        self.earth = Earth(self.earthdistance, self.eartheccentricity)
        
    def coordinates(self, d):
        (X, Y) = self.earth.coordinates(d)
        D = 365/12
        beta = (d * 2 * pi) / D
        (x, y) = (X+(self.distance*cos(beta)), Y+(self.distance*sin(beta))) # location of moon relative to earth on a 2D coordinate grid
        return (x, y)
    
'''
The main program that runs all the coordinates of the moon relative to the earth per day in a year.
'''
def main():
    r = 10
    e = 0.85
    R = 3
    earth = Earth(r, e)
    moon = Moon(r, e, R)
    
    for d in range(0, 366):
        (X, Y) = earth.coordinates(d)
        (x, y) = moon.coordinates(d)
        print('At day', str(d) + ',', 'earth is at (', X, ',', Y, ') and\n', \
              '\t   moon is at (', x, ',', y, ').')

if __name__ == '__main__':
    main()