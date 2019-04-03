## Author(s): Akaninyene Eyoh, Ulysses Yu, Daniel Yan, Keaton Ufheil
## Date: 2018-11-06
## Email: akaninyene.e.eyoh@vanderbilt.edu, ulysses.l.yu@vanderbilt.edu,
# daniel.yan@vanderbilt.edu
## Filename: locations.py
## Description: Implements node structure of Stevenson hallways, stairs,
# and elevators.

import re

# Constants
DEFAULT_STAIRCASE_LENGTH = 1
# By default, set elevators to length 10 to prefer stairs.
DEFAULT_ELEVATOR_LENGTH = 10
DEFAULT_HALLWAY_LENGTH = 5
DEFAULT_ID = ""
NUMBER_TO_BUILDING = {
    '1': 'math',
    '2': 'molecbio'
}


# defines a parent class for location
# this stores an adjacency list and provides a mechanism for accessing them
class Location:
    def __init__(self, adjList=[], id_name=DEFAULT_ID):
        self.adjList = adjList
        self.id_name = id_name
        self.url_base = re.search('[0-9-]+$', self.id_name).group(0)

    # adds the adjacency list to the locations
    def set_adj_list(self, adjList):
        self.adjList = adjList

    def get_adj_list(self):
        return self.adjList

    def to_string(self):
        return self.id_name


# defines a hallway class that extends Location
# this stores an adjacency list, room list, and the length of the hallway
class Hallway(Location):
    def __init__(self, adjList=[], roomList=[], topviewAboveList=[], topviewBelowList=[], topviewLeftList=[], topviewRightList=[], topviewOrderList=[], length=DEFAULT_HALLWAY_LENGTH, id_name=DEFAULT_ID, url_base=''):
        super().__init__(adjList=adjList, id_name=id_name)
        self.length = length
        self.roomList = roomList
        self.topviewAboveList = topviewAboveList
        self.topviewBelowList = topviewBelowList
        self.topviewLeftList = topviewLeftList
        self.topviewRightList= topviewRightList
        self.topviewOrderList = topviewOrderList
        # to be set when traversed for directions
        self.directionTraversed = None

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

    def get_url(self, direction):
        view = 'v1' if direction else 'v2'
        return NUMBER_TO_BUILDING[self.url_base[0]] + '_' + 'hallway_' + self.url_base[2:] + view + '.jpg'


# this defines an elevator class
# the elevator does not have rooms attached to it
# default length set to 1.1 so that stairs are preferred
class Elevator(Location):
    length = DEFAULT_ELEVATOR_LENGTH
    def __init__(self, adjList=[], id_name=DEFAULT_ID, url_base=''):
        super().__init__(adjList=adjList, id_name=id_name)

    def get_floor(self):
        return self.floor

    def get_url(self):
        return NUMBER_TO_BUILDING[self.url_base[0]] + '_' + 'elevator_' + self.url_base[2:] + '.jpg'


# this defines a staircase class
# the staircase does not have rooms attached to it
# default length set to 1
class Staircase(Location):
    length = DEFAULT_STAIRCASE_LENGTH
    def __init__(self, adjList=[], id_name=DEFAULT_ID, url_base=''):
        super().__init__(adjList=adjList, id_name=id_name)

    def get_floor(self):
        return self.floor

    def get_url(self):
        return NUMBER_TO_BUILDING[self.url_base[0]] + '_' + 'staircase_' + self.url_base[2:] + '.jpg'
