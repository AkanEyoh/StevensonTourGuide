from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .src import shortest_path

# this is the function that takes in a view and returns 
def get_route(request, start, end):

    # this calls on the shortest path function to return the shortest path as a list of objects
    class_instance = shortest_path.shortest_path()
    route = class_instance.get_path_from_rooms(start, end)
    ret_list = []
    ret_value = {}

    # this is here to display the return values
    for location in route:
        print(location.to_string())
        ret_list.append(location.to_string())

    ret_value["return_list"] = ret_list
    response = JsonResponse(ret_value, safe=False)

    return response
