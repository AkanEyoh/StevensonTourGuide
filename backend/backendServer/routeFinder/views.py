# Authored by Ulysses Yu
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import sys
sys.path.insert(0, './../src/')
import shortest_path

# this is the function that takes in a view and returns 
def get_route(request, start, end):

    # get directions as text along with the paths to the images
    # associated with the path to take
    directions, image_paths = shortest_path.get_directions(start, end)

    if not directions:
        ret_value = {}
        ret_value["return_list"] = ["False"]
        response = JsonResponse(ret_value)
    else:
            
        ret_list = []
        ret_value = {}

        ret_value["return_list"] = directions
        response = JsonResponse(ret_value)

    return response
