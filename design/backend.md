## Language
Language choice for the backend is Python.

## Stevenson Representation in Python
The goal is to represent Stevenson as a graph, where the nodes are the different hallways/stairs since they are connected to each other. To reduce the number of nodes in the graph, the rooms are not represented in the graph. Instead, since each room is connected to a hallway, each room will be mapped to the hallway that it is adjacent to.

When the user enters in the room number to start and destination room numbers, we will find the corresponding hallways using the map and then use the start hallway as the starting point in breadth first search, and the end hallway as the goal. We decided to use breadth first search since the branching factor will be fairly low (each hallway is usually only connected to a few other hallways), and breadth first search guarantees the shortest path will be found