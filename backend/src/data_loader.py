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
## Building 1 (MATH) Locations##
#########################
## Floor 1 Locations 
staircase1_1_1 = locations.Staircase(id_name="staircase1-1-1")

hallway1_1_1 = locations.Hallway(id_name="hallway1-1-1")

elevator1_1 = locations.Elevator(id_name="elevator1-1")

hallway1_1_2 = locations.Hallway(id_name="hallway1-1-2")

staircase1_1_2 = locations.Staircase(id_name="staircase1-1-2")

## Floor 2 Locations

staircase1_2_1 = locations.Staircase(id_name="staircase1-2-1")

hallway1_2_1 = locations.Hallway(id_name="hallway1-2-1")

elevator1_2 = locations.Elevator(id_name="elevator1-2")

hallway1_2_2 = locations.Hallway(id_name="hallway1-2-2")

staircase1_2_2 = locations.Staircase(id_name="staircase1-2-2")

##################################
## Set relations for Building 1 (MATH)##
##################################
## Floor 1 Locations
staircase1_1_1.adjList = [hallway1_1_1, staircase1_2_1]
staircase1_1_1.floor = 1

hallway1_1_1.roomList = ["1113", "1114", "1115", "1117", "1118", "1120", "1122"]
hallway1_1_1.adjList = [staircase1_1_1, elevator1_1, hallway1_1_2]
hallway1_1_1.length = 7
hallway1_1_1.topviewAboveList = ["1120", staircase1_1_1, "1118", "1114"]
hallway1_1_1.topviewBelowList = ["1117", "1115", "1113", elevator1_1]
hallway1_1_1.topviewLeftList = ["1122"]
hallway1_1_1.topviewRightList = [hallway1_1_2]
hallway1_1_1.topviewOrderList = ["1122", "1120", "1117", staircase1_1_1, "1118", "1115", "1114", "1113", elevator1_1]


elevator1_1.adjList = [hallway1_1_1, hallway1_1_2, elevator1_2]
elevator1_1.floor = 1

hallway1_1_2.roomList = ["1103", "1107", "1109", "1110", "1110A", "1110B",
                       "1110C", "1130"]
hallway1_1_2.adjList = [staircase1_1_2, elevator1_1, hallway1_1_1]
hallway1_1_2.length = 8
hallway1_1_2.topviewAboveList = [staircase1_1_2, "1110C", "1110B", "1110A", "1110"]
hallway1_1_2.topviewBelowList = [elevator1_1, "1109", "1107", "1103"]
hallway1_1_2.topviewLeftList = [hallway1_1_1]
hallway1_1_2.topviewRightList = []
hallway1_1_2.topviewOrderList = [staircase1_1_2, elevator1_1, "1110C", "1109", "1107", "1110B", "1110A", "1110", "1103", staircase1_1_2]

staircase1_1_2.adjList = [hallway1_1_2, staircase1_2_2]
staircase1_1_2.floor = 1

## Floor 2 locations

staircase1_2_1.adjList = [hallway1_2_1, staircase1_1_1]
staircase1_2_1.floor = 2

hallway1_2_1.roomList = ["1232", "1224", "1222", "1220", "1225", "1218"]
hallway1_2_1.adjList = [staircase1_2_1, elevator1_2, hallway1_2_2]
hallway1_2_1.length = 6
hallway1_2_1.topviewAboveList = ["1232", staircase1_2_1, "1224", "1222", "1220", "1218"]
hallway1_2_1.topviewBelowList = ["1225", elevator1_2]
hallway1_2_1.topviewLeftList = []
hallway1_2_1.topviewRightList = [hallway1_2_2]
hallway1_2_1.topviewOrderList = ["1232", staircase1_2_1, "1224", "1222", "1225", "1220", elevator1_2, "1218"]

elevator1_2.adjList = [hallway1_2_1, elevator1_1]
elevator1_2.floor = 2

hallway1_2_2.roomList = ["1219", "1214", "1210", "1206"]
hallway1_2_2.adjList = [staircase1_2_2, elevator1_2, hallway1_2_1]
hallway1_2_2.length = 7
hallway1_2_2.topviewAboveList = ["1214", "1210", "1206", staircase1_2_2]
hallway1_2_2.topviewBelowList = [elevator1_2, "1219"]
hallway1_2_2.topviewLeftList = [hallway1_2_1]
hallway1_2_2.topviewRightList = []
hallway1_2_2.topviewOrderList = [elevator1_2, "1219", "1214", "1210", "1206", staircase1_2_2]

staircase1_2_2.adjList = [hallway1_2_2, staircase1_1_2]
staircase1_2_2.floor = 2


stevenson_math = [staircase1_1_1, staircase1_1_2, elevator1_1, hallway1_1_1, hallway1_1_2, staircase1_2_1, staircase1_2_2, elevator1_2, hallway1_2_1, hallway1_2_2]

#########################
## Building 2 (MOLEC. BIO) Locations##
#########################
## Floor 1 Locations 
staircase2_1_1 = locations.Staircase(id_name="staircase2-1-1")

hallway2_1_1 = locations.Hallway(id_name="hallway2-1-1")

hallway2_1_2 = locations.Hallway(id_name="hallway2-1-2")

hallway2_1_3 = locations.Hallway(id_name="hallway2-1-3")

hallway2_1_4 = locations.Hallway(id_name="hallway2-1-4")


elevator1_1 = locations.Elevator(id_name="elevator1-1")

hallway1_1_2 = locations.Hallway(id_name="hallway1-1-2")

staircase1_1_2 = locations.Staircase(id_name="staircase1-1-2")

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
