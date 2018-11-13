## Author(s): Daniel Yan
## Date: 2018-11-11
## Email: daniel.yan@vanderbilt.edu

## Description: Implements Dijkstra's shortest path to find the shortest path
## from each location to any other location.

## Imports
from src import data_loader as d
from src import locations as loc

def shortest_path(graph, node):
    """
    Run Dijkstra's algorithm to find the shortest paths from the given location
    to all other locations.
    :param graph: Graph containing the locations to run the shortest paths.
    Should contain a list of all location nodes.
    :param node: Start location to get paths from.
    :return: Map containing each location mapped to the shortest route to
    that location from the node parameter.
    """
    # Create set of unvisited nodes.
    unvisited = get_unvisited(graph, node)
    # Get initial set of visited nodes as the node passed as parameter
    visited = set()
    visited.add(node)

def get_unvisited(graph, node):
    """
    Get a set of all nodes in a graph except the node passed as a parameter.
    :param graph: List of location objects representing a graph.
    :param node: The given location that should not be in the set.
    :return: Set of location objects excluding the node passed as parameter.
    """
    unvisited = set()
    for location in graph:
        if location != node:
            unvisited.add(location)
    return unvisited
