﻿# circle.py by tfbanks
# !/usr/bin/env python3

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2
  
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter/2

    @property
    def area(self):
        return pi * self.radius**2

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)
 
    def __str__(self):
        return 'Circle with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __gt__(self, other):
        return Circle(self.radius > other.radius)

    def __ge__(self, other):
        return Circle(self.radius >= other.radius)

    def __lt__(self, other):
        return Circle(self.radius < other.radius)

    def __le__(self, other):
        return Circle(self.radius <= other.radius)

    def __eq__(self, other):
        return Circle(self.radius == other.radius)
    
    def __ne__(self, other):
        return Circle(self.radius != other.radius)

    def sort_key(self):
        return self.radius
