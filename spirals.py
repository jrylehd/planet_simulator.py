'''
This module imports the classes Earth and Moon and uses their attributes to make an animation in a GUI using tkinter.
It should create a spiral of the moon that rotates around the earth as the earth rotates around the sun.
'''

from tkinter import Tk, Button, Canvas, Scale
from tkinter import W, E, N, S, ALL
import math
from earth import Earth
from moon import Moon

'''
This creates the Spirals class which can be used to command the GUI how to behave.
'''
class Spirals:
    
    def __init__(self): # initializes all the back end and front end of the visualization when the GUI is prompted to open
        self.window = Tk()
        self.window.title('spirals')
        self.canvas = Canvas(self.window, width=400, height=400, bg='white')
        self.togo = False
        
        # set the use and orientation of the scales and look
        self.refresh_rate_scale = Scale(self.window, from_=0, to=100, resolution=1, tickinterval=20, orient='horizontal', length=400)
        self.eccentricity_scale = Scale(self.window, from_=0.50, to=1.00, resolution=0.05, tickinterval=0.05, orient='vertical', length=400)
        self.R_scale = Scale(self.window, from_=1.0, to=3.0, resolution=0.01, tickinterval=0.2, orient='vertical', length=400)

        # set the use of the button and the text within and overall formats what the button looks like and what it does
        self.start_button = Button(self.window, text='start', command=self.start_animation)
        self.stop_button = Button(self.window, text='stop', command=self.stop_animation)

        # set the location of the canvas in the GUI
        self.canvas.grid(row=1, column=1, columnspan=2)
    
        # set the location of the scales in the GUI
        self.refresh_rate_scale.grid(row=0, column=1, columnspan=2)
        self.eccentricity_scale.grid(row=1, column=0)
        self.R_scale.grid(row=1, column=3)
   
        # set the location of the buttons in the GUI
        self.start_button.grid(row=2, column=1, sticky=E+W)
        self.stop_button.grid(row=2, column=2, sticky=E+W)
   
        # show the initialization setting on the scales for when the GUI is opened up
        self.refresh_rate_scale.set(60)
        self.eccentricity_scale.set(0.85)
        self.R_scale.set(2.0)

        # set the primary coordinates of the sun, earth, and moon relative to the each other respectively
        r = 10
        e = self.eccentricity_scale.get()
        R = self.R_scale.get()
        self.earth = Earth(r, e)
        self.moon = Moon(r, e, R)
        (X, Y) = self.earth.coordinates(0)
        (x, y) = self.moon.coordinates(0)

        sun_radius = 12
        sun_center = 400 / 2
        self.canvas.create_oval(sun_center - sun_radius, sun_center - sun_radius,
                                sun_center + sun_radius, sun_center + sun_radius,
                                fill = 'yellow', outline = '')

        planet_radius = 6
        planet_center_x = sun_center + (X + 15) * 400 / 40
        planet_center_y = sun_center - (Y + 20) * 400 / 40
        self.canvas.create_oval(planet_center_x - planet_radius, planet_center_y - planet_radius,
                                planet_center_x + planet_radius, planet_center_y + planet_radius,
                                fill = 'blue', outline = '')

        satellite_radius = 3
        satellite_center_x = planet_center_x + (x + 15) * 400 / 40
        satellite_center_y = planet_center_y - (y + 20) * 400 / 40
        self.canvas.create_oval(satellite_center_x - satellite_radius, satellite_center_y - satellite_radius,
                                satellite_center_x + satellite_radius, satellite_center_y + satellite_radius,
                                fill = 'red', outline = '')
        
        self.window.mainloop()

    '''This is the program to animate the continuous plotting of coordinates to represent the location of the moon relative to where the 
    earth should be when it rotates around the sun per day.'''
    def animate(self):
        r = 10
        e = self.eccentricity_scale.get()
        R = self.R_scale.get()
        
        day = 0
        while day < 365:
            X, Y = self.earth.coordinates(day)
            x, y = self.moon.coordinates(day)
            
            sun_radius = 12
            sun_center = 400 / 2
            self.canvas.create_oval(sun_center - sun_radius, sun_center - sun_radius,
                                    sun_center + sun_radius, sun_center + sun_radius,
                                    fill = 'yellow', outline = '')

            planet_center_x = sun_center + (X + 15) * 400 / 30
            planet_center_y = sun_center - (Y + 20) * 400 / 40

            satellite_radius = 3
            satellite_center_x = planet_center_x (x + 15) * 400 / 30
            satellite_center_y = planet_center_y - (y + 20) * 400 / 40
            self.canvas.create_oval(satellite_center_x - satellite_radius, satellite_center_y - satellite_radius,
                                    satellite_center_x + satellite_radius, satellite_center_y + satellite_radius,
                                    fill = 'red', outline = '')

            day += 1
            self.window.update()
            refresh_rate = int(self.refresh_rate_scale.get())
            self.window.after(refresh_rate)
    
    '''This tells the GUI to start the animation when the button "start" is pressed.'''
    def start_animation(self):
        self.togo = True
        self.animate()

    '''This stops the animation within the GUI.'''
    def stop_animation(self):
        self.togo = False

if __name__ == "__main__":
    gui = Spirals()