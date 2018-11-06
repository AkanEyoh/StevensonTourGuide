## Author(s): Akaninyene Eyoh, Daniel Yan
## Date: 2018-11-06
## Email: akaninyene.e.eyoh@vanderbilt.edu, daniel.yan@vanderbilt.edu
## Filename: locations_test.py
## Description: Tests for node structure of Stevenson hallways, stairs,
# and elevators from src/locations.py

## Import Libraries
from src import locations
import pytest

# Test for initialization of staircase class.
def test_staircase_init_1():
    adj_list = ["element1", "element2", "element3"]
    tester = locations.Staircase(adj_list)
    assert tester.get_adj_list() == adj_list

# Test for initialization of elevator class.
def test_elevator_init_1():
    adj_list = ["element1", "element2", "element3", "element4"]
    tester2 = locations.Elevator(adj_list)
    assert tester2.get_adj_list() == adj_list

# Test for initialization of hallway class and adj_list.
def test_hallway_init_1():
    adj_list = ["element1", "element2", "element3", "element4", "element5"]
    room_list = ["room1", "room2", "room3"]
    tester3 = locations.Hallway(adj_list, room_list, 5)
    assert tester3.get_adj_list() == adj_list

# Test for initialization of hallway class and length
def test_hallway_init_2():
    adj_list = ["element1", "element2", "element3", "element4", "element5"]
    room_list = ["room1", "room2", "room3"]
    tester3 = locations.Hallway(adj_list, room_list, 5)
    assert tester3.get_length() == 5

# Tests for initialization of hallway class and room_list
def test_hallway_init_2():
    adj_list = ["element1", "element2", "element3", "element4", "element5"]
    room_list = ["room1", "room2", "room3"]
    tester3 = locations.Hallway(adj_list, room_list, 5)
    assert tester3.get_room_list() == room_list

# Test for set_adj_list
def test_hallway_init_2():
    adj_list = ["element1", "element2", "element3", "element4", "element5"]
    room_list = ["room1", "room2", "room3"]
    adj_list_new = ["element1", "element2", "element3", "element4", "element5",
               "element6"]
    room_list_new = ["room1", "room2", "room3", "room4"]
    tester3 = locations.Hallway(adj_list, room_list, 5)
    tester3.set_room_list(room_list_new)
    tester3.set_length(4)
    tester3.set_adj_list(adj_list_new)
    assert tester3.get_adj_list() == adj_list_new

# Test for set_length
def test_hallway_init_2():
    adj_list = ["element1", "element2", "element3", "element4", "element5"]
    room_list = ["room1", "room2", "room3"]
    adj_list_new = ["element1", "element2", "element3", "element4", "element5",
               "element6"]
    room_list_new = ["room1", "room2", "room3", "room4"]
    tester3 = locations.Hallway(adj_list, room_list, 5)
    tester3.set_room_list(room_list_new)
    tester3.set_length(4)
    tester3.set_adj_list(adj_list_new)
    assert tester3.get_length() == 4

# Test for set_room_list
def test_hallway_init_2():
    adj_list = ["element1", "element2", "element3", "element4", "element5"]
    room_list = ["room1", "room2", "room3"]
    adj_list_new = ["element1", "element2", "element3", "element4", "element5",
               "element6"]
    room_list_new = ["room1", "room2", "room3", "room4"]
    tester3 = locations.Hallway(adj_list, room_list, 5)
    tester3.set_room_list(room_list_new)
    tester3.set_length(4)
    tester3.set_adj_list(adj_list_new)
    assert tester3.get_room_list() == room_list_new