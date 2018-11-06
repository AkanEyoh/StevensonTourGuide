## Author(s): Akaninyene Eyoh
## Date: 2018-11-06
## Email: akaninyene.e.eyoh@vanderbilt.edu
## Filename: locations.py
## Description: Implements node structure of Stevenson hallways, stairs, and elevators.

class Location:
    def __init__(self, adjList):
        self.adjList = adjList

class Hallway(Location):
    def __init__(self, adjList, length):
        super().__init__(self, adjList)
        self.length = length

class Elevator(Location):
    def __init__(self, adjList):
        super().__init__(self, adjList)

class Staircase(Location):
    def __init__(self, adjList):
        super().__init__(self, adjList)
