## Author(s): Akaninyene Eyoh, Daniel Yan
## Date: 2018-11-06
## Email: akaninyene.e.eyoh@vanderbilt.edu, daniel.yan@vanderbilt.edu
## Filename: dataLoader.py
## Description: Loads the data for adjacency lists and room lists into in
# each location type.

## Format:
## Hallways are split down the middle and separated by an elevator, however
# hallways on the same floor still act as
#  adjacent nodes to each other.

## Naming Convention:
## staircaseX_Y: X = floor number, Y = end of hallway (1 = bottom half,
# 2 = top half)
## hallwayX_Y: X = floor number, Y = end of hallway (1 = bottom half, 2 = top
#  half)
## elevatorX: X = which floor an elevator stops at

## Determining length of hallway was relative to how many classrooms were in
# 1 hallway

import locations

#########################
## Initialize Locations##
#########################
## Floor 1 Locations
staircase1_1 = locations.Staircase(id_name="staircase1-1")

hallway1_1 = locations.Hallway(id_name="hallway1-1")

elevator1 = locations.Elevator(id_name="elevator1")

hallway1_2 = locations.Hallway(id_name="hallway1-2")

staircase1_2 = locations.Staircase(id_name="staircase1-2")

##################################
## Set attributes for locations.##
##################################
## Floor 1 Locations
staircase1_1.adjList = [hallway1_1]

hallway1_1.roomList = ["1113", "1114", "1115", "1117", "1118", "1120", "1122"]
hallway1_1.adjList = [staircase1_1, elevator1, hallway1_2]
hallway1_1.length = 7
hallway1_1.topviewAboveList = ["1120", staircase1_1, "1118", "1114"]
hallway1_1.topviewBelowList = ["1117", "1115", "1113", elevator1]
hallway1_1.topviewLeftList = ["1122"]
hallway1_1.topviewRightList = [hallway1_2]
hallway1_1.topviewOrderList = ["1120", "1170", staircase1_1, "1118", "1115", "1114", "1113", elevator1]


elevator1.adjList = [hallway1_1, hallway1_2]

hallway1_2.roomList = ["1103", "1107", "1109", "1110", "1110A", "1110B",
                       "1110C", "1130"]
# New stuff starts here
hallway1_2.adjList = [staircase1_2, elevator1, hallway1_1]
hallway1_2.length = 8
hallway1_2.topviewAboveList = ["1130", "1110C", "1110B", "1110A", "1110"]
hallway1_2.topviewBelowList = ["1109", "1107", "1103"]
hallway1_2.topviewLeftList = [hallway1_1]
hallway1_2.topviewRightList = []
hallway1_2.topviewOrderList = ["1130", "1110C", "1109", "1107", "1110B", "1110A", "1110", "1103"]
# New stuff ends here

##################### Reid's stuff starts here

# Building 2 Floor 1 Initialize data
staircase2_1 = locations.Staircase(id_name="staircase2-1")
hallway2_1 = locations.Hallway(id_name="hallway2-1")
hallway2_2 = locations.Hallway(id_name="hallway2-2")
elevator2_1 = locations.Elevator(id_name="elevator2-1")
hallway2_3 = locations.Hallway(id_name="hallway2-3")
staircase2_3 = locations.Staircase(id_name="staircase2-3")

# Load data
staircase2_1.adjList = [hallway2_1]
hallway2_1.roomList = ["100A", "102", "102A", "102B", "107"]
hallway2_1.adjList = [staircase2_1, hallway1_2]
hallway2_1.adjList = [staircase2_1, hallway1_2, hallway2_2, elevator2_1]


####################### Reid's stuff ends here

staircase1_2.adjList = [hallway1_2]

stevenson_math = [staircase1_1, staircase1_2, elevator1, hallway1_1, hallway1_2]

graph = stevenson_math

# Create set containing all locations in the graph
locations_set = set(graph)

# Create dictionary mapping rooms to the adjacent hallway
rooms_map = {}
# Go through all locations in map
for location in graph:
    # Only hallways have an adjacency list of rooms.
    if isinstance(location, locations.Hallway):
        # Each value in the adjacency list should be a key, and the value is
        # the corresponding hallway
        for room in location.roomList:
            rooms_map[room] = location
