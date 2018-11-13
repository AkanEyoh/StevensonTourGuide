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
# 1 hallway.

from src import locations

#########################
## Initialize Locations##
#########################
## Floor 1 Locations
staircase1_1 = locations.Staircase()

hallway1_1 = locations.Hallway()

elevator1 = locations.Elevator()

hallway1_2 = locations.Hallway()

staircase1_2 = locations.Staircase()

## Floor 2 Locations
staircase2_1 = locations.Staircase()

hallway2_1 = locations.Hallway()
elevator2 = locations.Elevator()

# back area that leads outside
hallway2_2 = locations.Hallway()

staircase2_2 = locations.Staircase()

# Floor 3 Locations
staircase3_1 = locations.Staircase()

hallway3_1 = locations.Hallway()

elevator3 = locations.Elevator()

hallway3_2 = locations.Hallway()

staircase3_2 = locations.Staircase()

# Floor 4 Locations
staircase4_1 = locations.Staircase()

hallway4_1 = locations.Hallway()

elevator4 = locations.Elevator()

hallway4_2 = locations.Hallway()

staircase4_2 = locations.Staircase()

# Floor 5 Locations
staircase5_1 = locations.Staircase()

hallway5_1 = locations.Hallway()

elevator5 = locations.Elevator()

hallway5_2 = locations.Hallway()

staircase5_2 = locations.Staircase()

##################################
## Set attributes for locations.##
##################################
## Floor 1 Locations
staircase1_1.adjList = [hallway1_1, staircase2_1]

hallway1_1.roomList = ["1113", "1114", "1115", "1117", "1118", "1120", "1122"]
hallway1_1.adjList = [staircase1_1, elevator1, hallway1_2]
hallway1_1.length = 7

elevator1.adjList = [hallway1_1, hallway1_2, elevator2, elevator3, elevator4,
                     elevator5]

hallway1_2.roomList = ["1103", "1107", "1109", "1110", "1110A", "1110B",
                       "1110C", "1130"]
hallway1_2.adjList = [staircase1_2, elevator1, hallway1_1]
hallway1_2.length = 8

staircase1_2.adjList = [hallway1_2, staircase2_2]

## Floor 2 Locations
staircase2_1.adjList = [hallway2_1, staircase1_1, staircase3_1]

hallway2_1.roomList = ["1210", "1214", "1216", "1220", "1221", "1222", "1224",
                       "1227", "1232"]
hallway2_1.adjList = [staircase2_1, elevator2, hallway2_2]
hallway2_1.length = 9

elevator2.adjList = [hallway2_1, elevator1, elevator3, elevator4, elevator5]

# back area that leads outside
hallway2_2.roomList = ["1206", "1206A", "1219"]
hallway2_2.adjList = [staircase2_2, elevator2, hallway2_1]
hallway2_2.length = 3

staircase2_2.adjList = [hallway2_2, staircase1_2]

# Floor 3 Locations
staircase3_1.adjList = [hallway3_1, staircase2_1, staircase4_1]

hallway3_1.roomList = ["1322", "1323", "1324", "1326", "1326A", "1326B",
                       "1326C", "1326D", "1326E", "1326F", "1326G"]
hallway3_1.adjList = [staircase3_1, elevator3, hallway3_2]
hallway3_1.length = 11

elevator3.adjList = [hallway3_1, hallway3_2, elevator1, elevator2, elevator4,
                     elevator5]

hallway3_2.roomList = ["1307", "1308", "1309", "1310", "1312", "1313"]
hallway3_2.adjList = [staircase3_2, elevator3, hallway3_1]
hallway3_2.length = 6

staircase3_2.adjList = [hallway3_2, staircase4_2]

# Floor 4 Locations
staircase4_1.adjList = [hallway4_1, staircase3_1, staircase5_1]

hallway4_1.roomList = ["1422", "1424", "1425", "1426", "1427", "1428", "1431",
                       "1432"]
hallway4_1.adjList = [staircase4_1, elevator4, hallway4_2]
hallway4_1.length = 8

elevator4.adjList = [hallway4_1, hallway4_2, elevator1, elevator2, elevator3,
                     elevator5]

hallway4_2.roomList = ["1401", "1403", "1404", "1405", "1407", "1408", "1410",
                       "1411", "1412", "1413", "1414", "1415", "1416", "1418",
                       "1419", "1420"]
hallway4_2.adjList = [staircase4_2, elevator4, hallway4_1]
hallway4_2.length = 16

staircase4_2.adjList = [hallway4_2, staircase3_2, staircase5_2]

# Floor 5 Locations
staircase5_1.adjList = [hallway5_1, staircase4_1]

hallway5_1.roomList = ["1523", "1524", "1525", "1526", "1527", "1528", "1529",
                       "1531", "1532", "1533"]
hallway5_1.adjList = [staircase5_1, elevator5, hallway5_2]
hallway5_1.length = 10

elevator5.adjList = [hallway5_1, hallway5_2, elevator1, elevator2, elevator3,
                     elevator4]

hallway5_2.roomList = ["1502", "1503", "1504", "1505", "1507", "1510", "1511",
                       "1512", "1513", "1514", "1515", "1516", "1518", "1520",
                       "1522"]
hallway5_2.adjList = [staircase5_2, elevator5, hallway5_1]
hallway5_2.length = 15

staircase5_2.adjList = [hallway5_2, staircase4_2]

## Graph that is a list of all locations
stevenson_math = [staircase1_1, staircase1_2, staircase2_1, staircase2_2,
                  staircase3_1, staircase3_2, staircase4_1, staircase4_2,
                  staircase5_1, staircase5_2, elevator1, elevator2,
                  elevator3, elevator4, elevator5, hallway1_1, hallway1_2,
                  hallway2_1, hallway2_2, hallway3_1, hallway3_2, hallway4_1,
                  hallway4_2, hallway5_1, hallway5_2]