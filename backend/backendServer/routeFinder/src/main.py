## Author(s): Akaninyene Eyoh
## Date: 2018-11-08
## Email: akaninyene.e.eyoh@vanderbilt.edu
## Filename: main.py
## Description: Main method for application that combines locations, bfs, and data_loader to find
#  shortest path from one room to another.

# from src import bfs
from src import locations
from src import data_loader

def main_func():
    start_room = input("Hello User. Welcome to Steveson Tour Guide. Today, I will help you find your classroom. Which room in " \
          "Stevenson are you currently located?")
    type(start_room)
    end_room = input("OK understood! Which room are you trying to find?")
    type(end_room)
    print("OK, follow these instructions to find your room!")
    # run bfs, print out instructions

if __name__== '__main__':
      main_func()
