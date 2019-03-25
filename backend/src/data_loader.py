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
staircase1_1_1 = locations.Staircase(id_name="staircase1-1-1", url_base='1_1_1')

hallway1_1_1 = locations.Hallway(id_name="hallway1-1-1", url_base='1_1_1')

elevator1_1 = locations.Elevator(id_name="elevator1-1", url_base='1_1')

hallway1_1_2 = locations.Hallway(id_name="hallway1-1-2", url_base='1_1_2')

staircase1_1_2 = locations.Staircase(id_name="staircase1-1-2", url_base='1_1_2')

## Floor 2 Locations

staircase1_2_1 = locations.Staircase(id_name="staircase1-2-1", url_base='1_2_1')

hallway1_2_1 = locations.Hallway(id_name="hallway1-2-1", url_base='1_2_1')

elevator1_2 = locations.Elevator(id_name="elevator1-2", url_base='1_2')

hallway1_2_2 = locations.Hallway(id_name="hallway1-2-2", url_base='1_2_2')

staircase1_2_2 = locations.Staircase(id_name="staircase1-2-2", url_base='1_2_2')

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
hallway2_2_3.adjList = [hallway2_2_2]  # TODO: connect to building 3 (whichever is next to here)
hallway2_2_3.length = len(hallway2_2_3.roomList)
hallway2_2_3.topviewLeftList = ["2212"]
hallway2_2_3.topviewAboveList = []  # TODO: Same as above!!!!!!!!!!!!!
hallway2_2_3.topviewRightList = []  # TODO: May need to say there are outside exits here
hallway2_2_3.topviewBelowList = [hallway2_2_2]
hallway2_2_3.topviewOrderList = ["2212", hallway2_2_2]  # TODO: Add connection to building 3

### Floor 3
staircase2_3_1 = locations.Staircase(id_name="staircase2-3-1")
staircase2_3_2 = locations.Staircase(id_name="staircase2-3-2")
elevator2_3_1 = locations.Elevator(id_name="elevator2-3-1")
hallway2_3_1 = locations.Hallway(id_name="hallway2-3-1")

staircase2_3_1.adjList = [hallway2_3_1, staircase2_2_1, staircase2_1_1]

staircase2_3_2.adjList = [hallway2_3_1]

elevator2_3_1.adjList = [hallway2_3_1, elevator2_2_1, elevator2_1_1]

hallway2_3_1.roomList = ["2325", "2327", "2337", "2314", "2316", "2318", "2320", "2322", "2326",
                         "2328", "2332", "2336"]
hallway2_3_1.adjList = [staircase2_3_1, elevator2_3_1, staircase2_3_2]
hallway2_3_1.length = len(hallway2_3_1.adjList)
hallway2_3_1.topviewLeftList = [staircase2_3_1]
hallway2_3_1.topviewAboveList = ["2325", "2327", "2337"]
hallway2_3_1.topviewRightList = [staircase2_3_2]
hallway2_3_1.topviewBelowList = [elevator2_3_1, "2314", "2316", "2318", "2320", "2322", "2326",
                                 "2328", "2332", "2336"]
hallway2_3_1.topviewOrderList = [staircase2_3_1, "2325", "2327", "2337", staircase2_3_2,
                                 "2336", "2332", "2328", "2326", "2322", "2320", "2318", "2316",
                                 "2314", elevator2_3_1]


## Floor 4
staircase2_4_1 = locations.Staircase(id_name="staircase2-4-1")
staircase2_4_2 = locations.Staircase(id_name="staircase2-4-2")
elevator2_4_1 = locations.Elevator(id_name="elevator2-4-1")
hallway2_4_1 = locations.Hallway(id_name="hallway2-4-1")
hallway2_4_2 = locations.Hallway(id_name="hallway2-4-2")
hallway2_4_3 = locations.Hallway(id_name="hallway2-4-3")

staircase2_4_1.adjList = [hallway2_4_2, staircase2_3_1, staircase2_2_1, staircase2_1_1]

staircase2_4_2.adjList = [hallway2_4_2, staircase2_3_2]

elevator2_4_1.adjList = [hallway2_4_1, elevator2_3_1, elevator2_2_1, elevator2_1_1]

hallway2_4_1.roomList = ["2402", "2401", "2442"] #TODO Could make conflict since this room is techinically part of the other hallway in a way
hallway2_4_1.adjList = [elevator2_4_1, hallway2_4_2]
hallway2_4_1.length = len(hallway2_4_1.roomList)
hallway2_4_1.topviewLeftList = ["2402"]
hallway2_4_1.topviewAboveList = ["2401"]
hallway2_4_1.topviewRightList = ["2442"]
hallway2_4_1.topviewBelowList = ["2442"]
hallway2_4_1.topviewOrderList = ["2402", hallway2_4_2, "2401", "2442", elevator2_4_1]

