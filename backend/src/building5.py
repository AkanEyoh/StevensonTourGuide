## Author(s): Akaninyene Eyoh
## Date: 2019-2-25
## Email: akaninyene.e.eyoh@vanderbilt.edu
## Filename: dataLoader.py (Building 5)

## Science & Engineering (Building 5 Locations)

# Floor 1
sci_staircase1 = locations.Staircase(id_name="sci_staircase1")
sci_staircase2 = locations.Staircase(id_name="sci_staircase2")
sci_staircase3 = locations.Staircase(id_name="sci_staircase3")

sci_hallway1_1 = locations.Hallway(id_name="math_hallway1-1")

sci_elevator1 = locations.Elevator(id_name="math_elevator1")

sci_hallway1_2 = locations.Hallway(id_name="math_hallway1-2")

sci_staircase1_2 = locations.Staircase(id_name="math_staircase1-2")

sci_hallway1_1.roomList = ["134", "134A", "134B", "136"]
math_hallway1_1.adjList = [math_staircase1_1, math_elevator1, math_hallway1_2]
math_hallway1_1.length = 7

