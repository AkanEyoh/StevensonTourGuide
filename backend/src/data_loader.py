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

hallway1_2 = locations.Hallway(id_name="hallway 1-2")

staircase1_2 = locations.Staircase(id_name="staircase1-2")

##################################
## Set attributes for locations.##
##################################
## Floor 1 Locations
staircase1_1.adjList = [hallway1_1]

hallway1_1.roomList = ["1113", "1114", "1115", "1117", "1118", "1120", "1122"]
hallway1_1.adjList = [staircase1_1, elevator1, hallway1_2]
hallway1_1.length = len(hallway1_1.roomList)
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
hallway1_2.length = len(hallway1_2.adjList)
hallway1_2.topviewAboveList = ["1130", "1110C", "1110B", "1110A", "1110"]
hallway1_2.topviewBelowList = ["1109", "1107", "1103"]
hallway1_2.topviewLeftList = [hallway1_1]
hallway1_2.topviewRightList = []
hallway1_2.topviewOrderList = ["1130", "1110C", "1109", "1107", "1110B", "1110A", "1110", "1103"]
# New stuff ends here

##################### Building 2 stuff starts here


### Floor 1
# Building 2 Floor 1 Initialize data
staircase2_1_1 = locations.Staircase(id_name="staircase2-1-1")
hallway2_1_1 = locations.Hallway(id_name="hallway2-1-1")
hallway2_1_2 = locations.Hallway(id_name="hallway2-1-2")
elevator2_1_1 = locations.Elevator(id_name="elevator2-1-1")
hallway2_1_3 = locations.Hallway(id_name="hallway2-1-3")
hallway2_1_4 = locations.Hallway(id_name="hallway2-1-4")
hallway2_1_5 = locations.Hallway(id_name="hallway2-1-5")

# Load data
staircase2_1_1.adjList = [hallway2_1_1]

hallway2_1_1.roomList = ["2100A", "2102", "2102A", "2102B", "2107"]
hallway2_1_1.adjList = [staircase2_1_1, hallway2_1_2, elevator2_1_1]
hallway2_1_1.length = len(hallway2_1_1.roomList)
hallway2_1_1.topviewAboveList = [hallway2_1_2]
hallway2_1_1.topviewBelowList = ["2100A", "2102", "2102A", "2102B", "2107"]
hallway2_1_1.topViewLeftList = []
hallway2_1_1.topviewRightList = []
hallway2_1_1.topviewOrderList = ["2100A", "2102", "2102A", "2102B", "2107"]

# hallway2_1_2.adjList = [hallway2_1_1]
hallway2_1_2.roomList = ["2101", "2105", "2104", "2106", "2120", "2121", "2129", "2128"]
hallway2_1_2.adjList = [hallway2_1_1, hallway2_1_3]
hallway2_1_2.length = len(hallway2_1_2.roomList)
hallway2_1_2.topviewAboveList = ["2105", "2121"]
hallway2_1_2.topviewBelowList = ["2100A", "2102", "2102A", "2102B", "2107"]
hallway2_1_2.topViewLeftList = ["2101"]
hallway2_1_2.topviewRightList = [hallway2_1_3]
hallway2_1_2.topviewOrderList = ["2101", hallway2_1_1, "2105", "2104", "2106", "2121", "2129",
                                 "2128", hallway2_1_3]

# hallway2_1_3.adjList = [hallway2_1_2, hallway2_1_4]
hallway2_1_3.roomList = ["2126", "2127"]
hallway2_1_3.adjList = [hallway2_1_2, hallway2_1_4, hallway2_1_5]
hallway2_1_3.length = len(hallway2_1_3.roomList)
hallway2_1_3.topviewLeftList = [hallway2_1_4]
hallway2_1_3.topviewAboveList = []
hallway2_1_3.topviewRightList = ["2126", hallway2_1_5]
hallway2_1_3.topviewBelowList = ["2121", "2127"]
hallway2_1_3.topviewOrderList = ["2121", hallway2_1_4, hallway2_1_5, "2126", "2127", hallway2_1_2]

hallway2_1_4.roomList = ["2121", "2122"]
hallway2_1_4.adjList = [hallway2_1_3]
hallway2_1_4.length = len(hallway2_1_4)
hallway2_1_4.topviewLeftList = ["2121"]
hallway2_1_4.topviewAboveList = []
hallway2_1_4.topviewRightList = ["2122"]
hallway2_1_4.topviewBelowList = [hallway2_1_3]
hallway2_1_4.topviewOrderList = ["2121", "2122", hallway2_1_3]

hallway2_1_5.roomList = ["2127", "2126", "2125", "2124", "2123", "2122"]
hallway2_1_5.adjList = [hallway2_1_3]
hallway2_1_5.length = len(hallway2_1_5.roomList)
hallway2_1_5.topviewLeftList = ["2127"]
hallway2_1_5.topviewAboveList = [hallway2_1_3, "2122"]
hallway2_1_5.topviewRightList = ["2123"]
hallway2_1_5.topviewBelowList = ["2126", "2125", "2124"]
hallway2_1_5.topviewOrderList = ["2127", hallway2_1_3, "2122", "2123", "2124", "2125", "2126"]

### Floor 2
staircase2_2_1 = locations.Staircase(id_name="staircase2-2-1")
elevator2_2_1 = locations.Elevator(id_name="elevator2-2-1")
hallway2_2_1 = locations.Hallway(id_name="hallway2-2-1")
hallway2_2_2 = locations.Hallway(id_name="hallway2-2-2")
hallway2_2_3 = locations.Hallway(id_name="hallway2-2-3")

staircase2_2_1.adjList = [hallway2_2_1, staircase2_1_1]

elevator2_2_1.adjList = [hallway2_2_1, elevator2_1_1]

hallway2_2_1.roomList = ["2220"]
hallway2_2_1.adjList = [staircase2_2_1, elevator2_2_1]
hallway2_2_1.length = len(hallway2_2_1.roomList)
hallway2_2_1.topviewLeftList = [staircase2_2_1]
hallway2_2_1.topviewAboveList = [hallway2_1_2]
hallway2_2_1.topviewRightList = ["2220"]
hallway2_2_1.topviewBelowList = [elevator2_2_1]
hallway2_2_1.topviewOrderList = [staircase2_2_1, hallway2_1_2, "2220", elevator2_2_1]

hallway2_2_2.roomList = ["2200", "2212"]
hallway2_2_2.adjList = [hallway2_2_1, hallway2_2_3]
hallway2_2_2.length = len(hallway2_2_2.roomList)
hallway2_2_2.topviewLeftList = ["2200"]
hallway2_2_2.topviewAboveList = ["2212"]
hallway2_2_2.topviewRightList = [hallway2_2_3]
hallway2_2_2.topviewBelowList = [hallway2_2_1]
hallway2_2_2.topviewOrderList = ["2200", "2212", hallway2_2_3, hallway2_2_1]

hallway2_2_3.roomList = ["2212"]
hallway2_2_3.adjList = [hallway2_2_2] # TODO: connect to building 3/4 (whichever is next to here)
hallway2_2_3.length = len(hallway2_2_3.roomList)
hallway2_2_3.topviewLeftList = ["2212"]
hallway2_2_3.topviewAboveList = [] # TODO: Same as above!!!!!!!!!!!!!
hallway2_2_3.topviewRightList = [] # TODO: May need to say there are outside exits here
hallway2_2_3.topviewBelowList = [hallway2_2_2]
hallway2_2_3.topviewOrderList = ["2212", hallway2_2_2] # TODO: Add connection to next building

####################### Building 2 stuff ends here

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
