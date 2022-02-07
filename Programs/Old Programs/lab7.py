from maze import *
from room import *

my_rooms = []
my_rooms.append(Room("This room is the entrance."))
my_rooms.append(Room("This room has a table. Maybe a dinning room?"))
my_rooms.append(Room("This room has a dog kennel... but no dog"))
my_rooms.append(Room("This looks like a living room. The couch seems a bit torn up."))
my_rooms.append(Room("No wait Maybe this is the dining room. It has a large table set with chairs"))
my_rooms.append(Room("This is for sure the kitchen."))
my_rooms.append(Room("Just a walking room between rooms... Damn this place is big"))
my_rooms.append(Room("Okay I know we shouldn't rule out bedrooms, but usually I don't sleep with pentagrams and 15 candles."))
my_rooms.append(Room("This is either a nice looking trash room, or someone had a rough time in this Den"))
my_rooms.append(Room("Looks like a laundry room. How come the laundry room looks fine compared to everywhere else?"))
my_rooms.append(Room("This room has almost nothing in it but I think this next door leads to the Garage"))
my_rooms.append(Room("This room is the Garage Exit. Good Job."))
#room 0 is south of room 1
my_rooms[0].setNorth(my_rooms[1])
my_rooms[1].setSouth(my_rooms[0])
#room 2 is west of room 1
my_rooms[1].setWest(my_rooms[2])
my_rooms[2].setEast(my_rooms[1])
#room 8 is east of room 1
my_rooms[1].setEast(my_rooms[8])
my_rooms[8].setWest(my_rooms[1])
#room 3 is north of room 2
my_rooms[2].setNorth(my_rooms[3])
my_rooms[3].setSouth(my_rooms[2])
#room 4 is north of room 3
my_rooms[3].setNorth(my_rooms[4])
my_rooms[4].setSouth(my_rooms[3])
#room 5 is east of room 4
my_rooms[5].setWest(my_rooms[4])
my_rooms[4].setEast(my_rooms[5])
#room 6 is east of room 5
my_rooms[6].setWest(my_rooms[5])
my_rooms[5].setEast(my_rooms[6])
#room 7 is south of room 6
my_rooms[6].setSouth(my_rooms[7])
my_rooms[7].setNorth(my_rooms[6])
#room 8 is south of room 7
my_rooms[7].setSouth(my_rooms[8])
my_rooms[8].setNorth(my_rooms[7])
#room 9 is east of room 6
my_rooms[6].setEast(my_rooms[9])
my_rooms[9].setWest(my_rooms[6])
#room 10 is east of room 9
my_rooms[9].setEast(my_rooms[10])
my_rooms[10].setWest(my_rooms[9])
#room 11 is south of room 10
my_rooms[11].setNorth(my_rooms[10])
my_rooms[10].setSouth(my_rooms[11])

my_maze = Maze(my_rooms[0],my_rooms[11])

print("Welcome the Cyber Maze.")
print("You wake up in a room.")

while True:
    print(my_maze.getCurrent())
    if my_maze.atExit() == True:
        print("You found the exit!")
        break
    user = input("Enter direction to move. | North | West | East | South | Restart |\n")

    if user.lower() == 'north':
        if my_maze.moveNorth() != False:
            pass
        else:
            print('Direction invalid, try again.')
    
    elif user.lower() == 'west':
        if my_maze.moveWest() != False:
            pass
        else:
            print('Direction invalid, try again.')
    
    elif user.lower() == 'east':
        if my_maze.moveEast() != False:
            pass
        else:
            print('Direction invalid, try again.')
    
    elif user.lower() == 'south':
        if my_maze.moveSouth() != False:
            pass
        else:
            print('Direction invalid, try again.')
    
    elif user.lower() == 'restart':
        my_maze.reset()
    
    else:
        print('Direction invalid, try again.')
    