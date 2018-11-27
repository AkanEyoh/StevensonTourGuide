from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .src import shortest_path

# this is the function that takes in a view and returns 
def get_route(request, start, end):

    class_instance = shortest_path.shortest_path()

    route = class_instance.get_path_from_rooms(start, end)

    response = HttpResponse()
    for location in route:
        print(location.to_string())
        response.write(location.to_string())

    return response
