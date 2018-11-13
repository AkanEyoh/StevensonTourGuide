## Author(s): Daniel Yan
## Date: 2018-11-11
## Email: daniel.yan@vanderbilt.edu

## Description: Implements Dijkstra's shortest path to find the shortest path
## from each location to any other location.

## Import statements
import queue  # Priority queue
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
    unvisited = get_unvisited(graph)

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

    # Initialize priority queue with a tuple of the form (distance, location)
    # where the distance represents the priority of the location in the
    # priority queue.
    pqueue = create_priority_queue(graph, start)


def get_unvisited(graph):
    """
    Get a set of all nodes in a graph.
    :param graph: List of location objects representing a graph.
    :return: Set of all location objects in the graph.
    """
    return set(location for location in graph)


def create_priority_queue(graph, start, distances):
    """
    Return a priority queue with all locations in the graph set with a
    priority that corresponds to the map in distances.
    :param graph: List of locations representing a graph.
    :param start: Start location that should have priority set to 0.
    :param distances: Dictionary mapping the locations to the distances from
    start.
    :return: A priority queue object with tuples such that all locations have
    priority infinity except for the start location.
    """
    pqueue = queue.PriorityQueue()
    # Add all locations except for the start location
    for location in graph:
        if location != start:
            # Create tuple containing distance as priority and the location
            tuple = (distances[location], location)
            # Add the tuple to the priority queue

    return set(location for location in graph)
