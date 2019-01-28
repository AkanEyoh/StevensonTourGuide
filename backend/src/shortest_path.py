## Author(s): Daniel Yan
## Date: 2018-11-11
## Email: daniel.yan@vanderbilt.edu

## Description: Implements Dijkstra's shortest path to find the shortest path
## from each location to any other location.

## Constants
INFINITY = 999999  # Placeholder to initialize distances to "infinity"

# Import libraries
import data_loader as dl
import locations

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
    from the start location to the end location. Return false if the start
    location is not in the graph.
    """
    # Create initial set of unvisited nodes.
    unvisited = set(location for location in graph)

    # Return false if the start location is not in the graph.
    if start not in unvisited:
        return False

    # Create a dictionary to map each location to its estimated distance,
    # with the initial distance set to infinity except for the start
    # location, which has its distance set to 0.
    distances = {location: INFINITY for location in graph}
    distances[start] = 0

    # Create a dictionary to map each location to the shortest path. Paths
    # are initially empty except for the start node, which is mapped to
    # itself. Each path is a list of locations with the start location as the
    # first element and the end location as the last element.
    paths = {location: [] for location in graph}
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
        # Get path to minimum node.
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


# Dictionary containing mapping each location in Stevenson to shortest path
# map for each location.
stevenson_paths = dict()
for location in dl.graph:
    stevenson_paths[location] = shortest_path(graph=dl.graph, start=location)


def get_path_from_rooms(start_room, end_room):
    """
    Given two strings representing a room, use the dictionary mapping the
    rooms to hallways to find a start and end location, and use the
    stevenson_paths dictionary to find and return the shortest path, which is
    a list of locations to traverse.
    :param start_room: String representing room to start from.
    :param end_room: String representing room to end at.
    :return: List of locations representing a path from the start room to the
    end room. If either of the rooms do not exist in Stevenson, return False.
    """
    # Get the corresponding locations for the start and end room
    start_loc = dl.rooms_map.get(start_room)
    end_loc = dl.rooms_map.get(end_room)
    # Return false if either of the rooms does not exist.
    if start_loc is None or end_loc is None:
        return False
    # Get dictionary with all shortest paths for the start location.
    all_paths = stevenson_paths.get(start_loc)
    # Return the shortest path to the end location from the dictionary of all
    # shortest paths. Return false if there is not a corresponding location.
    path = all_paths.get(end_loc)
    if path is None:
        return False
    else:
        return path

def is_hallway(loc):
    """
    Returns if the given location is a hallway
    :param loc: the location to be checked
    :return whether the location is a hallway
    """
    return isinstance(loc, locations.Hallway)

def is_turning_junction(loc1, loc2):
    """
    Returns if the two locations form a turning junction,
    i.e. if the user needs to be given a turning direction here
    :param loc1: first location
    :param loc2: second location
    :return whether there is a turning juncture
    """
    return is_hallway(loc2) and (not is_hallway(loc1) or loc1 in loc2.topviewOrderList)

def find_turn(loc1, loc2, loc3, direction):
    """
    Determnes what turn should be made when the user is travelling from
    loc1 to loc2 and outputs a string representing that direction. E.g.
    'Turn right at the hallway.' Note this also includes when the user
    doesn't need to turn and just travels straight on.
    :param loc1: start location
    :param loc2: intermediate location (must be a hallway)
    :param loc3: location to go to view loc2
    :return string representing correct direction to go
    """
    direction_grid = [['right', 'left'], ['left', 'right']]

    if loc1 in loc2.topviewAboveList:
        entry_top_oriented = 0
    elif loc1 in loc2.topviewBelowList:
        entry_top_oriented = 1

    if is_hallway(loc3) and loc3 not in loc2.topviewAboveList + loc2.topviewBelowList:
        # going from a hallway into another hallway of same orientation
        if loc3 in loc2.topviewLeftList:
            dest_left = 0
        elif loc3 in loc2.topviewRightList:
            dest_left = 1
    else:
        # going from hallway into a room / stair / perpendicular hallway
        loc1_dist_to_right = loc2.topviewOrderList.index(loc1)
        loc3_dist_to_right = loc2.topviewOrderList.index(loc3)
        if loc3_dist_to_right < loc1_dist_to_right:
            dest_left = 0
        else:
            dest_left = 1

    return ['Take a ' + direction_grid[entry_top_oriented][dest_left], dest_left == 0]

def path_to_string(path, start, dest):
    """ 
    Takes the path produced by get_paths_from_rooms and produces
    a string representing the instructions that should be taken by the 
    user to arrive at their destination
    :param path: the path produced by get_paths_from_rooms
    :param start: the starting room
    :param dest: the destination room
    :return a string representing the directions
    """
    cur_direction = None
    cur_loc = start
    path_string = ''
    while len(path) != 0:
        next_loc = path[0]
        path = path[1:]

        if is_turning_junction(cur_loc, next_loc):
    
            if cur_loc in next_loc.topviewLeftList:
                # door / staircase / elevator already faces into hallway
                # no turn necessary
                path_string += 'Continue straight ahead\n'
                cur_direction = 'right'

            elif cur_loc in next_loc.topviewRightList:
                path_string += 'Continue straight ahead\n'
                cur_direction = 'left'

            else:
                try:
                    # future_loc is the location after next_loc in path
                    future_loc = path[0]
                    ret = find_turn(cur_loc, next_loc, future_loc)
                    path_string += ret[0]
                    if ret[1]:
                        cur_direction = 'left'
                    else:
                        cur_direction = 'right' 

                except IndexError: 
                    ret = find_turn(cur_loc, next_loc, dest)
                    path_string += ret[0]
                    if ret[1]:
                        cur_direction = 'left'
                    else:
                        cur_direction = 'right'

        # user travelling straight through a hallway
        # no directions needed
        elif is_hallway(cur_loc) and is_hallway(next_loc):
            pass

        elif 
