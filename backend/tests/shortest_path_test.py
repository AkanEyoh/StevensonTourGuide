## Author(s): Daniel Yan
## Date: 2018-11-11
## Email: daniel.yan@vanderbilt.edu
## Filename: shortest_path_test.py
## Description: Tests for src/shortest_path.py which implements Dijkstra's
# shortest path to find shortest paths from each location to other locations.

## Libraries to import
from src import data_loader as dl
from src import shortest_path as sp
import pytest
import queue # For testing with priority queue
