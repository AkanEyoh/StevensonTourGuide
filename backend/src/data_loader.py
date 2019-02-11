## Author(s): Akaninyene Eyoh, Daniel Yan, Reid Wilson, Keaton Ufheil
## Date: 2018-11-06
## Email: akaninyene.e.eyoh@vanderbilt.edu, daniel.yan@vanderbilt.edu
## Filename: dataLoader.py
## Description: Loads the data for adjacency lists and room lists into in
# each location type.

## Format:
## Hallways are split down the middle and separated by an elevator, however
#  hallways on the same floor still act as
#  adjacent nodes to each other.

## Naming Convention:
## staircaseX_Y: X = floor number, Y = end of hallway (1 = bottom half,
# 2 = top half)
## hallwayX_Y: X = floor number, Y = end of hallway (1 = bottom half, 2 = top
#  half)
## elevatorX: X = which floor an elevator stops at

## Determining length of hallway was relative to how many classrooms were in
# 1 hallway.

from src import locations

#########################
## Initialize Locations##
#########################
## Floor 1 Locations 
math_staircase1_1 = locations.Staircase(id_name="math_staircase1-1")

math_hallway1_1 = locations.Hallway(id_name="math_hallway1-1")

math_elevator1 = locations.Elevator(id_name="math_elevator1")

math_hallway1_2 = locations.Hallway(id_name="math_hallway1-2")

math_staircase1_2 = locations.Staircase(id_name="math_staircase1-2")

## Floor 2 Locations
math_staircase2_1 = locations.Staircase(id_name="math_staircase2-1")

math_hallway2_1 = locations.Hallway(id_name="math_hallway2-1")
math_elevator2 = locations.Elevator(id_name="math_elevator2")

# back area that leads outside
math_hallway2_2 = locations.Hallway(id_name="math_hallway2-2")

math_staircase2_2 = locations.Staircase(id_name="math_staircase2-2")

# Floor 3 Locations
math_staircase3_1 = locations.Staircase(id_name="math_staircase3-1")

math_hallway3_1 = locations.Hallway(id_name="math_hallway3-1")

math_elevator3 = locations.Elevator(id_name="math_elevator3")

math_hallway3_2 = locations.Hallway(id_name="math_hallway3-2")

math_staircase3_2 = locations.Staircase(id_name="math_staircase3-2")

# Floor 4 Locations
math_staircase4_1 = locations.Staircase(id_name="math_staircase4-1")

math_hallway4_1 = locations.Hallway(id_name="math_hallway4-1")

math_elevator4 = locations.Elevator(id_name="math_elevator4")

math_hallway4_2 = locations.Hallway(id_name="math_hallway4-2")

math_staircase4_2 = locations.Staircase(id_name="math_staircase4-2")

# Floor 5 Locations
math_staircase5_1 = locations.Staircase(id_name="math_staircase5-1")

math_hallway5_1 = locations.Hallway(id_name="math_hallway5-1")

math_elevator5 = locations.Elevator(id_name="math_elevator5")

math_hallway5_2 = locations.Hallway(id_name="math_hallway5-2")

math_staircase5_2 = locations.Staircase(id_name="math_staircase5-2")

#Bio locations start
bio_staircase2_1 = locations.Staircase(id_name="bio_staircase2_1")

bio_hallway2_1 = locations.Hallway(id_name="bio_hallway2_1")

bio_hallway2_2 = locations.Hallway(id_name="bio_hallway2_2")

##################################
## Set attributes for locations.##
##################################
## Floor 1 Locations
math_staircase1_1.adjList = [math_hallway1_1, math_staircase2_1]

math_hallway1_1.roomList = ["1113", "1114", "1115", "1117", "1118", "1120", "1122"]
math_hallway1_1.adjList = [math_staircase1_1, math_elevator1, math_hallway1_2]
math_hallway1_1.length = 7

math_elevator1.adjList = [math_hallway1_1, math_hallway1_2, math_elevator2, math_elevator3, math_elevator4,
                     math_elevator5]

math_hallway1_2.roomList = ["1103", "1107", "1109", "1110", "1110A", "1110B",
                       "1110C", "1130"]
math_hallway1_2.adjList = [math_staircase1_2, math_elevator1, math_hallway1_1, bio_hallway2_1]
math_hallway1_2.length = 8

math_staircase1_2.adjList = [math_hallway1_2, math_staircase2_2]

## Floor 2 Locations
math_staircase2_1.adjList = [math_hallway2_1, math_staircase1_1, math_staircase3_1]

math_hallway2_1.roomList = ["1210", "1214", "1216", "1220", "1221", "1222", "1224",
                       "1227", "1232"]
math_hallway2_1.adjList = [math_staircase2_1, math_elevator2, math_hallway2_2]
math_hallway2_1.length = 9

