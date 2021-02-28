#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 22:33:18 2021

@author: jonas
"""

"""
    This script contains two classes to show object definition and inheritance.
"""

class Bike:
    """
    This class simulates behaviour of a bike.
    
    Methods
    -------
    __init__(self, driver, max_gear)
    increaseGears(self)
    decreaseGears(self)
    whosDriving(self)
    """
    
    # Minimal number of gears
    min_gear = 1
    
    def __init__(self, driver: str, max_gear: int):
        """
        Constructor

        Parameters
        ----------
        driver : str
            Name of the dude riding the bike.
        max_gear : int
            maximal numbers of gears.

        Returns
        -------
        Instance of Bike.

        """
        # Set the parameters as attributes
        self.driver = driver
        self.max_gear = int(max_gear)
        # Check if the parameter max_gear makes sense
        if self.max_gear < self.min_gear: self.max_gear = self.min_gear + 1
        # Set the starting value for gear attribute
        self.gear = int( (self.max_gear + self.min_gear) / 2 )
        
    def increaseGears(self):
        """
        Increase the gears by one.

        Returns
        -------
        None.

        """
        self.gear += 1
        if self.gear > self.max_gear: self.gear = self.max_gear
        print(f"Change gears to {self.gear}.")
        
    def decreaseGears(self):
        """
        Decrease the gears by one.

        Returns
        -------
        None.

        """
        self.gear -= 1
        if self.gear < self.min_gear: self.gear = self.min_gear
        print(f"Change gears to {self.gear}.")
        
    def whosDriving(self):
        """
        Print the name of the driver.

        Returns
        -------
        None.

        """
        print(f"{self.driver} is riding the bike.")
        
class Tandem(Bike):
    """
    This class inherites from Bike. Simulates a tandem bike.
    
    Methods
    -------
    __init__(self, driver, codriver, max_gear)
    setGear(self, new_gear)
    whosDriving(self)    
    """
    
    def __init__(self, driver: str, codriver: str, max_gear: int):
        """
        Constructor

        Parameters
        ----------
        driver : str
            Dude whos riding the tandem.
        codriver : str
            Other dude whos riding the tandem.
        max_gear : int
            Maximal number of gears.

        Returns
        -------
        Instance of Tandem.

        """
        # Call the constructor of the base class
        Bike.__init__(self, driver, max_gear)
        # Set parameter as attribute
        self.codriver = codriver
        
    def setGear(self, new_gear: int):
        """
        Change the gears to specific gear.

        Parameters
        ----------
        new_gear : int
            New gears to change to.

        Returns
        -------
        None.

        """
        if new_gear >= self.min_gear and new_gear <= self.max_gear: 
            self.gear = new_gear
            print(f"Change gears to {self.gear}.")
        else: 
            print("Can't change gears.")
        
    def whosDriving(self):
        """
        Print the name of the driver and codriver.

        Returns
        -------
        None.

        """
        print(f"{self.driver} and {self.codriver} are riding the tandem.")