hallway2_4_2.roomList = ["2402", "2401", "2413", "2401B", "2417", "2425", "2431", "2433", "2435",
        "2437", "2439", "2442", "2438", "2434", "2430", "2426", "2422", "2418", "2416", "2414"] #TODO Please recheck the map for room 2433, it's a little vuage
hallway2_4_2.adjList = [staircase2_4_1, hallway2_4_3, staircase2_4_2]
hallway2_4_2.length = len(hallway2_4_2.roomList)
hallway2_4_2.topviewLeftList = ["2402"]
hallway2_4_2.topviewAboveList = ["2401", "2413", "2401B", "2417", "2425", "2431", "2433",
        "2435", "2437", "2439", hallway2_4_3]
hallway2_4_2.topviewRightList = ["2442"]
hallway2_4_2.topviewBelowList = [staircase2_4_2, "2438", "2434", "2430", "2426", "2422", "2418",
        "2416", "2414", hallway2_4_1, staircase2_4_1]
hallway2_4_2.topviewOrderList = ["2402", "2401", "2413", "2401B", "2417", "2425", "2431", "2433",
        "2435", "2437", "2439", hallway2_4_3, "2442"]


## Floor 5

staircase2_5_1 = locations.Staircase(id_name="staircase2-5-1")
staircase2_5_2 = locations.Staircase(id_name="staircase2-5-2")
elevator2_5_1 = locations.Elevator(id_name="elevator2-5-1")
hallway2_5_1 = locations.Hallway(id_name="hallway2-5-1")
hallway2_5_2 = locations.Hallway(id_name="hallway2-5-2")
hallway2_5_3 = locations.Hallway(id_name="hallway2-5-3")
hallway2_5_4 = locations.Hallway(id_name="hallway2-5-4")
hallway2_5_5 = locations.Hallway(id_name="hallway2-5-5")

staircase2_5_1.adjList = [hallway2_5_2, staircase2_4_1, staircase2_3_1,
                          staircase2_2_1, staircase2_1_1]

staircase2_5_2.adjList = [hallway2_5_2, staircase2_4_2, staircase2_3_2]

elevator2_5_1.adjList = [hallway2_5_1, elevator2_4_1, elevator2_3_1, elevator2_2_1, elevator2_1_1]

hallway2_5_1.roomList = []
hallway2_5_1.adjList = [elevator2_5_1, hallway2_5_2]
hallway2_5_1.length = len(hallway2_5_1.roomList)
hallway2_5_1.topviewLeftList = []
hallway2_5_1.topviewAboveList = [hallway2_5_2]
hallway2_5_1.topviewRightList = []
hallway2_5_1.topviewBelowList = [elevator2_5_1]
hallway2_5_1.topviewOrderList = [elevator2_5_1, hallway2_5_2]

hallway2_5_2.roomList = ["2501", '2501A', '2513', '2517', '2517A', '2517B', '2517C', '2521',
                         '2521A', '2521B', '2523', '2523B', '2527', '2527A', '2527B', '2527C',
                         '2537', '2535', '2542', '2534B', '2534A', '2530', '2528', '2524',
                         '2522', '2520' '2518', '2516','2514']  # TODO Check on rooms 2521B, 2521A, and 2523B, ESPECIALLY ROOMS 2531 2533
hallway2_5_2.adjList = [staircase2_5_1, hallway2_5_1, hallway2_5_3, hallway2_5_4, staircase2_5_2]
hallway2_5_2.length = len(hallway2_5_2.roomList)
hallway2_5_2.topviewLeftList = []  # TODO Connection to another building
hallway2_5_2.topviewAboveList = ["2501", '2501A', '2513', '2517', '2517A', '2517B', '2517C',
                                 '2521', '2521A', '2521B', '2523', '2523B', '2527', '2527A',
                                 '2527B', '2527C', hallway2_5_3, hallway2_5_4, '2535', '2537',
                                 '2537C', '2537D', '2537E', '2537G', '2537F']
hallway2_5_2.topviewRightList = ['2542', '2542A']
hallway2_5_2.topviewBelowList = [staircase2_5_2, '2534B', '2534A', '2530', '2528', '2524',
                                 '2524A', '2524B', '2524C', '2522', '2520' '2518', '2516',
                                 '2514', hallway2_5_1, staircase2_5_1]
hallway2_5_2.topviewOrderList = ["2501", '2501A', '2513', '2517', '2517A', '2517B', '2517C',
                                 '2521', '2521A', '2521B', '2523', '2523B', '2527', '2527A',
                                 '2527B', '2527C', hallway2_5_3, hallway2_5_4, '2535', '2537',
                                 '2537C', '2537D', '2537E', '2537G', '2537F','2542', '2542A',
                                 staircase2_5_2, '2534B', '2534A', '2530', '2528', '2524',
                                 '2524A', '2524B', '2524C', '2522', '2520' '2518', '2516',
                                 '2514', hallway2_5_1, staircase2_5_1]


