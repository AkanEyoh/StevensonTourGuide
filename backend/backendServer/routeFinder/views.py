from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .src import shortest_path

# this is the function that takes in a view and returns 
def get_route(request, start, end):

    class_instance = shortest_path.shortest_path()

    route = class_instance.get_path_from_rooms(start, end)
    print(route)
    response = HttpResponse()
    response.write("<p>This is the start: </p>")
    response.write(start)
    response.write("<p>This is the end: </p>")
    response.write(end)
    return response
