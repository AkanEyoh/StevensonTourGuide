## Language
Language choice for the backend is Python because it is fairly easy to implement the graph as a list of location objects that contain an adjacency list of other location objects. Python works well for this since the list of locations just contains pointers to other location objects rather than the actual locations. We plan to use Flask to connect the Python backend to the frontend.

## Stevenson Representation in Python
The goal is to represent Stevenson as a graph, where the nodes are the different hallways/stairs since they are connected to each other. To reduce the number of nodes in the graph, the rooms are not represented in the graph. Instead, since each room is connected to a hallway, each room will be mapped to the hallway that it is adjacent to.

When the user enters in the room number to start and destination room numbers, we will find the shortest route from the start to end location by looking up the shortest route from a map that was created when the program first starts. The shortest routes will be determined by using Dijkstra's shortest path. Since the structure of Stevenson building does not change, we can run the computation to find the shortest path from any location to all other locations once and store that information.


## Graph implementation
The idea is to implement the graph of the hallways/stairs as an edge list so that each hallway/stair contains a list of the adjacent hallways, since the branching factor for hallways should be fairly low. The graph will be a list of all the location objects, and each location objects will contain an adjacency list that contains all location objects it is adjacent to (this works in Python since it will just be a list of pointers to the other location objects).