hallway2_5_3.roomList = ['2527', '2527A', '2527B', '2527C']
hallway2_5_3.adjList = []
hallway2_5_3.length = len(hallway2_5_1.roomList)
hallway2_5_3.topviewLeftList = []
hallway2_5_3.topviewAboveList = []
hallway2_5_3.topviewRightList = []
hallway2_5_3.topviewBelowList = []
hallway2_5_3.topviewOrderList = []



## Floor 6

staircase2_6_1 = locations.Staircase(id_name="staircase2-6-1")
staircase2_6_2 = locations.Staircase(id_name="staircase2-6-2")
elevator2_6_1 = locations.Elevator(id_name="elevator2-6-1")
hallway2_6_1 = locations.Hallway(id_name="hallway2-6-1")


staircase2_6_1.adjList = [hallway2_6_1, staircase2_5_1, staircase2_4_1,
        staircase2_3_1, staircase2_2_1, staircase2_1_1]

staircase2_6_2.adjList = [] # TODO

elevator2_6_1.adjList = [hallway2_6_1, elevator2_5_1, elevator2_4_1,
        elevator2_3_1, elevator2_2_1, elevator2_1_1]

hallway2_6_1.roomList = ['2603', '2605B', '2605A', '2605C',
        '2600B', '2605', '2609', '2612']
hallway2_6_1.adjList = [staircase2_6_1, staircase2_6_2, elevator2_6_1]
hallway2_6_1.length = len(hallway2_6_1.roomList)
hallway2_6_1.topviewLeftList = [staircase2_6_2, '2603']
hallway2_6_1.topviewAboveList = ['2605B', '2605A', '2605C', '2600B']
hallway2_6_1.topviewRightList = ['2605', '2609', '2612']
hallway2_6_1.topviewBelowList = [elevator2_6_1, staircase2_6_1]
hallway2_6_1.topviewOrderList = [staircase2_6_2, '2603','2605B', '2605A',
        '2605C', '2600B', '2605', '2609', '2612', elevator2_6_1, staircase2_6_1 ]

## Floor 7

staircase2_7_1 = locations.Staircase(id_name="staircase2-7-1")
elevator2_7_1 = locations.Elevator(id_name="elevator2-7-1")
hallway2_7_1 = locations.Hallway(id_name="hallway2-7-1")
hallway2_7_2 = locations.Hallway(id_name="hallway2-7-2")

staircase2_7_1.adjList = [hallway2_7_2]

elevator2_7_1.adjList = [hallway2_7_2, elevator2_6_1, elevator2_5_1, elevator2_4_1,
        elevator2_3_1, elevator2_2_1, elevator2_1_1]

hallway2_7_1.roomList = ['2700A', '2700', '2705']
hallway2_7_1.adjList = [hallway2_7_2, elevator2_7_1]
hallway2_7_1.length = len(hallway2_7_1.adjList)
hallway2_7_1.topviewLeftList = []
hallway2_7_1.topviewAboveList = ['2700']
hallway2_7_1.topviewRightList = ['2705']
hallway2_7_1.topviewBelowList = [elevator2_7_1, '2700A']
hallway2_7_1.topviewOrderList = [hallway2_7_2, '2700', '2705', '2700A', elevator2_7_1]

hallway2_7_2.roomList = ['2700', '2701', '2703', '2700', '2700A', '2707', '2704', '2708', '2712',
        '2716', '2720', '2724', '2726', '2740', '2721', '2719', '2715', '2713', '2700C']
hallway2_7_2.adjList = [staircase2_7_1, hallway2_7_1]
hallway2_7_2.length = len(hallway2_7_2.adjList)
hallway2_7_2.topviewLeftList = ['2700']
hallway2_7_2.topviewAboveList = ['2704', '2708', '2712', '2716', '2720', '2724', '2726']
hallway2_7_2.topviewRightList = []
hallway2_7_2.topviewBelowList = ['2721', '2719', '2715', '2713', '2707', '2700A', '2703', '2701']
hallway2_7_2.topviewOrderList = ['2700', '2704', '2708', '2712', '2716', '2720', '2724', '2726',
        '2740', staircase2_7_1, '2721', '2719', '2715', '2713', '2700C', '2707', '2700A', '2703', '2701']














####################### Building 2 stuff ends here
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
staircase2_1_1 = locations.Staircase(id_name="staircase2-1-1", url_base='2_1_1')

hallway2_1_1 = locations.Hallway(id_name="hallway2-1-1", url_base='2_1_1')

hallway2_1_2 = locations.Hallway(id_name="hallway2-1-2", url_base='2_1_2')

hallway2_1_3 = locations.Hallway(id_name="hallway2-1-3", url_base='2_1_3')

hallway2_1_4 = locations.Hallway(id_name="hallway2-1-4", url_base='2_1_4')


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
