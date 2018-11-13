## Author(s): Daniel Yan
## Date: 2018-11-08
## Email: daniel.yan@vanderbilt.edu
## Filename: bfs_test.py
## Description: Tests for src/bfs_test.py which contains the breadth first
## search logic for the hallways.

## Import libraries
from src import bfs
from src import data_loader as dl
from src import locations
import pytest

# Test that bfs works for trivial case where start and end location are
# are the same
def test_bfs_1():
    assert bfs.bfs(start=dl.hallway2_2, end=dl.hallway2_2) == [dl.hallway2_2]

# Test that bfs returns false if it is not possible to arrive at end location.
def test_bfs_2():
    loc1 = locations.Hallway()
    assert bfs.bfs(start=dl.hallway1_1, end=loc1) == False

# Test that bfs returns false if the start location does not have anything
# in the adj_list
def test_bfs_3():
    loc1 = locations.Hallway()
    assert bfs.bfs(start=loc1, end=dl.hallway1_1) == False

# Test cases for bfs where there is a valid route
# def test_bfs_4():
#     assert bfs.bfs(start=dl.staircase1_1, end=dl.staircase2_2) == [
#         dl.staircase1_1, dl.staircase2_1, dl.staircase2_2]