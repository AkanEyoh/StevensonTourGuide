## Author(s): Akaninyene Eyoh
## Date: 2018-11-06
## Email: akaninyene.e.eyoh@vanderbilt.edu
## Filename: locations.py
## Description: Implements node structure of Stevenson hallways, stairs, and elevators.

# defines a parent class for location
# this stores an adjacency list and provides a mechanism for accessing them
class Location:
    def __init__(self, adjList):
        self.adjList = adjList
        print(self.adjList)

    # adds the adjacency list to the locations
    def set_adj_list(self, adjList):
        self.adjList = adjList

    def get_adj_list(self):
        return self.adjList

# defines a hallway class that extends Location
# this stores an adjacency list, room list, and the length of the hallway
class Hallway(Location):
    def __init__(self, adjList, roomList, length):
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
class Elevator(Location):
    def __init__(self, adjList):
        super().__init__(adjList)

# this defines a staircase class
# the staircase does not have rooms attached to it
class Staircase(Location):
    def __init__(self, adjList):
        super().__init__(adjList)

adjList = ["element1", "element2", "element3"]
tester = Staircase(adjList)
print(tester.get_adj_list())

adjList = ["element1", "element2", "element3", "element4"]
tester2 = Elevator(adjList)
print(tester2.get_adj_list())

adjList = ["element1", "element2", "element3", "element4", "element5"]
roomList = ["room1", "room2", "room3"]
tester3 = Hallway(adjList, roomList, 5)
print(tester3.get_adj_list())
print(tester3.get_length())
print(tester3.get_room_list())

adjList = ["element1", "element2", "element3", "element4", "element5", "element6"]
roomList = ["room1", "room2", "room3", "room4"]

tester3.set_room_list(roomList)
tester3.set_length(4)
tester3.set_adj_list(adjList)
print(tester3.get_adj_list())
print(tester3.get_length())
print(tester3.get_room_list())