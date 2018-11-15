## Author(s): Daniel Yan
## Date: 2018-11-11
## Email: daniel.yan@vanderbilt.edu

## Description: Implements Dijkstra's shortest path to find the shortest path
## from each location to any other location.

## Import statements
import queue  # Priority queue
import heapq
from src import data_loader as dl
from src import locations as loc

## Constants
INFINITY = 999999  # Placeholder to initialize distances to "infinity"


def shortest_path(graph, start):
    """
    Run Dijkstra's algorithm to find the shortest paths from the given location
    to all other locations.
    :param graph: Graph containing the locations to run the shortest paths.
    Should contain a list of all location nodes.
    :param start: Start location to get paths from.
    :return: Dictionary containing each location mapped to a list of
    locations representing the shortest path from the start location to that
    location. A location mapped to an empty list means that there is no path
    from the start location to the end location.
    """
    # Create initial set of unvisited nodes.
    unvisited = set(location for location in graph)

    # Create a dictionary to map each location to its estimated distance,
    # with the initial distance set to infinity except for the start
    # location, which has its distance set to 0.
    distances = {location: INFINITY for location in dl.graph}
    distances[start] = 0

    # Create a dictionary to map each location to the shortest path. Paths
    # are initially empty except for the start node, which is mapped to
    # itself. Each path is a list of locations with the start location as the
    # first element and the end location as the last element.
    paths = {location: [] for location in dl.graph}
    paths[start] = [start]

    # Set minimum path length in the unvisited set to be 0 initially to
    # represent the start node.
    min_len = 0
    min_node = start

    # Keep finding shortest path unless the minimum in the unvisited set is
    # infinity, in which case the remaining locations are not reachable.
    while (min_len < INFINITY):
        # Mark the minimum node as visited
        unvisited.remove(min_node)
        # Get neighbors of minimum node in unvisited set, as well as the path
        # for the minimum node
        neighbors = min_node.adjList
        min_node_path = paths[min_node]
        # Get all the neighbors of minimum node and see if they are visited.
        # If they are unvisited, check if the path through the minimum node
        # has a smaller length than the current path length for that node. If
        # so, update with the path through the minimum node.
        for location in min_node.adjList:
            old_length = distances[location]
            new_length = min_len + location.length
            if location in unvisited and new_length < old_length:
                distances[location] = new_length
                # Copy old path and append the current location
                new_path = min_node_path.copy()
                new_path.append(location)
                # Set minimum path to the new path
                paths[location] = new_path

        # Get the new minimum length and node for next iteration of algorithm
        min_len = INFINITY
        for location in unvisited:
            if distances[location] < min_len:
                min_len = distances[location]
                min_node = location

    # Return map of paths
    return paths
