## Author(s): Daniel Yan
## Date: 2018-11-08
## Email: daniel.yan@vanderbilt.edu
## Filename: data_loader_test.py
## Description: Tests for src/data_loader.py which loads in data
## from the Vanderbilt Stevenson Math building.

# Import libraries
from src import data_loader as dl
from src import locations
import pytest


##########################
## Tests for staircases ##
##########################

# Test that adj_list for staircase is correct
def test_staircase_1():
    assert dl.staircase5_2.get_adj_list() == [dl.hallway5_2, dl.staircase4_2]


# Test that a staircase is an instance of a Staircase object
def test_staircase_2():
    assert isinstance(dl.staircase5_2, locations.Staircase)


# Test that a staircase is an instance of a Location object
def test_staircase_3():
    assert isinstance(dl.staircase5_2, locations.Location)


# Test that a getting a hallway from the adj_list of a staircase works
# correctly.
def test_staircase_4():
    hallway5_2 = dl.staircase5_2.get_adj_list()[0]
    assert hallway5_2.get_adj_list() == [dl.staircase5_2, dl.elevator5,
                                         dl.hallway5_1]


def test_staircase_5():
    hallway5_2 = dl.staircase5_2.get_adj_list()[0]
    assert hallway5_2.get_length() == 15


def test_staircase_6():
    hallway5_2 = dl.staircase5_2.get_adj_list()[0]
    assert hallway5_2.get_room_list() == ["1502", "1503", "1504", "1505",
                                          "1507", "1510", "1511", "1512",
                                          "1513", "1514", "1515", "1516",
                                          "1518", "1520", "1522"]


# Test that we can chain a second step from the hallway adjacent to a staircase
# to another elevator.
def test_staircase_7():
    hallway5_2 = dl.staircase5_2.get_adj_list()[0]
    elevator5 = hallway5_2.get_adj_list()[1]
    assert elevator5.get_adj_list() == [dl.hallway5_1, dl.hallway5_2,
                                        dl.elevator1, dl.elevator2,
                                        dl.elevator3, dl.elevator4]

#########################
## Tests for elevators ##
#########################

# Check that elevator is an instance of an Elevator object.
def test_elevator_1():
    assert isinstance(dl.elevator1, locations.Elevator)

# Check that elevator is an instance of a Location object.
def test_elevator_2():
    assert isinstance(dl.elevator1, locations.Location)


########################
## Tests for hallways ##
########################

# Check that hallway is an instance of a Hallway object.
def test_hallway_1():
    assert isinstance(dl.hallway2_2, locations.Hallway)

# Check that hallway is an instance of a Location object.
def test_hallway_2():
    assert isinstance(dl.hallway2_2, locations.Location)