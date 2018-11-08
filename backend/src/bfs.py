## Author(s): Daniel Yan
## Date: 2018-11-02
## Email: daniel.yan@vanderbilt.edu

## Description: Implement breadth first search algorithm for traversing nodes
##(which are hallways, stairs, elevators, etc) to find path from start to end
## location.

## Import libraries
import locations
import queue # Queues for breadth first search

## Class constants
# Each item in the queue is stored as a list with location at index
# 0 of the list and the current route as index 1 of that list.
LOCATION = 0
ROUTE = 1

def bfs (start, end, queue=queue.Queue(), route=[], visited=set()):
    """
    Use breath first search to find a route from the start location to the
    end location. Route stores the route to return.

    :param start: Location to start the search.
    :param end: Goal location for the search.
    :param route: List of locations that need to be traversed.
    :param queue: Queue to use for breadth first search.
    :param set: Set of visited nodes to avoid visiting them again.
    :return: Path from start location to the end location.
    """
    # Add the start location to the queue with the current route and mark
    # the start location as visited.
    queue.put([start, route])
    visited.add(start)
    # Keep searching as long as the queue is not empty
    while(not queue.empty()):
        # Get the first item on the queue
        current_item = queue.get()
        # Get the corresponding location and route for that item
        current_location = current_item[0]
        current_route = current_item[1]
        # Add the current location to the new route
        new_route = current_route.append(current_location)
        # If the location is the end location, simply return the new route.
        if current_location == end:
            return new_route
        # Otherwise, get all the locations adjacent to the current location
        else:
            for location in current_location.adjList:
                # Mark unvisited adjacent locations as visited and
                # add them to the queue with the new route.
                if location not in visited:
                    visited.add(location)
                    queue.put([location, route])
    # Return false if no location is found.
    return False