math_elevator2.adjList = [math_hallway2_1, math_hallway2_2 math_elevator1, math_elevator3, math_elevator4, math_elevator5]

# back area that leads outside
math_hallway2_2.roomList = ["1206", "1206A", "1219"]
math_hallway2_2.adjList = [math_staircase2_2, math_elevator2, math_hallway2_1]
math_hallway2_2.length = 3

math_staircase2_2.adjList = [math_hallway2_2, math_staircase1_2]

# Floor 3 Locations
math_staircase3_1.adjList = [math_hallway3_1, math_staircase2_1, math_staircase4_1]

math_hallway3_1.roomList = ["1322", "1323", "1324", "1326", "1326A", "1326B",
                       "1326C", "1326D", "1326E", "1326F", "1326G"]
math_hallway3_1.adjList = [math_staircase3_1, math_elevator3, math_hallway3_2]
math_hallway3_1.length = 11

math_elevator3.adjList = [math_hallway3_1, math_hallway3_2, math_elevator1, math_elevator2, math_elevator4,
                     math_elevator5]

math_hallway3_2.roomList = ["1307", "1308", "1309", "1310", "1312", "1313"]
math_hallway3_2.adjList = [math_staircase3_2, math_elevator3, math_hallway3_1]
math_hallway3_2.length = 6

math_staircase3_2.adjList = [math_hallway3_2, math_staircase4_2]

# Floor 4 Locations
math_staircase4_1.adjList = [math_hallway4_1, math_staircase3_1, math_staircase5_1]

math_hallway4_1.roomList = ["1422", "1424", "1425", "1426", "1427", "1428", "1431",
                       "1432"]
math_hallway4_1.adjList = [math_staircase4_1, math_elevator4, math_hallway4_2]
math_hallway4_1.length = 8

math_elevator4.adjList = [math_hallway4_1, math_hallway4_2, math_elevator1, math_elevator2, math_elevator3,
                     math_elevator5]

math_hallway4_2.roomList = ["1401", "1403", "1404", "1405", "1407", "1408", "1410",
                       "1411", "1412", "1413", "1414", "1415", "1416", "1418",
                       "1419", "1420"]
math_hallway4_2.adjList = [math_staircase4_2, math_elevator4, math_hallway4_1]
math_hallway4_2.length = 16

math_staircase4_2.adjList = [math_hallway4_2, math_staircase3_2, math_staircase5_2]

# Floor 5 Locations
math_staircase5_1.adjList = [math_hallway5_1, math_staircase4_1]

math_hallway5_1.roomList = ["1523", "1524", "1525", "1526", "1527", "1528", "1529",
                       "1531", "1532", "1533"]
math_hallway5_1.adjList = [math_staircase5_1, math_elevator5, math_hallway5_2]
math_hallway5_1.length = 10

math_elevator5.adjList = [math_hallway5_1, math_hallway5_2, math_elevator1, math_elevator2, math_elevator3,
                     math_elevator4]

math_hallway5_2.roomList = ["1502", "1503", "1504", "1505", "1507", "1510", "1511",
                       "1512", "1513", "1514", "1515", "1516", "1518", "1520",
                       "1522"]
math_hallway5_2.adjList = [math_staircase5_2, math_elevator5, math_hallway5_1]
math_hallway5_2.length = 15

math_staircase5_2.adjList = [math_hallway5_2, math_staircase4_2]

##################### Reid's stuff starts here


# Load data
bio_staircase2_1.adjList = [hallway2_1]

bio_hallway2_1.roomList = ["100A", "102", "102A", "102B", "107"]
bio_hallway2_1.adjList = [bio_staircase2_1, bio_hallway1_2, bio_hallway2_2, bio_elevator2_1]

bio_hallway2_2.roomList = ["101", "105"]
bio_hallway2_2.roomList = ["121A", "121B","121C", "121D", "120", "129", "128", "122"]

####################### Reid's stuff ends here

# Graph that is a list of all locations. Set the initial graph to the
stevenson_network = [math_staircase1_1, math_staircase1_2, math_staircase2_1, math_staircase2_2,
                  math_staircase3_1, math_staircase3_2, math_staircase4_1, math_staircase4_2,
                  math_staircase5_1, math_staircase5_2, math_elevator1, math_elevator2, math_elevator3,
                  math_elevator4, math_elevator5, math_hallway1_1, math_hallway1_2, math_hallway2_1,
                  math_hallway2_2, math_hallway3_1, math_hallway3_2, math_hallway4_1, math_hallway4_2,
                  math_hallway5_1, math_hallway5_2, bio_staircase2_1, bio_hallway2_1,
		  bio_hallway2_2]

graph = stevenson_network

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