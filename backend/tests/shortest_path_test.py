# ## Author(s): Daniel Yan
# ## Date: 2018-11-11
# ## Email: daniel.yan@vanderbilt.edu
# ## Filename: shortest_path_test.py
# ## Description: Tests for src/shortest_path.py which implements Dijkstra's
# # shortest path to find shortest paths from each location to other locations.
#
# ## Libraries to import
# from src import data_loader as dl
# from src import shortest_path as sp
# import pytest
# import queue # For testing with priority queue
#
# # Tests for creating the priority queue
# # Test that queue includes all locations
# def test_priority_queue_1():
#     queue = sp.create_priority_queue(dl.stevenson_math, dl.staircase3_2)
#     assert queue.qsize == 25
#
# # Test that the initial node is given priority of 0 initially.
# def test_priority_queue_2():
#     queue = sp.create_priority_queue(dl.stevenson_math, dl.staircase3_2)
#     assert queue.qsize == 25

