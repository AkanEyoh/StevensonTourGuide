## Author(s): Akaninyene Eyoh, Ulysses Yu, Daniel Yan
## Date: 2018-11-06
## Email: akaninyene.e.eyoh@vanderbilt.edu, ulysses.l.yu@vanderbilt.edu, daniel.yan@vanderbilt.edu
## Filename: locations.py
## Description: Implements node structure of Stevenson hallways, stairs, and elevators.

# defines a parent class for location
# this stores an adjacency list and provides a mechanism for accessing them
class Location:
    def __init__(self, adjList=[], id="", length = 1):
        self.adjList = adjList
        self.id = id
        self.length = length

    # adds the adjacency list to the locations
    def set_adj_list(self, adjList):
        self.adjList = adjList

    def get_adj_list(self):
        return self.adjList

    def to_string(self):
        return self.id

# defines a hallway class that extends Location
# this stores an adjacency list, room list, and the length of the hallway
class Hallway(Location):
    def __init__(self, adjList=[], roomList=[], length=0):
        super().__init__(adjList)
        self.roomList = roomList
        self.length = length

    # functions that operate on the rooms of a hallway
    def get_room_list(self):
        return self.roomList
    
    def set_room_list(self, room_list):
        self.roomList = room_list

    # functions that operate on the length of the hallway
    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

# this defines an elevator class
# the elevator does not have rooms attached to it
# default length set to 1.1 so that stairs are preferred
class Elevator(Location):
    def __init__(self, adjList=[], length=1.1):
        super().__init__(adjList=adjList, length=length)

# this defines a staircase class
# the staircase does not have rooms attached to it
# default length set to 1
class Staircase(Location):
    def __init__(self, adjList=[], length=1):
        super().__init__(adjList=adjList, length=length)